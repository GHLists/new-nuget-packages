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

## Latest list — 2026-10-04 08:20 UTC

New packages created between 2026-10-04 07:20 UTC and 2026-10-04 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T08-20-28-346367Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 07:22:06 | [NacosNetX](https://www.nuget.org/packages/NacosNetX) | 2.0.0 | NacosNetX | NacosNetX is a production-oriented .NET SDK for Nacos configuration, naming, gR… |
| 2026-10-04 07:23:36 | [Webority.Email.Outreach.Ai](https://www.nuget.org/packages/Webority.Email.Outreach.Ai) | 0.29.0 | Webority Technologies | AI reply classification for Webority.Email.Outreach over Webority.Ai judgment:… |
| 2026-10-04 07:24:17 | [Webority.Ai.Anthropic](https://www.nuget.org/packages/Webority.Ai.Anthropic) | 0.8.0 | Webority Technologies | The Anthropic transport for Webority.Ai: agents run on Claude models hosted in… |
| 2026-10-04 07:26:42 | [ZL.Simulator.Cli](https://www.nuget.org/packages/ZL.Simulator.Cli) | 1.1.0 | UseThink | 工业仪器仿真器平台：用软件仿真 DMM/电源/电子负载/SCPI/Modbus/自定义协议设备，支持多会话、可配置协议 JSON、gRPC 无头控制面与 AI… |
| 2026-10-04 07:28:23 | [Bitzsoft.Integrations.DocumentPreview.All](https://www.nuget.org/packages/Bitzsoft.Integrations.DocumentPreview.All) | 1.0.0 | Bitzsoft | 文档预览聚合包 — 包含文档预览抽象层、官方自托管实现与 Polly 弹性重试依赖注入扩展 |
| 2026-10-04 07:28:24 | [Bitzsoft.Integrations.DocumentPreview.SelfHosted](https://www.nuget.org/packages/Bitzsoft.Integrations.DocumentPreview.SelfHosted) | 1.0.0 | Bitzsoft | 文档预览自托管官方实现 — HMAC-SHA256 签名计算、短时效门票签发与高可用状态轮询探针 |
| 2026-10-04 07:28:26 | [Bitzsoft.Integrations.DocumentPreview](https://www.nuget.org/packages/Bitzsoft.Integrations.DocumentPreview) | 1.0.0 | Bitzsoft | 文档预览抽象层 — 统一接口定义与基础模型（IDocumentPreviewProvider / PreviewRequest / PreviewTicket… |
| 2026-10-04 07:31:33 | [Vestigium.Helpers.Kql](https://www.nuget.org/packages/Vestigium.Helpers.Kql) | 1.0.1 | Vestigium | KQL-inspired filter dialect and field catalog. |
| 2026-10-04 07:48:30 | [EzyBoardViewer](https://www.nuget.org/packages/EzyBoardViewer) | 0.1.0 | Loshop-Studio | .NET port of EzyBoardViewer: parse Suibian (随身答) board zips and cloud notes, ex… |
| 2026-10-04 08:00:48 | [Fizzy.McapSharp](https://www.nuget.org/packages/Fizzy.McapSharp) | 0.1.0 | Fizzy | File-based .NET bindings to the official Rust MCAP implementation. |
| 2026-10-04 08:14:53 | [DotFramework.Core.Data.SqlServer](https://www.nuget.org/packages/DotFramework.Core.Data.SqlServer) | 4.5.0 | dotFramework | Stored-procedure data access for SQL Server on Dapper and Microsoft.Data.SqlCli… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
