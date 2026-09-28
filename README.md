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

## Latest list — 2026-09-28 23:19 UTC

New packages created between 2026-09-28 22:20 UTC and 2026-09-28 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T23-19-48-090258Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 22:34:03 | [ComparableLinqAnalyzer](https://www.nuget.org/packages/ComparableLinqAnalyzer) | 0.0.2 | ComparableLinqAnalyzer | Roslyn analyzer that reports MinBy, MaxBy, OrderBy, OrderByDescending, Order, O… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
