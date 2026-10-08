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

## Latest list — 2026-10-08 02:20 UTC

New packages created between 2026-10-08 01:21 UTC and 2026-10-08 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T02-20-56-617326Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 01:23:45 | [ZXUI.Controls](https://www.nuget.org/packages/ZXUI.Controls) | 0.2.21-alpha | ZXUI Authors | Logic-only control library for Avalonia. Pair with a ZXUI.Themes.* package for… |
| 2026-10-08 01:24:40 | [ZXUI.Themes.Sample](https://www.nuget.org/packages/ZXUI.Themes.Sample) | 0.2.21-alpha | ZXUI Authors | Simple minimal line-style theme for ZXUI.Controls, built on Avalonia FluentThem… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
