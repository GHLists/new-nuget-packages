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

## Latest list — 2026-11-07 15:21 UTC

New packages created between 2026-11-07 14:21 UTC and 2026-11-07 15:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T15-21-25-524632Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 14:25:40 | [Canton.Ledger.AspNetCore](https://www.nuget.org/packages/Canton.Ledger.AspNetCore) | 0.8.0 | Peaceful Studio OÜ | ASP.NET Core integration for the Canton Ledger API clients. AddCantonLedgerProb… |
| 2026-11-07 14:25:54 | [Splice.Api.Token.Registry.Client](https://www.nuget.org/packages/Splice.Api.Token.Registry.Client) | 0.10.0.21 | Peaceful Studio OÜ | Typed HTTP client for the Splice Token Standard registry off-ledger API (token… |
| 2026-11-07 14:27:04 | [NormalizeAutoCADReferences](https://www.nuget.org/packages/NormalizeAutoCADReferences) | 1.0.0 | eirikksan | Normalizes AutoCAD managed assembly metadata and integrates compile-time refere… |
| 2026-11-07 14:38:37 | [Shirasagi0012.Material3Expressive.Avalonia](https://www.nuget.org/packages/Shirasagi0012.Material3Expressive.Avalonia) | 0.1.0 | Shirasagi0012 | Material 3 Expressive theme and controls for Avalonia, ported from Compose Mate… |
| 2026-11-07 14:42:21 | [Meziantou.Framework.Geo.Maps](https://www.nuget.org/packages/Meziantou.Framework.Geo.Maps) | 1.0.0 | meziantou | Loads offline map bundles: the borders, states and provinces, cities, rivers, l… |
| 2026-11-07 14:42:21 | [Meziantou.Framework.Geo.Maps.GeoPackage](https://www.nuget.org/packages/Meziantou.Framework.Geo.Maps.GeoPackage) | 1.0.0 | meziantou | Reads and writes the map bundles of Meziantou.Framework.Geo.Maps as GeoPackage… |
| 2026-11-07 14:42:22 | [Meziantou.Framework.Geo.Maps.Tool](https://www.nuget.org/packages/Meziantou.Framework.Geo.Maps.Tool) | 1.0.0 | meziantou | CLI to generate the offline map bundles of Meziantou.Framework.Geo.Maps: the bo… |
| 2026-11-07 14:42:37 | [GlanceWidgets.ApiSdk](https://www.nuget.org/packages/GlanceWidgets.ApiSdk) | 1.0.0 | Glance Widgets | SDK for generating Glance Widgets API responses |
| 2026-11-07 14:57:51 | [Lengko.Datatables.Winform](https://www.nuget.org/packages/Lengko.Datatables.Winform) | 1.0.0 | LengkoDev, Cas | Interactive, modern tabular data grid component for Windows Forms inspired by D… |
| 2026-11-07 15:13:01 | [CarchaLabs.Seal.Runtime](https://www.nuget.org/packages/CarchaLabs.Seal.Runtime) | 0.1.0 | Carcha Labs | Carcha Seal for .NET 5+ (and .NET Standard 2.0 hosts other than .NET Framework)… |
| 2026-11-07 15:13:02 | [CarchaLabs.Seal.NetFramework](https://www.nuget.org/packages/CarchaLabs.Seal.NetFramework) | 0.1.0 | Carcha Labs | Carcha Seal for .NET Framework 4.6.2+ apps (AnyCPU, x86, x64, ARM64; PackageRef… |
| 2026-11-07 15:13:03 | [CarchaLabs.Seal](https://www.nuget.org/packages/CarchaLabs.Seal) | 0.1.0 | Carcha Labs | Carcha Seal for .NET: licensing for desktop apps that keeps working offline. Ac… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
