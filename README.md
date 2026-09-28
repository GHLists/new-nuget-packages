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

## Latest list — 2026-09-28 01:20 UTC

New packages created between 2026-09-28 00:20 UTC and 2026-09-28 01:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T01-20-36-346891Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 00:32:00 | [SemiWare](https://www.nuget.org/packages/SemiWare) | 1.0.0 | blubeatbee | My first attempt publishing a NuGet package. |
| 2026-09-28 01:12:53 | [ZeroAsset](https://www.nuget.org/packages/ZeroAsset) | 1.0.0 | Phong Võ | High-Performance Digital Asset Management, Zero-Byte Variant Branching, and Hie… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
