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

## Latest list — 2026-10-06 00:20 UTC

New packages created between 2026-10-05 23:19 UTC and 2026-10-06 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T00-20-05-932728Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 23:41:35 | [JasperFx.Events.InMemory](https://www.nuget.org/packages/JasperFx.Events.InMemory) | 2.81.0 | Jeremy D. Miller,Jaedyn Tonee | An in-memory document and event store for prototyping a Critter Stack applicati… |
| 2026-10-06 00:10:09 | [WASU.Plugin.FormEngine](https://www.nuget.org/packages/WASU.Plugin.FormEngine) | 26.1006.8 | WASU.Plugin.FormEngine | Package Description |
| 2026-10-06 00:13:14 | [WASU.Plugin.DNC](https://www.nuget.org/packages/WASU.Plugin.DNC) | 26.1006.8 | WASU.Plugin.DNC | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
