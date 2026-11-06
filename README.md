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

## Latest list — 2026-11-06 18:20 UTC

New packages created between 2026-11-06 17:20 UTC and 2026-11-06 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T18-20-23-307592Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 17:23:53 | [ScrubTest.Debug.Storage](https://www.nuget.org/packages/ScrubTest.Debug.Storage) | 1.1.0 | Orthosilicate | Read/Write managment for data |
| 2026-11-06 17:25:41 | [Ternary.Data.Query](https://www.nuget.org/packages/Ternary.Data.Query) | 10.0.3 | Jacob Dahlke | A provider-neutral query model (filters in nested and/or groups, sorting, pagin… |
| 2026-11-06 17:46:24 | [pgembed](https://www.nuget.org/packages/pgembed) | 0.1.0 | Babu Annamalai | Run PostgreSQL locally without installing it: named instances of any version in… |
| 2026-11-06 17:55:30 | [ScrubTest.Debug.Settings](https://www.nuget.org/packages/ScrubTest.Debug.Settings) | 1.1.0 | Orthosilicate | Settings Managment Framework |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
