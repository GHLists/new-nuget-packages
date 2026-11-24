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

## Latest list — 2026-11-24 18:20 UTC

New packages created between 2026-11-24 17:19 UTC and 2026-11-24 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T18-20-42-739295Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 17:21:16 | [TelegramBotKit.Polling](https://www.nuget.org/packages/TelegramBotKit.Polling) | 0.4.0 | NickFeD | Long-polling delivery using TelegramBotKit shared update execution. |
| 2026-11-24 17:21:18 | [TelegramBotKit.Webhook.AspNetCore](https://www.nuget.org/packages/TelegramBotKit.Webhook.AspNetCore) | 0.4.0 | NickFeD | ASP.NET Core webhook delivery using TelegramBotKit shared update execution. |
| 2026-11-24 17:40:16 | [TUtility.Core](https://www.nuget.org/packages/TUtility.Core) | 2.1.4 | TUtility.Core | .NET 基础工具库，提供缓存与对象池、定时调度、机器信息、JSON 序列化、安全算法和雪花 ID 等通用功能。 |
| 2026-11-24 17:51:57 | [Amoraller.Windows.SplashScreen](https://www.nuget.org/packages/Amoraller.Windows.SplashScreen) | 1.0.1 | Amoraller | A WPF splash screen for Windows that preserves image transparency during fade-o… |
| 2026-11-24 18:00:35 | [Kanject.Core.Realtime.Abstractions](https://www.nuget.org/packages/Kanject.Core.Realtime.Abstractions) | 1.0.0 | Akinsanya Omogbolahan | Kanject Core realtime abstractions — the transport-neutral contract a product p… |
| 2026-11-24 18:00:43 | [Kanject.Core.Realtime](https://www.nuget.org/packages/Kanject.Core.Realtime) | 1.0.0 | Akinsanya Omogbolahan | Kanject Core realtime — AddRealtime() and the in-process default transport for… |
| 2026-11-24 18:00:45 | [Kanject.Core.Realtime.Provider.AwsApiGateway](https://www.nuget.org/packages/Kanject.Core.Realtime.Provider.AwsApiGateway) | 1.0.0 | Akinsanya Omogbolahan | Kanject Core realtime over API Gateway WebSockets (proposal 0058 P2): UseApiGat… |
| 2026-11-24 18:00:47 | [Kanject.Core.Realtime.Provider.AwsApiGateway.TestKit](https://www.nuget.org/packages/Kanject.Core.Realtime.Provider.AwsApiGateway.TestKit) | 1.0.0 | Akinsanya Omogbolahan | Kanject Core realtime over API Gateway WebSockets, test kit (xUnit, proposal 00… |
| 2026-11-24 18:00:49 | [Kanject.Core.Realtime.Provider.AwsAppSync](https://www.nuget.org/packages/Kanject.Core.Realtime.Provider.AwsAppSync) | 1.0.0 | Akinsanya Omogbolahan | Kanject Core realtime over AWS AppSync Events (proposal 0058 P3): UseAppSyncEve… |
| 2026-11-24 18:00:50 | [Kanject.Core.Realtime.TestKit](https://www.nuget.org/packages/Kanject.Core.Realtime.TestKit) | 1.0.0 | Akinsanya Omogbolahan | Kanject Core realtime contract suite (xUnit): RealtimeTransportContractTests, t… |
| 2026-11-24 18:07:41 | [FonsecaFramework.Ai.Documents](https://www.nuget.org/packages/FonsecaFramework.Ai.Documents) | 2026.11.24.1 | FonsecaFramework.Ai.Documents | Optional document extractors for FonsecaFramework.Ai knowledge indexing: PDF (P… |
| 2026-11-24 18:09:58 | [Strybok](https://www.nuget.org/packages/Strybok) | 0.1.0 | Strybok | Strybok deep-link SDK for .NET: resolves Universal Links / App Links to an in-a… |
| 2026-11-24 18:09:59 | [Strybok.Maui](https://www.nuget.org/packages/Strybok.Maui) | 0.1.0 | Strybok | .NET MAUI glue for the Strybok deep-link SDK: registers the SDK in dependency i… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
