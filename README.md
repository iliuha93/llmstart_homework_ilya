# LLM-ассистент для Telegram

Телеграм-бот с ИИ для консультаций клиентов по услугам компании.

**Студент:** Митин Илья  
**Статус:** В разработке

## 🚀 Быстрый старт

### 1. Создайте бота в Telegram

1. Найдите @BotFather в Telegram
2. Отправьте команду `/newbot`
3. Введите имя бота (например: "LLM Assistant")
4. Введите username (например: "llm_assistant_bot")
5. **Скопируйте токен** (выглядит как `1234567890:ABCdefGhIJKlmNoPQRsTuVwXYz`)

### 2. Настройте окружение

**Вариант A: Создание через консоль (рекомендуемый)**

Windows (PowerShell):
```powershell
echo 'BOT_TOKEN=ваш_токен_здесь' > .env
echo 'LOG_LEVEL=INFO' >> .env
```

Linux/Mac:
```bash
echo 'BOT_TOKEN=ваш_токен_здесь' > .env
echo 'LOG_LEVEL=INFO' >> .env
```

**Вариант B: Создание вручную**

Создайте файл `.env` в корне проекта и скопируйте:

```env
# Telegram Bot
BOT_TOKEN=ваш_токен_от_botfather_сюда

# OpenRouter API (для следующих итераций)
OPENROUTER_API_KEY=your_openrouter_key_here
MODEL_NAME=meta-llama/llama-3.1-8b-instruct:free

# Logging
LOG_LEVEL=INFO
```

### 3. Установите зависимости и запустите

```bash
pip install aiogram openai python-dotenv
python main.py
```

### 4. Протестируйте бота

1. Найдите вашего бота в Telegram по username
2. Отправьте любое сообщение: `Привет`
3. Ожидаемый ответ: `Эхо: Привет`

## 📁 Структура проекта

```
llmstart_homework_ilya/
├── main.py              # Точка входа приложения
├── config.py            # Конфигурация переменных окружения
├── bot/
│   ├── __init__.py
│   └── handlers.py      # Обработчики сообщений
├── llm/
│   ├── __init__.py
│   └── client.py        # Клиент для работы с LLM
├── tests/
│   └── test_bot.py      # Тесты
├── doc/
│   ├── botfather_setup.md  # Подробная инструкция по BotFather
│   ├── tasklist.md         # План разработки
│   └── vision.md           # Техническое видение
└── .env                 # Ваши переменные окружения (создаете сами)
```

## 🎯 План разработки

- ✅ **Итерация 1:** Базовая инфраструктура (эхо-бот)
- ⬜ **Итерация 2:** Интеграция с LLM
- ⬜ **Итерация 3:** Управление диалогами
- ⬜ **Итерация 4:** Сценарии работы
- ⬜ **Итерация 5:** Деплой и финализация

Подробный план в [doc/tasklist.md](./doc/tasklist.md)

## 🛠 Технологии

- **Python 3.11+**
- **aiogram** - работа с Telegram Bot API
- **OpenAI Client** - работа с LLM через OpenRouter
- **python-dotenv** - управление переменными окружения 