import chromadb
from sentence_transformers import SentenceTransformer
import ollama

print("Загрузка модели и базы данных...")
model_emb = SentenceTransformer('all-MiniLM-L6-v2')
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(name="garage_knowledge")


def ask(question: str):
    print("\n🤖 Генерация ответа...")

    # 1. Поиск
    question_embedding = model_emb.encode(question).tolist()
    results = collection.query(query_embeddings=[question_embedding], n_results=2)

    if not results['documents'][0]:
        print("❌ Ничего не найдено.")
        return

    # 2. Берём ТОЛЬКО первый (самый релевантный) кусок
    best_text = results['documents'][0][0]
    source = results['metadatas'][0][0]['source']

    print(f"\n📄 Найден источник: {source}")
    print(f"📝 Содержимое: {best_text[:200]}...")

    # 3. Жёсткий промпт
    # 3. Промпт для LLM
    prompt = f"""Ты — автоэксперт. Ответь на вопрос КОРОТКО, на русском языке, используя ТОЛЬКО информацию ниже.
    Ответ должен быть из 3-5 предложений. Не добавляй ничего от себя.

    ИНФОРМАЦИЯ:
    {context}

    ВОПРОС: {question.text}

    КРАТКИЙ ОТВЕТ НА РУССКОМ:"""

    try:
        response = ollama.chat(
            model='llama3.2',
            messages=[{'role': 'user', 'content': prompt}]
        )
        answer = response['message']['content']
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    print("\n" + "=" * 60)
    print(f"🔍 Вопрос: {question}")
    print("=" * 60)
    print(f"\n🤖 ОТВЕТ:\n{answer}")
    print("=" * 60)


if __name__ == "__main__":
    print("\n🚗 Гараж знаний — RAG (упрощённый режим)")
    while True:
        q = input("\n❓ Вопрос: ")
        if q.lower() in ["выход", "exit"]:
            break
        if q.strip():
            ask(q)