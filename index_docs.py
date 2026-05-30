import os
import chromadb
from sentence_transformers import SentenceTransformer

# 1. Загружаем модель для эмбеддингов (бесплатная, локальная)
print("Загрузка модели эмбеддингов...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Создаём или подключаем ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="garage_knowledge")

# 3. Путь к папке с Markdown-файлами
DOCS_PATH = "C:/Users/isach/RAG-assistant"


def read_md_files(root_path):
    """Рекурсивно читает все .md файлы и возвращает список (путь, содержимое)"""
    files_content = []
    for dirpath, _, filenames in os.walk(root_path):
        for file in filenames:
            if file.endswith(".md"):
                full_path = os.path.join(dirpath, file)
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if content.strip():
                        relative_path = os.path.relpath(full_path, root_path)
                        files_content.append((relative_path, content))
    return files_content


# 4. Читаем все файлы
print("Чтение Markdown-файлов...")
files = read_md_files(DOCS_PATH)
print(f"Найдено {len(files)} файлов")

# 5. Индексация
print("Индексация в ChromaDB...")
for i, (file_path, content) in enumerate(files):
    # Разбиваем на чанки по 500 символов
    chunks = [content[i:i + 500] for i in range(0, len(content), 500)]

    for j, chunk in enumerate(chunks):
        chunk_id = f"{file_path}_chunk_{j}"
        embedding = model.encode(chunk).tolist()

        collection.upsert(
            ids=[chunk_id],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{"source": file_path, "chunk": j}]
        )

print(f"Индексация завершена! Добавлено документов: {collection.count()}")