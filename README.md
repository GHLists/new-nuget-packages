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

## Latest list — 2026-11-22 02:19 UTC

New packages created between 2026-11-22 01:21 UTC and 2026-11-22 02:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T02-19-17-003031Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 01:31:13 | [ConsealDev.Conseal](https://www.nuget.org/packages/ConsealDev.Conseal) | 0.7.0 | consealdev | Encrypted sync backend for ASP.NET Core: the sync and circle routes of the Cons… |
| 2026-11-22 01:50:21 | [barvad.RotatingBloomFilter](https://www.nuget.org/packages/barvad.RotatingBloomFilter) | 1.0.0 | barvad | Thread-safe Bloom filters for .NET, including a lock-free rotating Bloom filter… |
| 2026-11-22 01:53:13 | [Capay.Dto](https://www.nuget.org/packages/Capay.Dto) | 1.1.0-beta | dto | Package Description |
| 2026-11-22 02:08:02 | [Chondrite.Core](https://www.nuget.org/packages/Chondrite.Core) | 0.9.0-alpha02 | LEAP 71 | Core immutable object identity and canonical SHA-256 hashing for Chondrite. |
| 2026-11-22 02:08:56 | [VideoShot.CaptionSafeArea](https://www.nuget.org/packages/VideoShot.CaptionSafeArea) | 0.1.0 | js-upup | Compute a caption-safe pixel rectangle from video dimensions and percentage mar… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
