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

## Latest list — 2026-10-21 00:21 UTC

New packages created between 2026-10-20 23:22 UTC and 2026-10-21 00:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T00-21-41-740253Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 23:25:11 | [Oracle.ManagedDataAccess.DependencyInjection](https://www.nuget.org/packages/Oracle.ManagedDataAccess.DependencyInjection) | 23.26.400 | Oracle | PLACEHOLDER: This NuGet package supports dependency injection for ODP.NET Core. |
| 2026-10-21 00:01:09 | [FiveM.Nui.Contracts](https://www.nuget.org/packages/FiveM.Nui.Contracts) | 1.0.0 | Rainbe | Generates TypeScript contract declarations from C# NUI DTOs. |
| 2026-10-21 00:01:28 | [FiveM.Nui](https://www.nuget.org/packages/FiveM.Nui) | 1.0.0 | Rainbe | Modern, high-performance, strongly typed bridge between C# client scripts and N… |
| 2026-10-21 00:06:24 | [TikTokShop.Api](https://www.nuget.org/packages/TikTokShop.Api) | 0.1.0 | Isaac Kogan | TikTok Shop API client for .NET 8+: signed requests, shop cipher handling, the… |
| 2026-10-21 00:12:47 | [Microsoft.PowerApps.AppInsights.BatchedTelemetry](https://www.nuget.org/packages/Microsoft.PowerApps.AppInsights.BatchedTelemetry) | 4.0.46 | Microsoft | This package contains the assemblies required for logging telemetry to Applicat… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
