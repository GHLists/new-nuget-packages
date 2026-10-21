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

## Latest list — 2026-10-21 06:21 UTC

New packages created between 2026-10-21 05:20 UTC and 2026-10-21 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T06-21-00-6927Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 05:21:12 | [Stellaegis.Backplane.PostgreSQL](https://www.nuget.org/packages/Stellaegis.Backplane.PostgreSQL) | 5.0.1 | FRi | Stellaegis backplane journal on PostgreSQL: the events the hub relayed, kept in… |
| 2026-10-21 05:21:13 | [Stellaegis.Backplane.Client](https://www.nuget.org/packages/Stellaegis.Backplane.Client) | 5.0.1 | FRi | Stellaegis backplane client: the bus of a host that reaches the hub of the appl… |
| 2026-10-21 05:21:13 | [Stellaegis.Backplane.Server](https://www.nuget.org/packages/Stellaegis.Backplane.Server) | 5.0.1 | FRi | Stellaegis backplane hub: a SignalR hub mapped in the application's host, under… |
| 2026-10-21 05:21:14 | [Stellaegis.Backplane](https://www.nuget.org/packages/Stellaegis.Backplane) | 5.0.1 | FRi | Stellaegis backplane: the internal event bus of an application assembled from s… |
| 2026-10-21 05:21:36 | [Bitzsoft.Integrations.Translation.DeepL](https://www.nuget.org/packages/Bitzsoft.Integrations.Translation.DeepL) | 1.0.0 | Bitzsoft | DeepL API 实现 — v2/translate 原生批量与 detected_source_language 回显，glossary / contex… |
| 2026-10-21 05:22:29 | [Stellaegis.Operations.AspNetCore](https://www.nuget.org/packages/Stellaegis.Operations.AspNetCore) | 5.0.0 | FRi | ASP.NET Core endpoints for Stellaegis.Operations: launch, follow and cancel the… |
| 2026-10-21 05:22:29 | [Stellaegis.Operations.PostgreSQL](https://www.nuget.org/packages/Stellaegis.Operations.PostgreSQL) | 5.0.0 | FRi | PostgreSQL stores for Stellaegis.Operations (schema ops): the jobs, claimed ato… |
| 2026-10-21 05:22:30 | [Stellaegis.Operations](https://www.nuget.org/packages/Stellaegis.Operations) | 5.0.0 | FRi | Jobs run outside requests, in a compartment or on the assembly: launched by a u… |
| 2026-10-21 05:26:26 | [Bitzsoft.Integrations.Translation.Google](https://www.nuget.org/packages/Bitzsoft.Integrations.Translation.Google) | 1.0.0 | Bitzsoft | Google Cloud Translation v2 官方 API 实现（非免费网关）— q 数组原生批量、detect 检测含置信度、languages… |
| 2026-10-21 05:31:27 | [Bitzsoft.Integrations.Translation.AI.Tongyi](https://www.nuget.org/packages/Bitzsoft.Integrations.Translation.AI.Tongyi) | 1.0.0 | Bitzsoft | 阿里云百炼通义翻译（Qwen-MT）实现 — OpenAI 兼容端点 + translation_options 原生术语干预（terms）与领域提示（dom… |
| 2026-10-21 05:38:59 | [GameSharp.Random](https://www.nuget.org/packages/GameSharp.Random) | 1.0.0 | willbldn | High-performance, zero-allocation random generation and procedural tools for .N… |
| 2026-10-21 05:39:15 | [Bitzsoft.Integrations.Translation.AI.Baidu](https://www.nuget.org/packages/Bitzsoft.Integrations.Translation.AI.Baidu) | 1.0.0 | Bitzsoft | 百度大模型文本翻译实现 — 翻译指令（reference）注入风格与术语约束、控制台术语库干预（needIntervene）、llm/nmt 双引擎，实现 I… |
| 2026-10-21 05:44:40 | [Bitzsoft.Integrations.Translation.AI.Volcengine](https://www.nuget.org/packages/Bitzsoft.Integrations.Translation.AI.Volcengine) | 1.0.0 | Bitzsoft | 火山引擎机器翻译大模型实现 — matx_translate 端点原生批量（单次 16 条）与术语直传（corpus.glossary_list / 控制台术… |
| 2026-10-21 05:48:50 | [Bitzsoft.Integrations.Translation.AI.OpenAI](https://www.nuget.org/packages/Bitzsoft.Integrations.Translation.AI.OpenAI) | 1.0.0 | Bitzsoft | OpenAI 兼容网关大模型翻译实现 — 通吃 OpenAI / 智谱 GLM / DeepSeek / Kimi / 通义千问 compatible 端点，… |
| 2026-10-21 05:53:06 | [Indiko.Blocks.AI.OpenRouter](https://www.nuget.org/packages/Indiko.Blocks.AI.OpenRouter) | 4.3.1 | INDIKO | Building Blocks AI OpenRouter: one API key for hundreds of models, with provide… |
| 2026-10-21 05:53:31 | [Bitzsoft.Integrations.Translation.AI.Anthropic](https://www.nuget.org/packages/Bitzsoft.Integrations.Translation.AI.Anthropic) | 1.0.0 | Bitzsoft | Anthropic Claude 大模型翻译实现 — 复用既有 AI.Anthropic 原生 Messages 适配器，法律术语约束提示词 + 分段回拼 +… |
| 2026-10-21 05:57:13 | [CSEPDI.LicenseGenDll](https://www.nuget.org/packages/CSEPDI.LicenseGenDll) | 1.0.0 | Eziriz | .NET Reactor License Gen SDK，支持 .NET Framework 4.x / .NET Core / .NET 5+ |
| 2026-10-21 05:58:20 | [Bitzsoft.Integrations.Translation.All](https://www.nuget.org/packages/Bitzsoft.Integrations.Translation.All) | 1.0.0 | Bitzsoft | 翻译服务聚合包 — 传统机翻（阿里云 / 百度 / 腾讯云 / 有道 / DeepL / Google 官方）+ AI 翻译（通义 Qwen-MT / 百度大… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
