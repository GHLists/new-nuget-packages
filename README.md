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

## Latest list — 2026-10-13 08:19 UTC

New packages created between 2026-10-13 07:21 UTC and 2026-10-13 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T08-19-32-637067Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 07:28:47 | [Webority.Delivery](https://www.nuget.org/packages/Webority.Delivery) | 0.12.0 | Webority Technologies | Versioned links to a product's authored static assets, the files listed in the… |
| 2026-10-13 07:54:53 | [CSStack.DDD](https://www.nuget.org/packages/CSStack.DDD) | 0.1.1 | Uta Sugane | A lightweight toolkit of building blocks for Domain-Driven Design (DDD) in C#.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
