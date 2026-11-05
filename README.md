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

## Latest list — 2026-11-05 12:19 UTC

New packages created between 2026-11-05 11:20 UTC and 2026-11-05 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T12-19-40-019011Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 11:21:02 | [DepartmentDepartmentPackage](https://www.nuget.org/packages/DepartmentDepartmentPackage) | 1.0.0 | Satyasri | My resusable Department code |
| 2026-11-05 11:58:06 | [NCache.Caching.Hybrid](https://www.nuget.org/packages/NCache.Caching.Hybrid) | 5.3.800 | Alachisoft | NCache implementation for ASP.NET Core HybridCache providing Local L1 and distr… |
| 2026-11-05 12:01:58 | [Shravya.CustomNugetPackage](https://www.nuget.org/packages/Shravya.CustomNugetPackage) | 1.0.0 | Shravya | My first custom NuGet package |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
