<div align="center">

![Agent Zero](/docs/res/header.png)

# `Agent Zero`

[![Thanks to Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Thanks%20to%20Sponsors-FF69B4?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/frdel) [![Join our Skool Community](https://img.shields.io/badge/Skool-Join%20our%20Community-4A90E2?style=for-the-badge&logo=skool&logoColor=white)](https://www.skool.com/agent-zero) [![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/B8KZKNsPpj) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AgentZeroFW) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jan-tomasek/) [![Follow on Warpcast](https://img.shields.io/badge/Warpcast-Follow-5A32F3?style=for-the-badge)](https://warpcast.com/agent-zero)

> **注意：** Agent Zero 不使用 Twitter/X。任何声称代表此项目的 Twitter/X 账户均为虚假账户。

[安装](./docs/installation.md) •
[如何更新](./docs/installation.md#how-to-update-agent-zero) •
[文档](./docs/README.md) •
[使用方法](./docs/usage.md)

</div>


[![Showcase](/docs/res/showcase-thumb.png)](https://youtu.be/lazLNcEYsiQ)



访问 [www.agent-zero.ai](https://agent-zero.ai) 获取更多信息

[![Browser Agent](/docs/res/web_screenshot.jpg)](https://agent-zero.ai)



> [!NOTE]
> **🎉 v0.8.1 发布**：现在推出浏览器代理，能够使用 Chromium 进行网页交互！这使得 Agent Zero 能够自主浏览网页、收集信息并与网页内容互动。


https://github.com/user-attachments/assets/c168759d-57d8-4b43-b62a-1026afcf52e6

## 一个与您共同成长和学习的个人有机代理框架

- Agent Zero 不是一个预定义的代理框架。它旨在动态、有机地成长，并随着您的使用而学习。
- Agent Zero 完全透明、可读、易懂、可定制且具有交互性。
- Agent Zero 将计算机作为工具来完成其（您的）任务。

# 💡 主要功能

1. **通用助手**

- Agent Zero 未预设特定任务（但可以设置）。它旨在成为一个通用的个人助手。给它一个任务，它将收集信息、执行命令和代码、与其他代理实例协作，并尽力完成任务。
- 它具有持久记忆，使其能够记住以前的解决方案、代码、事实、指令等，以便将来更快、更可靠地解决任务。

![Agent 0 Working](/docs/res/ui-screen-2.png)

2. **计算机作为工具**

- Agent Zero 使用操作系统作为工具来完成其任务。它没有预设的单一用途工具。相反，它可以编写自己的代码并使用终端根据需要创建和使用自己的工具。
- 其工具库中唯一的默认工具是在线搜索、记忆功能、通信（与用户和其他代理）以及代码/终端执行。其他一切都由代理本身创建，或者可以由用户扩展。
- 工具使用功能已从头开发，即使对于非常小的模型也具有最佳兼容性和可靠性。
- **默认工具：** Agent Zero 包括知识、网页内容、代码执行和通信等工具。
- **创建自定义工具：** 通过创建自己的自定义工具来扩展 Agent Zero 的功能。
- **仪器：** 仪器是一种新型工具，允许您创建可由 Agent Zero 调用的自定义函数和过程。

3. **多代理协作**

- 每个代理都有一个上级代理为其分配任务和指令。然后每个代理向上级报告。
- 在链中的第一个代理（Agent 0）的情况下，上级是人类用户；代理没有区别。
- 每个代理都可以创建其下级代理来帮助分解和解决子任务。这有助于所有代理保持其上下文清晰和专注。

![Multi-agent](docs/res/physics.png)
![Multi-agent 2](docs/res/physics-2.png)

4. **完全可定制和可扩展**

- 这个框架中几乎没有任何东西是硬编码的。没有任何东西是隐藏的。一切都可以由用户扩展或更改。
- 整个行为由 **prompts/default/agent.system.md** 文件中的系统提示定义。更改此提示将显著改变框架。
- 框架不以任何方式引导或限制代理。没有代理必须遵循的硬编码轨道。
- 发送给代理通信循环中的每个提示、每个小消息模板都可以在 **prompts/** 文件夹中找到并更改。
- 每个默认工具都可以在 **python/tools/** 文件夹中找到并更改或复制以创建新的预定义工具。

![Prompts](/docs/res/prompts.png)

5. **沟通是关键**

- 给您的代理一个适当的系统提示和指令，它就能创造奇迹。
- 代理可以与它们的上级和下级沟通，提问、给出指令和提供指导。在系统提示中指导您的代理如何有效沟通。
- 终端界面是实时流式传输和交互式的。您可以随时停止和干预。如果您看到您的代理方向错误，请立即停止并告知它。
- 这个框架有很多自由度。您可以指示您的代理定期向上级报告，请求继续的许可。您可以指示它们在决定何时委派子任务时使用积分系统。上级可以复核下级的成果并提出异议。可能性是无限的。

## 🚀 您可以使用 Agent Zero 构建的东西

- **开发项目** - `"创建一个带有实时数据可视化的 React 仪表板"`

- **数据分析** - `"分析上季度 NVIDIA 销售数据并创建趋势报告"`

- **内容创作** - `"撰写一篇关于微服务的技术博客文章"`

- **系统管理** - `"为我们的网络服务器设置一个监控系统"`

- **研究** - `"收集并总结五篇关于 CoT 提示的最新 AI 论文"`

# ⚙️ 安装

点击观看视频，了解如何安装 Agent Zero：

[![Testing Video](/docs/res/new_vid.jpg)](https://www.youtube.com/watch?v=cHDCCSr1YRI&t=24s)

Agent Zero 文档的 [此页面](./docs/installation.md) 提供了 Windows、macOS 和 Linux 的详细设置指南和视频。

### ⚡ 快速开始

```bash
# 使用 Docker 拉取并运行

docker pull frdel/agent-zero-run
docker run -p 50001:80 frdel/agent-zero-run

# 访问 http://localhost:50001 开始
```

- 开发人员和贡献者：从 [发布页面](https://github.com/frdel/agent-zero/releases) 下载适用于您系统的完整二进制文件，然后按照 [此处提供](https://github.com/frdel/agent-zero/releases) 的说明进行操作。

## 🐳 完全 Docker 化，支持语音转文本和文本转语音

![Settings](docs/res/settings-page-ui.png)

- 可定制的设置允许用户根据自己的需求调整代理的行为和响应。
- Web UI 输出非常清晰、流畅、多彩、可读且具有交互性；没有任何隐藏。
- 您可以直接在 Web UI 中加载或保存聊天。
- 您在终端中看到的相同输出会自动保存到每个会话的 **logs/** 文件夹中的 HTML 文件中。

![Time example](/docs/res/time_example.jpg)

- 代理输出实时流式传输，允许用户随时阅读并干预。
- 无需编码；只需提示和沟通技巧。
- 凭借可靠的系统提示，即使对于小型模型，该框架也可靠，包括精确的工具使用。

## 👀 请记住

1. **Agent Zero 可能很危险！**

- 通过适当的指令，Agent Zero 能够做很多事情，甚至可能对您的计算机、数据或账户造成潜在危险。始终在隔离环境（如 Docker）中运行 Agent Zero，并小心您的愿望。

2. **Agent Zero 是基于提示的。**

- 整个框架由 **prompts/** 文件夹引导。代理指南、工具指令、消息、实用 AI 功能，都在那里。


## 📚 阅读文档

| 页面 | 描述 |
|-------|-------------|
| [安装](./docs/installation.md) | 安装、设置和配置 |
| [使用方法](./docs/usage.md) | 基本和高级使用 |
| [架构](./docs/architecture.md) | 系统设计和组件 |
| [贡献](./docs/contributing.md) | 如何贡献 |
| [故障排除](./docs/troubleshooting.md) | 常见问题及其解决方案 |

## 🎯 更新日志

### 即将推出

- **知识和 RAG 工具**
- **规划和调度**

> [!IMPORTANT]
>
>**自 v0.7 以来 frdel/agent-zero Docker 镜像的更改：**
>
> 新的 Docker 镜像 `frdel/agent-zero-run` 提供了新的统一环境。

### v0.8.1
- **浏览器代理**
- **用户体验改进**

### v0.8

- **Docker 运行时**
- **新消息历史和摘要系统**
- **代理行为更改和管理**
- **文本转语音 (TTS) 和语音转文本 (STT)**
- **Web UI 中的设置页面**
- **SearXNG 集成取代 Perplexity + DuckDuckGo**
- **文件浏览器功能**
- **KaTeX 数学可视化支持**
- **聊天内文件附件**

### v0.7

- **自动记忆**
- **UI 改进**
- **仪器**
- **扩展框架**
- **反思提示**
- **错误修复**

## 🤝 社区与支持

- 加入我们的 [Discord](https://discord.gg/B8KZKNsPpj) 进行实时讨论，或访问我们的 [Skool 社区](https://www.skool.com/agent-zero)。
- 关注我们的 [YouTube 频道](https://www.youtube.com/@AgentZeroFW) 获取实践解释和教程
- [报告问题](https://github.com/frdel/agent-zero/issues) 以获取错误修复和功能
