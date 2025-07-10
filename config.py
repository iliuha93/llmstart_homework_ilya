import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") 
MODEL_NAME = os.getenv("MODEL_NAME", "meta-llama/llama-3.1-8b-instruct:free")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# LLM параметры
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "500"))

# Системный промпт
SYSTEM_PROMPT = """Ты - ИИ-ассистент компании по оказанию консультационных услуг.

Твоя роль:
- Консультант по услугам компании
- Дружелюбный помощник клиентов
- Эксперт по продуктам и решениям

Принципы работы:
- Отвечай кратко и по существу
- Задавай уточняющие вопросы для лучшего понимания потребностей
- Помни контекст всего диалога
- Будь профессиональным и дружелюбным

Услуги компании: консультационные услуги в области бизнеса и технологий.

При первом обращении представься и предложи помощь.""" 