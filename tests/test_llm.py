import pytest
from unittest.mock import patch
from llm.client import get_llm_response

@pytest.mark.asyncio
async def test_llm_simple_response():
    """Тест простого запроса к LLM"""
    dialog = [
        {"role": "system", "content": "Ты помощник"},
        {"role": "user", "content": "Привет"}
    ]
    
    response = await get_llm_response(dialog)
    assert isinstance(response, str)
    assert len(response) > 0

@pytest.mark.asyncio
async def test_llm_error_handling():
    """Тест обработки ошибок LLM"""
    dialog = []
    
    response = await get_llm_response(dialog)
    assert isinstance(response, str)
    assert len(response) > 0

@pytest.mark.asyncio
async def test_llm_with_empty_key():
    """Тест работы с пустым API ключом"""
    with patch('llm.client.OPENROUTER_API_KEY', None):
        dialog = [{"role": "user", "content": "test"}]
        response = await get_llm_response(dialog)
        assert "OpenRouter API ключ не настроен" in response 