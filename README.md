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

## Latest list — 2026-11-05 09:21 UTC

New packages created between 2026-11-05 08:20 UTC and 2026-11-05 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T09-21-15-806251Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 08:37:34 | [Fuaran.Facts](https://www.nuget.org/packages/Fuaran.Facts) | 0.1.0 | Andrew J. Willshire | Fuaran.Facts - the .NET reference implementation of the Fact wire specification… |
| 2026-11-05 08:49:07 | [NeoAstra.Mcp](https://www.nuget.org/packages/NeoAstra.Mcp) | 1.12.0 | NeoAstra.Mcp | MCP plugin for NeoAstra: in a development session, the application connects to… |
| 2026-11-05 09:05:02 | [EntityTracker.AspNetCore](https://www.nuget.org/packages/EntityTracker.AspNetCore) | 0.1.0 | EntityTracker.AspNetCore | Attribute-driven EF Core change notifications with scoped SignalR subscriptions. |
| 2026-11-05 09:06:14 | [Kameleon](https://www.nuget.org/packages/Kameleon) | 1.0.0 | Matt Gordon | A theme engine for Blazor sites: compiled and static themes, per-tenant and per… |
| 2026-11-05 09:06:21 | [Kameleon.Abstractions](https://www.nuget.org/packages/Kameleon.Abstractions) | 1.0.0 | Matt Gordon | The contracts and components a Kameleon theme is built with. A theme package re… |
| 2026-11-05 09:06:27 | [Kameleon.Data](https://www.nuget.org/packages/Kameleon.Data) | 1.0.0 | Matt Gordon | Provider-agnostic data model for the Kameleon theme engine's tenant and user se… |
| 2026-11-05 09:06:35 | [Kameleon.Data.MySql](https://www.nuget.org/packages/Kameleon.Data.MySql) | 1.0.0 | Matt Gordon | MySQL storage for the Kameleon theme engine. |
| 2026-11-05 09:06:41 | [Kameleon.Data.Npgsql](https://www.nuget.org/packages/Kameleon.Data.Npgsql) | 1.0.0 | Matt Gordon | PostgreSQL storage for the Kameleon theme engine. |
| 2026-11-05 09:06:49 | [Kameleon.Data.Sql](https://www.nuget.org/packages/Kameleon.Data.Sql) | 1.0.0 | Matt Gordon | SQL Server storage for the Kameleon theme engine. |
| 2026-11-05 09:06:55 | [Kameleon.Data.Sqlite](https://www.nuget.org/packages/Kameleon.Data.Sqlite) | 1.0.0 | Matt Gordon | SQLite storage for the Kameleon theme engine. |
| 2026-11-05 09:07:00 | [Kameleon.Services](https://www.nuget.org/packages/Kameleon.Services) | 1.0.0 | Matt Gordon | Theme catalog, eligibility, resolution and settings for the Kameleon theme engi… |
| 2026-11-05 09:10:07 | [NetLiu.PowerShellLib](https://www.nuget.org/packages/NetLiu.PowerShellLib) | 2.0.2 | 刘冬云 | 强类型 PowerShell 调用封装：Source / Target / Stage 三端点 + 传输门面，编译期由增量生成器生成命令扩展方法，支持本地、W… |
| 2026-11-05 09:10:35 | [NetLiu.PowerShellLib.Runtime](https://www.nuget.org/packages/NetLiu.PowerShellLib.Runtime) | 2.0.2 | 刘冬云 | NetLiu.PowerShellLib 的运行时实现：为 net472 提供 Windows PowerShell 5.1 引擎、为 net8.0 提供 P… |
| 2026-11-05 09:15:21 | [Mockly.Server](https://www.nuget.org/packages/Mockly.Server) | 1.14.0 | Dennis Doomen | Exposes a Mockly HttpMock as a real loopback HTTP server for callers that canno… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
