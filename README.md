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

## Latest list — 2026-10-09 15:21 UTC

New packages created between 2026-10-09 14:20 UTC and 2026-10-09 15:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T15-21-07-636002Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 14:26:37 | [IronMarten.Bearing.Connect](https://www.nuget.org/packages/IronMarten.Bearing.Connect) | 1.0.0 | Iron Marten | Package Description |
| 2026-10-09 14:32:28 | [Filoroch.Template.Solution](https://www.nuget.org/packages/Filoroch.Template.Solution) | 1.0.0 | Filipe Dhunior | Template reutilizável para projetos .NET com Clean Architecture, DDD, OpenTelem… |
| 2026-10-09 14:40:56 | [FreeDotnetFonts](https://www.nuget.org/packages/FreeDotnetFonts) | 1.0.2 | Six Labors and contributors,… | Community-maintained, Apache-2.0 licensed fork of SixLabors.Fonts 1.0.1. Assemb… |
| 2026-10-09 14:41:41 | [Crumpled.VerifyOwnership](https://www.nuget.org/packages/Crumpled.VerifyOwnership) | 1.0.0 | Crumpled Dog | Google Search Console site-ownership verification for Umbraco - automatically s… |
| 2026-10-09 14:42:42 | [Zhytech.FactoryCenter](https://www.nuget.org/packages/Zhytech.FactoryCenter) | 1.2.0 | zhytech | 配置驱动 + 动态路由的通用工厂编排引擎。业务(BizList)经路由(BizToFactory)编排多个工厂(FactoryList)，入参按获取方式装配上… |
| 2026-10-09 14:49:03 | [Bfs.Seed.Functions.Core](https://www.nuget.org/packages/Bfs.Seed.Functions.Core) | 0.1.0 | Black Forest Sentinel | Grundausstattung für Azure Functions (dotnet-isolated) in Sentinel-Seed-Projekt… |
| 2026-10-09 15:07:20 | [Shiny.Net.HttpServer.FileSync](https://www.nuget.org/packages/Shiny.Net.HttpServer.FileSync) | 2.1.0 | aritchie,ShinyLib | Dropbox-style file sync for Shiny.Net.HttpServer. Files are split into content-… |
| 2026-10-09 15:07:20 | [Shiny.Net.HttpServer.NuGet](https://www.nuget.org/packages/Shiny.Net.HttpServer.NuGet) | 2.1.0 | aritchie,ShinyLib | A private NuGet feed for Shiny.Net.HttpServer — the NuGet V3 protocol (service… |
| 2026-10-09 15:07:29 | [Shiny.Net.HttpServer.FileSync.Client](https://www.nuget.org/packages/Shiny.Net.HttpServer.FileSync.Client) | 2.1.0 | aritchie,ShinyLib | The client for Shiny.Net.HttpServer.FileSync: keeps a local folder and the serv… |
| 2026-10-09 15:07:31 | [Shiny.Net.HttpServer.Npm](https://www.nuget.org/packages/Shiny.Net.HttpServer.Npm) | 2.1.0 | aritchie,ShinyLib | A private npm registry for Shiny.Net.HttpServer — the registry API npm, pnpm an… |
| 2026-10-09 15:13:40 | [AnthoDingo.Setup.Providers](https://www.nuget.org/packages/AnthoDingo.Setup.Providers) | 3.0.0 | AnthoDingo | Pilotes SQL Server, MySQL/MariaDB, PostgreSQL et SQLite pour AnthoDingo.Setup :… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
