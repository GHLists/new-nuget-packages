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

## Latest list — 2026-10-06 07:20 UTC

New packages created between 2026-10-06 06:20 UTC and 2026-10-06 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T07-20-54-705235Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 06:21:47 | [Invex.Extensions.Logging.Utils](https://www.nuget.org/packages/Invex.Extensions.Logging.Utils) | 0.5.0 | Declan Smith | Useful utilities for Microsoft.Extensions.Logging |
| 2026-10-06 06:25:20 | [ConnectivityProbe](https://www.nuget.org/packages/ConnectivityProbe) | 1.0.0 | Fatih Umut Memişoğlu | Lets an application test, from inside each of its own pods/instances, whether i… |
| 2026-10-06 06:27:19 | [MarketSDK](https://www.nuget.org/packages/MarketSDK) | 1.0.0 | Focussoft HQ LLC | The MarketSDK client for .NET. |
| 2026-10-06 06:31:35 | [DP.Blazor.MapLibre.ProjPlugin](https://www.nuget.org/packages/DP.Blazor.MapLibre.ProjPlugin) | 2.1.0 | Denis Polagaev | Any-projection plugin for DP.Blazor.MapLibre (maplibre-proj / backproj / proj-w… |
| 2026-10-06 06:31:36 | [DP.Blazor.MapLibre.PmtilesPlugin](https://www.nuget.org/packages/DP.Blazor.MapLibre.PmtilesPlugin) | 2.1.0 | Denis Polagaev | PMTiles protocol plugin for DP.Blazor.MapLibre (pmtiles:// sources via HTTP Ran… |
| 2026-10-06 06:45:22 | [InstrumentComponents](https://www.nuget.org/packages/InstrumentComponents) | 0.1.1 | josh-hemphill | High-level instrument discovery and typed IVI-inspired classes — VISA-agnostic… |
| 2026-10-06 06:45:23 | [InstrumentComponents.Visa](https://www.nuget.org/packages/InstrumentComponents.Visa) | 0.1.1 | josh-hemphill | NI-VISA / Keysight VISA backend for InstrumentComponents over vendor-neutral Iv… |
| 2026-10-06 06:45:44 | [CookiesRegTech.Umbraco](https://www.nuget.org/packages/CookiesRegTech.Umbraco) | 1.0.0 | SKYNET TECHNOLOGIES USA LLC | CookiesRegTech cookie consent: guided connect, banner with automatic tracker bl… |
| 2026-10-06 07:10:38 | [Leander.Configuration](https://www.nuget.org/packages/Leander.Configuration) | 1.0.1 | Leander Tilsted Jul Withen | Configuration contracts: every key with its primitive, presence and description… |
| 2026-10-06 07:10:42 | [SI.WA.UI.Aether](https://www.nuget.org/packages/SI.WA.UI.Aether) | 1.1.0 | seriiiastreb@gmail.com | Aether theme for the WA.Core Blazor UI: the AetherUI component library (Kit/, c… |
| 2026-10-06 07:14:08 | [FEB.EventSourcing.TestKit](https://www.nuget.org/packages/FEB.EventSourcing.TestKit) | 9.2.1 | FEB Solutions | Test helpers for FEB.EventSourcing: snapshot contract roundtrip assertions for… |
| 2026-10-06 07:14:09 | [FEB.EventSourcing.Sql](https://www.nuget.org/packages/FEB.EventSourcing.Sql) | 9.2.1 | FEB Solutions | Relational persistence core for FEB.EventSourcing (events, snapshots, outbox) o… |
| 2026-10-06 07:14:12 | [FEB.EventSourcing.StateContracts](https://www.nuget.org/packages/FEB.EventSourcing.StateContracts) | 9.2.1 | FEB Solutions | Aggregate state contracts shared by snapshotting and caching ([AutoSnapshot], [… |
| 2026-10-06 07:14:12 | [FEB.EventSourcing.SqlServer](https://www.nuget.org/packages/FEB.EventSourcing.SqlServer) | 9.2.1 | FEB Solutions | SQL Server persistence for FEB.EventSourcing (events, snapshots, outbox) via Mi… |
| 2026-10-06 07:14:13 | [FEB.EventSourcing.Postgres](https://www.nuget.org/packages/FEB.EventSourcing.Postgres) | 9.2.1 | FEB Solutions | PostgreSQL persistence for FEB.EventSourcing (events, snapshots, outbox) via Np… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
