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

## Latest list — 2026-11-20 09:20 UTC

New packages created between 2026-11-20 08:19 UTC and 2026-11-20 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T09-20-56-230889Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 08:31:11 | [NovaWpf.Mcp](https://www.nuget.org/packages/NovaWpf.Mcp) | 2027.1.2 | DGJ | MCP server for AI assistants such as Kiro: the NovaWpf framework rules, the Nov… |
| 2026-11-20 08:35:30 | [GrayMint.Wallet](https://www.nuget.org/packages/GrayMint.Wallet) | 1.0.1 | GrayMint | A double-entry ledger for PostgreSQL and SQL Server, with tables of its own in… |
| 2026-11-20 08:35:44 | [Mfarzz.CleanArchitecture.Template](https://www.nuget.org/packages/Mfarzz.CleanArchitecture.Template) | 1.0.0 | Muhammad Fariz | Modern .NET 10 Clean Architecture Monolith Web API Starter Template with CQRS (… |
| 2026-11-20 08:46:05 | [Aneiang.Yarp.Plugin.FaultInjection](https://www.nuget.org/packages/Aneiang.Yarp.Plugin.FaultInjection) | 2.3.0.40 | AneiangSoft Team | Fault injection plugin for Aneiang.Yarp gateway: adds latency or failures to a… |
| 2026-11-20 08:46:30 | [Aneiang.Yarp.Templates](https://www.nuget.org/packages/Aneiang.Yarp.Templates) | 2.3.0.40 | AneiangSoft Team | dotnet new templates for Aneiang.Yarp: a gateway with routes, storage and dashb… |
| 2026-11-20 08:56:36 | [ITBees.OCPP](https://www.nuget.org/packages/ITBees.OCPP) | 8.0.8 | ITBees | OCPP 1.6J (JSON over WebSocket) central system for EV chargers, hosted inside a… |
| 2026-11-20 08:57:14 | [Fable.Ranvier.D5.Graph3D.Wgpu](https://www.nuget.org/packages/Fable.Ranvier.D5.Graph3D.Wgpu) | 0.5.0 | Ranvier contributors | Browser/Fable adapters and reactive GPU sinks bridging Ranvier.D5.Graph3D layou… |
| 2026-11-20 08:57:15 | [Fable.Ranvier.D5.Graph3D.Wgpu.Traced](https://www.nuget.org/packages/Fable.Ranvier.D5.Graph3D.Wgpu.Traced) | 0.5.0 | Ranvier contributors | Browser/Fable adapters and reactive GPU sinks bridging Ranvier.D5.Graph3D layou… |
| 2026-11-20 08:57:19 | [Fable.Ranvier.D5.Wgpu.View](https://www.nuget.org/packages/Fable.Ranvier.D5.Wgpu.View) | 0.5.0 | Ranvier contributors | Browser WebGPU and WebGL2 interactive 3D plot host and multi-pass subplot grid… |
| 2026-11-20 08:57:20 | [Fable.Ranvier.D5.Wgpu.View.Traced](https://www.nuget.org/packages/Fable.Ranvier.D5.Wgpu.View.Traced) | 0.5.0 | Ranvier contributors | Browser WebGPU and WebGL2 interactive 3D plot host and multi-pass subplot grid… |
| 2026-11-20 08:57:31 | [Ranvier.D5.Graph3D.Wgpu](https://www.nuget.org/packages/Ranvier.D5.Graph3D.Wgpu) | 0.5.0 | Ranvier contributors | Adapters and reactive GPU sinks bridging Ranvier.D5.Graph3D layouts directly to… |
| 2026-11-20 08:57:32 | [Ranvier.D5.Graph3D.Wgpu.Traced](https://www.nuget.org/packages/Ranvier.D5.Graph3D.Wgpu.Traced) | 0.5.0 | Ranvier contributors | Adapters and reactive GPU sinks bridging Ranvier.D5.Graph3D layouts directly to… |
| 2026-11-20 09:06:52 | [Defra.Livestock.Sdk.Core](https://www.nuget.org/packages/Defra.Livestock.Sdk.Core) | 0.2.0 | Defra | Shared building blocks for Livestock Information Service (LIS) .NET services, i… |
| 2026-11-20 09:07:19 | [Jtext103.CFET2.Things.PlcDmmAI](https://www.nuget.org/packages/Jtext103.CFET2.Things.PlcDmmAI) | 1.1.1 | Jtext103 | CFET2 IBasicAI driver for reading DMM6500 data buffered by a Siemens S7-1500 PL… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
