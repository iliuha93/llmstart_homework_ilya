from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo_handler(message: Message) -> None:
    """Эхо-обработчик сообщений"""
    await message.answer(f"Эхо: {message.text}") 