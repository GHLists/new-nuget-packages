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

## Latest list — 2026-11-09 14:19 UTC

New packages created between 2026-11-09 13:21 UTC and 2026-11-09 14:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T14-19-08-859913Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 13:23:46 | [Fusonic.Extensions.Aspire.Hosting](https://www.nuget.org/packages/Fusonic.Extensions.Aspire.Hosting) | 10.3.0 | Fusonic | Extensions for the Aspire AppHost: group containers as a Docker Compose stack,… |
| 2026-11-09 13:24:42 | [Webority.EntityProfiles](https://www.nuget.org/packages/Webority.EntityProfiles) | 0.2.1 | Webority.EntityProfiles | Per-head entity profiles for an EF Core DbContext several web heads share: a ge… |
| 2026-11-09 13:24:46 | [Webority.HeadGuard](https://www.nuget.org/packages/Webority.HeadGuard) | 0.2.1 | Webority.HeadGuard | Starts each deployed .NET head up to the point before it serves, with only its… |
| 2026-11-09 13:25:45 | [KpokPatagon.Data.PostgreSql](https://www.nuget.org/packages/KpokPatagon.Data.PostgreSql) | 10.3.26313.2 | Marcelo Vargas | Database interface for PostgreSQL of Kpok Patagon Framework. |
| 2026-11-09 13:28:42 | [Tubatools.SteamToolbox](https://www.nuget.org/packages/Tubatools.SteamToolbox) | 1.0.0 | 图吧工具箱 | Steam 工具箱插件：本机账号与多存储库游戏管理、封面与时长、SteamKit 挂时长 |
| 2026-11-09 13:33:47 | [DotNetQuery](https://www.nuget.org/packages/DotNetQuery) | 0.1.0 | DotNetQuery contributors | Core query client for DotNetQuery: single-flight deduplication, stale-while-rev… |
| 2026-11-09 13:33:48 | [DotNetQuery.Abstractions](https://www.nuget.org/packages/DotNetQuery.Abstractions) | 0.1.0 | DotNetQuery contributors | Provider-agnostic abstractions for DotNetQuery, a React Query-style query and m… |
| 2026-11-09 13:33:49 | [DotNetQuery.DevTools](https://www.nuget.org/packages/DotNetQuery.DevTools) | 0.1.0 | DotNetQuery contributors | OpenTelemetry metrics, activities and a live statistics inspector for DotNetQue… |
| 2026-11-09 13:33:49 | [DotNetQuery.Persistence](https://www.nuget.org/packages/DotNetQuery.Persistence) | 0.1.0 | DotNetQuery contributors | Optional offline persistence for DotNetQuery client hosts (Blazor, MAUI). Not i… |
| 2026-11-09 13:33:50 | [DotNetQuery.Redis](https://www.nuget.org/packages/DotNetQuery.Redis) | 0.1.0 | DotNetQuery contributors | Redis-backed IQueryStore for DotNetQuery with atomic tag versioning and a distr… |
| 2026-11-09 13:33:51 | [DotNetQuery.SourceGenerator](https://www.nuget.org/packages/DotNetQuery.SourceGenerator) | 0.1.0 | DotNetQuery contributors | Roslyn source generator and analyzer that turn [Cache]/[InvalidateCache] attrib… |
| 2026-11-09 13:38:28 | [SimdSkia.Avalonia.Android](https://www.nuget.org/packages/SimdSkia.Avalonia.Android) | 0.1.4 | hnlyf168 | Android Activity, input and framebuffer presentation for SimdSkia managed CPU/S… |
| 2026-11-09 13:51:17 | [Themia.Modules.Identity.SecondFactor](https://www.nuget.org/packages/Themia.Modules.Identity.SecondFactor) | 0.58.0 | Sarawut Phaekuntod | Bridge between Themia.SecondFactor and Themia Identity — the second-factor poli… |
| 2026-11-09 13:52:14 | [GroupDocs.Assembly.Mcp](https://www.nuget.org/packages/GroupDocs.Assembly.Mcp) | 26.11.0 | GroupDocs Contributors | MCP server for GroupDocs.Assembly — generate Word, Excel, PowerPoint, PDF and e… |
| 2026-11-09 13:53:54 | [Onde.Code](https://www.nuget.org/packages/Onde.Code) | 1.1.2 | Seto Elkahfi | Coding agent for fine-tuning, managing and deploying models on Onde Inference. |
| 2026-11-09 14:03:57 | [PanasonicComfortCloudClient](https://www.nuget.org/packages/PanasonicComfortCloudClient) | 1.0.0 | Neil Colvin | Independent typed asynchronous C# client for Panasonic Comfort Cloud and Aquare… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
