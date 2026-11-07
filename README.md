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

## Latest list — 2026-11-07 17:19 UTC

New packages created between 2026-11-07 16:18 UTC and 2026-11-07 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T17-19-44-611039Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 16:21:30 | [DbTest.Core](https://www.nuget.org/packages/DbTest.Core) | 0.1.0 | dbaitest | Engine-agnostic core for database integration test harnesses: container lifecyc… |
| 2026-11-07 16:21:31 | [DbTest.PostgreSql](https://www.nuget.org/packages/DbTest.PostgreSql) | 0.1.0 | dbaitest | PostgreSQL engine for DbTest: container lifecycle, dollar-quote-safe schema app… |
| 2026-11-07 16:21:32 | [DbTest.Cli](https://www.nuget.org/packages/DbTest.Cli) | 0.1.0 | dbaitest | Command line front end for DbTest: start a container, apply a schema, report on… |
| 2026-11-07 16:21:33 | [DbTest.MsSql](https://www.nuget.org/packages/DbTest.MsSql) | 0.1.0 | dbaitest | SQL Server engine for DbTest: container lifecycle, GO-batch schema application… |
| 2026-11-07 16:21:33 | [DbTest.MySql](https://www.nuget.org/packages/DbTest.MySql) | 0.1.0 | dbaitest | MySQL engine for DbTest: container lifecycle, DELIMITER-aware schema applicatio… |
| 2026-11-07 16:45:35 | [QRCoder-Png](https://www.nuget.org/packages/QRCoder-Png) | 0.11.0 | Raffael Herrmann, Joerg Plene… | QRCoder is a simple library, written in C#.NET, which enables you to create QR… |
| 2026-11-07 16:51:56 | [vimdrill.any](https://www.nuget.org/packages/vimdrill.any) | 0.4.0 | Michał Szopa | Daily Vim drills checked by diff, in any editor: Rider, VS Code, Zed or termina… |
| 2026-11-07 16:51:58 | [vimdrill.linux-musl-x64](https://www.nuget.org/packages/vimdrill.linux-musl-x64) | 0.4.0 | Michał Szopa | Daily Vim drills checked by diff, in any editor: Rider, VS Code, Zed or termina… |
| 2026-11-07 16:51:59 | [vimdrill.linux-x64](https://www.nuget.org/packages/vimdrill.linux-x64) | 0.4.0 | Michał Szopa | Daily Vim drills checked by diff, in any editor: Rider, VS Code, Zed or termina… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
