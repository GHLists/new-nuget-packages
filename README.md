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

## Latest list — 2026-11-03 20:21 UTC

New packages created between 2026-11-03 19:21 UTC and 2026-11-03 20:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T20-21-17-362691Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 19:24:33 | [PrivateMarkets.Metrics](https://www.nuget.org/packages/PrivateMarkets.Metrics) | 0.4.0 | Nicolas | Performance metrics for private equity and private markets funds: TVPI, DPI, RV… |
| 2026-11-03 19:24:34 | [PrivateMarkets.Metrics.Mcp](https://www.nuget.org/packages/PrivateMarkets.Metrics.Mcp) | 0.4.0 | Nicolas | MCP server exposing PrivateMarkets.Metrics (fund metrics, PME, vintage summarie… |
| 2026-11-03 19:34:30 | [Bakverk.Blazor](https://www.nuget.org/packages/Bakverk.Blazor) | 1.0.2 | Ola Bäcker | Common Blazor components and utilities built on MudBlazor |
| 2026-11-03 19:50:21 | [Badger.SqlMigrate](https://www.nuget.org/packages/Badger.SqlMigrate) | 0.1.0 | Lone Badger Tech, LLC | Badger SQL Migrate: free, cross-platform, hash-certified database migrations fo… |
| 2026-11-03 19:50:32 | [Eternet.Imports.Contracts](https://www.nuget.org/packages/Eternet.Imports.Contracts) | 1.0.0 | Eternet.Imports.Contracts | Package Description |
| 2026-11-03 19:57:41 | [Indigina.DCM.BookingManager.WebApi](https://www.nuget.org/packages/Indigina.DCM.BookingManager.WebApi) | 1.0.0 | Indigina | Package contains web api for DCM.BookingManager service. |
| 2026-11-03 19:57:42 | [Indigina.DCM.BookingManager.Client](https://www.nuget.org/packages/Indigina.DCM.BookingManager.Client) | 1.0.0 | Indigina | Package contains client for DCM.BookingManager service. |
| 2026-11-03 20:09:43 | [TabBlazor.Linq2GraphQL](https://www.nuget.org/packages/TabBlazor.Linq2GraphQL) | 1.7.39-beta | Joakim Dangården | Linq2GraphQL adapter for TabBlazor DataView: sorts, searches, filters and pages… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
