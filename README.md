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

## Latest list — 2026-10-14 03:19 UTC

New packages created between 2026-10-14 02:20 UTC and 2026-10-14 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T03-19-36-092091Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 02:48:32 | [PrintLog.SlicerSettings](https://www.nuget.org/packages/PrintLog.SlicerSettings) | 0.1.0 | Christopher Hoffman | Parses the settings OrcaSlicer, PrusaSlicer, Bambu Studio, FLSun Slicer and Any… |
| 2026-10-14 02:50:19 | [LlamaLogic.TuningDescriptions](https://www.nuget.org/packages/LlamaLogic.TuningDescriptions) | 1.0.0 | LlamaLogic | Read the tuning descriptions (TDESCs) Maxis publishes for The Sims 4. |
| 2026-10-14 02:59:12 | [iTool.ObjectStorage](https://www.nuget.org/packages/iTool.ObjectStorage) | 4.0.0 | Jian Zhu | Protocol-neutral object storage with Redis compatibility and an S3 provider. |
| 2026-10-14 03:02:13 | [m2nj.Utilities](https://www.nuget.org/packages/m2nj.Utilities) | 1.0.0 | m2nj | Utility helpers for SMTP email sending in .NET. |
| 2026-10-14 03:04:47 | [iTool.LuceneStore.Storage](https://www.nuget.org/packages/iTool.LuceneStore.Storage) | 4.0.0 | Jian Zhu | Index storage based on Redis and Garnet. |
| 2026-10-14 03:08:38 | [iTool.Framework.Storage](https://www.nuget.org/packages/iTool.Framework.Storage) | 4.0.0 | iTool.Framework.Storage | Protocol-neutral stream storage contracts with an S3-compatible provider. |
| 2026-10-14 03:12:04 | [iTool.DataFabric.Provider](https://www.nuget.org/packages/iTool.DataFabric.Provider) | 4.0.0 | iTool.DataFabric.Provider | Unified State/List/Aggregate/Batch data provider with Orleans hot-state compati… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
