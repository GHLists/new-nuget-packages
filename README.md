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

## Latest list — 2026-10-22 03:22 UTC

New packages created between 2026-10-22 02:21 UTC and 2026-10-22 03:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T03-22-21-869179Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 02:24:45 | [Bitbound.GitNotesMcp](https://www.nuget.org/packages/Bitbound.GitNotesMcp) | 0.1.7 | Jared Goodwin | A Model Context Protocol (MCP) server for creating, reading, editing, and searc… |
| 2026-10-22 02:28:05 | [ConvexDecomposition.NET](https://www.nuget.org/packages/ConvexDecomposition.NET) | 1.0.0 | David Katz | Core of the .NET convex decomposition packages (CuACD.NET, CoACD.NET, VHACD.NET… |
| 2026-10-22 02:28:06 | [VHACD.NET](https://www.nuget.org/packages/VHACD.NET) | 4.1.0 | David Katz | .NET bindings for V-HACD 4 (Voxelized Hierarchical Approximate Convex Decomposi… |
| 2026-10-22 02:28:06 | [CoACD.NET](https://www.nuget.org/packages/CoACD.NET) | 1.0.14 | David Katz | .NET bindings for CoACD (Approximate Convex Decomposition for 3D Meshes with Co… |
| 2026-10-22 02:28:09 | [CuACD.NET](https://www.nuget.org/packages/CuACD.NET) | 0.1.0 | David Katz | .NET bindings for CuACD, a fully GPU-resident approximate convex decomposition… |
| 2026-10-22 02:38:36 | [OpenXmlForge](https://www.nuget.org/packages/OpenXmlForge) | 1.0.0 | Matheus Medeiros | Modern, high-performance .NET 10+ Word (DOCX) template engine built on OpenXML… |
| 2026-10-22 02:41:23 | [DuckByte.Titanium.ModAPI](https://www.nuget.org/packages/DuckByte.Titanium.ModAPI) | 0.1.0 | Dan | Modding API for Titanium. |
| 2026-10-22 02:51:18 | [Bitzsoft.Integrations.SyntheticData](https://www.nuget.org/packages/Bitzsoft.Integrations.SyntheticData) | 1.0.4 | Bitzsoft | Bitzsoft 智能合成数据与 Mock 引擎核心 — 支持无锁单调雪花 ID、DDD 实体穿透绑定、防碰撞唯一性保障与级联不变量 |
| 2026-10-22 03:00:18 | [ZeroMapper.Abstractions](https://www.nuget.org/packages/ZeroMapper.Abstractions) | 1.0.0 | ZeroMapper contributors | A strict, source-generated object mapper for .NET with protected members and ex… |
| 2026-10-22 03:00:58 | [ZeroMapper.Generator](https://www.nuget.org/packages/ZeroMapper.Generator) | 1.0.0 | ZeroMapper contributors | A strict, source-generated object mapper for .NET with protected members and ex… |
| 2026-10-22 03:01:33 | [ZeroMapper](https://www.nuget.org/packages/ZeroMapper) | 1.0.0 | ZeroMapper contributors | A strict, source-generated object mapper for .NET with protected members and ex… |
| 2026-10-22 03:12:16 | [Chime](https://www.nuget.org/packages/Chime) | 0.0.1 | v.la@live.cn | Chime |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
