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

## Latest list — 2026-10-16 06:20 UTC

New packages created between 2026-10-16 05:22 UTC and 2026-10-16 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T06-20-34-433397Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 05:26:19 | [ORT](https://www.nuget.org/packages/ORT) | 1.0.0 | GreatBear | Clean ONNX Runtime 1.31.0 repack: net8.0 / .NET Framework 4.6.1 managed assembl… |
| 2026-10-16 05:51:09 | [Gil.Tree](https://www.nuget.org/packages/Gil.Tree) | 0.20.0 | iyulab | Gil's experimental tree judgment path: a resolver that answers repeated LLM req… |
| 2026-10-16 06:04:19 | [Esatto.Umbraco.Backoffice.AICosts](https://www.nuget.org/packages/Esatto.Umbraco.Backoffice.AICosts) | 1.0.0 | Carl Schéle | Estimated AI costs for Umbraco.AI in the backoffice: a Costs tab next to Analyt… |
| 2026-10-16 06:06:32 | [MonixOne.OpenObservability](https://www.nuget.org/packages/MonixOne.OpenObservability) | 1.0.0 | Shulyakovsky.E | Central OpenTelemetry logs, traces, metrics, Sentry, HTTP body masking and auto… |
| 2026-10-16 06:12:16 | [Bitzsoft.Integrations.DocumentGeneration](https://www.nuget.org/packages/Bitzsoft.Integrations.DocumentGeneration) | 1.0.1 | Bitzsoft | 文档生成抽象层 — 统一接口定义与基础模型（IDocumentGenerationProvider / GenerateDocumentRequest / G… |
| 2026-10-16 06:12:19 | [Bitzsoft.Integrations.DocumentGeneration.SelfHosted](https://www.nuget.org/packages/Bitzsoft.Integrations.DocumentGeneration.SelfHosted) | 1.0.1 | Bitzsoft | 文档生成自托管官方实现 — 针对 Gateway/Compose 微服务的 HTTP 通信、状态探针与 ProblemDetails 异常解析 |
| 2026-10-16 06:12:22 | [Bitzsoft.Integrations.DocumentGeneration.All](https://www.nuget.org/packages/Bitzsoft.Integrations.DocumentGeneration.All) | 1.0.1 | Bitzsoft | 文档生成聚合包 — 包含文档生成抽象层、官方自托管实现与 Polly 弹性重试依赖注入扩展 |
| 2026-10-16 06:13:00 | [Kentico.Xperience.Labs.VirtualInbox.Admin](https://www.nuget.org/packages/Kentico.Xperience.Labs.VirtualInbox.Admin) | 2.0.0 | Kentico Software | Adds Administration application UI for Xperience by Kentico Virtual Inbox. |
| 2026-10-16 06:13:02 | [Kentico.Xperience.Labs.VirtualInbox.MCP](https://www.nuget.org/packages/Kentico.Xperience.Labs.VirtualInbox.MCP) | 2.0.0 | Kentico Software | Adds MCP server tools for Xperience by Kentico Virtual Inbox. |
| 2026-10-16 06:13:05 | [Kentico.Xperience.Labs.VirtualInbox](https://www.nuget.org/packages/Kentico.Xperience.Labs.VirtualInbox) | 2.0.0 | Kentico Software | Adds core object types and services for Xperience by Kentico Virtual Inbox. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
