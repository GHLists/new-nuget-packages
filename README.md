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

## Latest list — 2026-10-20 18:22 UTC

New packages created between 2026-10-20 17:21 UTC and 2026-10-20 18:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T18-22-16-711783Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 17:24:45 | [APIVerve.API.BarcodeReader](https://www.nuget.org/packages/APIVerve.API.BarcodeReader) | 1.2.1 | APIVerve | Barcode Reader decodes 1D barcodes from an uploaded image or an image URL, incl… |
| 2026-10-20 17:25:05 | [SafeMigrations.Core](https://www.nuget.org/packages/SafeMigrations.Core) | 0.1.0 | rahulnagrikar | Inspect EF Core migrations for production safety risks. |
| 2026-10-20 17:26:08 | [SafeMigrations.Rules](https://www.nuget.org/packages/SafeMigrations.Rules) | 0.1.0 | rahulnagrikar | Inspect EF Core migrations for production safety risks. |
| 2026-10-20 17:26:36 | [SafeMigrations.EFCore](https://www.nuget.org/packages/SafeMigrations.EFCore) | 0.1.0 | rahulnagrikar | Inspect EF Core migrations for production safety risks. |
| 2026-10-20 17:28:04 | [Prowl.Origami.CSharp](https://www.nuget.org/packages/Prowl.Origami.CSharp) | 3.8.7 | Prowl Contributors | Roslyn backed C# language services for the Origami CodeEditor: completion, quic… |
| 2026-10-20 17:35:50 | [PowerForge.Web.Protocols](https://www.nuget.org/packages/PowerForge.Web.Protocols) | 3.0.171 | Przemyslaw Klys | Dependency-free web interchange: IndexNow, sitemaps, syndication feeds and JSON… |
| 2026-10-20 17:41:25 | [OmniEurope.Documents](https://www.nuget.org/packages/OmniEurope.Documents) | 1.0.0 | OmniEurope contributors | Create, edit, convert and read Word, Excel, PDF, Markdown and CSV documents, wi… |
| 2026-10-20 17:43:17 | [Metronome.OpenAPI](https://www.nuget.org/packages/Metronome.OpenAPI) | 0.1.0 | OpenAPI, Jamie Howarth | A .NET library for accessing Metronome's OpenAPI-compatible API endpoints |
| 2026-10-20 17:48:36 | [FinClient](https://www.nuget.org/packages/FinClient) | 0.1.1 | BizJaya TechLab S/B | Official .NET SDK for the FinCopy public API: hosted MetaTrader accounts, tradi… |
| 2026-10-20 17:49:01 | [IBeam.Management.Identity.Target.Api](https://www.nuget.org/packages/IBeam.Management.Identity.Target.Api) | 2.16.0 | MedPACTech | Optional target API for app-scoped customer Identity management. |
| 2026-10-20 17:49:02 | [IBeam.Management.Identity.Target.Services](https://www.nuget.org/packages/IBeam.Management.Identity.Target.Services) | 2.16.0 | MedPACTech | Optional app-scoped customer Identity management services, separate from suppor… |
| 2026-10-20 17:50:39 | [ResXLocalization.MessageFormat](https://www.nuget.org/packages/ResXLocalization.MessageFormat) | 2.0.0 | David Liebeherr, rent-a-devel… | The opt-in ICU MessageFormat formatter for ResXLocalization: plural and select… |
| 2026-10-20 18:03:58 | [JJConsulting.DbUp.Cli](https://www.nuget.org/packages/JJConsulting.DbUp.Cli) | 1.0.1 | JJConsulting | Local and CI SQL Server migration commands using JJConsulting.DbUp. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
