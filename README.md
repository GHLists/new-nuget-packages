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

## Latest list — 2026-10-23 10:20 UTC

New packages created between 2026-10-23 09:22 UTC and 2026-10-23 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T10-20-21-922553Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 09:22:28 | [Localisation.Core](https://www.nuget.org/packages/Localisation.Core) | 3.0.0 | Chris Pulman | Localisation libraries for WPF and Avalonia |
| 2026-10-23 09:22:29 | [Localisation.Generators](https://www.nuget.org/packages/Localisation.Generators) | 3.0.0 | Chris Pulman | Localisation libraries for WPF and Avalonia |
| 2026-10-23 09:22:40 | [Weard](https://www.nuget.org/packages/Weard) | 0.0.1-placeholder | Weard | AgenticGuard SDK for .NET: tamper-evident records of what AI agents do. Placeho… |
| 2026-10-23 09:23:09 | [Weard.AgenticGuard](https://www.nuget.org/packages/Weard.AgenticGuard) | 0.0.1-placeholder | Weard | AgenticGuard SDK for .NET: tamper-evident records of what AI agents do. Placeho… |
| 2026-10-23 09:36:32 | [LiteSpec.Analyzers](https://www.nuget.org/packages/LiteSpec.Analyzers) | 2.0.0 | Litenova Solutions | Roslyn analyzers that check a .NET application against the LiteSpec standard: l… |
| 2026-10-23 09:36:33 | [LiteSpec.Cli](https://www.nuget.org/packages/LiteSpec.Cli) | 2.0.0 | Litenova Solutions | The LiteSpec command line: authoring checks, the provision index, consumer and… |
| 2026-10-23 09:39:03 | [SystemD.Crystal](https://www.nuget.org/packages/SystemD.Crystal) | 1.0.0 | SystemD.Crystal contributors | An embeddable storage engine for .NET, built on a write-ahead log over RocksDB:… |
| 2026-10-23 09:52:43 | [Beresta.Markdown.Wpf.Editor](https://www.nuget.org/packages/Beresta.Markdown.Wpf.Editor) | 0.9.0 | Porohkun | Markdown editor for WPF on Beresta.Markdown.Wpf: edits the source right inside… |
| 2026-10-23 10:03:53 | [Licentivo.Launch](https://www.nuget.org/packages/Licentivo.Launch) | 0.1.1 | Licentivo Launch | Launch merchant accounts with official Licentivo runtime authorization. |
| 2026-10-23 10:05:38 | [NextLevel.DWH](https://www.nuget.org/packages/NextLevel.DWH) | 1.1.0 | NextLevel | The NextLevel data-warehouse channel in one package: a producer side that turns… |
| 2026-10-23 10:06:24 | [PolishOpenData.Rcn](https://www.nuget.org/packages/PolishOpenData.Rcn) | 1.6.0 | JacekSmi | Typed .NET client for RCN (Rejestr Cen Nieruchomości) of GUGiK: real-estate tra… |
| 2026-10-23 10:08:01 | [InternalClock](https://www.nuget.org/packages/InternalClock) | 1.0.0 | YourName | 进程内软件时钟。时间由调用方委托提供，两次校准之间用 Stopwatch 推算，不读本机墙钟。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
