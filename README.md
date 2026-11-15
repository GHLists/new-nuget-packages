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

## Latest list — 2026-11-15 13:21 UTC

New packages created between 2026-11-15 12:21 UTC and 2026-11-15 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T13-21-47-383964Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 12:38:15 | [Indigauge.Core](https://www.nuget.org/packages/Indigauge.Core) | 0.1.0 | Indigauge.Core | Package Description |
| 2026-11-15 12:39:08 | [Neph.GenericLibs.Net.DatabaseLib](https://www.nuget.org/packages/Neph.GenericLibs.Net.DatabaseLib) | 0.1.0 | Neph | Provider-agnostic database abstractions for EF Core (generic DbContext, trackin… |
| 2026-11-15 12:42:20 | [Infrastructure.MvvmBase](https://www.nuget.org/packages/Infrastructure.MvvmBase) | 1.0.0 | Sukhov A.A. | A NuGet package providing a reusable base class for loading indicators and back… |
| 2026-11-15 12:47:26 | [PclIO](https://www.nuget.org/packages/PclIO) | 0.1.0 | mahach666 | Reads and converts point cloud files in several scanner and project formats (.e… |
| 2026-11-15 12:47:27 | [PclIO.Cli](https://www.nuget.org/packages/PclIO.Cli) | 0.1.0 | mahach666 | Command line tool that inspects point cloud files, lists their scans, prints sa… |
| 2026-11-15 12:48:28 | [Vek](https://www.nuget.org/packages/Vek) | 1.0.0 | Amin Sabaghi | Blazor Component Library based on Material Design principles with an emphasis o… |
| 2026-11-15 12:49:39 | [MarkdownToPdf.Tool](https://www.nuget.org/packages/MarkdownToPdf.Tool) | 0.1.0 | John Scott | Command line tool that converts Markdown files into polished PDF documents. No… |
| 2026-11-15 12:49:39 | [Reetus.MarkdownToPdf](https://www.nuget.org/packages/Reetus.MarkdownToPdf) | 0.1.0 | John Scott | Dependency-free Markdown (CommonMark + GFM) to PDF converter with TrueType font… |
| 2026-11-15 12:54:21 | [Indigauge.Revit](https://www.nuget.org/packages/Indigauge.Revit) | 0.1.0 | Indigauge.Revit | Opt-in, privacy-conscious Indigauge adapter for Revit 2027. |
| 2026-11-15 12:54:45 | [Indigauge.Revit.Wpf](https://www.nuget.org/packages/Indigauge.Revit.Wpf) | 0.1.0 | Indigauge.Revit.Wpf | Optional native WPF feedback UI for the Indigauge Revit adapter. |
| 2026-11-15 13:00:10 | [Neph.GenericLibs.Net.AzureSqlLib](https://www.nuget.org/packages/Neph.GenericLibs.Net.AzureSqlLib) | 0.1.0 | Neph | Azure SQL / SQL Server provider for DatabaseLib: EF Core registration and desig… |
| 2026-11-15 13:01:00 | [IgrisModz.Plugin.ThemeKit](https://www.nuget.org/packages/IgrisModz.Plugin.ThemeKit) | 1.0.0 | IgrisModz | Shared theme and style functionality for Plugin.ThemeKit. |
| 2026-11-15 13:01:01 | [IgrisModz.Plugin.ThemeKit.Maui](https://www.nuget.org/packages/IgrisModz.Plugin.ThemeKit.Maui) | 1.0.0 | IgrisModz | Theme and style helper for .NET MAUI applications |
| 2026-11-15 13:01:03 | [IgrisModz.Plugin.ThemeKit.WinUI](https://www.nuget.org/packages/IgrisModz.Plugin.ThemeKit.WinUI) | 1.0.0 | IgrisModz | Theme and style helper for .NET WinUI applications |
| 2026-11-15 13:04:43 | [Pacem.OpenXml.OfficeExcel](https://www.nuget.org/packages/Pacem.OpenXml.OfficeExcel) | 1.1.1-cauchy | Cristian Merighi | Utilities to read and write .xlsx files. |
| 2026-11-15 13:09:51 | [OmniDev.Cli](https://www.nuget.org/packages/OmniDev.Cli) | 0.1.0 | mequann | Universal Polyglot Dev Orchestrator & Concurrent Runner with Smart Failure Diag… |
| 2026-11-15 13:12:11 | [1llum1n4t1s.NAudio.Nam](https://www.nuget.org/packages/1llum1n4t1s.NAudio.Nam) | 4.0.11 | Mark Heath, Contributors, ゆろち | Native C# inference for Neural Amp Modeler (NAM) guitar amp and pedal captures.… |
| 2026-11-15 13:12:58 | [MusselDiagram.Core](https://www.nuget.org/packages/MusselDiagram.Core) | 1.0.0 | machi_pon | Model, rules, validation, routing, undo and JSON of MusselDiagram, without UI |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
