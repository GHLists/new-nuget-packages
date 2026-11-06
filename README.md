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

## Latest list — 2026-11-06 08:19 UTC

New packages created between 2026-11-06 07:19 UTC and 2026-11-06 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T08-19-48-032713Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 07:25:27 | [RhythmBase.RhythmDoctor.View](https://www.nuget.org/packages/RhythmBase.RhythmDoctor.View) | 1.0.5 | obugs | Draw all Rhythm Doctor event elements in SkiaSharp. |
| 2026-11-06 08:04:09 | [ValIO.Application](https://www.nuget.org/packages/ValIO.Application) | 0.1.0 | ValIO Contributors | ValIO orchestration engine. Use to embed code generation in your host applicati… |
| 2026-11-06 08:12:35 | [HealthCheck.Component](https://www.nuget.org/packages/HealthCheck.Component) | 1.0.3 | HealthCheck.Component | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
