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

## Latest list — 2026-11-03 04:20 UTC

New packages created between 2026-11-03 03:19 UTC and 2026-11-03 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T04-20-50-839315Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 03:42:16 | [Ptht365.Microservice.DevKit](https://www.nuget.org/packages/Ptht365.Microservice.DevKit) | 1.0.0 | Nguyen Viet Dung | Dev kit client for Ptht365 mini apps: sign in with personas served by the shell… |
| 2026-11-03 03:42:17 | [SunDoge.ShardPack](https://www.nuget.org/packages/SunDoge.ShardPack) | 0.1.1 | SunDoge | Linux x64 (.NET 8+) ShardPack streams backed by Rust, with Zstd and AES-256-GCM. |
| 2026-11-03 04:01:19 | [Soenneker.TypesafeAi.OpenApiClientUtil](https://www.nuget.org/packages/Soenneker.TypesafeAi.OpenApiClientUtil) | 11.0.4 | Jake Soenneker | A thread-safe utility for obtaining TypesafeAi's OpenApiClient singleton. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
