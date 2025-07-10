import pytest
from bot.handlers import echo_handler

def test_bot_import():
    """ТЕСТ базового импорта модулей"""
    assert echo_handler is not None 