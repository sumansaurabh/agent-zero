<div align="center">

![Agent Zero](/docs/res/header.png)

# `Agent Zero`

[![感谢赞助商](https://img.shields.io/badge/GitHub%20Sponsors-感谢赞助商-FF69B4?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/frdel) [![加入我们的 Skool 社区](https://img.shields.io/badge/Skool-加入我们的社区-4A90E2?style=for-the-badge&logo=skool&logoColor=white)](https://www.skool.com/agent-zero) [![加入我们的 Discord](https://img.shields.io/badge/Discord-加入我们的服务器-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/B8KZKNsPpj) [![在 YouTube 订阅](https://img.shields.io/badge/YouTube-订阅-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AgentZeroFW) [![在 LinkedIn 关注](https://img.shields.io/badge/LinkedIn-关注-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jan-tomasek/) [![在 Warpcast 关注](https://img.shields.io/badge/Warpcast-关注-5A32F3?style=for-the-badge)](https://warpcast.com/agent-zero)

> **注意：** Agent Zero 不使用 Twitter/X。任何声称代表本项目的 Twitter/X 账号都是假的。

[安装指南](./docs/installation.md) •
[如何更新](./docs/installation.md#how-to-update-agent-zero) •
[文档](./docs/README.md) •
[使用方法](./docs/usage.md)

</div>


[![展示](/docs/res/showcase-thumb.png)](https://youtu.be/lazLNcEYsiQ)



访问 [www.agent-zero.ai](https://agent-zero.ai) 获取更多信息

[![浏览器代理](/docs/res/web_screenshot.jpg)](https://agent-zero.ai)



> [!NOTE]
> **🎉 v0.8.1 发布**: 现在提供可使用 Chromium 进行网页交互的浏览器代理！这使得 Agent Zero 能够自主浏览网页、收集信息并与网页内容进行交互。


https://github.com/user-attachments/assets/c168759d-57d8-4b43-b62a-1026afcf52e6

## 一个与您一起成长和学习的个人化、有机的智能体框架

- Agent Zero 不是一个预定义的智能体框架。它被设计为动态的、有机成长的,并随着您的使用而学习。
- Agent Zero 完全透明、可读、可理解、可定制且具有交互性。
- Agent Zero 将计算机作为工具来完成它的(您的)任务。

# 💡 核心功能

1. **通用助手**

- Agent Zero 不是为特定任务预编程的(但可以做到)。它旨在成为一个通用的个人助手。给它一个任务,它会收集信息、执行命令和代码、与其他智能体实例协作,并尽力完成任务。
- 它具有持久性记忆,允许它记住以前的解决方案、代码、事实、指令等,以便将来更快、更可靠地解决任务。

![Agent 0 工作中](/docs/res/ui-screen-2.png)

2. **将计算机作为工具**

- Agent Zero 使用操作系统作为工具来完成其任务。它没有预编程的单一用途工具。相反,它可以编写自己的代码并使用终端根据需要创建和使用自己的工具。
- 其工具库中唯一的默认工具是在线搜索、记忆功能、通信(与用户和其他智能体)以及代码/终端执行。其他一切都由智能体本身创建,或者可以由用户扩展。
- 工具使用功能从头开发,即使是非常小的模型也能实现最佳兼容性和可靠性。
- **默认工具:** Agent Zero 包含知识、网页内容、代码执行和通信等工具。
- **创建自定义工具:** 通过创建自己的自定义工具来扩展 Agent Zero 的功能。
- **仪器:** 仪器是一种新型工具,允许您创建可由 Agent Zero 调用的自定义函数和程序。

3. **多智能体协作**

- 每个智能体都有一个上级智能体给它分配任务和指令。然后每个智能体向其上级报告。
- 对于链中的第一个智能体(Agent 0),上级是人类用户;智能体看不出有什么区别。
- 每个智能体都可以创建其下属智能体来帮助分解和解决子任务。这有助于所有智能体保持上下文清晰和专注。

![多智能体](docs/res/physics.png)
![多智能体 2](docs/res/physics-2.png)

4. **完全可定制和可扩展**

- 这个框架中几乎没有硬编码的内容。没有隐藏的东西。用户可以扩展或更改一切。
- 整个行为由 **prompts/default/agent.system.md** 文件中的系统提示定义。更改此提示可以大大改变框架。
- 该框架不会以任何方式引导或限制智能体。没有硬编码的规则要求智能体必须遵循。
- 每个提示、在智能体通信循环中发送给它的每个小消息模板都可以在 **prompts/** 文件夹中找到并更改。
- 每个默认工具都可以在 **python/tools/** 文件夹中找到,并且可以更改或复制以创建新的预定义工具。

![提示](/docs/res/prompts.png)

5. **沟通是关键**

- 给您的智能体一个适当的系统提示和指令,它可以创造奇迹。
- 智能体可以与其上级和下属沟通,提出问题、给出指令并提供指导。在系统提示中指导您的智能体如何有效沟通。
- 终端界面是实时流式传输和交互式的。您可以随时停止和干预。如果您看到您的智能体朝着错误的方向前进,只需立即停止并告诉它。
- 这个框架有很大的自由度。您可以指导您的智能体定期向上级报告,请求继续的许可。您可以指导他们在决定何时委派子任务时使用评分系统。上级可以仔细检查下属的结果并提出异议。可能性是无限的。

## 🚀 您可以使用 Agent Zero 构建的东西

- **开发项目** - `"创建一个具有实时数据可视化的 React 仪表板"`

- **数据分析** - `"分析上季度的英伟达销售数据并创建趋势报告"`

- **内容创作** - `"撰写一篇关于微服务的技术博客文章"`

- **系统管理** - `"为我们的网络服务器设置监控系统"`

- **研究** - `"收集并总结五篇关于 CoT 提示的最新 AI 论文"`

# ⚙️ 安装

点击打开视频学习如何安装 Agent Zero:

[![测试视频](/docs/res/new_vid.jpg)](https://www.youtube.com/watch?v=cHDCCSr1YRI&t=24s)

Windows、macOS 和 Linux 的详细设置指南及视频可以在 Agent Zero 文档的[此页面](./docs/installation.md)中找到。

### ⚡ 快速开始

```bash
# 使用 Docker 拉取并运行

docker pull frdel/agent-zero-run
docker run -p 50001:80 frdel/agent-zero-run

# 访问 http://localhost:50001 开始使用
```

- 开发者和贡献者: 从[发布页面](https://github.com/frdel/agent-zero/releases)下载适用于您系统的完整二进制文件,然后按照[此处提供的说明](./docs/installation.md#in-depth-guide-for-full-binaries-installation)进行操作。

## 🐳 完全 Docker 化,支持语音转文本和文本转语音

![设置](docs/res/settings-page-ui.png)

- 可自定义的设置允许用户根据需要调整智能体的行为和响应。
- Web UI 输出非常简洁、流畅、色彩丰富、可读且具有交互性;没有任何隐藏内容。
- 您可以直接在 Web UI 中加载或保存聊天记录。
- 您在终端中看到的相同输出会自动保存到 **logs/** 文件夹中的 HTML 文件中,用于每个会话。

![时间示例](/docs/res/time_example.jpg)

- 智能体输出是实时流式传输的,允许用户随时阅读并进行干预。
- 不需要编码;只需要提示和沟通技巧。
- 通过可靠的系统提示,即使使用小型模型,该框架也很可靠,包括精确的工具使用。

## 👀 请记住

1. **Agent Zero 可能很危险!**

- 通过适当的指令,Agent Zero 能够做很多事情,甚至可能对您的计算机、数据或账户采取潜在危险的行动。始终在隔离环境(如 Docker)中运行 Agent Zero,并小心您的请求。

2. **Agent Zero 基于提示。**

- 整个框架由 **prompts/** 文件夹引导。智能体指南、工具说明、消息、实用 AI 功能,都在那里。


## 📚 阅读文档

| 页面 | 描述 |
|-------|-------------|
| [安装](./docs/installation.md) | 安装、设置和配置 |
| [使用](./docs/usage.md) | 基本和高级使用 |
| [架构](./docs/architecture.md) | 系统设计和组件 |
| [贡献](./docs/contributing.md) | 如何贡献 |
| [故障排除](./docs/troubleshooting.md) | 常见问题及其解决方案 |

## 🎯 更新日志

### 即将推出

- **知识和 RAG 工具**
- **计划和调度**

> [!IMPORTANT]
>
>**自 v0.7 以来对 frdel/agent-zero Docker 镜像的更改:**
>
> 新的 Docker 镜像 `frdel/agent-zero-run` 提供了新的统一环境。

### v0.8.1
- **浏览器代理**
- **用户体验改进**

### v0.8

- **Docker 运行时**
- **新的消息历史和摘要系统**
- **智能体行为更改和管理**
- **文本转语音 (TTS) 和语音转文本 (STT)**
- **Web UI 中的设置页面**
- **SearXNG 集成替代 Perplexity + DuckDuckGo**
- **文件浏览器功能**
- **KaTeX 数学可视化支持**
- **聊天中的文件附件**

### v0.7

- **自动记忆**
- **UI 改进**
- **仪器**
- **扩展框架**
- **反思提示**
- **错误修复**

## 🤝 社区和支持

- [加入我们的 Discord](https://discord.gg/B8KZKNsPpj) 进行实时讨论或[访问我们的 Skool 社区](https://www.skool.com/agent-zero)。
- [关注我们的 YouTube 频道](https://www.youtube.com/@AgentZeroFW) 获取实践说明和教程
- [报告问题](https://github.com/frdel/agent-zero/issues) 进行错误修复和功能请求
