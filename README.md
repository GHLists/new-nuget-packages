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

## Latest list — 2026-11-05 06:42 UTC

New packages created between 2026-11-05 06:18 UTC and 2026-11-05 06:42 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T06-42-07-858639Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 06:23:41 | [Cratis.Showrunner.BoxOffice.Product](https://www.nuget.org/packages/Cratis.Showrunner.BoxOffice.Product) | 1.15.0 | Cratis | Box Office Product — everything a managed product does for its operator, such a… |
| 2026-11-05 06:31:30 | [DynaSharp.Coordination](https://www.nuget.org/packages/DynaSharp.Coordination) | 0.2.0 | DynaSharp.Coordination | Distributed coordination on DynamoDB for DynaSharp: a lease on a named lock wit… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
