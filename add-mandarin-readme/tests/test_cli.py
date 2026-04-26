import pytest
from click.testing import CliRunner
from unittest.mock import AsyncMock, MagicMock
from add_mandarin_readme.cli import main

def test_cli_basic(mocker, tmp_path):
    # Setup mock file
    input_file = tmp_path / "README.md"
    input_file.write_text("English content", encoding="utf-8")
    output_file = tmp_path / "README.zh-CN.md"
    
    # Mock settings to avoid missing API key error
    mock_settings = MagicMock()
    mock_settings.openai_api_key = "fake_key"
    mock_settings.openai_base_url = "https://api.openai.com/v1"
    mock_settings.model_name = "gpt-4o"
    mocker.patch("add_mandarin_readme.cli.get_settings", return_value=mock_settings)
    mocker.patch("add_mandarin_readme.cli.load_dotenv")
    
    # Mock TranslationAgent.translate_stream
    async def mock_stream(text):
        yield "Translated content"
        
    mock_agent_instance = MagicMock()
    mock_agent_instance.translate_stream = mock_stream
    mocker.patch("add_mandarin_readme.cli.TranslationAgent", return_value=mock_agent_instance)
    
    runner = CliRunner()
    result = runner.invoke(main, ["--input", str(input_file), "--output", str(output_file)])
    
    assert result.exit_code == 0
    assert "Success!" in result.output
    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8") == "Translated content"
