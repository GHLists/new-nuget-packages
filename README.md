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

## Latest list — 2026-11-28 04:21 UTC

New packages created between 2026-11-28 03:21 UTC and 2026-11-28 04:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-28T04-21-15-996013Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-28 03:28:22 | [Pushq](https://www.nuget.org/packages/Pushq) | 1.0.0 | blissfulrays | Official .NET client for pushq, a self-hosted HTTP push task queue (an open-sou… |
| 2026-11-28 03:35:18 | [DataGateway](https://www.nuget.org/packages/DataGateway) | 1.0.0 | Maxim Konstantinovski | Read-only JSON and MCP endpoints over relational data for ASP.NET Core apps: li… |
| 2026-11-28 03:35:19 | [DataGateway.Core](https://www.nuget.org/packages/DataGateway.Core) | 1.0.0 | Maxim Konstantinovski | DataGateway's catalog model, query validation and error contract. Brought in by… |
| 2026-11-28 03:35:20 | [DataGateway.Data](https://www.nuget.org/packages/DataGateway.Data) | 1.0.0 | Maxim Konstantinovski | DataGateway's catalog reader and database engine base classes. Derive DatabaseE… |
| 2026-11-28 03:35:21 | [DataGateway.Data.PostgreSql](https://www.nuget.org/packages/DataGateway.Data.PostgreSql) | 1.0.0 | Maxim Konstantinovski | DataGateway's PostgreSQL engine (Npgsql). Register it with AddEngine to serve c… |
| 2026-11-28 03:35:23 | [DataGateway.Data.Snowflake](https://www.nuget.org/packages/DataGateway.Data.Snowflake) | 1.0.0 | Maxim Konstantinovski | DataGateway's Snowflake engine. Register it with AddEngine to serve catalogued… |
| 2026-11-28 03:35:24 | [DataGateway.Data.SqlServer](https://www.nuget.org/packages/DataGateway.Data.SqlServer) | 1.0.0 | Maxim Konstantinovski | DataGateway's SQL Server engine (Microsoft.Data.SqlClient). Register it with Ad… |
| 2026-11-28 03:38:43 | [BnSpellNum](https://www.nuget.org/packages/BnSpellNum) | 0.1.0 | Ediphas Labs | Spell out numbers in Bangla: words, currency (taka/paisa), ordinals, years and… |
| 2026-11-28 03:52:32 | [Tydocx](https://www.nuget.org/packages/Tydocx) | 0.1.0 | tydocx contributors | Convert Typst documents to editable Word (.docx) files. |
| 2026-11-28 04:02:09 | [NetPublishOptimizer](https://www.nuget.org/packages/NetPublishOptimizer) | 0.9.0 | PLFJY | Unified .NET publish optimization SDK. |
| 2026-11-28 04:02:11 | [NetPublishOptimizer.Diagnostics.EventPipe](https://www.nuget.org/packages/NetPublishOptimizer.Diagnostics.EventPipe) | 0.9.0 | PLFJY | Optional EventPipe collector for NetPublishOptimizer. Installed independently o… |
| 2026-11-28 04:02:13 | [NetPublishOptimizer.MSBuild](https://www.nuget.org/packages/NetPublishOptimizer.MSBuild) | 0.9.0 | PLFJY | Opt-in MSBuild post-publish integration that orchestrates the NetPublishOptimiz… |
| 2026-11-28 04:02:15 | [NetPublishOptimizer.Tool](https://www.nuget.org/packages/NetPublishOptimizer.Tool) | 0.9.0 | PLFJY | Command-line optimizer and validator for already-published .NET application dir… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
