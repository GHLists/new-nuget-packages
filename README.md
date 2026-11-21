# New NuGet packages

Hourly lists of packages newly created on
[nuget.org](https://www.nuget.org/), built from the [v3 catalog](
https://api.nuget.org/v3/catalog0/index.json) of every package operation
nuget.org publishes. Each package touched in the window is checked against
its registration index, whose earliest `published` timestamp decides whether
the package was created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-nuget-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-21 13:20 UTC

New packages created between 2026-11-21 12:20 UTC and 2026-11-21 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T13-20-29-784949Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 12:21:05 | [PilotClientSdk](https://www.nuget.org/packages/PilotClientSdk) | 2.1.4 | PilotOpenTools | Общий модуль для клиентских модулей Pilot: статистика использования (Grafana),… |
| 2026-11-21 12:22:43 | [Bitzsoft.Integrations.AI.Knowledge](https://www.nuget.org/packages/Bitzsoft.Integrations.AI.Knowledge) | 1.2.0 | Bitzsoft | 企业知识检索与租户感知 RAG 编排层 — IKnowledgeStore Seam、Qdrant Adapter、访问控制、RRF 混合重排与引用上下文（替… |
| 2026-11-21 12:22:57 | [Bitzsoft.Integrations.AI.Mcp](https://www.nuget.org/packages/Bitzsoft.Integrations.AI.Mcp) | 1.2.0 | Bitzsoft | 安全的 MCP Client 与 Server 双端集成 — 支持 Streamable HTTP、stdio、工具白名单、多租户凭据解析、PAT 认证与 E… |
| 2026-11-21 12:23:31 | [Bitzsoft.Integrations.AI.Hermes](https://www.nuget.org/packages/Bitzsoft.Integrations.AI.Hermes) | 1.2.0 | Bitzsoft | Bitzsoft AI-Hermes 智能体运行时 Harness 核心包 — 承载多阶段生命周期钩子管线、大结果旁路产物仓、跨数据集十进制分析引擎、工具依赖… |
| 2026-11-21 12:23:46 | [Bitzsoft.Integrations.AI.Agents](https://www.nuget.org/packages/Bitzsoft.Integrations.AI.Agents) | 1.2.0 | Bitzsoft | Microsoft Agent Framework 统一集成 — Provider-neutral Agent、BitzAgentBuilder、会话持久化桥… |
| 2026-11-21 12:24:32 | [Bitzsoft.Integrations.AI.All](https://www.nuget.org/packages/Bitzsoft.Integrations.AI.All) | 1.2.0 | Bitzsoft | Bitzsoft AI 套件 1.2.0 独立运行期聚合元包 — 一键引入全部 11 个活跃 Bitzsoft.Integrations.AI.* 运行期包（… |
| 2026-11-21 12:37:21 | [oneAPI.OSPRay.NET.runtime.win](https://www.nuget.org/packages/oneAPI.OSPRay.NET.runtime.win) | 3.2.0 | Chiretallyn | Native Windows (win-x64) runtime binaries for oneAPI.OSPRay.NET (Intel OSPRay 3… |
| 2026-11-21 12:39:59 | [oneAPI.OSPRay.NET.runtime.osx](https://www.nuget.org/packages/oneAPI.OSPRay.NET.runtime.osx) | 3.2.0 | Chiretallyn | Native macOS (osx-arm64 Apple Silicon and osx-x64 Intel) runtime binaries for o… |
| 2026-11-21 12:42:13 | [ExecutionFlow.Extensions.Logging](https://www.nuget.org/packages/ExecutionFlow.Extensions.Logging) | 2.0.0 | Gustavo Viana | Microsoft.Extensions.Logging (ILogger) integration for ExecutionFlow handler lo… |
| 2026-11-21 12:42:15 | [ExecutionFlow.Hosting](https://www.nuget.org/packages/ExecutionFlow.Hosting) | 2.0.0 | Gustavo Viana | Runs ExecutionFlow recurring handlers inside the .NET Generic Host, locally and… |
| 2026-11-21 12:51:08 | [ControlBoxForCustom](https://www.nuget.org/packages/ControlBoxForCustom) | 1.0.0 | ControlBoxForCustom | コントロールボックスをツールボックスでドラッグしてドロップして設置するだけで 使えるパッケージです。 各ボックスタイプにネイティブヒットテストも付いています。… |
| 2026-11-21 12:52:59 | [Revit.Themes](https://www.nuget.org/packages/Revit.Themes) | 0.1.0 | Kristoffer Tungland | Revit's own light and dark theme colors for WPF add-in windows, read from the r… |
| 2026-11-21 13:12:46 | [FlyAotOrm.Abstractions](https://www.nuget.org/packages/FlyAotOrm.Abstractions) | 1.0.0 | FlyAotOrm contributors | FlyAotOrm 是 NativeAOT 优先的轻量级 ORM，适合 AI 辅助开发的工具类和小型应用。本包提供实体映射特性与公共契约，配合 Core 和… |
| 2026-11-21 13:15:33 | [FlyAotOrm.Generator](https://www.nuget.org/packages/FlyAotOrm.Generator) | 1.0.0 | FlyAotOrm contributors | FlyAotOrm 是 NativeAOT 优先的轻量级 ORM，适合 AI 辅助开发的工具类和小型应用。本包在编译期生成实体元数据、类型化表和列、CRUD、… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
