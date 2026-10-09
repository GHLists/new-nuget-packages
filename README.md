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

## Latest list — 2026-10-09 07:20 UTC

New packages created between 2026-10-09 06:20 UTC and 2026-10-09 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T07-20-19-708341Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 06:22:39 | [LogicLooper.Diagnostics](https://www.nuget.org/packages/LogicLooper.Diagnostics) | 1.7.0 | Cysharp | Provides diagnostic and monitoring support for LogicLooper. |
| 2026-10-09 06:36:18 | [HoneyPlayBox.OpenSDK](https://www.nuget.org/packages/HoneyPlayBox.OpenSDK) | 1.0.1-beta | HoneyPlayBox | HoneyPlayBox BLE toy SDK for .NET |
| 2026-10-09 06:50:00 | [GroveGames.Database](https://www.nuget.org/packages/GroveGames.Database) | 0.1.0 | Grove Games | Fast, crash-safe local document database for games on .NET, Unity and Godot |
| 2026-10-09 07:05:10 | [Packata.ResourceReaders.Database](https://www.nuget.org/packages/Packata.ResourceReaders.Database) | 0.44.0 | Cédric L. Charlier | Database resource reader provider for Packata. |
| 2026-10-09 07:05:12 | [Packata.ResourceReaders.Excel](https://www.nuget.org/packages/Packata.ResourceReaders.Excel) | 0.44.0 | Cédric L. Charlier | Excel resource reader provider for Packata. |
| 2026-10-09 07:05:13 | [Packata.ResourceReaders.FixedWidth](https://www.nuget.org/packages/Packata.ResourceReaders.FixedWidth) | 0.44.0 | Cédric L. Charlier | Fixed-width resource reader provider for Packata. |
| 2026-10-09 07:05:15 | [Packata.ResourceReaders.KeyValue](https://www.nuget.org/packages/Packata.ResourceReaders.KeyValue) | 0.44.0 | Cédric L. Charlier | LTSV and logfmt resource reader providers for Packata. |
| 2026-10-09 07:05:16 | [Packata.ResourceReaders.Ndjson](https://www.nuget.org/packages/Packata.ResourceReaders.Ndjson) | 0.44.0 | Cédric L. Charlier | NDJSON resource reader provider for Packata. |
| 2026-10-09 07:05:18 | [Packata.ResourceReaders.Parquet](https://www.nuget.org/packages/Packata.ResourceReaders.Parquet) | 0.44.0 | Cédric L. Charlier | Parquet resource reader provider for Packata. |
| 2026-10-09 07:05:19 | [Packata.ResourceReaders.WebLogs](https://www.nuget.org/packages/Packata.ResourceReaders.WebLogs) | 0.44.0 | Cédric L. Charlier | Common and W3C web-log resource reader providers for Packata. |
| 2026-10-09 07:10:46 | [Blazor.Untranslated](https://www.nuget.org/packages/Blazor.Untranslated) | 0.1.0 | Vlad Mihalachi | Fails the build when a Blazor component (.razor) renders literal text instead o… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
