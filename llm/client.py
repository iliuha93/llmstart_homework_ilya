import logging
from openai import AsyncOpenAI
from config import OPENROUTER_API_KEY, MODEL_NAME, LLM_TEMPERATURE, LLM_MAX_TOKENS

logger = logging.getLogger(__name__)

# Проверка наличия API ключа при импорте
if not OPENROUTER_API_KEY:
    logger.error("OPENROUTER_API_KEY не найден в .env файле!")

# Инициализация клиента OpenRouter
client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

async def get_llm_response(dialog_history: list) -> str:
    """
    Получение ответа от LLM с подробной диагностикой
    """
    try:
        logger.info(f"🚀 Отправка запроса к LLM:")
        logger.info(f"  - Сообщений в истории: {len(dialog_history)}")
        logger.info(f"  - Модель: {MODEL_NAME}")
        logger.info(f"  - Температура: {LLM_TEMPERATURE}")
        logger.info(f"  - Макс токены: {LLM_MAX_TOKENS}")
        
        # Проверка API ключа
        if not OPENROUTER_API_KEY:
            raise ValueError("OpenRouter API ключ не настроен")
            
        response = await client.chat.completions.create(
            model=MODEL_NAME,
            messages=dialog_history,
            temperature=LLM_TEMPERATURE,
            max_tokens=LLM_MAX_TOKENS
        )
        
        answer = response.choices[0].message.content
        logger.info(f"✅ Получен ответ от LLM: {len(answer)} символов")
        
        return answer
        
    except Exception as e:
        error_type = type(e).__name__
        error_msg = str(e)
        
        logger.error(f"❌ ОШИБКА LLM: {error_type}")
        logger.error(f"   Сообщение: {error_msg}")
        logger.error(f"   Модель: {MODEL_NAME}")
        logger.error(f"   API ключ установлен: {bool(OPENROUTER_API_KEY)}")
        
        # Возвращаем детализированную ошибку для диагностики
        return f"Ошибка {error_type}: {error_msg}" 