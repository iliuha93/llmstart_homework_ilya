# Makefile для автоматизации задач LLM-ассистента
# Студент: Митин Илья

# Переменные
IMAGE_NAME = llmstart-bot
CONTAINER_NAME = llmstart-bot-container
PYTHON = python
PIP = pip

# Цвета для вывода
GREEN = \033[0;32m
YELLOW = \033[1;33m
RED = \033[0;31m
NC = \033[0m # No Color

.PHONY: help install dev-install run test clean docker-build docker-run docker-stop docker-logs docker-clean all

# Помощь по командам
help:
	@echo "$(GREEN)Доступные команды:$(NC)"
	@echo "  $(YELLOW)install$(NC)      - Установка зависимостей"
	@echo "  $(YELLOW)dev-install$(NC)  - Установка зависимостей для разработки"
	@echo "  $(YELLOW)run$(NC)          - Запуск бота локально"
	@echo "  $(YELLOW)test$(NC)         - Запуск тестов"
	@echo "  $(YELLOW)clean$(NC)        - Очистка временных файлов"
	@echo ""
	@echo "$(GREEN)Docker команды:$(NC)"
	@echo "  $(YELLOW)docker-build$(NC) - Сборка Docker образа"
	@echo "  $(YELLOW)docker-run$(NC)   - Запуск бота в Docker"
	@echo "  $(YELLOW)docker-stop$(NC)  - Остановка Docker контейнера"
	@echo "  $(YELLOW)docker-logs$(NC)  - Просмотр логов Docker контейнера"
	@echo "  $(YELLOW)docker-clean$(NC) - Удаление Docker образа и контейнера"
	@echo ""
	@echo "  $(YELLOW)all$(NC)          - Полная сборка и тестирование"

# Установка зависимостей
install:
	@echo "$(GREEN)Установка зависимостей...$(NC)"
	$(PIP) install --upgrade pip
	$(PIP) install -e .

# Установка зависимостей для разработки
dev-install: install
	@echo "$(GREEN)Установка зависимостей для разработки...$(NC)"
	$(PIP) install -e ".[dev]"

# Запуск бота локально
run:
	@echo "$(GREEN)Запуск бота локально...$(NC)"
	@if [ ! -f .env ]; then \
		echo "$(RED)Ошибка: Файл .env не найден!$(NC)"; \
		echo "$(YELLOW)Создайте .env файл с токенами BOT_TOKEN и OPENROUTER_API_KEY$(NC)"; \
		exit 1; \
	fi
	$(PYTHON) main.py

# Запуск тестов
test:
	@echo "$(GREEN)Запуск тестов...$(NC)"
	$(PYTHON) -m pytest tests/ -v

# Очистка временных файлов
clean:
	@echo "$(GREEN)Очистка временных файлов...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type f -name "*.pyd" -delete 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true

# Сборка Docker образа
docker-build:
	@echo "$(GREEN)Сборка Docker образа...$(NC)"
	docker build -t $(IMAGE_NAME) .

# Запуск бота в Docker
docker-run: docker-build
	@echo "$(GREEN)Запуск бота в Docker...$(NC)"
	@if [ ! -f .env ]; then \
		echo "$(RED)Ошибка: Файл .env не найден!$(NC)"; \
		echo "$(YELLOW)Создайте .env файл с токенами BOT_TOKEN и OPENROUTER_API_KEY$(NC)"; \
		exit 1; \
	fi
	docker run -d \
		--name $(CONTAINER_NAME) \
		--env-file .env \
		--restart unless-stopped \
		$(IMAGE_NAME)
	@echo "$(GREEN)Контейнер запущен: $(CONTAINER_NAME)$(NC)"

# Остановка Docker контейнера
docker-stop:
	@echo "$(GREEN)Остановка Docker контейнера...$(NC)"
	docker stop $(CONTAINER_NAME) 2>/dev/null || true
	docker rm $(CONTAINER_NAME) 2>/dev/null || true

# Просмотр логов Docker контейнера
docker-logs:
	@echo "$(GREEN)Логи Docker контейнера:$(NC)"
	docker logs -f $(CONTAINER_NAME)

# Удаление Docker образа и контейнера
docker-clean: docker-stop
	@echo "$(GREEN)Удаление Docker образа...$(NC)"
	docker rmi $(IMAGE_NAME) 2>/dev/null || true

# Полная сборка и тестирование
all: clean dev-install test docker-build
	@echo "$(GREEN)Полная сборка завершена!$(NC)"

# Проверка статуса
status:
	@echo "$(GREEN)Статус системы:$(NC)"
	@echo "Python версия: $$($(PYTHON) --version)"
	@echo "Pip версия: $$($(PIP) --version)"
	@if docker --version >/dev/null 2>&1; then \
		echo "Docker версия: $$(docker --version)"; \
	else \
		echo "$(YELLOW)Docker не установлен$(NC)"; \
	fi
	@if [ -f .env ]; then \
		echo "$(GREEN)Файл .env найден$(NC)"; \
	else \
		echo "$(RED)Файл .env отсутствует$(NC)"; \
	fi 