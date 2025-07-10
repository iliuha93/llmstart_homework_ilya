import logging
from aiogram import Router
from aiogram.types import Message
from llm.client import get_llm_response
from config import SYSTEM_PROMPT

logger = logging.getLogger(__name__)
router = Router()

# Хранение диалогов в памяти
dialogs = {}

@router.message()
async def llm_handler(message: Message) -> None:
    """Обработчик сообщений с интеграцией LLM"""
    chat_id = str(message.chat.id)
    user_message = message.text
    
    logger.info(f"📨 Получено сообщение от {chat_id}: {user_message[:50]}...")
    
    # Инициализация диалога если его нет
    if chat_id not in dialogs:
        dialogs[chat_id] = {
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT}
            ]
        }
        logger.info(f"🆕 Создан новый диалог для {chat_id}")
    
    # Добавление сообщения пользователя
    dialogs[chat_id]["messages"].append({
        "role": "user", 
        "content": user_message
    })
    
    # Получение ответа от LLM
    llm_response = await get_llm_response(dialogs[chat_id]["messages"])
    
    # Добавление ответа в историю
    dialogs[chat_id]["messages"].append({
        "role": "assistant",
        "content": llm_response
    })
    
    logger.info(f"📤 Отправка ответа пользователю {chat_id}")
    
    # Отправка ответа пользователю
    await message.answer(llm_response) 