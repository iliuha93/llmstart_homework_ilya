# Настройка бота через BotFather

## Шаги создания бота

1. Откройте Telegram и найдите @BotFather
2. Отправьте команду `/newbot`
3. Введите имя бота (например: "LLM Assistant")
4. Введите username (например: "llm_assistant_bot")
5. Скопируйте токен бота

## Настройка

- Сохраните токен в файл `.env` как `BOT_TOKEN`
- Дополнительно настройте описание через `/setdescription`

## Пример токена

```
BOT_TOKEN=1234567890:ABCdefGhIJKlmNoPQRsTuVwXYz
```

## Дополнительные команды BotFather

- `/setdescription` - установить описание бота
- `/setabouttext` - установить текст "О боте"
- `/setcommands` - установить список команд 