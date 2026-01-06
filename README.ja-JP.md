<div align="center">

![Agent Zero](/docs/res/header.png)

# `Agent Zero`

[![Thanks to Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Thanks%20to%20Sponsors-FF69B4?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/frdel) [![Join our Skool Community](https://img.shields.io/badge/Skool-Join%20our%20Community-4A90E2?style=for-the-badge&logo=skool&logoColor=white)](https://www.skool.com/agent-zero) [![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/B8KZKNsPpj) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AgentZeroFW) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jan-tomasek/) [![Follow on Warpcast](https://img.shields.io/badge/Warpcast-Follow-5A32F3?style=for-the-badge)](https://warpcast.com/agent-zero)

> **注記:** Agent ZeroはTwitter/Xを使用していません。このプロジェクトを代表すると主張するTwitter/Xアカウントはすべて偽物です。

[インストール](./docs/installation.md) •
[更新方法](./docs/installation.md#how-to-update-agent-zero) •
[ドキュメント](./docs/README.md) •
[使用方法](./docs/usage.md)

</div>


[![Showcase](/docs/res/showcase-thumb.png)](https://youtu.be/lazLNcEYsiQ)



詳細については [www.agent-zero.ai](https://agent-zero.ai) をご覧ください

[![Browser Agent](/docs/res/web_screenshot.jpg)](https://agent-zero.ai)



> [!NOTE]
> **🎉 v0.8.1 リリース**: Chromiumを使用したウェブインタラクションが可能なブラウザエージェントを搭載！これにより、Agent Zeroはウェブを閲覧し、情報を収集し、ウェブコンテンツと自律的に対話できるようになります。


https://github.com/user-attachments/assets/c168759d-57d8-4b43-b62a-1026afcf52e6

## あなたと共に成長し学習する、個人的で有機的なエージェントフレームワーク

- Agent Zeroは、事前に定義されたエージェントフレームワークではありません。使用するにつれて動的に、有機的に成長し、学習するように設計されています。
- Agent Zeroは完全に透明で、読みやすく、理解しやすく、カスタマイズ可能で、インタラクティブです。
- Agent Zeroは、その（あなたの）タスクを達成するためのツールとしてコンピューターを使用します。

# 💡 主な機能

1. **汎用アシスタント**

- Agent Zeroは特定のタスク向けに事前にプログラムされていません（ただし、そうすることも可能です）。汎用的なパーソナルアシスタントとして機能することを意図しています。タスクを与えると、情報を収集し、コマンドとコードを実行し、他のエージェントインスタンスと協力し、それを達成するために最善を尽くします。
- 永続的なメモリを備えており、以前の解決策、コード、事実、指示などを記憶し、将来のタスクをより速く、より確実に解決できます。

![Agent 0 Working](/docs/res/ui-screen-2.png)

2. **ツールとしてのコンピューター**

- Agent Zeroは、タスクを達成するためのツールとしてオペレーティングシステムを使用します。事前にプログラムされた単一目的のツールはありません。代わりに、独自のコードを記述し、ターミナルを使用して必要に応じて独自のツールを作成および使用できます。
- その武器庫にある唯一のデフォルトツールは、オンライン検索、メモリ機能、通信（ユーザーおよび他のエージェントとの）、およびコード/ターミナル実行です。その他すべてはエージェント自身によって作成されるか、ユーザーによって拡張できます。
- ツール使用機能は、非常に小さなモデルでも最も互換性があり信頼できるように、ゼロから開発されました。
- **デフォルトツール:** Agent Zeroには、知識、ウェブページコンテンツ、コード実行、通信などのツールが含まれています。
- **カスタムツールの作成:** 独自のカスタムツールを作成して、Agent Zeroの機能を拡張します。
- **インストゥルメント:** インストゥルメントは、Agent Zeroによって呼び出すことができるカスタム関数とプロシージャを作成できる新しいタイプのツールです。

3. **マルチエージェント協力**

- すべてのエージェントには、タスクと指示を与える上位エージェントがいます。その後、すべてエージェントは上位エージェントに報告します。
- チェーンの最初のエージェント（Agent 0）の場合、上位エージェントは人間ユーザーであり、エージェントは違いを認識しません。
- すべてのエージェントは、サブタスクを分解して解決するのに役立つ下位エージェントを作成できます。これにより、すべてのエージェントがコンテキストをクリーンで集中した状態に保つことができます。

![Multi-agent](docs/res/physics.png)
![Multi-agent 2](docs/res/physics-2.png)

4. **完全にカスタマイズ可能で拡張可能**

- このフレームワークでは、ほとんど何もハードコードされていません。何も隠されていません。すべてはユーザーによって拡張または変更できます。
- 全体の動作は、**prompts/default/agent.system.md** ファイルのシステムプロンプトによって定義されます。このプロンプトを変更すると、フレームワークが劇的に変化します。
- フレームワークは、エージェントをいかなる方法でもガイドしたり制限したりしません。エージェントが従わなければならないハードコードされたレールはありません。
- すべてのプロンプト、エージェントとの通信ループでエージェントに送信されるすべての小さなメッセージテンプレートは、**prompts/** フォルダーにあり、変更できます。
- すべてのデフォルトツールは、**python/tools/** フォルダーにあり、変更したりコピーして新しい事前定義ツールを作成したりできます。

![Prompts](/docs/res/prompts.png)

5. **コミュニケーションが鍵**

- エージェントに適切なシステムプロンプトと指示を与えれば、奇跡を起こすことができます。
- エージェントは、上位エージェントや下位エージェントと通信し、質問したり、指示を与えたり、ガイダンスを提供したりできます。システムプロンプトでエージェントに効果的なコミュニケーション方法を指示してください。
- ターミナルインターフェースはリアルタイムでストリーミングされ、インタラクティブです。いつでも停止して介入できます。エージェントが間違った方向に進んでいるのを見たら、すぐに停止して伝えてください。
- このフレームワークには多くの自由があります。エージェントに、継続する許可を求めるために定期的に上位エージェントに報告するように指示できます。サブタスクを委任する時期を決定する際に、ポイントスコアリングシステムを使用するように指示できます。上位エージェントは、下位エージェントの結果を再確認し、異議を唱えることができます。可能性は無限大です。

## 🚀 Agent Zeroで構築できるもの

- **開発プロジェクト** - `"リアルタイムデータ視覚化機能を備えたReactダッシュボードを作成する"`

- **データ分析** - `"前四半期のNVIDIA販売データを分析し、トレンドレポートを作成する"`

- **コンテンツ作成** - `"マイクロサービスに関する技術ブログ記事を執筆する"`

- **システム管理者** - `"ウェブサーバーの監視システムをセットアップする"`

- **研究** - `"CoTプロンプトに関する最近のAI論文を5つ収集して要約する"`

# ⚙️ インストール

Agent Zeroのインストール方法を学ぶには、ビデオをクリックして開いてください:

[![Testing Video](/docs/res/new_vid.jpg)](https://www.youtube.com/watch?v=cHDCCSr1YRI&t=24s)

Windows、macOS、Linux向けの詳しいセットアップガイドとビデオは、Agent Zeroドキュメントの[このページ](./docs/installation.md)でご覧いただけます。

### ⚡ クイックスタート

```bash
# Dockerでプルして実行

docker pull frdel/agent-zero-run
docker run -p 50001:80 frdel/agent-zero-run

# http://localhost:50001 にアクセスして開始
```

- 開発者および貢献者の方へ: システム用の完全なバイナリを[リリースぺージ](https://github.com/frdel/agent-zero/releases)からダウンロードし、[こちらに記載されている手順](./docs/installation.md#in-depth-guide-for-full-binaries-installation)に従ってください。

## 🐳 完全なDocker化、音声認識とTTSを搭載

![Settings](docs/res/settings-page-ui.png)

- カスタマイズ可能な設定により、ユーザーはエージェントの動作と応答をニーズに合わせて調整できます。
- Web UIの出力は非常にクリーンで、流動的で、カラフルで、読みやすく、インタラクティブです。何も隠されていません。
- Web UI内でチャットを直接ロードまたは保存できます。
- ターミナルに表示されるのと同じ出力が、セッションごとに自動的に**logs/**フォルダーのHTMLファイルに保存されます。

![Time example](/docs/res/time_example.jpg)

- エージェントの出力はリアルタイムでストリーミングされるため、ユーザーは読み進めながらいつでも介入できます。
- コーディングは不要で、プロンプトとコミュニケーションスキルのみが必要です。
- 堅牢なシステムプロンプトがあれば、小さなモデルでも、正確なツール使用を含め、フレームワークは信頼できます。

## 👀 留意事項

1. **Agent Zeroは危険な場合があります！**

- 適切な指示があれば、Agent Zeroはコンピューター、データ、アカウントに関して潜在的に危険な行動を含む、多くのことを実行できます。Agent Zeroは常に隔離された環境（Dockerなど）で実行し、何をするか注意してください。

2. **Agent Zeroはプロンプトベースです。**

- フレームワーク全体は**prompts/**フォルダーによってガイドされます。エージェントのガイドライン、ツールの指示、メッセージ、ユーティリティAI機能、すべてそこにあります。


## 📚 ドキュメントを読む

| ページ | 説明 |
|-------|-------------|
| [インストール](./docs/installation.md) | インストール、セットアップ、構成 |
| [使用方法](./docs/usage.md) | 基本的な使用方法と高度な使用方法 |
| [アーキテクチャ](./docs/architecture.md) | システム設計とコンポーネント |
| [貢献](./docs/contributing.md) | 貢献方法 |
| [トラブルシューティング](./docs/troubleshooting.md) | 一般的な問題とその解決策 |

## 🎯 変更履歴

### 近日公開

- **知識とRAGツール**
- **計画とスケジューリング**

> [!IMPORTANT]
>
>**v0.7以降のfrdel/agent-zero Dockerイメージの変更点:**
>
> 新しいDockerイメージ `frdel/agent-zero-run` は、新しい統合環境を提供します。

### v0.8.1
- **ブラウザエージェント**
- **UXの改善**

### v0.8

- **Dockerランタイム**
- **新しいメッセージ履歴と要約システム**
- **エージェントの動作変更と管理**
- **テキスト読み上げ (TTS) と音声認識 (STT)**
- **Web UIの設定ページ**
- **Perplexity + DuckDuckGoに代わるSearXNG統合**
- **ファイルブラウザ機能**
- **KaTeX数式表示のサポート**
- **チャット内ファイル添付**

### v0.7

- **自動メモリ**
- **UIの改善**
- **インストゥルメント**
- **拡張フレームワーク**
- **リフレクションプロンプト**
- **バグ修正**

## 🤝 コミュニティとサポート

- ライブディスカッションには[Discordに参加](https://discord.gg/B8KZKNsPpj)するか、[Skoolコミュニティを訪問](https://www.skool.com/agent-zero)してください。
- 実践的な説明とチュートリアルについては[YouTubeチャンネルをフォロー](https://www.youtube.com/@AgentZeroFW)してください
- バグ修正と機能については[問題を報告](https://github.com/frdel/agent-zero/issues)してください
