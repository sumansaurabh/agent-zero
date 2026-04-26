# add-mandarin-readme

`add-mandarin-readme` is a production-ready CLI tool and AI agent that automatically translates your project's English `README.md` into high-quality, idiomatic Mandarin Chinese (`README.zh-CN.md`) using an LLM.

## Features

- **High Quality**: Uses GPT-4o (or other LLMs) for idiomatic translations.
- **Markdown Preservation**: Maintains all formatting, code blocks, and URLs.
- **Real-time Feedback**: Streaming output to the terminal with beautiful formatting.
- **Easy Configuration**: Simple setup via environment variables or CLI flags.

## Installation

Ensure you have [Poetry](https://python-poetry.org/) installed.

```bash
git clone https://github.com/sumansaurabh/agent-zero.git
cd agent-zero/add-mandarin-readme
poetry install
```

## Setup

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Add your OpenAI API key to the `.env` file:
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the tool using poetry:

```bash
poetry run add-mandarin-readme --input README.md --output README.zh-CN.md
```

### CLI Options

- `--input`, `-i`: Path to the source README (default: `README.md`).
- `--output`, `-o`: Path to save the translated README (default: `README.zh-CN.md`).
- `--model`, `-m`: LLM model to use (default: `gpt-4o`).
- `--api-key`: Optional API key override.

## Development

Run tests using pytest:

```bash
poetry run pytest
```
