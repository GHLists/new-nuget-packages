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

## Latest list — 2026-10-31 04:20 UTC

New packages created between 2026-10-31 03:20 UTC and 2026-10-31 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T04-20-13-436136Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 03:27:50 | [Outer.APM](https://www.nuget.org/packages/Outer.APM) | 10.0.0 | OuterWolf | Zero-config OpenTelemetry (traces, metrics, logs) wiring for ASP.NET Core .NET… |
| 2026-10-31 03:50:15 | [Messaia.Net.Base.Mail.Api](https://www.nuget.org/packages/Messaia.Net.Base.Mail.Api) | 10.2.0-beta06 | Fouad Messaia | Package Description |
| 2026-10-31 03:50:17 | [Messaia.Net.Base.Mail.Contracts](https://www.nuget.org/packages/Messaia.Net.Base.Mail.Contracts) | 10.2.0-beta06 | Fouad Messaia | Package Description |
| 2026-10-31 03:50:19 | [Messaia.Net.Base.Mail.DataAccess](https://www.nuget.org/packages/Messaia.Net.Base.Mail.DataAccess) | 10.2.0-beta06 | Fouad Messaia | Package Description |
| 2026-10-31 03:50:22 | [Messaia.Net.Base.Mail.Enums](https://www.nuget.org/packages/Messaia.Net.Base.Mail.Enums) | 10.2.0-beta06 | Fouad Messaia | Package Description |
| 2026-10-31 03:50:24 | [Messaia.Net.Base.Mail.Mapping](https://www.nuget.org/packages/Messaia.Net.Base.Mail.Mapping) | 10.2.0-beta06 | Fouad Messaia | Package Description |
| 2026-10-31 03:50:26 | [Messaia.Net.Base.Mail.Models](https://www.nuget.org/packages/Messaia.Net.Base.Mail.Models) | 10.2.0-beta06 | Fouad Messaia | Package Description |
| 2026-10-31 03:50:28 | [Messaia.Net.Base.Mail.Repositories](https://www.nuget.org/packages/Messaia.Net.Base.Mail.Repositories) | 10.2.0-beta06 | Fouad Messaia | Package Description |
| 2026-10-31 03:50:30 | [Messaia.Net.Base.Mail.Repositories.Impl](https://www.nuget.org/packages/Messaia.Net.Base.Mail.Repositories.Impl) | 10.2.0-beta06 | Fouad Messaia | Package Description |
| 2026-10-31 03:50:32 | [Messaia.Net.Base.Mail.Services](https://www.nuget.org/packages/Messaia.Net.Base.Mail.Services) | 10.2.0-beta06 | Fouad Messaia | Package Description |
| 2026-10-31 03:50:34 | [Messaia.Net.Base.Mail.Services.Impl](https://www.nuget.org/packages/Messaia.Net.Base.Mail.Services.Impl) | 10.2.0-beta06 | Fouad Messaia | Package Description |
| 2026-10-31 03:50:37 | [Messaia.Net.Base.Mail.ViewModels](https://www.nuget.org/packages/Messaia.Net.Base.Mail.ViewModels) | 10.2.0-beta06 | Fouad Messaia | Package Description |
| 2026-10-31 03:50:39 | [Messaia.Net.Base.Mail.Workers](https://www.nuget.org/packages/Messaia.Net.Base.Mail.Workers) | 10.2.0-beta06 | Fouad Messaia | Package Description |
| 2026-10-31 03:59:56 | [Thunder.Dbf.Sql](https://www.nuget.org/packages/Thunder.Dbf.Sql) | 0.1.0 | ProjectThunder | Migrate dBASE and FoxPro tables to SQLite, SQL Server or PostgreSQL, and keep t… |
| 2026-10-31 03:59:56 | [Thunder.Dbf](https://www.nuget.org/packages/Thunder.Dbf) | 0.1.0 | ProjectThunder | Pure .NET engine for dBASE, FoxPro and Clipper files: tables, memos and indexes… |
| 2026-10-31 03:59:57 | [thunder-dbf](https://www.nuget.org/packages/thunder-dbf) | 0.1.0 | ProjectThunder | thunder-dbf: check, inspect, import, export and migrate dBASE and FoxPro data f… |
| 2026-10-31 04:01:05 | [Moka.AI.Mcp](https://www.nuget.org/packages/Moka.AI.Mcp) | 0.5.0 | jacobwi, BCat, Moka | Model Context Protocol (MCP) client integration for Moka.AI — connect MCP serve… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
