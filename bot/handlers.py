import logging
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from llm.client import get_llm_response
from config import SYSTEM_PROMPT

logger = logging.getLogger(__name__)
router = Router()

# Хранение диалогов в памяти
dialogs = {}

@router.message(Command("start"))
async def start_handler(message: Message) -> None:
    """Приветствие нового пользователя"""
    chat_id = str(message.chat.id)
    
    logger.info(f"🚀 Новый пользователь {chat_id} использует команду /start")
    
    welcome_text = """👋 Добро пожаловать в TechConsult Pro!

Я - ИИ-ассистент компании по оказанию консультационных услуг. Помогу вам:

🎯 Бизнес-консультирование
💻 Технологические консультации  
🔍 Аналитические услуги

Команды:
/help - справка по командам
/services - полный список услуг
/contact - контакты менеджера

Расскажите, с какими задачами я могу помочь?"""
    
    await message.answer(welcome_text)

@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    """Справка по командам бота"""
    help_text = """📖 Доступные команды:

/start - приветствие и знакомство
/help - эта справка
/services - список всех услуг компании
/contact - контакты для связи с менеджером

Просто напишите мне сообщение, и я помогу с консультацией по услугам нашей компании! 💬"""
    
    await message.answer(help_text)

@router.message(Command("services"))
async def services_handler(message: Message) -> None:
    """Полный список услуг компании"""
    services_text = """🏢 Услуги TechConsult Pro:

🎯 **Бизнес-консультирование:**
• Стратегическое планирование и развитие бизнеса
• Анализ рынка и конкурентов
• Оптимизация бизнес-процессов
• Управление проектами

💻 **Технологические консультации:**
• Цифровая трансформация компаний
• Разработка IT-стратегии
• Консультации по выбору технологий
• Автоматизация процессов

🔍 **Аналитические услуги:**
• Анализ данных и Business Intelligence
• Исследования рынка
• Аудит текущих процессов
• Рекомендации по улучшениям

Расскажите о ваших задачах, и я подберу подходящие решения! 🚀"""
    
    await message.answer(services_text)

@router.message(Command("contact"))
async def contact_handler(message: Message) -> None:
    """Контакты для связи с менеджером"""
    contact_text = """📞 Контакты для связи:

👩‍💼 Менеджер: Анна Петрова
📧 Email: manager@techconsult.pro
📱 Телефон: +7 (495) 123-45-67

Анна свяжется с вами в рабочее время (пн-пт, 9:00-18:00 МСК) для обсуждения деталей и составления индивидуального предложения.

Также можете продолжить консультацию со мной! 💬"""
    
    await message.answer(contact_text)

@router.message()
async def llm_handler(message: Message) -> None:
    """Обработчик сообщений с интеграцией LLM"""
    chat_id = str(message.chat.id)
    user_message = message.text
    
    logger.info(f"📨 Получено сообщение от {chat_id}: {user_message[:50]}...")
    
    # Проверяем, первое ли это обращение пользователя
    is_first_contact = chat_id not in dialogs
    
    # Инициализация диалога если его нет
    if is_first_contact:
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
    
    # Если это первое обращение (не через /start), добавляем приветствие
    if is_first_contact:
        greeting_prefix = """👋 Здравствуйте! Я - ИИ-ассистент компании TechConsult Pro.

Рад знакомству! Наша компания специализируется на консультационных услугах в области бизнеса и технологий.

"""
        llm_response = greeting_prefix + llm_response
        logger.info(f"🎉 Добавлено приветствие для нового клиента {chat_id}")
    
    # Добавление ответа в историю (без приветствия, чтобы не засорять контекст)
    dialogs[chat_id]["messages"].append({
        "role": "assistant",
        "content": llm_response if not is_first_contact else llm_response[len(greeting_prefix):]
    })
    
    logger.info(f"📤 Отправка ответа пользователю {chat_id}")
    
    # Отправка ответа пользователю
    await message.answer(llm_response) 