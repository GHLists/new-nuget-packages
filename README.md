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

## Latest list — 2026-11-10 04:20 UTC

New packages created between 2026-11-10 03:20 UTC and 2026-11-10 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T04-20-22-569095Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 03:27:51 | [RocksDb.Managed](https://www.nuget.org/packages/RocksDb.Managed) | 26.11.7901 | Curiosity GmbH | Fully managed, async-first C# port of RocksDB with on-disk binary compatibility. |
| 2026-11-10 03:27:53 | [RocksDb.Managed.Replication](https://www.nuget.org/packages/RocksDb.Managed.Replication) | 26.11.7901 | Curiosity GmbH | Replication (checkpoint + WAL streaming), planned switchover and a Raft cluster… |
| 2026-11-10 03:27:56 | [RocksDb.Managed.Replication.MagicOnion](https://www.nuget.org/packages/RocksDb.Managed.Replication.MagicOnion) | 26.11.7901 | Curiosity GmbH | gRPC (MagicOnion) transport and hosting for RocksDb.Managed.Replication: replic… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
