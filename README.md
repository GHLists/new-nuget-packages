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

## Latest list — 2026-11-02 08:20 UTC

New packages created between 2026-11-02 07:20 UTC and 2026-11-02 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T08-20-58-683649Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 07:23:47 | [Egami.Video.Hevc](https://www.nuget.org/packages/Egami.Video.Hevc) | 1.2.0 | Lars Dytterud | HEVC (H.265) decoding for Egami.Video, in managed code: Main, Main 10, Main 12… |
| 2026-11-02 07:26:42 | [ConventionAssertions.AspNetCore](https://www.nuget.org/packages/ConventionAssertions.AspNetCore) | 0.18.0 | Niklas Wendel | Package Description |
| 2026-11-02 07:41:17 | [XyloCode.EFCore.Extensions](https://www.nuget.org/packages/XyloCode.EFCore.Extensions) | 1.0.0 | xylocode | An EF Core extension library for high-performance bulk data synchronization usi… |
| 2026-11-02 07:55:46 | [RT.MesWeb.DataProviders](https://www.nuget.org/packages/RT.MesWeb.DataProviders) | 1.2.0 | JacoryWang | Database providers and sequence abstraction for mes system |
| 2026-11-02 08:01:39 | [GroveGames.Scheduling](https://www.nuget.org/packages/GroveGames.Scheduling) | 0.1.1 | Grove Games | Zero-allocation delayed callbacks with scaled, unscaled and realtime clocks for… |
| 2026-11-02 08:08:05 | [apcsm](https://www.nuget.org/packages/apcsm) | 3.0.0 | higashitaniyume, ClassicByte | CesiumLoader CLI tool (apcsm) for Astral Party mod development and packaging. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
