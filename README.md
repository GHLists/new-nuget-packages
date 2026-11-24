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

## Latest list — 2026-11-24 14:20 UTC

New packages created between 2026-11-24 13:20 UTC and 2026-11-24 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T14-20-44-33574Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 13:25:06 | [TheBuilder.CacheTags](https://www.nuget.org/packages/TheBuilder.CacheTags) | 0.1.0 | Daniel Schmidt | Tag Umbraco Delivery API responses with cache keys, and purge exactly the right… |
| 2026-11-24 13:33:51 | [Vespertan.Avalonia.DataGrid](https://www.nuget.org/packages/Vespertan.Avalonia.DataGrid) | 1.1.0 | Vespertan | Vespertan fork of the Avalonia DataGrid control, with Fluent and Simple themes. |
| 2026-11-24 13:35:26 | [Nox.Grid](https://www.nuget.org/packages/Nox.Grid) | 1.0.0 | Nox | NoxGrid: a custom-drawn WinForms grid and spreadsheet component (.NET Framework… |
| 2026-11-24 13:35:28 | [Nox.Grid.Server](https://www.nuget.org/packages/Nox.Grid.Server) | 1.0.0 | Nox | Server package for the NoxGrid web grid (@novnox/grid), .NET Standard 2.0 (.NET… |
| 2026-11-24 13:55:12 | [LogMill](https://www.nuget.org/packages/LogMill) | 2.3.3 | Rare Crew | Library contains object called BaseLogMillHandler (and something more) which re… |
| 2026-11-24 13:55:35 | [LogMill.Web](https://www.nuget.org/packages/LogMill.Web) | 2.3.0 | Rare Crew | Library contains extension methods for BaseLogMillHandler, which allow logging… |
| 2026-11-24 13:55:46 | [LogMill.ApplicationStatus](https://www.nuget.org/packages/LogMill.ApplicationStatus) | 2.3.2 | Rare Crew | Library contains extension methods for BaseLogMillHandler, which allow logging… |
| 2026-11-24 13:55:56 | [LogMill.ApplicationStatus.Web](https://www.nuget.org/packages/LogMill.ApplicationStatus.Web) | 2.3.2 | Rare Crew | Library contains extension methods for BaseLogMillHandler, which implements bas… |
| 2026-11-24 13:57:26 | [Signals.Aspects.Configuration.AzureKeyVault](https://www.nuget.org/packages/Signals.Aspects.Configuration.AzureKeyVault) | 4.0.0 | Signals.Aspects.Configuration… | Package Description |
| 2026-11-24 14:02:26 | [Datatrans.Net](https://www.nuget.org/packages/Datatrans.Net) | 1.0.0 | Clément Favre | Unofficial .NET client for the Datatrans payment API (v1): transactions (init,… |
| 2026-11-24 14:03:43 | [KpsV2.Client](https://www.nuget.org/packages/KpsV2.Client) | 2.0.1 | colakkonur | Sağlık Bakanlığı Kimlik Paylaşım Sistemi (KPS v2) için resmî olmayan .NET istem… |
| 2026-11-24 14:10:27 | [StudioElf.IssueTracker.Sdk](https://www.nuget.org/packages/StudioElf.IssueTracker.Sdk) | 1.0.0 | StudioElf | Standalone .NET client for the StudioElf CRM Issue Tracker error ingestion API.… |
| 2026-11-24 14:10:47 | [StudioElf.IssueTracker.Sdk.Logging](https://www.nuget.org/packages/StudioElf.IssueTracker.Sdk.Logging) | 1.0.0 | StudioElf | Microsoft.Extensions.Logging provider for the StudioElf Issue Tracker SDK. Capt… |
| 2026-11-24 14:11:03 | [StudioElf.IssueTracker.Sdk.Serilog](https://www.nuget.org/packages/StudioElf.IssueTracker.Sdk.Serilog) | 1.0.0 | StudioElf | Optional Serilog sink for the StudioElf Issue Tracker SDK. The core SDK does no… |
| 2026-11-24 14:11:18 | [StudioElf.IssueTracker.Sdk.Oqtane](https://www.nuget.org/packages/StudioElf.IssueTracker.Sdk.Oqtane) | 1.0.0 | StudioElf | Oqtane enrichment for the StudioElf Issue Tracker SDK: platform version, entry-… |
| 2026-11-24 14:14:41 | [RungerHeimdall.Engine](https://www.nuget.org/packages/RungerHeimdall.Engine) | 1.0.0 | RungerHeimdall contributors | Host-independent rule engine shared by RungerHeimdall analyzers and CLI. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
