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

## Latest list — 2026-10-17 03:18 UTC

New packages created between 2026-10-17 02:18 UTC and 2026-10-17 03:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T03-18-52-133775Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 02:19:20 | [PiSharp.Durable](https://www.nuget.org/packages/PiSharp.Durable) | 1.2.0.1 | PiSharp contributors | EXPERIMENTAL. Durable agent harness for PiSharp, a port of Pi's pi-durable: ses… |
| 2026-10-17 02:19:22 | [PiSharp.Durable.Tools](https://www.nuget.org/packages/PiSharp.Durable.Tools) | 1.2.0.1 | PiSharp contributors | EXPERIMENTAL. Execution environment, coding tools, tool_search and code mode fo… |
| 2026-10-17 02:19:22 | [PiSharp.Durable.Sqlite](https://www.nuget.org/packages/PiSharp.Durable.Sqlite) | 1.2.0.1 | PiSharp contributors | EXPERIMENTAL. SQLite storage for PiSharp.Durable on Microsoft.Data.Sqlite with… |
| 2026-10-17 02:29:06 | [EasyCore.Agent.GraphRAG](https://www.nuget.org/packages/EasyCore.Agent.GraphRAG) | 8.3.4 | WZHY | Configurable model-assisted entity and relationship extraction for graph retrie… |
| 2026-10-17 02:30:46 | [EasyCore.Graph.Abstractions](https://www.nuget.org/packages/EasyCore.Graph.Abstractions) | 8.3.4 | WZHY | Provider-neutral property graph contracts, typed metadata, and configurable tra… |
| 2026-10-17 02:32:00 | [EasyCore.Graph.ArangoDB](https://www.nuget.org/packages/EasyCore.Graph.ArangoDB) | 8.3.4 | WZHY | ArangoDB property graph persistence with injectable HTTP transport, JSON metada… |
| 2026-10-17 02:32:22 | [EasyCore.Graph.FalkorDB](https://www.nuget.org/packages/EasyCore.Graph.FalkorDB) | 8.3.4 | WZHY | FalkorDB graph storage and parameterized Cypher queries with caller-owned Redis… |
| 2026-10-17 02:32:41 | [EasyCore.Graph.Gremlin](https://www.nuget.org/packages/EasyCore.Graph.Gremlin) | 8.3.4 | WZHY | Configurable Apache TinkerPop Gremlin graph persistence with injected clients,… |
| 2026-10-17 02:33:05 | [EasyCore.Graph.Neo4j](https://www.nuget.org/packages/EasyCore.Graph.Neo4j) | 8.3.4 | WZHY | Neo4j graph persistence, typed entities and relationships, configurable travers… |
| 2026-10-17 02:35:52 | [EasyCore.Workflow](https://www.nuget.org/packages/EasyCore.Workflow) | 8.3.4 | WZHY | Typed state graphs with conditional routing, fan-out, reducers, durable checkpo… |
| 2026-10-17 03:06:13 | [Meziantou.Framework.QRCode.Imaging](https://www.nuget.org/packages/Meziantou.Framework.QRCode.Imaging) | 1.0.0 | meziantou | Renders QR codes and barcodes of Meziantou.Framework.QRCode as Meziantou.Framew… |
| 2026-10-17 03:06:38 | [WindowStateManager](https://www.nuget.org/packages/WindowStateManager) | 1.0.0 | WindowStateManager | WindowStateManager is a lightweight WinUI 3 utility that automatically saves, r… |
| 2026-10-17 03:07:00 | [ELF.Modules.Http.ResumableDownload](https://www.nuget.org/packages/ELF.Modules.Http.ResumableDownload) | 0.9.0 | ELF INTERNATIONAL EXPRESS CO.… | 續傳大檔下載器：多來源備援、HTTP Range 續傳、sha256 驗證、跨行程鎖檔與進度回報。 |
| 2026-10-17 03:12:27 | [Zpdf](https://www.nuget.org/packages/Zpdf) | 0.1.0 | Zpdf | A PDF writer and text reader (zpdf, in Zig) for .NET. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
