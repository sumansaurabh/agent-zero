from typing import AsyncGenerator
from openai import AsyncOpenAI, APIError, RateLimitError
from rich.console import Console
from .config import Settings
from .prompts import SYSTEM_PROMPT, get_user_prompt

class TranslationAgent:
    def __init__(self, settings: Settings):
        self.client = AsyncOpenAI(
            api_key=settings.openai_api_key,
            base_url=settings.openai_base_url
        )
        self.model = settings.model_name
        self.console = Console()

    async def translate_stream(self, text: str) -> AsyncGenerator[str, None]:
        try:
            stream = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": get_user_prompt(text)},
                ],
                stream=True,
            )

            async for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content

        except RateLimitError:
            self.console.print("[red]Error: Rate limit exceeded. Please try again later.[/red]")
            raise
        except APIError as e:
            self.console.print(f"[red]Error: OpenAI API returned an error: {e}[/red]")
            raise
        except Exception as e:
            self.console.print(f"[red]Error: An unexpected error occurred: {e}[/red]")
            raise
