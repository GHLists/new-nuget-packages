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

## Latest list — 2026-10-26 22:20 UTC

New packages created between 2026-10-26 21:19 UTC and 2026-10-26 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T22-20-29-968529Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 21:25:16 | [ArcKids.AlibabaCloud.OSS.V2](https://www.nuget.org/packages/ArcKids.AlibabaCloud.OSS.V2) | 0.3.0 | ArcKids | Alibaba Cloud OSS SDK for .NET V2 |
| 2026-10-26 21:32:21 | [Wayfinder.Umbraco.Starter](https://www.nuget.org/packages/Wayfinder.Umbraco.Starter) | 6.1.0 | Jonny Muir | Try Wayfinder on a fresh Umbraco site with no code: a home page, a sample servi… |
| 2026-10-26 21:42:12 | [Patterns.DDD.MassTransit](https://www.nuget.org/packages/Patterns.DDD.MassTransit) | 1.0.0 | Nugi Gigauri | Publishes Patterns.DDD aggregates' domain events as integration events through… |
| 2026-10-26 21:42:12 | [Patterns.DDD](https://www.nuget.org/packages/Patterns.DDD) | 1.0.0 | Nugi Gigauri | Small, dependency-free DDD building blocks for .NET: Entity, AggregateRoot, dom… |
| 2026-10-26 21:42:13 | [Patterns.DDD.Application](https://www.nuget.org/packages/Patterns.DDD.Application) | 1.0.0 | Nugi Gigauri | Application-layer contracts for Patterns.DDD: unit of work, integration events… |
| 2026-10-26 21:43:48 | [EntMap](https://www.nuget.org/packages/EntMap) | 0.0.1 | WssIDs | Source generator and runtime infrastructure for high-performance mapping |
| 2026-10-26 21:58:23 | [RuleLoom.AspNetCore](https://www.nuget.org/packages/RuleLoom.AspNetCore) | 0.7.0 | Stefan Totev | ASP.NET Core endpoints for RuleLoom: app.MapRuleLoom("/rules") serves the catal… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
