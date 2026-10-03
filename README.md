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

## Latest list — 2026-10-03 03:20 UTC

New packages created between 2026-10-03 02:20 UTC and 2026-10-03 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T03-20-19-430473Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 02:43:42 | [BYO.Integrations](https://www.nuget.org/packages/BYO.Integrations) | 0.38.0-g44c8ceaa36 | BYO.Integrations | Package Description |
| 2026-10-03 02:45:40 | [GamePassStorage](https://www.nuget.org/packages/GamePassStorage) | 0.1.1 | Christopher van Rooyen | A game-agnostic reader/writer for Xbox Connected Storage (wgs) save folders use… |
| 2026-10-03 02:45:40 | [GamePassStorage.Tool](https://www.nuget.org/packages/GamePassStorage.Tool) | 0.1.1 | Christopher van Rooyen | Command-line tool for Game Pass (Xbox Connected Storage, "wgs") save folders: l… |
| 2026-10-03 02:45:41 | [GamePassStorage.Adapters.AbioticFactor](https://www.nuget.org/packages/GamePassStorage.Adapters.AbioticFactor) | 0.1.1 | Christopher van Rooyen | Game adapter for Abiotic Factor's Game Pass saves: classifies containers, reads… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
