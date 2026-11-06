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

## Latest list — 2026-11-06 05:20 UTC

New packages created between 2026-11-06 04:19 UTC and 2026-11-06 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T05-20-25-473133Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 04:57:07 | [SqlLinq.Units](https://www.nuget.org/packages/SqlLinq.Units) | 2.0.0 | lennykean | Unit conversion in SqlLinq queries, using UnitsNet.Metadata. |
| 2026-11-06 04:57:08 | [SqlLinq.TimeSeries](https://www.nuget.org/packages/SqlLinq.TimeSeries) | 2.0.0 | lennykean | Time series queries for SqlLinq. |
| 2026-11-06 04:57:50 | [Mekhane](https://www.nuget.org/packages/Mekhane) | 1.0.0 | itzmerobby | A simple library for creating modular applications in C#. The future of softwar… |
| 2026-11-06 04:57:55 | [Mekhane.AspNet](https://www.nuget.org/packages/Mekhane.AspNet) | 1.0.0 | itzmerobby | ASP.NET Core integration for building modular applications with Mekhane. |
| 2026-11-06 04:57:59 | [Mekhane.DependencyInjection](https://www.nuget.org/packages/Mekhane.DependencyInjection) | 1.0.0 | itzmerobby | Dependency injection and Generic Host integration for Mekhane. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
