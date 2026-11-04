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

## Latest list — 2026-11-04 08:20 UTC

New packages created between 2026-11-04 07:21 UTC and 2026-11-04 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T08-20-59-425291Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 07:37:06 | [BlogKrafter](https://www.nuget.org/packages/BlogKrafter) | 1.0.0 | Matt Gordon | A drop-in Blazor blog for ASP.NET Core sites: public pages, feeds and an editor… |
| 2026-11-04 07:37:09 | [BlogKrafter.Data](https://www.nuget.org/packages/BlogKrafter.Data) | 1.0.0 | Matt Gordon | Provider-agnostic data model for the BlogKrafter blog engine. |
| 2026-11-04 07:37:15 | [BlogKrafter.Data.Npgsql](https://www.nuget.org/packages/BlogKrafter.Data.Npgsql) | 1.0.0 | Matt Gordon | PostgreSQL storage for the BlogKrafter blog engine. |
| 2026-11-04 07:37:20 | [BlogKrafter.Data.MySql](https://www.nuget.org/packages/BlogKrafter.Data.MySql) | 1.0.0 | Matt Gordon | MySQL storage for the BlogKrafter blog engine. |
| 2026-11-04 07:37:25 | [BlogKrafter.Data.Sql](https://www.nuget.org/packages/BlogKrafter.Data.Sql) | 1.0.0 | Matt Gordon | SQL Server storage for the BlogKrafter blog engine. |
| 2026-11-04 07:37:30 | [BlogKrafter.Data.Sqlite](https://www.nuget.org/packages/BlogKrafter.Data.Sqlite) | 1.0.0 | Matt Gordon | SQLite storage for the BlogKrafter blog engine. |
| 2026-11-04 07:37:34 | [BlogKrafter.Services](https://www.nuget.org/packages/BlogKrafter.Services) | 1.0.0 | Matt Gordon | Services, content rendering and feeds for the BlogKrafter blog engine. |
| 2026-11-04 07:42:25 | [Lemon.Hub.Client](https://www.nuget.org/packages/Lemon.Hub.Client) | 0.2.0 | Tracy Ma | Signing in to the Lemon hub as a public OpenID Connect client (authorization co… |
| 2026-11-04 07:42:27 | [Lemon.Hub.Client.Desktop](https://www.nuget.org/packages/Lemon.Hub.Client.Desktop) | 0.2.0 | Tracy Ma | Signing in to the Lemon hub from a desktop app: the system browser, and the ans… |
| 2026-11-04 07:42:29 | [Lemon.Hub.Client.Browser](https://www.nuget.org/packages/Lemon.Hub.Client.Browser) | 0.2.0 | Tracy Ma | Signing in to the Lemon hub from a WebAssembly app, by redirect to the sign-in… |
| 2026-11-04 07:49:54 | [SonnetDB.CAP](https://www.nuget.org/packages/SonnetDB.CAP) | 5.0.0 | maikebing | DotNetCore.CAP integration with SonnetDB Document Store and MQ through SonnetDB… |
| 2026-11-04 07:49:56 | [SonnetDB.Client](https://www.nuget.org/packages/SonnetDB.Client) | 5.0.0 | maikebing | SonnetDB 原生 HTTP/2 Frame 远程访问基础库，不包含嵌入式引擎或 REST 回落。 |
| 2026-11-04 07:49:58 | [SonnetDB.Protocol](https://www.nuget.org/packages/SonnetDB.Protocol) | 5.0.0 | maikebing | SonnetDB 二进制 Frame 信封、操作码和安全二进制基础类型，不依赖数据库引擎。 |
| 2026-11-04 07:49:59 | [SonnetDB.Testcontainers](https://www.nuget.org/packages/SonnetDB.Testcontainers) | 5.0.0 | maikebing | SonnetDB 的 Testcontainers for .NET 模块，用于在集成测试中启动临时 SonnetDB Server 容器并生成远程连接字符串。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
