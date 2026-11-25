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

## Latest list — 2026-11-25 13:21 UTC

New packages created between 2026-11-25 12:20 UTC and 2026-11-25 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T13-21-04-978322Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 12:25:10 | [Zvec.Native](https://www.nuget.org/packages/Zvec.Native) | 0.8.1 | TheBitBrine | Native Zvec libraries (win-x64, linux-x64, linux-arm64, osx-arm64) and P/Invoke… |
| 2026-11-25 12:49:10 | [PocketBase.SDK.Abstractions](https://www.nuget.org/packages/PocketBase.SDK.Abstractions) | 1.0.2 | PocketBase.SDK contributors | Abstractions, DTOs and options for PocketBase.SDK. |
| 2026-11-25 12:49:11 | [PocketBase.SDK](https://www.nuget.org/packages/PocketBase.SDK) | 1.0.2 | PocketBase.SDK contributors | .NET client for PocketBase (core client and services). |
| 2026-11-25 12:49:12 | [PocketBase.SDK.DependencyInjection](https://www.nuget.org/packages/PocketBase.SDK.DependencyInjection) | 1.0.2 | PocketBase.SDK contributors | Dependency injection helpers for PocketBase.SDK. |
| 2026-11-25 12:50:17 | [ZeroAlloc.Platform](https://www.nuget.org/packages/ZeroAlloc.Platform) | 0.1.0 | Markism-JA | Zero-allocation OS primitives for .NET 10 and netstandard2.1 (64-bit AnyCPU): P… |
| 2026-11-25 12:51:07 | [NSystem.Data.MoonPdf.WinForm](https://www.nuget.org/packages/NSystem.Data.MoonPdf.WinForm) | 2025.6.6 | ErikZhouXin | PDF操作库,基于MoonPdf |
| 2026-11-25 12:54:36 | [Luxoft.Bss.Platform.RabbitMq.Base](https://www.nuget.org/packages/Luxoft.Bss.Platform.RabbitMq.Base) | 1.6.12-rabbit-schem… | Bss.Platform.RabbitMq.Base | Package Description |
| 2026-11-25 12:54:38 | [Luxoft.Bss.Platform.RabbitMq.Schemas](https://www.nuget.org/packages/Luxoft.Bss.Platform.RabbitMq.Schemas) | 1.6.12-rabbit-schem… | Bss.Platform.RabbitMq.Schemas | Package Description |
| 2026-11-25 12:55:17 | [VecTiles.Common](https://www.nuget.org/packages/VecTiles.Common) | 0.1.0 | Dirk Weltz | Core package of the VecTiles.NET vector tile mapping stack. It bundles the shar… |
| 2026-11-25 12:55:18 | [VecTiles.Mapsforge](https://www.nuget.org/packages/VecTiles.Mapsforge) | 0.1.0 | Dirk Weltz | Mapsforge support for the VecTiles.NET vector tile mapping stack. It bundles Ve… |
| 2026-11-25 12:55:20 | [VecTiles.Mapsui](https://www.nuget.org/packages/VecTiles.Mapsui) | 0.1.0 | Dirk Weltz | Mapsui integration for the VecTiles.NET vector tile mapping stack. Provides Vec… |
| 2026-11-25 12:55:22 | [VecTiles.OpenMapTiles](https://www.nuget.org/packages/VecTiles.OpenMapTiles) | 0.1.0 | Dirk Weltz | OpenMapTiles support for the VecTiles.NET vector tile mapping stack. It bundles… |
| 2026-11-25 12:55:23 | [VecTiles.Skia](https://www.nuget.org/packages/VecTiles.Skia) | 0.1.0 | Dirk Weltz | Skia based renderer for the VecTiles.NET vector tile mapping stack. Provides Ve… |
| 2026-11-25 13:03:19 | [Telerik.Reporting.Schema](https://www.nuget.org/packages/Telerik.Reporting.Schema) | 20.3.26.1125 | Progress Software Corporation | This package generates JSON schemas and validates JSON report-item definitions… |
| 2026-11-25 13:03:47 | [ChartNivra](https://www.nuget.org/packages/ChartNivra) | 1.0.0 | ChartNivra | Cross-platform .NET charting library with Cartesian, financial, statistical, po… |
| 2026-11-25 13:04:38 | [WpfSmoke](https://www.nuget.org/packages/WpfSmoke) | 0.1.0 | signalnotnoise | Build and launch a WPF app and report startup diagnostics as JSON. |
| 2026-11-25 13:04:43 | [Wpflow.Wpf](https://www.nuget.org/packages/Wpflow.Wpf) | 1.0.0 | bizouarn | Contrôles WPF de Wpflow : FlowView, nodes, handles, edges, MiniMap, Controls, N… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
