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

## Latest list — 2026-10-13 22:20 UTC

New packages created between 2026-10-13 21:19 UTC and 2026-10-13 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T22-20-51-230467Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 21:33:17 | [Raycoon.RayMigrator.Repository.ReadModel](https://www.nuget.org/packages/Raycoon.RayMigrator.Repository.ReadModel) | 0.17.0 | RAYCOON.com GmbH | Technology-neutral read model of the RayMigrator repository: the table and colu… |
| 2026-10-13 21:33:44 | [Rustyprint](https://www.nuget.org/packages/Rustyprint) | 1.0.0 | Ryan Verschuren | rustyprint renders HTML and CSS to PDF with a layout engine of its own, written… |
| 2026-10-13 21:43:42 | [Vespertan.VisualStudio.AgentProxy.Client](https://www.nuget.org/packages/Vespertan.VisualStudio.AgentProxy.Client) | 0.9.0 | Vespertan | Command-line client for the local VS Agent Proxy Visual Studio extension. |
| 2026-10-13 21:46:49 | [MetatraderSharp](https://www.nuget.org/packages/MetatraderSharp) | 1.0.0 | Rosamund Holder | A C# wrapper library which simplifies the use of MTsocketAPI for MT4 and MT5 |
| 2026-10-13 21:49:13 | [Kentico.Xperience.Labs.ComponentRegistry.Admin](https://www.nuget.org/packages/Kentico.Xperience.Labs.ComponentRegistry.Admin) | 3.0.0-prerelease-1 | Kentico Software | Adds Administration Module for Xperience Component Registry Module. |
| 2026-10-13 21:49:15 | [Kentico.Xperience.Labs.ComponentRegistry.MCP](https://www.nuget.org/packages/Kentico.Xperience.Labs.ComponentRegistry.MCP) | 3.0.0-prerelease-1 | Kentico Software | Adds MCP tools for Xperience Component Registry. |
| 2026-10-13 21:49:18 | [Kentico.Xperience.Labs.ComponentRegistry](https://www.nuget.org/packages/Kentico.Xperience.Labs.ComponentRegistry) | 3.0.0-prerelease-1 | Kentico Software | Adds services for Xperience Component Registry. |
| 2026-10-13 21:50:25 | [Belin.Akismet.FSharp](https://www.nuget.org/packages/Belin.Akismet.FSharp) | 1.0.0 | CedX | Prevent comment spam using the Akismet service. |
| 2026-10-13 22:06:56 | [Switchknife.Journal](https://www.nuget.org/packages/Switchknife.Journal) | 0.1.0 | Yehor Hrabovskyi | A durable step journal on SQLite: each side effect of a flow records its intent… |
| 2026-10-13 22:08:17 | [Ontos.Core](https://www.nuget.org/packages/Ontos.Core) | 1.0.0 | Pdawg | Attributes and enums consumed by Ontos decoder generators. |
| 2026-10-13 22:08:18 | [Ontos.ARM32](https://www.nuget.org/packages/Ontos.ARM32) | 1.0.0 | Pdawg | ARM32 decoder source generator for Ontos. |
| 2026-10-13 22:12:17 | [Authio.Testing](https://www.nuget.org/packages/Authio.Testing) | 0.7.0 | auth.io | Test an application that uses Authio without an Authio server: an in-memory fak… |
| 2026-10-13 22:12:58 | [CacheAnalyzer.Core](https://www.nuget.org/packages/CacheAnalyzer.Core) | 0.1.1 | vadiks93 | Advisory response analysis for discovering caching opportunities without modify… |
| 2026-10-13 22:12:59 | [CacheAnalyzerHelper](https://www.nuget.org/packages/CacheAnalyzerHelper) | 0.1.1 | vadiks93 | Advisory response analysis for discovering caching opportunities without modify… |
| 2026-10-13 22:13:01 | [CacheAnalyzer.AspNetCore](https://www.nuget.org/packages/CacheAnalyzer.AspNetCore) | 0.1.1 | vadiks93 | Advisory response analysis for discovering caching opportunities without modify… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
