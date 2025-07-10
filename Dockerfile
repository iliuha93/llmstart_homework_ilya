# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Копируем файлы с зависимостями
COPY pyproject.toml ./

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -e .

# Копируем исходный код приложения
COPY . .

# Создаем пользователя для безопасности
RUN adduser --disabled-password --gecos '' botuser && \
    chown -R botuser:botuser /app
USER botuser

# Настраиваем переменные окружения
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Порт не нужен для Telegram бота, но можем добавить для мониторинга
EXPOSE 8000

# Проверка работоспособности (опционально)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

# Команда запуска
CMD ["python", "main.py"] 