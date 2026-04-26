# add-mandarin-readme

`add-mandarin-readme` 是一个生产级别的命令行工具和 AI 代理，它可以自动将您项目的英文 `README.md` 通过大语言模型（LLM）翻译成高质量、地道的中文版本（`README.zh-CN.md`）。

## 特性

- **高质量**: 使用 GPT-4o（或其他 LLM）进行地道的翻译。
- **保留 Markdown 格式**: 完美保留所有格式、代码块和 URL。
- **实时反馈**: 在终端中通过精美的格式流式输出结果。
- **简单配置**: 通过环境变量或 CLI 标志轻松设置。

## 安装

确保您已安装 [Poetry](https://python-poetry.org/)。

```bash
git clone https://github.com/sumansaurabh/agent-zero.git
cd agent-zero/add-mandarin-readme
poetry install
```

## 设置

1. 将 `.env.example` 复制为 `.env`：
   ```bash
   cp .env.example .env
   ```
2. 在 `.env` 文件中添加您的 OpenAI API 密钥：
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

## 使用方法

使用 poetry 运行该工具：

```bash
poetry run add-mandarin-readme --input README.md --output README.zh-CN.md
```

### 命令行选项

- `--input`, `-i`: 源 README 的路径（默认：`README.md`）。
- `--output`, `-o`: 保存翻译后的 README 的路径（默认：`README.zh-CN.md`）。
- `--model`, `-m`: 要使用的 LLM 模型（默认：`gpt-4o`）。
- `--api-key`: 可选的 API 密钥覆盖。

## 开发

使用 pytest 运行测试：

```bash
poetry run pytest
```
