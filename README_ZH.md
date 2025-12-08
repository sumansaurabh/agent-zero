<div align="center">

![Agent Zero](/docs/res/header.png)

# `Agent Zero`

[![感谢赞助商](https://img.shields.io/badge/GitHub%20Sponsors-Thanks%20to%20Sponsors-FF69B4?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/frdel) [![加入我们的Skool社区](https://img.shields.io/badge/Skool-Join%20our%20Community-4A90E2?style=for-the-badge&logo=skool&logoColor=white)](https://www.skool.com/agent-zero) [![加入我们的Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/B8KZKNsPpj) [![在YouTube上订阅](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AgentZeroFW) [![在LinkedIn上联系](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jan-tomasek/) [![在Warpcast上关注](https://img.shields.io/badge/Warpcast-Follow-5A32F3?style=for-the-badge)](https://warpcast.com/agent-zero)

> **注意：** Agent Zero不使用Twitter/X。任何声称代表此项目的Twitter/X账号都是假冒的。

[安装指南](./docs/installation.md) •
[如何更新](./docs/installation.md#how-to-update-agent-zero) •
[文档](./docs/README.md) •
[使用说明](./docs/usage.md)

</div>


[![展示](/docs/res/showcase-thumb.png)](https://youtu.be/lazLNcEYsiQ)



访问 [www.agent-zero.ai](https://agent-zero.ai) 了解更多信息

[![浏览器代理](/docs/res/web_screenshot.jpg)](https://agent-zero.ai)



> [!NOTE]
> **🎉 v0.8.1 版本发布**：现在具备浏览器代理功能，能够使用Chromium进行网络交互！这使Agent Zero能够自主浏览网页、收集信息并与网络内容互动。


https://github.com/user-attachments/assets/c168759d-57d8-4b43-b62a-1026afcf52e6

## 一个与你一起成长和学习的个人有机代理框架

- Agent Zero不是一个预定义的代理框架。它被设计为动态的、有机成长的，并在你使用它的过程中不断学习。
- Agent Zero完全透明、可读、可理解、可定制且具有交互性。
- Agent Zero将计算机作为工具来完成它（你的）任务。

# 💡 核心特性

1. **通用助手**

- Agent Zero不是为特定任务预编程的（但可以这样做）。它旨在成为一个通用的个人助手。给它一个任务，它将收集信息、执行命令和代码、与其他代理实例协作，并尽最大努力完成任务。
- 它具有持久记忆，允许它记住以前的解决方案、代码、事实、指令等，以便将来更快更可靠地解决任务。

![Agent 0工作中](/docs/res/ui-screen-2.png)

2. **将计算机作为工具**

- Agent Zero使用操作系统作为工具来完成任务。它没有预编程的单一用途工具。相反，它可以编写自己的代码并使用终端根据需要创建和使用自己的工具。
- 它的默认工具集中唯一的工具是在线搜索、记忆功能、通信（与用户和其他代理）以及代码/终端执行。其他一切都由代理本身创建，或者可以由用户扩展。
- 工具使用功能是从零开发的，即使是非常小的模型也能实现最大的兼容性和可靠性。
- **默认工具：** Agent Zero包含知识、网页内容、代码执行和通信等工具。
- **创建自定义工具：** 通过创建自己的自定义工具来扩展Agent Zero的功能。
- **Instruments：** Instruments是一种新型工具，允许你创建可由Agent Zero调用的自定义函数和过程。

3. **多代理协作**

- 每个代理都有一个上级代理给它分配任务和指令。然后每个代理向其上级报告。
- 对于链中的第一个代理（Agent 0），上级是人类用户；代理看不出任何区别。
- 每个代理都可以创建其下级代理来帮助分解和解决子任务。这有助于所有代理保持其上下文清晰和集中。

![多代理](docs/res/physics.png)
![多代理2](docs/res/physics-2.png)

4. **完全可定制和可扩展**

- 这个框架中几乎没有硬编码的内容。没有隐藏的东西。一切都可以由用户扩展或更改。
- 整个行为由**prompts/default/agent.system.md**文件中的系统提示定义。更改此提示，框架将发生巨大变化。
- 框架不以任何方式引导或限制代理。没有代理必须遵循的硬编码规则。
- 发送给代理在其通信循环中的每个提示、每个小消息模板都可以在**prompts/**文件夹中找到并更改。
- 每个默认工具都可以在**python/tools/**文件夹中找到，并可以更改或复制以创建新的预定义工具。

![提示](/docs/res/prompts.png)

5. **沟通是关键**

- 给你的代理一个适当的系统提示和指令，它可以创造奇迹。
- 代理可以与其上级和下级沟通，提出问题、给出指令并提供指导。在系统提示中指导你的代理如何有效沟通。
- 终端界面是实时流式传输和交互式的。你可以随时停止和干预。如果你看到你的代理朝错误的方向前进，只需立即停止并告诉它。
- 这个框架有很大的自由度。你可以指示你的代理定期向上级报告，要求继续许可。你可以指示他们在决定何时委派子任务时使用评分系统。上级可以双重检查下级的结果并提出异议。可能性是无限的。

## 🚀 你可以用Agent Zero构建的东西

- **开发项目** - `"创建一个带有实时数据可视化的React仪表板"`

- **数据分析** - `"分析上季度的NVIDIA销售数据并创建趋势报告"`

- **内容创作** - `"写一篇关于微服务的技术博客文章"`

- **系统管理** - `"为我们的Web服务器设置监控系统"`

- **研究** - `"收集并总结五篇关于CoT提示的最新AI论文"`

# ⚙️ 安装

点击打开视频学习如何安装Agent Zero：

[![测试视频](/docs/res/new_vid.jpg)](https://www.youtube.com/watch?v=cHDCCSr1YRI&t=24s)

Windows、macOS和Linux的详细设置指南以及视频可以在Agent Zero文档的[此页面](./docs/installation.md)中找到。

### ⚡ 快速开始

```bash
# 使用Docker拉取并运行

docker pull frdel/agent-zero-run
docker run -p 50001:80 frdel/agent-zero-run

# 访问 http://localhost:50001 开始使用
```

- 开发者和贡献者：从[发布页面](https://github.com/frdel/agent-zero/releases)下载适用于你系统的完整二进制文件，然后按照[此处提供的说明](./docs/installation.md#in-depth-guide-for-full-binaries-installation)操作。

## 🐳 完全Docker化，支持语音转文本和文本转语音

![设置](docs/res/settings-page-ui.png)

- 可自定义的设置允许用户根据需要调整代理的行为和响应。
- Web UI输出非常清晰、流畅、多彩、可读且交互式；没有任何隐藏内容。
- 你可以直接在Web UI中加载或保存聊天记录。
- 你在终端中看到的相同输出会自动保存到**logs/**文件夹中的HTML文件，每个会话一个。

![时间示例](/docs/res/time_example.jpg)

- 代理输出是实时流式传输的，允许用户随时阅读并干预。
- 不需要编码；只需要提示和沟通技巧。
- 使用可靠的系统提示，即使是小型模型，框架也很可靠，包括精确的工具使用。

## 👀 请记住

1. **Agent Zero可能很危险！**

- 在适当的指导下，Agent Zero能够做很多事情，甚至可能对你的计算机、数据或账户造成危险的操作。始终在隔离环境（如Docker）中运行Agent Zero，并小心你的要求。

2. **Agent Zero基于提示。**

- 整个框架由**prompts/**文件夹引导。代理指南、工具说明、消息、实用AI功能，都在那里。


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

- **知识和RAG工具**
- **计划和调度**

> [!IMPORTANT]
>
>**自v0.7以来frdel/agent-zero Docker镜像的更改：**
>
> 新的Docker镜像`frdel/agent-zero-run`提供了新的统一环境。

### v0.8.1
- **浏览器代理**
- **用户体验改进**

### v0.8

- **Docker运行时**
- **新的消息历史和摘要系统**
- **代理行为更改和管理**
- **文本转语音（TTS）和语音转文本（STT）**
- **Web UI中的设置页面**
- **SearXNG集成替代Perplexity + DuckDuckGo**
- **文件浏览器功能**
- **KaTeX数学可视化支持**
- **聊天中的文件附件**

### v0.7

- **自动记忆**
- **UI改进**
- **Instruments**
- **扩展框架**
- **反思提示**
- **Bug修复**

## 🤝 社区和支持

- [加入我们的Discord](https://discord.gg/B8KZKNsPpj)进行实时讨论或[访问我们的Skool社区](https://www.skool.com/agent-zero)。
- [关注我们的YouTube频道](https://www.youtube.com/@AgentZeroFW)获取实践解释和教程
- [报告问题](https://github.com/frdel/agent-zero/issues)以进行错误修复和功能请求
