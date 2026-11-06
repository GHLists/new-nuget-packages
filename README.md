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

## Latest list — 2026-11-06 20:18 UTC

New packages created between 2026-11-06 19:21 UTC and 2026-11-06 20:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T20-18-55-09833Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 19:22:47 | [StateAlchemist.Hosting](https://www.nuget.org/packages/StateAlchemist.Hosting) | 1.4.0 | Harry Cordewener | Runs a StateAlchemist machine for the lifetime of a .NET Generic Host: started… |
| 2026-11-06 19:32:33 | [SC.Configuration.Provider.Mongo](https://www.nuget.org/packages/SC.Configuration.Provider.Mongo) | 0.0.1 | Security Research PoC | Benign dependency-confusion proof-of-concept package. It contains no executable… |
| 2026-11-06 19:34:37 | [Glacier.Rag](https://www.nuget.org/packages/Glacier.Rag) | 1.2.0 | Ian Cowley | Pure C# .NET 10 in-process GraphRAG engine. Unifies dense SIMD vector search (G… |
| 2026-11-06 19:35:32 | [Fsdb](https://www.nuget.org/packages/Fsdb) | 0.1.0 | Helge Sverre | An embeddable F# database with a MySQL-compatible SQL engine and wire protocol. |
| 2026-11-06 19:48:31 | [Mietex.CosmosDb](https://www.nuget.org/packages/Mietex.CosmosDb) | 0.1.0 | Pawel Mieten | Opinionated Cosmos DB persistence primitives: partition-scoped contexts, transa… |
| 2026-11-06 20:11:59 | [PepperDash.Essentials.BuildTools.SchemaGen](https://www.nuget.org/packages/PepperDash.Essentials.BuildTools.SchemaGen) | 0.1.1 | PepperDash Technology | Extracts device facts and Portal-ready config schemas from a PepperDash Essenti… |
| 2026-11-06 20:12:03 | [PepperDash.Essentials.BuildTools.Readme](https://www.nuget.org/packages/PepperDash.Essentials.BuildTools.Readme) | 0.1.0 | PepperDash Technology | Keeps a PepperDash Essentials plugin README in sync with its code: .NET and Ess… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
