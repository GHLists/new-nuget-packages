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

## Latest list — 2026-11-26 01:19 UTC

New packages created between 2026-11-26 00:18 UTC and 2026-11-26 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T01-19-38-836965Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 00:41:13 | [DbRelay.Abstractions](https://www.nuget.org/packages/DbRelay.Abstractions) | 0.1.0 | DbRelay contributors | Contracts for DbRelay, a lightweight transactional outbox for .NET: IOutbox, Ou… |
| 2026-11-26 00:41:14 | [DbRelay.PostgreSql](https://www.nuget.org/packages/DbRelay.PostgreSql) | 0.1.0 | DbRelay contributors | PostgreSQL storage provider for DbRelay (Npgsql): transactional outbox inserts… |
| 2026-11-26 00:41:15 | [DbRelay](https://www.nuget.org/packages/DbRelay) | 0.1.0 | DbRelay contributors | DbRelay engine: transactional outbox registration, background dispatcher with l… |
| 2026-11-26 01:13:21 | [WASU.Plugin.Iot.Storage.Timescale](https://www.nuget.org/packages/WASU.Plugin.Iot.Storage.Timescale) | 26.1126.9 | WASU.Plugin.Iot.Storage.Times… | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
