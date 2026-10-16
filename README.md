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

## Latest list — 2026-10-16 04:20 UTC

New packages created between 2026-10-16 03:21 UTC and 2026-10-16 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T04-20-36-909115Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 03:45:06 | [MPointCloud](https://www.nuget.org/packages/MPointCloud) | 1.0.0 | Mekneo | High-performance point-cloud data I/O for .NET with PCD, XYZ, PLY, and PTS supp… |
| 2026-10-16 03:51:48 | [gigatoken_cs](https://www.nuget.org/packages/gigatoken_cs) | 0.12.0 | Gigatoken contributors | High-throughput BPE / SentencePiece tokenizer (.NET 10 port of gigatoken). |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
