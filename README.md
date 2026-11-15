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

## Latest list — 2026-11-15 01:19 UTC

New packages created between 2026-11-15 00:19 UTC and 2026-11-15 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T01-19-05-507772Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 00:32:47 | [Dekaf.Streams.Extensions.Hosting](https://www.nuget.org/packages/Dekaf.Streams.Extensions.Hosting) | 1.28.0-beta | Dekaf Contributors | Microsoft.Extensions.Hosting integration for Dekaf.Streams |
| 2026-11-15 00:32:48 | [Dekaf.Streams.Storage.ZoneTree](https://www.nuget.org/packages/Dekaf.Streams.Storage.ZoneTree) | 1.28.0-beta | Dekaf Contributors | Persistent state stores for Dekaf.Streams, backed by the managed ZoneTree LSM e… |
| 2026-11-15 00:32:48 | [Dekaf.Streams.Testing](https://www.nuget.org/packages/Dekaf.Streams.Testing) | 1.28.0-beta | Dekaf Contributors | Deterministic in-memory test driver for Dekaf.Streams topologies |
| 2026-11-15 00:32:49 | [Dekaf.Streams](https://www.nuget.org/packages/Dekaf.Streams) | 1.28.0-beta | Dekaf Contributors | Stream processing for Dekaf: typed topology DSL, processor API, state stores, w… |
| 2026-11-15 00:44:57 | [Pain001.Sdk](https://www.nuget.org/packages/Pain001.Sdk) | 0.0.88 | Sebastien Rousseau | Typed .NET client for the pain001 REST API (pain001 serve): validate, generate… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
