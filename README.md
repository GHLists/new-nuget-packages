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

## Latest list — 2026-10-10 15:20 UTC

New packages created between 2026-10-10 14:19 UTC and 2026-10-10 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T15-20-38-668619Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 14:23:30 | [KenyanCloud.Sdk](https://www.nuget.org/packages/KenyanCloud.Sdk) | 0.6.1 | Kenyan Cloud | Typed clients for the Kenyan Cloud control plane and Lango database proxy fleet. |
| 2026-10-10 14:23:33 | [KenyanCloud.Cli](https://www.nuget.org/packages/KenyanCloud.Cli) | 0.6.1 | Kenyan Cloud | Command-line client for the Kenyan Cloud control plane. |
| 2026-10-10 14:23:36 | [KenyanCloud.McpServer](https://www.nuget.org/packages/KenyanCloud.McpServer) | 0.6.1 | Kenyan Cloud | Governed stdio MCP server for the Kenyan Cloud control plane. |
| 2026-10-10 14:28:35 | [XUnitAssured.Http.AspNetCore](https://www.nuget.org/packages/XUnitAssured.Http.AspNetCore) | 6.5.0 | Carlos Andrew Costa Bezerra | HTTP tests against your own ASP.NET Core API with XUnitAssured.Http: ApiFixture… |
| 2026-10-10 14:34:53 | [KanjiVariants.Cli](https://www.nuget.org/packages/KanjiVariants.Cli) | 1.2.0 | Koichi Kobayashi | A .NET tool for checking educational and Joyo kanji in UTF-8 TXT files and SRT… |
| 2026-10-10 14:41:12 | [PulseTrade.Comm.ResourceNode.Line](https://www.nuget.org/packages/PulseTrade.Comm.ResourceNode.Line) | 0.1.0-alpha8 | PulseTrade.Comm.ResourceNode.… | RN-owned encrypted LINE admission, durable single reply claim and signed gatewa… |
| 2026-10-10 14:41:21 | [PulseTrade.Comm.Spa.Host.LINE.Client](https://www.nuget.org/packages/PulseTrade.Comm.Spa.Host.LINE.Client) | 0.1.0-alpha5 | PulseTrade.Comm.Spa.Host.LINE… | Package Description |
| 2026-10-10 14:49:27 | [Lycen.Storage.EntityFramework.PostgreSql](https://www.nuget.org/packages/Lycen.Storage.EntityFramework.PostgreSql) | 0.5.1 | NRTH | Lycen PostgreSQL integration for runtime persistence. |
| 2026-10-10 14:49:28 | [Lycen.Storage.EntityFramework.SqlServer](https://www.nuget.org/packages/Lycen.Storage.EntityFramework.SqlServer) | 0.5.1 | NRTH | Lycen SQL Server integration for runtime persistence. |
| 2026-10-10 14:49:29 | [Lycen.Storage.EntityFramework.MySql](https://www.nuget.org/packages/Lycen.Storage.EntityFramework.MySql) | 0.5.1 | NRTH | Lycen MySQL and MariaDB integration for runtime persistence. |
| 2026-10-10 14:49:30 | [Lycen.Storage.Redis](https://www.nuget.org/packages/Lycen.Storage.Redis) | 0.5.1 | NRTH | Lycen optional shared Redis certificate and artifact caching. |
| 2026-10-10 14:55:06 | [Meziantou.Framework.Imaging](https://www.nuget.org/packages/Meziantou.Framework.Imaging) | 1.0.0 | meziantou | Fully managed, performance-oriented image library for .NET: PNG, APNG, GIF, JPE… |
| 2026-10-10 14:55:53 | [Lantean.Roslyn.Workbench.Mcp.Plugins](https://www.nuget.org/packages/Lantean.Roslyn.Workbench.Mcp.Plugins) | 1.0.0 | Lantean Code | Trusted in-process plugin contracts and authoring diagnostics for Roslyn Workbe… |
| 2026-10-10 14:59:44 | [Vamp808.Localization.KeysGenerator](https://www.nuget.org/packages/Vamp808.Localization.KeysGenerator) | 0.1.0 | Vamp808 | Source generator: strongly-typed constants for .resx localization keys. |
| 2026-10-10 15:00:19 | [Fizzy.ImageViewer.Cuda](https://www.nuget.org/packages/Fizzy.ImageViewer.Cuda) | 1.2.0 | Fizzy.ImageViewer.Cuda | Optional CUDA image display and pixel queries with consumer-owned execution sco… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
