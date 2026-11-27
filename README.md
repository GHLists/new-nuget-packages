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

## Latest list — 2026-11-27 17:20 UTC

New packages created between 2026-11-27 16:22 UTC and 2026-11-27 17:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T17-20-42-107666Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 16:26:02 | [Prowl.Courier](https://www.nuget.org/packages/Prowl.Courier) | 4.0.0 | Prowl Contributors | Dependency-free game networking transports: a pluggable connection/transport AP… |
| 2026-11-27 16:26:06 | [Prowl.Runtime](https://www.nuget.org/packages/Prowl.Runtime) | 4.0.0 | Prowl Contributors | The runtime of the Prowl game engine: scenes, GameObjects and components, rende… |
| 2026-11-27 16:26:10 | [Prowl.Graphite.Debugger.Viewer](https://www.nuget.org/packages/Prowl.Graphite.Debugger.Viewer) | 4.0.0 | Prowl Contributors | Viewer and render profiler UI for Graphite debugger recordings. |
| 2026-11-27 16:26:12 | [Prowl.Graphite.Rendering.Tools](https://www.nuget.org/packages/Prowl.Graphite.Rendering.Tools) | 4.0.0 | Prowl Contributors | Editor and import time tools for Prowl.Graphite.Rendering: LOD chains and impos… |
| 2026-11-27 16:31:40 | [StonyGrey.McuMgr](https://www.nuget.org/packages/StonyGrey.McuMgr) | 0.1.0 | Stony Grey LLC | An MCUmgr client for .NET: the SMP protocol, the command groups Zephyr serves,… |
| 2026-11-27 16:41:08 | [Great.Parts.Cel.Filtering](https://www.nuget.org/packages/Great.Parts.Cel.Filtering) | 2.0.0 | The Great.Parts Authors | Translates list filters written in the AIP-160 syntax (google.aip.dev/160) into… |
| 2026-11-27 16:41:09 | [Great.Parts.Cel.Policy](https://www.nuget.org/packages/Great.Parts.Cel.Policy) | 2.0.0 | The Great.Parts Authors | CEL Policy for Great.Parts.Cel: read a policy in YAML (rules with variables, co… |
| 2026-11-27 16:41:09 | [Great.Parts.Cel.DependencyInjection](https://www.nuget.org/packages/Great.Parts.Cel.DependencyInjection) | 2.0.0 | The Great.Parts Authors | Dependency injection for Great.Parts.Cel: register CEL environments, a compilat… |
| 2026-11-27 16:41:10 | [Great.Parts.Cel.AspNetCore](https://www.nuget.org/packages/Great.Parts.Cel.AspNetCore) | 2.0.0 | The Great.Parts Authors | ASP.NET Core support for Great.Parts.Cel: CEL expressions in authorization poli… |
| 2026-11-27 16:46:17 | [ReportDesigner](https://www.nuget.org/packages/ReportDesigner) | 0.4.4 | ReportDesigner | Crystal-Reports-class report engine: JSON report definition + data -> HTML/PDF.… |
| 2026-11-27 16:55:44 | [Alkax.Sdk](https://www.nuget.org/packages/Alkax.Sdk) | 0.1.0 | Alkax | Official typed Alkax developer API client for .NET. |
| 2026-11-27 16:59:09 | [Mediana.Codecs.Mpeg2](https://www.nuget.org/packages/Mediana.Codecs.Mpeg2) | 0.1.49 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-27 17:05:32 | [Sponsorkit](https://www.nuget.org/packages/Sponsorkit) | 0.1.0 | Sponsorkit contributors | Build financial contributions (GitHub Sponsors, Open Collective) directly into… |
| 2026-11-27 17:14:00 | [YP.ModbusRestAPI.Core](https://www.nuget.org/packages/YP.ModbusRestAPI.Core) | 1.2.0 | YP | 自研轻量 Modbus TCP 协议栈与点位映射服务，零第三方协议依赖，支持 net8.0 / net10.0。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
