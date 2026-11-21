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

## Latest list — 2026-11-21 12:20 UTC

New packages created between 2026-11-21 11:20 UTC and 2026-11-21 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T12-20-40-879154Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 11:32:31 | [PenCsharpener.FsrsSharp](https://www.nuget.org/packages/PenCsharpener.FsrsSharp) | 6.0.0 | penCsharpener | C# port of ts-fsrs 6.0.0: the Free Spaced Repetition Scheduler (FSRS-3, 4, 4.5,… |
| 2026-11-21 11:40:58 | [oneAPI.OIDN.NET](https://www.nuget.org/packages/oneAPI.OIDN.NET) | 2.5.1 | Chiretallyn | Idiomatic, zero-overhead .NET bindings for Intel Open Image Denoise 2.5.1 (AI r… |
| 2026-11-21 11:55:12 | [PerataSh.Sdk](https://www.nuget.org/packages/PerataSh.Sdk) | 0.5.9 | Peráta | Peráta's SDK for .NET: products, customers, checkouts, payments, subscriptions… |
| 2026-11-21 12:12:13 | [Vespertan.Toolkit](https://www.nuget.org/packages/Vespertan.Toolkit) | 1.0.0 | siwydym67 | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
