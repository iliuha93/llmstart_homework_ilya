# LLM-ассистент для Telegram

**TechConsult Pro** - Телеграм-бот с ИИ для консультаций клиентов по услугам компании.

**Студент:** Митин Илья  
**Статус:** ✅ Завершен

---

## 🚀 Быстрый старт

### 1. Создайте бота в Telegram

1. Найдите @BotFather в Telegram
2. Отправьте команду `/newbot`
3. Введите имя бота (например: "TechConsult Pro Assistant")
4. Введите username (например: "techconsult_pro_bot")
5. **Скопируйте токен** (выглядит как `1234567890:ABCdefGhIJKlmNoPQRsTuVwXYz`)

### 2. Получите API ключ OpenRouter

1. Зарегистрируйтесь на https://openrouter.ai
2. Создайте API ключ
3. **Скопируйте ключ** для использования в .env

### 3. Настройте окружение

Создайте файл `.env` в корне проекта:

```env
# ОБЯЗАТЕЛЬНЫЕ НАСТРОЙКИ
BOT_TOKEN=your_telegram_bot_token_here
OPENROUTER_API_KEY=your_openrouter_api_key_here

# ОПЦИОНАЛЬНЫЕ НАСТРОЙКИ (есть дефолты)
MODEL_NAME=deepseek/deepseek-r1-0528-qwen3-8b:free
LOG_LEVEL=INFO
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=500
```

### 4. Запуск

**Способ 1: Локальный запуск**
```bash
pip install -e .
python main.py
```

**Способ 2: С помощью Makefile (Linux/Mac)**
```bash
make install
make run
```

**Способ 3: Docker (рекомендуемый для продакшн)**
```bash
# Сборка и запуск
docker build -t llmstart-bot .
docker run -d --name llmstart-bot-container --env-file .env llmstart-bot

# Или с Makefile
make docker-run
```

---

## 🎯 Возможности бота

### Команды
- `/start` - приветствие и знакомство
- `/help` - справка по командам  
- `/services` - полный список услуг компании
- `/contact` - контакты менеджера

### Услуги TechConsult Pro

🎯 **Бизнес-консультирование:**
- Стратегическое планирование и развитие бизнеса
- Анализ рынка и конкурентов
- Оптимизация бизнес-процессов
- Управление проектами

💻 **Технологические консультации:**
- Цифровая трансформация компаний
- Разработка IT-стратегии
- Консультации по выбору технологий
- Автоматизация процессов

🔍 **Аналитические услуги:**
- Анализ данных и Business Intelligence
- Исследования рынка
- Аудит текущих процессов
- Рекомендации по улучшениям

### Сценарии работы
1. **Автоматическое приветствие** новых пользователей
2. **Интеллектуальное консультирование** на основе LLM
3. **Контекстные диалоги** с сохранением истории
4. **Эскалация к менеджеру** при сложных вопросах

---

## 📁 Структура проекта

```
llmstart_homework_ilya/
├── main.py              # Точка входа приложения
├── config.py            # Конфигурация переменных окружения
├── bot/
│   ├── __init__.py
│   └── handlers.py      # Обработчики сообщений и команд
├── llm/
│   ├── __init__.py
│   └── client.py        # Клиент для работы с LLM
├── tests/
│   └── test_bot.py      # Тесты
├── doc/                 # Документация
│   ├── botfather_setup.md  # Инструкция по BotFather
│   ├── tasklist.md         # План разработки
│   ├── vision.md           # Техническое видение
│   └── product_idea.md     # Идея продукта
├── Dockerfile           # Конфигурация Docker контейнера
├── Makefile            # Автоматизация задач
├── .dockerignore       # Исключения для Docker
├── pyproject.toml      # Конфигурация проекта
└── .env                # Переменные окружения (создаете сами)
```

---

## 🛠 Makefile команды

```bash
# Помощь
make help

# Установка и запуск
make install      # Установка зависимостей
make dev-install  # Установка с dev зависимостями
make run          # Запуск бота локально
make test         # Запуск тестов
make clean        # Очистка временных файлов

# Docker
make docker-build # Сборка Docker образа
make docker-run   # Запуск в Docker
make docker-stop  # Остановка контейнера
make docker-logs  # Просмотр логов
make docker-clean # Удаление образа

# Комплексные команды
make all          # Полная сборка и тестирование
make status       # Проверка статуса системы
```

---

## 🐳 Docker деплой

### Локальная сборка и запуск
```bash
# Сборка образа
docker build -t llmstart-bot .

# Запуск контейнера
docker run -d \
  --name llmstart-bot-container \
  --env-file .env \
  --restart unless-stopped \
  llmstart-bot

# Просмотр логов
docker logs -f llmstart-bot-container
```

### Production деплой
```bash
# Остановка и обновление
docker stop llmstart-bot-container
docker rm llmstart-bot-container
docker pull llmstart-bot:latest

# Запуск с политикой перезапуска
docker run -d \
  --name llmstart-bot-container \
  --env-file .env \
  --restart unless-stopped \
  --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  llmstart-bot:latest
```

---

## 🧪 Тестирование

### Ручное тестирование
1. Отправьте `/start` - должно появиться приветствие
2. Спросите про услуги: "Помогите с автоматизацией"
3. Проверьте команды `/services`, `/contact`, `/help`
4. Протестируйте эскалацию: задайте сложный вопрос

### Автоматические тесты
```bash
# Запуск тестов
python -m pytest tests/ -v

# Или через Makefile
make test
```

---

## 🎯 План разработки

- ✅ **Итерация 1:** Базовая инфраструктура (эхо-бот)
- ✅ **Итерация 2:** Интеграция с LLM
- ✅ **Итерация 3:** Управление диалогами
- ✅ **Итерация 4:** Сценарии работы
- ✅ **Итерация 5:** Деплой и финализация

Подробный план в [doc/tasklist.md](./doc/tasklist.md)

---

## 🛠 Технологии

- **Python 3.11+** - основной язык
- **aiogram** - работа с Telegram Bot API
- **OpenAI Client** - работа с LLM через OpenRouter
- **python-dotenv** - управление переменными окружения
- **Docker** - контейнеризация
- **Make** - автоматизация задач

---

## 📞 Поддержка

**В случае проблем:**

1. **Проверьте .env файл** - все ключи заполнены?
2. **Проверьте логи** - `docker logs llmstart-bot-container`
3. **Баланс OpenRouter** - есть ли кредиты на аккаунте?
4. **Токен бота** - активен ли в @BotFather?

**Контакты:**
- 👩‍💼 Менеджер: Анна Петрова
- 📧 Email: manager@techconsult.pro  
- 📱 Телефон: +7 (495) 123-45-67

---

## 📜 Лицензия

Проект создан в рамках домашнего задания курса LLMstart.  
**Автор:** Митин Илья 