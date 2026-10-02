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

## Latest list — 2026-10-02 06:20 UTC

New packages created between 2026-10-02 05:21 UTC and 2026-10-02 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T06-20-54-248974Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 05:34:36 | [Gil.Sqlite](https://www.nuget.org/packages/Gil.Sqlite) | 0.10.0 | iyulab | Gil's telemetry, habit statistics, promotion and review logs in a single SQLite… |
| 2026-10-02 06:12:40 | [Cratis.Arc.Screenplay.Embedded.Generation](https://www.nuget.org/packages/Cratis.Arc.Screenplay.Embedded.Generation) | 22.48.0 | all contributors | Generates the Screenplay documents a Cratis Arc application embeds - the same d… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
