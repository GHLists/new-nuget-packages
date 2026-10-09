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

## Latest list — 2026-10-09 11:19 UTC

New packages created between 2026-10-09 10:19 UTC and 2026-10-09 11:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T11-19-28-191619Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 10:38:48 | [MonixOne.Inbox](https://www.nuget.org/packages/MonixOne.Inbox) | 1.1.1 | Shulyakovsky.E | Ordered inbox for .NET 10, EF Core, PostgreSQL and NATS JetStream with transact… |
| 2026-10-09 10:58:44 | [SimplyWorks.Bitween.Adapters](https://www.nuget.org/packages/SimplyWorks.Bitween.Adapters) | 10.0.59 | Simplify9 | The Bitween adapter contract: the kinds of adapter Bitween runs (handler, mappe… |
| 2026-10-09 11:03:24 | [DijkstraFast](https://www.nuget.org/packages/DijkstraFast) | 1.0.0 | Oleksandr Semeniuk | Fast Dijkstra and A* shortest-path search for graphs with integer node indices.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
