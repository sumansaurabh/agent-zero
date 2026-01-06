<div align="center">

![Agent Zero](/docs/res/header.png)

# `Agent Zero`

[![Thanks to Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Thanks%20to%20Sponsors-FF69B4?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/frdel) [![Join our Skool Community](https://img.shields.io/badge/Skool-Join%20our%20Community-4A90E2?style=for-the-badge&logo=skool&logoColor=white)](https://www.skool.com/agent-zero) [![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/B8KZKNsPpj) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AgentZeroFW) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jan-tomasek/) [![Follow on Warpcast](https://img.shields.io/badge/Warpcast-Follow-5A32F3?style=for-the-badge)](https://warpcast.com/agent-zero)

> **注意:** Agent Zero は Twitter/X を使用していません。このプロジェクトを代表すると主張する Twitter/X アカウントはすべて偽物です。

[インストール](./docs/installation.md) •
[更新方法](./docs/installation.md#how-to-update-agent-zero) •
[ドキュメント](./docs/README.md) •
[使用方法](./docs/usage.md)

</div>


[![Showcase](/docs/res/showcase-thumb.png)](https://youtu.be/lazLNcEYsiQ)



詳細については [www.agent-zero.ai](https://agent-zero.ai) をご覧ください。

[![Browser Agent](/docs/res/web_screenshot.jpg)](https://agent-zero.ai)



> [!NOTE]
> **🎉 v0.8.1 リリース**: Chromium を使用してウェブインタラクションが可能なブラウザエージェントが登場しました！これにより、Agent Zero は自律的にウェブを閲覧し、情報を収集し、ウェブコンテンツとやり取りできます。


https://github.com/user-attachments/assets/c168759d-57d8-4b43-b62a-1026afcf52e6

## あなたと共に成長し、学ぶ個人的で有機的なエージェントフレームワーク

- Agent Zero は事前に定義されたエージェントフレームワークではありません。使用するにつれて動的に、有機的に成長し、学習するように設計されています。
- Agent Zero は完全に透明で、読みやすく、理解しやすく、カスタマイズ可能で、インタラクティブです。
- Agent Zero はコンピューターをツールとして使用して、その（あなたの）タスクを達成します。

# 💡 主な機能

1. **汎用アシスタント**

- Agent Zero は特定のタスク向けに事前プログラムされていません（ただし、可能です）。汎用パーソナルアシスタントとして機能することを意図しています。タスクを与えると、情報を収集し、コマンドとコードを実行し、他のエージェントインスタンスと協力し、そのタスクを達成するために最善を尽くします。
- 永続的なメモリを備えており、以前のソリューション、コード、事実、指示などを記憶して、将来のタスクをより迅速かつ確実に解決できます。

![Agent 0 Working](/docs/res/ui-screen-2.png)

2. **ツールとしてのコンピューター**

- Agent Zero はオペレーティングシステムをツールとして使用してタスクを達成します。事前にプログラムされた単一目的のツールはありません。代わりに、独自のコードを記述し、ターミナルを使用して必要に応じて独自のツールを作成および使用できます。
- その唯一のデフォルトツールは、オンライン検索、メモリ機能、通信（ユーザーおよび他のエージェントとの）、およびコード/ターミナル実行です。その他すべてはエージェント自身が作成するか、ユーザーが拡張できます。
- ツール使用機能は、非常に小さなモデルでも最も互換性があり信頼できるようにゼロから開発されました。
- **デフォルトツール:** Agent Zero には、知識、ウェブページコンテンツ、コード実行、通信などのツールが含まれています。
- **カスタムツールの作成:** 独自のカスタムツールを作成して、Agent Zero の機能を拡張します。
- **インストゥルメント:** インストゥルメントは、Agent Zero が呼び出すことができるカスタム関数とプロシージャを作成できる新しいタイプのツールです。

3. **マルチエージェント協力**

- 各エージェントには、タスクと指示を与える上位エージェントがいます。その後、各エージェントは上位エージェントに報告します。
- チェーン内の最初のエージェント（Agent 0）の場合、上位は人間ユーザーです。エージェントは違いを認識しません。
- 各エージェントは、サブタスクを分解して解決するのに役立つ下位エージェントを作成できます。これにより、すべてのエージェントがコンテキストを明確に保ち、集中できます。

![Multi-agent](docs/res/physics.png)
![Multi-agent 2](docs/res/physics-2.png)

4. **完全にカスタマイズ可能で拡張可能**

- このフレームワークでは、ほとんど何もハードコーディングされていません。何も隠されていません。すべてはユーザーによって拡張または変更できます。
- 全体の動作は、**prompts/default/agent.system.md** ファイルのシステムプロンプトによって定義されます。このプロンプトを変更すると、フレームワークが劇的に変わります。
- フレームワークは、エージェントをいかなる方法でも導いたり制限したりしません。エージェントが従うべきハードコーディングされたレールはありません。
- 通信ループでエージェントに送信されるすべてのプロンプト、すべての小さなメッセージテンプレートは、**prompts/** フォルダーで見つけて変更できます。
- すべてのデフォルトツールは、**python/tools/** フォルダーで見つけて変更したり、コピーして新しい事前定義ツールを作成したりできます。

![Prompts](/docs/res/prompts.png)

5. **コミュニケーションが鍵**

- エージェントに適切なシステムプロンプトと指示を与えれば、奇跡を起こすことができます。
- エージェントは上位者や下位者と通信し、質問したり、指示を与えたり、ガイダンスを提供したりできます。システムプロンプトでエージェントに効果的なコミュニケーション方法を指示してください。
- ターミナルインターフェイスはリアルタイムでストリーミングされ、インタラクティブです。いつでも停止して介入できます。エージェントが間違った方向に進んでいる場合は、すぐに停止して伝えてください。
- このフレームワークには多くの自由があります。エージェントに定期的に上位者に報告し、続行の許可を求めるように指示できます。サブタスクを委任する時期を決定する際に、ポイントスコアリングシステムを使用するように指示できます。上位者は下位者の結果を再確認し、異議を唱えることができます。可能性は無限大です。

## 🚀 Agent Zero で構築できるもの

- **開発プロジェクト** - `"リアルタイムデータ視覚化機能を備えた React ダッシュボードを作成する"`

- **データ分析** - `"前四半期の NVIDIA の販売データを分析し、トレンドレポートを作成する"`

- **コンテンツ作成** - `"マイクロサービスに関する技術ブログ記事を作成する"`

- **システム管理者** - `"ウェブサーバーの監視システムをセットアップする"`

- **研究** - `"CoT プロンプトに関する最近の AI 論文を 5 つ収集して要約する"`

# ⚙️ インストール

Agent Zero のインストール方法を学ぶためのビデオを開くには、クリックしてください。

[![Testing Video](/docs/res/new_vid.jpg)](https://www.youtube.com/watch?v=cHDCCSr1YRI&t=24s)

Windows、macOS、Linux の詳細なセットアップガイド（ビデオ付き）は、Agent Zero ドキュメントの [このページ](./docs/installation.md) で確認できます。

### ⚡ クイックスタート

```bash
# Docker を使用してプルして実行

docker pull frdel/agent-zero-run
docker run -p 50001:80 frdel/agent-zero-run

# http://localhost:50001 にアクセスして開始
```

- 開発者および貢献者：[リリースページ](https://github.com/frdel/agent-zero/releases) からシステム用の完全なバイナリをダウンロードし、[こちらで提供されている](./docs/installation.md#in-depth-guide-for-full-binaries-installation) 手順に従ってください。

## 🐳 完全な Docker 化、音声テキスト変換および TTS 対応

![Settings](docs/res/settings-page-ui.png)

- カスタマイズ可能な設定により、ユーザーはエージェントの動作と応答を自分のニーズに合わせて調整できます。
- Web UI の出力は非常にクリーンで、流動的で、カラフルで、読みやすく、インタラクティブです。何も隠されていません。
- Web UI 内でチャットを直接ロードまたは保存できます。
- ターミナルに表示されるのと同じ出力は、セッションごとに **logs/** フォルダーの HTML ファイルに自動的に保存されます。

![Time example](/docs/res/time_example.jpg)

- エージェントの出力はリアルタイムでストリーミングされ、ユーザーはいつでも読み進めて介入できます。
- コーディングは不要です。必要なのはプロンプトとコミュニケーションスキルだけです。
- 強固なシステムプロンプトがあれば、小さなモデルでも、正確なツール使用を含むフレームワークは信頼できます。

## 👀 留意事項

1. **Agent Zero は危険な場合があります！**

- 適切な指示があれば、Agent Zero はコンピューター、データ、アカウントに関して潜在的に危険な行動を含む多くのことを実行できます。Agent Zero は常に隔離された環境（Docker など）で実行し、何を望むかに注意してください。

2. **Agent Zero はプロンプトベースです。**

- フレームワーク全体は **prompts/** フォルダーによってガイドされます。エージェントのガイドライン、ツール指示、メッセージ、ユーティリティ AI 機能など、すべてそこにあります。


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

- **知識と RAG ツール**
- **計画とスケジューリング**

> [!IMPORTANT]
>
>**v0.7 以降の frdel/agent-zero Docker イメージの変更点:**
>
> 新しい Docker イメージ `frdel/agent-zero-run` は、新しい統合環境を提供します。

### v0.8.1
- **ブラウザエージェント**
- **UX の改善**

### v0.8

- **Docker ランタイム**
- **新しいメッセージ履歴と要約システム**
- **エージェントの動作変更と管理**
- **テキスト音声変換 (TTS) および音声テキスト変換 (STT)**
- **Web UI の設定ページ**
- **Perplexity + DuckDuckGo に代わる SearXNG 統合**
- **ファイルブラウザ機能**
- **KaTeX 数式可視化のサポート**
- **チャット内ファイル添付**

### v0.7

- **自動メモリ**
- **UI の改善**
- **インストゥルメント**
- **拡張フレームワーク**
- **リフレクションプロンプト**
- **バグ修正**

## 🤝 コミュニティとサポート

- ライブディスカッションには [Discord に参加](https://discord.gg/B8KZKNsPpj) するか、[Skool コミュニティ](https://www.skool.com/agent-zero) にアクセスしてください。
- 実践的な説明とチュートリアルについては [YouTube チャンネルをフォロー](https://www.youtube.com/@AgentZeroFW) してください。
- バグ修正と機能については [問題を報告](https://github.com/frdel/agent-zero/issues) してください。
