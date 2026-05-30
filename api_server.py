from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import chromadb
from sentence_transformers import SentenceTransformer
import ollama

# Инициализация
app = FastAPI(title="Гараж знаний API")

# Разрешаем запросы с любого источника (для разработки)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Загружаем модель и БД один раз при старте
print("Загрузка модели и базы данных...")
model_emb = SentenceTransformer('all-MiniLM-L6-v2')
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(name="garage_knowledge")
print("Готово!")


# Модель запроса
class Question(BaseModel):
    text: str


# Модель ответа
class Answer(BaseModel):
    response: str
    sources: list


@app.post("/ask", response_model=Answer)
async def ask_question(question: Question):
    # 1. Поиск по базе
    question_embedding = model_emb.encode(question.text).tolist()
    results = collection.query(query_embeddings=[question_embedding], n_results=5)

    if not results['documents'][0]:
        return Answer(
            response="В базе знаний нет информации по этому вопросу.",
            sources=[]
        )

    # 2. Собираем контекст и источники
    context_parts = []
    sources = list(set([m['source'] for m in results['metadatas'][0]]))

    for i in range(len(results['documents'][0])):
        doc_text = results['documents'][0][i]
        source = results['metadatas'][0][i]['source']
        context_parts.append(f"[Источник: {source}]\n{doc_text}")

    context = "\n\n---\n\n".join(context_parts)

    # 3. Промпт для LLM
    prompt = f"""Прочитай информацию и ответь на вопрос на русском языке.
В конце укажи источник в формате "📚 Источник: имя_файла.md".

ИНФОРМАЦИЯ:
{context}

ВОПРОС: {question.text}

ОТВЕТ:"""

    # 4. Генерация через Ollama
    try:
        response = ollama.chat(
            model='gemma2:9b',
            messages=[{'role': 'user', 'content': prompt}]
        )
        answer_text = response['message']['content']
    except Exception as e:
        answer_text = f"Ошибка генерации: {e}"

    return Answer(response=answer_text, sources=sources)


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)