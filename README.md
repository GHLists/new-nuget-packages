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

## Latest list — 2026-11-01 11:19 UTC

New packages created between 2026-11-01 10:18 UTC and 2026-11-01 11:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T11-19-54-590155Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 10:40:57 | [RePAKLib](https://www.nuget.org/packages/RePAKLib) | 1.0.0 | RePAKLib | RePak is a simple packaging system made for games, and designed for out of orde… |
| 2026-11-01 10:54:38 | [AnyMediator](https://www.nuget.org/packages/AnyMediator) | 2.0.0 | Andrea Ficarra | AnyMediator (formerly OpenMediatR) is a free, open-source (Apache-2.0) in-proce… |
| 2026-11-01 10:54:38 | [AnyMediator.Abstractions](https://www.nuget.org/packages/AnyMediator.Abstractions) | 2.0.0 | Andrea Ficarra | AnyMediator (formerly OpenMediatR) is a free, open-source (Apache-2.0) in-proce… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
