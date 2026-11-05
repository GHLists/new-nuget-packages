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

## Latest list — 2026-11-05 17:21 UTC

New packages created between 2026-11-05 16:22 UTC and 2026-11-05 17:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T17-21-26-648939Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 16:55:48 | [AspireCommander.Hosting](https://www.nuget.org/packages/AspireCommander.Hosting) | 0.2.1 | AspireCommander contributors | Adds a Midnight Commander-inspired terminal file browser to any resource in a .… |
| 2026-11-05 16:58:13 | [Gurux.DLMS.UI.Components](https://www.nuget.org/packages/Gurux.DLMS.UI.Components) | 1.0.2611.501 | Gurux Ltd | Reusable Gurux DLMS UI components for web, Windows, iOS, and Android applicatio… |
| 2026-11-05 17:02:19 | [IoTSharp.EntityFrameworkCore.LiteDB](https://www.nuget.org/packages/IoTSharp.EntityFrameworkCore.LiteDB) | 1.0.0 | IoTSharp | LiteDB provider for Entity Framework Core 10. |
| 2026-11-05 17:03:32 | [AndanteTribe.EntityAccessAnalyzer](https://www.nuget.org/packages/AndanteTribe.EntityAccessAnalyzer) | 1.0.0 | AndanteTribe | Enforces restricted public access to entities. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
