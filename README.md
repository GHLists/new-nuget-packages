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

## Latest list — 2026-11-21 15:21 UTC

New packages created between 2026-11-21 14:20 UTC and 2026-11-21 15:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T15-21-45-109875Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 14:22:04 | [Tinos.Api.Common](https://www.nuget.org/packages/Tinos.Api.Common) | 1.0.0-alpha | Tinos API contributors | The common API for Tinos |
| 2026-11-21 14:22:32 | [Dst.Api.Handler](https://www.nuget.org/packages/Dst.Api.Handler) | 2.0.1 | DST | Production-ready .NET 8 generic HTTP API and File handler library with unified… |
| 2026-11-21 14:53:58 | [FlowPDF](https://www.nuget.org/packages/FlowPDF) | 1.0.0 | Edwin Abreu & FlowPDF Contrib… | Enterprise reporting and document generation engine for .NET. Features a Fluent… |
| 2026-11-21 14:54:57 | [Font.Metadata](https://www.nuget.org/packages/Font.Metadata) | 1.0.0 | Dmitry Garavsky | Read SFNT/TTC, WOFF, WOFF2 and EOT font metadata on .NET 10 with partial result… |
| 2026-11-21 14:54:59 | [Font.Metadata.Spdx](https://www.nuget.org/packages/Font.Metadata.Spdx) | 1.0.0 | Dmitry Garavsky | Source-preserving SPDX analysis of decoded font license records and external li… |
| 2026-11-21 14:55:01 | [Font.Metadata.Tool](https://www.nuget.org/packages/Font.Metadata.Tool) | 1.0.0 | Dmitry Garavsky | Inspect font metadata and explicitly supplied license documents with plain or J… |
| 2026-11-21 15:06:07 | [MachinaXX.Chassis.Backup.GoogleDrive](https://www.nuget.org/packages/MachinaXX.Chassis.Backup.GoogleDrive) | 4.4.1 | Alan Benington | Google Drive (Shared Drive) store for the MachinaXX.Chassis database backup's r… |
| 2026-11-21 15:08:31 | [Fable.Lit.Dsl.Metrino](https://www.nuget.org/packages/Fable.Lit.Dsl.Metrino) | 1.0.0 | Jordan Marr | Metrino (Windows Phone / Windows 8 Metro design system) web component bindings… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
