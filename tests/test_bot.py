import pytest
from bot.handlers import llm_handler, dialogs
from aiogram.types import Message, Chat, User
from unittest.mock import AsyncMock, MagicMock

def test_bot_import():
    """ТЕСТ базового импорта модулей"""
    assert llm_handler is not None

@pytest.mark.asyncio
async def test_context_memory():
    """ТЕСТ сохранения контекста в диалоге"""
    
    # Подготовка тестовых данных
    test_chat_id = "test_chat_123"
    
    # Очистка тестового диалога
    if test_chat_id in dialogs:
        del dialogs[test_chat_id]
    
    # Создание мок-объектов для сообщений
    chat = Chat(id=int(test_chat_id), type="private")
    user = User(id=123, is_bot=False, first_name="Test")
    
    # Первое сообщение - представление пользователя
    message1 = Message(
        message_id=1,
        date=None,
        chat=chat,
        from_user=user,
        text="Привет, меня зовут Анна"
    )
    message1.answer = AsyncMock()
    
    # Отправка первого сообщения
    await llm_handler(message1)
    
    # Проверка, что диалог создан и содержит системный промпт
    assert test_chat_id in dialogs
    assert len(dialogs[test_chat_id]["messages"]) >= 2  # system + user + assistant
    
    # Второе сообщение - проверка памяти
    message2 = Message(
        message_id=2,
        date=None,
        chat=chat,
        from_user=user,
        text="Как меня зовут?"
    )
    message2.answer = AsyncMock()
    
    # Отправка второго сообщения
    await llm_handler(message2)
    
    # Проверка, что история диалога сохраняется
    assert len(dialogs[test_chat_id]["messages"]) >= 4  # system + user1 + assistant1 + user2 + assistant2
    
    # Проверка структуры диалога
    messages = dialogs[test_chat_id]["messages"]
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert messages[1]["content"] == "Привет, меня зовут Анна"
    assert messages[2]["role"] == "assistant"
    assert messages[3]["role"] == "user"
    assert messages[3]["content"] == "Как меня зовут?"
    
    print("✅ Тест контекстной памяти пройден успешно") 