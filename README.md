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

## Latest list — 2026-11-03 22:19 UTC

New packages created between 2026-11-03 21:20 UTC and 2026-11-03 22:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T22-19-50-625947Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 21:25:01 | [DrawnUi.Net.Game](https://www.nuget.org/packages/DrawnUi.Net.Game) | 1.10.8.17 | Nick Kovalsky aka AppoMobi an… | Base class for implementing a game with SkiaSharp on DrawnUI for .NET, for host… |
| 2026-11-03 21:45:17 | [AffirmSDK.DotNet](https://www.nuget.org/packages/AffirmSDK.DotNet) | 1.0.0 | Raghav Santhapur | .NET bindings for Affirm's iOS and Android SDKs, built and maintained by Raghav… |
| 2026-11-03 21:50:06 | [VeloxDev.Cli](https://www.nuget.org/packages/VeloxDev.Cli) | 11.0.0 | Axvser | Headless VeloxDev workflow host and stdio MCP server: load an archive and its c… |
| 2026-11-03 21:52:10 | [ShieldySdk](https://www.nuget.org/packages/ShieldySdk) | 1.0.2 | Shieldy | .NET client for Shieldy's native runtime: licensing, remote variables, files an… |
| 2026-11-03 22:04:53 | [Paging.Common](https://www.nuget.org/packages/Paging.Common) | 1.0.3 | Paging.Common | Provides shared core contracts, models, and abstractions for pagination, dynami… |
| 2026-11-03 22:13:53 | [Mule.DurableActions.Redis](https://www.nuget.org/packages/Mule.DurableActions.Redis) | 2.3.2 | Elysium Coding | Redis-backed authoritative durable storage for Mule actions, retries, cancellat… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
