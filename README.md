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

## Latest list — 2026-11-09 06:19 UTC

New packages created between 2026-11-09 05:19 UTC and 2026-11-09 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T06-19-12-690833Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 05:31:15 | [SriLankaHolidays](https://www.nuget.org/packages/SriLankaHolidays) | 1.1.2 | Sahan Ranasingha | Official Sri Lanka Public, Bank, and Mercantile holidays (including Full Moon P… |
| 2026-11-09 05:54:56 | [W.EntityFrameworkCore.Dameng.WDriver](https://www.nuget.org/packages/W.EntityFrameworkCore.Dameng.WDriver) | 0.6.0 | W.EntityFrameworkCore.Dameng.… | Runs the W.EntityFrameworkCore.Dameng provider on the W.DamengProvider ADO.NET… |
| 2026-11-09 05:55:23 | [Jaunt](https://www.nuget.org/packages/Jaunt) | 1.0.1 | AIDotNet | Jaunt: a fully managed, NativeAOT-compatible JavaScript engine for .NET. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
