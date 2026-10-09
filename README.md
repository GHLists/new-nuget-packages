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

## Latest list — 2026-10-09 04:18 UTC

New packages created between 2026-10-09 03:19 UTC and 2026-10-09 04:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T04-18-53-096642Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 03:27:52 | [JupiterScheduler.OperationClient](https://www.nuget.org/packages/JupiterScheduler.OperationClient) | 1.0.0 | JupiterScheduler.OperationCli… | SeaDate operation client adapter for Jupiter Scheduler. |
| 2026-10-09 03:29:57 | [HuangyuCN.Atlas.Sdk](https://www.nuget.org/packages/HuangyuCN.Atlas.Sdk) | 0.7.0 | huangyuCN | Atlas 帧协议 C# 客户端 SDK（Unity 优先）：四通道 + dual + 双层心跳 + 重连 + 三编码 |
| 2026-10-09 03:31:34 | [Web.Authentication](https://www.nuget.org/packages/Web.Authentication) | 1.0.0 | Dio Liew | A package to ease the configuration of JWT Authentication. |
| 2026-10-09 03:32:04 | [MorseCode.Avalonia.Controls](https://www.nuget.org/packages/MorseCode.Avalonia.Controls) | 0.1.0 | MorseCode Software LLC | Avalonia controls and converters for views that bind to view models written in… |
| 2026-10-09 03:32:16 | [Web.Authorization](https://www.nuget.org/packages/Web.Authorization) | 1.0.0 | Dio Liew | A package to ease the configuration of Authorization. |
| 2026-10-09 03:33:02 | [Web.Configuration](https://www.nuget.org/packages/Web.Configuration) | 1.0.0 | Dio Liew | A package to ease the configuration of Web. |
| 2026-10-09 03:33:41 | [Web.Exception](https://www.nuget.org/packages/Web.Exception) | 1.0.0 | Dio Liew | A package to ease the configuration of Web Exception. |
| 2026-10-09 03:34:15 | [Web.JWT](https://www.nuget.org/packages/Web.JWT) | 1.0.0 | Dio Liew | A package to ease the configuration of JWT configuration. |
| 2026-10-09 03:34:56 | [Web.OpenApi](https://www.nuget.org/packages/Web.OpenApi) | 1.0.0 | Dio Liew | A package to ease the configuration of OpenApi. |
| 2026-10-09 03:45:52 | [Manjalabs.Core](https://www.nuget.org/packages/Manjalabs.Core) | 1.0.0-pre-release | Manjalabs | Manjalabs core library: auth, caching, Camunda, logging, middleware, repository… |
| 2026-10-09 03:46:20 | [Manjalabs.Core.MySql](https://www.nuget.org/packages/Manjalabs.Core.MySql) | 1.0.0-pre-release | Manjalabs | MySQL (EF Core + Pomelo) data store for Manjalabs.Core: IRepoClient implementat… |
| 2026-10-09 03:49:21 | [GreatUtilities.JwtAuthenticationHelper](https://www.nuget.org/packages/GreatUtilities.JwtAuthenticationHelper) | 0.1.568-beta | Rodrigo Leal | Essencial tools to agile development. |
| 2026-10-09 03:56:02 | [Webority.Testing](https://www.nuget.org/packages/Webority.Testing) | 0.1.0 | Webority Technologies | Golden-file comparison and byte-pin checks for MSTest tests: Golden.Match compa… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
