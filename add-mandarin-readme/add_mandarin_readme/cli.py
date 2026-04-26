import asyncio
import click
from dotenv import load_dotenv
from rich.console import Console
from rich.status import Status
from rich.live import Live
from rich.markdown import Markdown

from .config import get_settings, Settings
from .file_handler import read_readme, write_readme
from .agent import TranslationAgent

async def run_translation(input_path: str, output_path: str, model: str, api_key: str):
    load_dotenv()
    
    settings = get_settings()
    if api_key:
        settings.openai_api_key = api_key
    if model:
        settings.model_name = model

    console = Console()
    
    try:
        content = read_readme(input_path)
    except FileNotFoundError as e:
        console.print(f"[red]{e}[/red]")
        return

    agent = TranslationAgent(settings)
    
    full_translation = ""
    
    console.print(f"[bold blue]Translating README from {input_path} to {output_path} using {settings.model_name}...[/bold blue]")
    
    with Status("Processing...", console=console) as status:
        with Live("", console=console, refresh_per_second=4) as live:
            async for chunk in agent.translate_stream(content):
                full_translation += chunk
                live.update(Markdown(full_translation))
    
    write_readme(output_path, full_translation)
    console.print(f"\n[bold green]Success![/bold green] Translated README saved to [cyan]{output_path}[/cyan]")

@click.command()
@click.option("--input", "-i", default="README.md", help="Path to the source README (default: README.md)")
@click.option("--output", "-o", default="README.zh-CN.md", help="Path to save the translated README (default: README.zh-CN.md)")
@click.option("--model", "-m", help="LLM model to use (default: from config or gpt-4o)")
@click.option("--api-key", help="OpenAI API key override")
def main(input: str, output: str, model: str, api_key: str):
    """Automatically translate your README.md to Mandarin Chinese."""
    asyncio.run(run_translation(input, output, model, api_key))

if __name__ == "__main__":
    main()
