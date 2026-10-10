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

## Latest list — 2026-10-10 03:20 UTC

New packages created between 2026-10-10 02:19 UTC and 2026-10-10 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T03-20-53-305283Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 02:28:15 | [SpectraUtils.AspNetCore](https://www.nuget.org/packages/SpectraUtils.AspNetCore) | 3.0.0 | Oğuzhan KARAGÜZEL | ASP.NET Core add-ons for SpectraUtils: file upload validation (allowed extensio… |
| 2026-10-10 02:37:33 | [Equatables](https://www.nuget.org/packages/Equatables) | 0.0.1-alpha | Scott Sanderson | Package Description |
| 2026-10-10 03:04:55 | [LogVue.Data](https://www.nuget.org/packages/LogVue.Data) | 1.0.0 | Matt Gordon | Provider-agnostic data model for the LogVue log dashboard. |
| 2026-10-10 03:05:13 | [LogVue.Services](https://www.nuget.org/packages/LogVue.Services) | 1.0.0 | Matt Gordon | Query engine, services and Serilog sink for the LogVue log dashboard. |
| 2026-10-10 03:05:30 | [LogVue.Data.Npgsql](https://www.nuget.org/packages/LogVue.Data.Npgsql) | 1.0.0 | Matt Gordon | PostgreSQL storage for the LogVue log dashboard. |
| 2026-10-10 03:05:44 | [LogVue](https://www.nuget.org/packages/LogVue) | 1.0.0 | Matt Gordon | An in-process Blazor dashboard for viewing, querying and deleting your ASP.NET… |
| 2026-10-10 03:06:00 | [LogVue.Data.MySql](https://www.nuget.org/packages/LogVue.Data.MySql) | 1.0.0 | Matt Gordon | MySQL storage for the LogVue log dashboard. |
| 2026-10-10 03:06:23 | [LogVue.Data.Sql](https://www.nuget.org/packages/LogVue.Data.Sql) | 1.0.0 | Matt Gordon | SQL Server storage for the LogVue log dashboard. |
| 2026-10-10 03:06:43 | [LogVue.Data.Sqlite](https://www.nuget.org/packages/LogVue.Data.Sqlite) | 1.0.0 | Matt Gordon | SQLite storage for the LogVue log dashboard. |
| 2026-10-10 03:11:20 | [Webority.Insights](https://www.nuget.org/packages/Webority.Insights) | 0.1.0 | Webority Technologies | Product insights a product hosts on its own data: daily collectors for PostHog… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
