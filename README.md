# 🚗 Гараж знаний — база знаний с AI-ассистентом

Публичная база знаний по автомобилям со встроенным RAG-ассистентом, который отвечает на вопросы строго по проверенному контенту и указывает источники.

![Главная страница](https://img.shields.io/badge/status-active-brightgreen)
![VitePress](https://img.shields.io/badge/VitePress-1.6.4-orange)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📋 О проекте

**«Гараж знаний»** — это учебный проект, созданный командой **«Нейрослоп»**. Мы прошли путь от пустого репозитория до работающего продукта: статический сайт + интеллектуальный AI-ассистент.

### 🎯 Цель проекта

Создать бесплатную структурированную базу знаний по автомобилям со встроенным AI-ассистентом, который отвечает **строго по проверенному контенту** и всегда указывает источник. Никаких выдумок — только то, что написано в базе.

### 🔍 Ключевые особенности

- **Структурированный контент** — 20+ страниц по трём разделам: подбор, обслуживание, документы
- **AI-ассистент (RAG)** — отвечает по смыслу, а не по ключевым словам
- **Поиск по базе знаний** — семантический поиск через эмбеддинги
- **Указание источников** — каждый ответ содержит ссылку на конкретный `.md` файл
- **Бесплатные технологии** — только открытые и бесплатные API
- **Контент как код** — всё хранится в Git, обновляется через пуши

---

## 🏗️ Архитектура проекта
📄 Markdown-файлы (контент)
↓
🌐 VitePress + Vue (статический сайт)
↓
🐍 FastAPI сервер (порт 8000)
↓
🔍 ChromaDB (векторный поиск) + 🤖 Ollama (локальная LLM)
↓
💬 Ответ с указанием источника

---

## 🛠️ Технологический стек

| Компонент | Технология |
|-----------|------------|
| **Фронтенд** | VitePress, Vue 3, TypeScript |
| **Стилизация** | CSS (кастомная тёмная тема) |
| **Бэкенд** | Python, FastAPI |
| **Векторная БД** | ChromaDB |
| **Эмбеддинги** | Sentence-Transformers (all-MiniLM-L6-v2) |
| **LLM** | Ollama (Llama 3.2) |
| **CI/CD** | GitHub Actions (в планах) |
| **Контроль версий** | Git, GitHub |

---

## 📂 Структура проекта
garage-knowledge/
├── .vitepress/
│ ├── config.mts # Конфигурация VitePress
│ └── theme/
│ ├── ChatWidget.vue # Vue-компонент чата
│ ├── Layout.vue # Макет с чатом
│ ├── custom.css # Стилизация (тёмная тема)
│ └── index.ts # Подключение темы
├── selection/ # Раздел «Подбор авто»
│ ├── index.md
│ ├── budget-100.md # До 100 000 ₽
│ ├── budget-200.md # 100 000 – 200 000 ₽
│ ├── budget-500.md # 300 000 – 500 000 ₽
│ └── budget-1000.md # 500 000 – 1 000 000 ₽
├── service/ # Раздел «Обслуживание»
│ ├── index.md
│ ├── device.md # Устройство автомобиля
│ ├── to-basics.md # Техобслуживание для новичков
│ └── checking.md # Проверка перед покупкой
├── docs/ # Раздел «Документы»
│ ├── index.md
│ ├── registration.md # Регистрация в ГИБДД
│ ├── tax.md # Транспортный налог
│ └── insurance.md # ОСАГО и Каско
├── index.md # Главная страница
├── api_server.py # FastAPI сервер для RAG
├── index_docs.py # Скрипт индексации Markdown-файлов
├── query.py # Тестирование RAG в консоли
├── requirements.txt # Python-зависимости
├── package.json # Node.js-зависимости
└── .gitignore # Исключения для Git

---

## 🚀 Быстрый старт

### Предварительные требования

- **Node.js** ≥ 20
- **Python** ≥ 3.10
- **Ollama** (установить с [ollama.com](https://ollama.com))

### 1. Клонирование репозитория

```bash
git clone https://github.com/isachenkoegor343-max/garage-knowledge.git
cd garage-knowledge

2. Установка фронтенда
bash
npm install
3. Установка Python-зависимостей
bash
pip install -r requirements.txt
4. Скачивание LLM модели
bash
ollama pull llama3.2
5. Индексация контента
bash
python index_docs.py
6. Запуск API-сервера (терминал 1)
bash
python api_server.py
Сервер запустится на http://127.0.0.1:8000.

7. Запуск сайта (терминал 2)
bash
npm run docs:dev
Сайт откроется на http://localhost:5173.

Установка фронтенда
bash
npm install
3. Установка Python-зависимостей
bash
pip install -r requirements.txt
4. Скачивание LLM модели
bash
ollama pull llama3.2
5. Индексация контента
bash
python index_docs.py
6. Запуск API-сервера (терминал 1)
bash
python api_server.py
Сервер запустится на http://127.0.0.1:8000.

7. Запуск сайта (терминал 2)
bash
npm run docs:dev
Сайт откроется на http://localhost:5173.