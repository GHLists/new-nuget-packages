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

## Latest list — 2026-11-07 20:18 UTC

New packages created between 2026-11-07 19:21 UTC and 2026-11-07 20:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T20-18-39-016921Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 19:22:23 | [Nantuc.CLI](https://www.nuget.org/packages/Nantuc.CLI) | 0.9.0 | RomanyPe | Package Description |
| 2026-11-07 19:32:12 | [VolcanoBlue.EventSourcing](https://www.nuget.org/packages/VolcanoBlue.EventSourcing) | 1.0.0 | William Santos | Event sourcing library with Models and EF Core. |
| 2026-11-07 19:34:30 | [FlatKeyValueConfiguration](https://www.nuget.org/packages/FlatKeyValueConfiguration) | 1.0.0 | Bridge Liu | A flat key/value configuration format for .NET. Simpler than INI, and stricter… |
| 2026-11-07 19:36:30 | [Hypha.Tools](https://www.nuget.org/packages/Hypha.Tools) | 1.5.0 | Starion Group S.A. | Fetches the upstream OMG SysML v2 / KerML sources and generates the hypha knowl… |
| 2026-11-07 19:36:33 | [Mediana.Codecs.Mpeg4Visual](https://www.nuget.org/packages/Mediana.Codecs.Mpeg4Visual) | 0.1.25 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 19:36:35 | [Mediana.Containers.Avi](https://www.nuget.org/packages/Mediana.Containers.Avi) | 0.1.25 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 19:36:36 | [Mediana.Codecs.Theora](https://www.nuget.org/packages/Mediana.Codecs.Theora) | 0.1.25 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 19:36:37 | [Mediana.Codecs.Vp9](https://www.nuget.org/packages/Mediana.Codecs.Vp9) | 0.1.25 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 19:36:41 | [Mediana.Codecs.Vp8](https://www.nuget.org/packages/Mediana.Codecs.Vp8) | 0.1.25 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 19:38:11 | [MviCore.Net.R3](https://www.nuget.org/packages/MviCore.Net.R3) | 1.0.0 | MviCore.Net.R3 | A simplified single-threaded MVICore implementation built on R3. |
| 2026-11-07 19:43:32 | [HoneyDrunk.Capabilities](https://www.nuget.org/packages/HoneyDrunk.Capabilities) | 0.1.0 | HoneyDrunk Studios | Runtime for HoneyDrunk Grid capabilities: an in-process registry, a guarded inv… |
| 2026-11-07 19:43:42 | [HoneyDrunk.Memory](https://www.nuget.org/packages/HoneyDrunk.Memory) | 0.1.0 | HoneyDrunk Studios | Runtime composition for HoneyDrunk agent memory: scope resolution gated by Auth… |
| 2026-11-07 19:54:45 | [Glacier.Formats](https://www.nuget.org/packages/Glacier.Formats) | 1.0.0 | Ian Cowley | Pure C# .NET 10 Zero-Allocation Columnar Interchange Formats (Apache Arrow IPC… |
| 2026-11-07 19:54:58 | [Glacier.Quant](https://www.nuget.org/packages/Glacier.Quant) | 1.0.0 | Ian Cowley | High-throughput SIMD and GPU post-training quantization kernels (Q4_K_M, Q8_0,… |
| 2026-11-07 19:55:08 | [Glacier.Media](https://www.nuget.org/packages/Glacier.Media) | 1.0.0 | Ian Cowley | Pure C# .NET 10 Generative Multimodal Media engine featuring FLUX.1 Flow-Matchi… |
| 2026-11-07 19:55:34 | [CoreSystem.OpenApi.Swashbuckle](https://www.nuget.org/packages/CoreSystem.OpenApi.Swashbuckle) | 1.0.0 | Federin Pastor Gutierrez Ortiz | Reusable OpenAPI and Swagger infrastructure for ASP.NET Core APIs. |
| 2026-11-07 20:01:50 | [Delimited](https://www.nuget.org/packages/Delimited) | 0.1.0-alpha1 | Nathan Wilson | F# codecs for reading and writing delimited text (CSV, TSV), built on Sylvan.Da… |
| 2026-11-07 20:03:15 | [z3l.FastHtmlParser](https://www.nuget.org/packages/z3l.FastHtmlParser) | 0.1.0 | z3l | Fast, low-allocation HTML/XML parser for scraping on .NET 9/10. About 10x (up t… |
| 2026-11-07 20:07:25 | [Disposed.Baldr](https://www.nuget.org/packages/Disposed.Baldr) | 2026.11.7.200716 | Thijs Janssen | Baldr is an embeddable broker core for .NET with send/subscribe and request/res… |
| 2026-11-07 20:11:24 | [Glacier.MemEx](https://www.nuget.org/packages/Glacier.MemEx) | 1.0.0 | Ian Cowley | Universal episodic memory engine uniting Chrono, DocTree, Vector, HippoRAG PPR,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
