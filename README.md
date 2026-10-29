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

## Latest list — 2026-10-29 03:19 UTC

New packages created between 2026-10-29 02:19 UTC and 2026-10-29 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T03-19-37-249563Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 02:34:51 | [Hi.Ltd.Communication](https://www.nuget.org/packages/Hi.Ltd.Communication) | 2026.10.29.1032 | chustange | 此基础库主要包含三菱MC，Modbus Tcp等通讯方法集成 |
| 2026-10-29 02:54:48 | [CamusDB.WebConsole](https://www.nuget.org/packages/CamusDB.WebConsole) | 0.16.2 | CamusDB | CamusDB.WebConsole allows database management from a Web UI. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
