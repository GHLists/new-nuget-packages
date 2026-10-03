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

## Latest list — 2026-10-03 09:20 UTC

New packages created between 2026-10-03 08:22 UTC and 2026-10-03 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T09-20-53-886902Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 08:49:27 | [M6d.Cortex](https://www.nuget.org/packages/M6d.Cortex) | 0.1.0 | M6d.Cortex | Turns an ASP.NET Core application into a Cortex dataset host: a manifest derive… |
| 2026-10-03 08:53:11 | [EvaluatedApplications.HoloGenome](https://www.nuget.org/packages/EvaluatedApplications.HoloGenome) | 0.1.0 | Evaluated Applications | Encode DNA as phasor holograms whose geometry comes from measured DNA physics.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
