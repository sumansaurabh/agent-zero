import pytest
from unittest.mock import AsyncMock, MagicMock
from add_mandarin_readme.agent import TranslationAgent
from add_mandarin_readme.config import Settings

@pytest.mark.asyncio
async def test_translate_stream(mocker):
    # Mock settings
    settings = Settings(openai_api_key="fake_key", model_name="gpt-4o")
    
    # Mock AsyncOpenAI
    mock_client = MagicMock()
    mocker.patch("add_mandarin_readme.agent.AsyncOpenAI", return_value=mock_client)
    
    # Mock the stream response
    mock_stream = AsyncMock()
    mock_client.chat.completions.create = AsyncMock(return_value=mock_stream)
    
    # Mock chunks
    chunk1 = MagicMock()
    chunk1.choices = [MagicMock(delta=MagicMock(content="Hello"))]
    chunk2 = MagicMock()
    chunk2.choices = [MagicMock(delta=MagicMock(content=" World"))]
    
    mock_stream.__aiter__.return_value = [chunk1, chunk2]
    
    agent = TranslationAgent(settings)
    chunks = []
    async for chunk in agent.translate_stream("Test content"):
        chunks.append(chunk)
    
    assert chunks == ["Hello", " World"]
    mock_client.chat.completions.create.assert_called_once()
