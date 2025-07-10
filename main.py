import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot.handlers import router
from config import BOT_TOKEN, LOG_LEVEL

async def main():
    logging.basicConfig(level=LOG_LEVEL)
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 