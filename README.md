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

## Latest list — 2026-10-09 14:20 UTC

New packages created between 2026-10-09 13:20 UTC and 2026-10-09 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T14-20-22-28661Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 13:26:27 | [JRK.JevRunner](https://www.nuget.org/packages/JRK.JevRunner) | 0.0.2 | Jeppe Roi Kristensen | Unofficial .NET client for Jev and the TypeSafe System One API. Submit applicat… |
| 2026-10-09 13:29:45 | [SI.WA.Import](https://www.nuget.org/packages/SI.WA.Import) | 1.0.0 | seriiiastreb@gmail.com | Data import for WA.Core: reads flat files (Excel, CSV, JSON, XML, HTML, Markdow… |
| 2026-10-09 13:33:13 | [RAGToolkit.AI.VectorData.Abstractions](https://www.nuget.org/packages/RAGToolkit.AI.VectorData.Abstractions) | 1.0.1 | gimmick | Experimental sparse vector abstractions for RAG vector providers. |
| 2026-10-09 13:33:17 | [RAGToolkit.AI.VectorData.Tei](https://www.nuget.org/packages/RAGToolkit.AI.VectorData.Tei) | 1.0.1 | gimmick | Text Embeddings Inference provider for sparse embedding generation. |
| 2026-10-09 13:33:19 | [RAGToolkit.AI.VectorData.Qdrant](https://www.nuget.org/packages/RAGToolkit.AI.VectorData.Qdrant) | 1.0.1 | gimmick | Experimental Qdrant vector store provider for RAGToolkit.AI.VectorData, based o… |
| 2026-10-09 13:34:12 | [aliyun-net-sdk-airegistry](https://www.nuget.org/packages/aliyun-net-sdk-airegistry) | 1.0.0 | Alibaba Cloud | Alibaba Cloud SDK for .NET |
| 2026-10-09 13:34:19 | [ExcelRenderer.Mapping](https://www.nuget.org/packages/ExcelRenderer.Mapping) | 1.8.0 | akrym1582 | Map C# objects and JSON into Excel templates with nested row arrays. |
| 2026-10-09 13:41:38 | [fairflip](https://www.nuget.org/packages/fairflip) | 1.0.0 | CarbonNeuron | A command-line coin flipper with cryptographic and comparison strategies. |
| 2026-10-09 13:52:34 | [DanishCvr](https://www.nuget.org/packages/DanishCvr) | 1.0.0 | Michael Vivet | Search and retrieve company, production unit, person and relation information f… |
| 2026-10-09 13:54:26 | [RAGToolkit.AI.DataRetrieval.Abstractions](https://www.nuget.org/packages/RAGToolkit.AI.DataRetrieval.Abstractions) | 1.0.0 | gimmick | Retrieval abstractions for RAG pipelines. |
| 2026-10-09 13:54:29 | [RAGToolkit.AI.DataRetrieval](https://www.nuget.org/packages/RAGToolkit.AI.DataRetrieval) | 1.0.0 | gimmick | Retrieval pipeline utilities for RAG. |
| 2026-10-09 13:54:32 | [RAGToolkit.AI.DataRetrieval.Tei](https://www.nuget.org/packages/RAGToolkit.AI.DataRetrieval.Tei) | 1.0.0 | gimmick | Text Embeddings Inference provider for RAGToolkit.AI.DataRetrieval. |
| 2026-10-09 13:54:35 | [RAGToolkit.AI.DataRetrieval.Cohere](https://www.nuget.org/packages/RAGToolkit.AI.DataRetrieval.Cohere) | 1.0.0 | gimmick | Cohere Rerank API provider for RAGToolkit.AI.DataRetrieval. |
| 2026-10-09 14:02:32 | [Snappiest](https://www.nuget.org/packages/Snappiest) | 0.9.0 | zcsizmadia | High-performance Snappy compression for .NET 8+, using SIMD and hardware intrin… |
| 2026-10-09 14:12:47 | [Meridian.Sluice](https://www.nuget.org/packages/Meridian.Sluice) | 0.2.0 | Max Anstey | Dependency-tracking invalidation for FusionCache. A cached value records what i… |
| 2026-10-09 14:12:48 | [Meridian.Sluice.EntityFrameworkCore](https://www.nuget.org/packages/Meridian.Sluice.EntityFrameworkCore) | 0.2.0 | Max Anstey | EF Core integration for Sluice: read helpers that take their dependencies from… |
| 2026-10-09 14:14:03 | [Backlot.Studio](https://www.nuget.org/packages/Backlot.Studio) | 0.2.0 | Jeroen Wijdeven Holding B.V. | Embeddable admin UI for Backlot. Call AddBacklotStudio() and MapBacklotStudio()… |
| 2026-10-09 14:14:04 | [Backlot.Testing.Defaults](https://www.nuget.org/packages/Backlot.Testing.Defaults) | 0.2.0 | Jeroen Wijdeven Holding B.V. | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
