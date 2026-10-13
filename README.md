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

## Latest list — 2026-10-13 13:18 UTC

New packages created between 2026-10-13 12:21 UTC and 2026-10-13 13:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T13-18-43-943284Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 12:26:34 | [LightUi](https://www.nuget.org/packages/LightUi) | 1.0.2 | vvsnow | 轻量 WPF 控件库：把 WPF 自带控件统一重刷成现代扁平外观，并提供 Flyout / MenuFlyout / DropDownButton / Tog… |
| 2026-10-13 12:28:06 | [Nimblesite.Sync.SqlServer](https://www.nuget.org/packages/Nimblesite.Sync.SqlServer) | 0.11.0-beta | ChristianFindlay | Package Description |
| 2026-10-13 12:32:41 | [Ternary.Data.LiteDb](https://www.nuget.org/packages/Ternary.Data.LiteDb) | 10.0.1 | Jacob Dahlke | A framework to simplify working with data from multiple sources, including file… |
| 2026-10-13 12:40:24 | [MemoryPack.Generator.DateTimeOffsetPatch](https://www.nuget.org/packages/MemoryPack.Generator.DateTimeOffsetPatch) | 1.21.4.1 | aminparsa18,Cysharp | Unofficial patched build of the MemoryPack source generator (based on Cysharp/M… |
| 2026-10-13 13:09:58 | [PowerTraces.Sqlite](https://www.nuget.org/packages/PowerTraces.Sqlite) | 1.4.0 | PowerTraces contributors | SQLite provider for PowerTraces — exports traces/logs to a local SQLite file, n… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
