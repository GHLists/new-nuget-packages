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

## Latest list — 2026-10-01 15:21 UTC

New packages created between 2026-10-01 14:20 UTC and 2026-10-01 15:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T15-21-17-307095Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 14:34:51 | [Eternet.AspNetCore.ServiceFabric.Swashbuckle.Legacy](https://www.nuget.org/packages/Eternet.AspNetCore.ServiceFabric.Swashbuckle.Legacy) | 1.0.0 | Eternet.AspNetCore.ServiceFab… | Package Description |
| 2026-10-01 14:54:36 | [ITBees.TicketSupport](https://www.nuget.org/packages/ITBees.TicketSupport) | 8.0.2 | ITBeesPL | Reusable ticketing support desk for ITBees applications: tickets raised from a… |
| 2026-10-01 14:58:46 | [Lebi.Titan.Fang](https://www.nuget.org/packages/Lebi.Titan.Fang) | 1.0.0 | Lebi | Package Description |
| 2026-10-01 15:03:27 | [FnsNet.NpdStatus](https://www.nuget.org/packages/FnsNet.NpdStatus) | 1.0.0 | ai-iskuzhin | A .NET client for the Russian Federal Tax Service public API that reports wheth… |
| 2026-10-01 15:07:19 | [PorticoSoft.Paragon](https://www.nuget.org/packages/PorticoSoft.Paragon) | 1.0.0 | PorticoSoft | Generates PDF, Word, PowerPoint and Excel reports from HTML templates and JSON… |
| 2026-10-01 15:07:25 | [PorticoSoft.Paragon.Designer](https://www.nuget.org/packages/PorticoSoft.Paragon.Designer) | 1.0.0 | PorticoSoft | The Paragon report designer, mounted inside your own application while you buil… |
| 2026-10-01 15:08:39 | [Lebi.Titan.Cheese](https://www.nuget.org/packages/Lebi.Titan.Cheese) | 1.0.0 | Lebi | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
