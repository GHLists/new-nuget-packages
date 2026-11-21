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

## Latest list — 2026-11-21 18:19 UTC

New packages created between 2026-11-21 17:19 UTC and 2026-11-21 18:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T18-19-15-321903Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 17:29:00 | [PgBolt.Abstractions](https://www.nuget.org/packages/PgBolt.Abstractions) | 0.1.0 | nightNo1r | PgBolt job contracts, client API, source generator and analyzers. |
| 2026-11-21 17:29:01 | [PgBolt.Postgres](https://www.nuget.org/packages/PgBolt.Postgres) | 0.1.0 | nightNo1r | PostgreSQL job storage, migrations and producer API for PgBolt. |
| 2026-11-21 17:29:02 | [PgBolt.Server](https://www.nuget.org/packages/PgBolt.Server) | 0.1.0 | nightNo1r | Hosted workers, queue scheduling and job execution for PgBolt. |
| 2026-11-21 17:29:03 | [PgBolt.Dashboard](https://www.nuget.org/packages/PgBolt.Dashboard) | 0.1.0 | nightNo1r | Embeddable ASP.NET Core dashboard for PgBolt (Razor components + htmx). |
| 2026-11-21 17:29:04 | [PgBolt.OpenTelemetry](https://www.nuget.org/packages/PgBolt.OpenTelemetry) | 0.1.0 | nightNo1r | OpenTelemetry instrumentation for PgBolt: trace source, meter and histogram buc… |
| 2026-11-21 17:34:52 | [TubeSharp](https://www.nuget.org/packages/TubeSharp) | 26.11.0-ea | Boba | A lightweight, strongly typed YouTube metadata client powered by the Innertube… |
| 2026-11-21 17:39:42 | [PocketCsvReader.NetTopologySuite](https://www.nuget.org/packages/PocketCsvReader.NetTopologySuite) | 2.79.0 | Cédric L. Charlier | Opt-in WKT and GeoJSON geometry parsers for PocketCsvReader. |
| 2026-11-21 17:56:54 | [Hermex.Testing](https://www.nuget.org/packages/Hermex.Testing) | 2.3.0 | Suresh Subramanian | Test helper for Hermex: wait for the email your app sends, then read its subjec… |
| 2026-11-21 18:00:20 | [Suwbackkit.Cli](https://www.nuget.org/packages/Suwbackkit.Cli) | 0.5.0 | Manomenu | The skeleton of a .NET command line that talks to a Suwbackkit server: the serv… |
| 2026-11-21 18:03:37 | [LifeAstroApi](https://www.nuget.org/packages/LifeAstroApi) | 0.1.0 | Ayanshu Life | Official .NET client for LifeAstroAPI (https://lifeastroapi.com), the Vedic ast… |
| 2026-11-21 18:03:38 | [LifeAstroApi.Extensions.DependencyInjection](https://www.nuget.org/packages/LifeAstroApi.Extensions.DependencyInjection) | 0.1.0 | Ayanshu Life | Registers the LifeAstroAPI .NET client (package LifeAstroApi) in Microsoft.Exte… |
| 2026-11-21 18:10:08 | [NetPdfKit.Core](https://www.nuget.org/packages/NetPdfKit.Core) | 1.1.0 | Ssewannonda Keith Edwin | Create, view, and manage PDF files with one fluent API. Lean core without image… |
| 2026-11-21 18:12:58 | [MattEland.HopeLab.Themes.Tokens](https://www.nuget.org/packages/MattEland.HopeLab.Themes.Tokens) | 0.1.12 | Matt Eland | The HopeLab theme token model: the shared token contract, theme token files, co… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
