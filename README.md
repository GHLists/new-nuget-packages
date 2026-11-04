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

## Latest list — 2026-11-04 02:20 UTC

New packages created between 2026-11-04 01:21 UTC and 2026-11-04 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T02-20-47-849837Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 01:26:16 | [Sevencat.ZlmSharp.MediaServer](https://www.nuget.org/packages/Sevencat.ZlmSharp.MediaServer) | 1.0.0 | sevencat | Package Description |
| 2026-11-04 01:28:34 | [cecloud.archive.chromium.headless.shell](https://www.nuget.org/packages/cecloud.archive.chromium.headless.shell) | 1248.0.0 | zsc | Microsoft.Playwright 浏览器运行环境，无头浏览器模式 |
| 2026-11-04 01:31:31 | [cecloud.archive.chromium](https://www.nuget.org/packages/cecloud.archive.chromium) | 1248.0.0 | zsc | Microsoft.Playwright 浏览器运行环境 |
| 2026-11-04 01:41:00 | [cecloud.archive.microsoft.playwright](https://www.nuget.org/packages/cecloud.archive.microsoft.playwright) | 1.64.1 | zsc | microsoft.playwright win32_x64 |
| 2026-11-04 01:45:31 | [Embedix.Core](https://www.nuget.org/packages/Embedix.Core) | 1.0.0 | Soheil Jashnsaz | A library for embedding .NET assembly dependencies. |
| 2026-11-04 01:58:10 | [FaultlineDispatcher.SqlServer](https://www.nuget.org/packages/FaultlineDispatcher.SqlServer) | 0.1.0 | Troy Crowe | SQL Server exception mapper for FaultlineDispatcher. Maps SqlException error nu… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
