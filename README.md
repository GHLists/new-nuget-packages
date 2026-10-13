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

## Latest list — 2026-10-13 16:21 UTC

New packages created between 2026-10-13 15:22 UTC and 2026-10-13 16:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T16-21-18-032042Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 15:24:10 | [Novior.MentorAgent.Abstractions](https://www.nuget.org/packages/Novior.MentorAgent.Abstractions) | 1.0.0 | Emanuele Longo, Antonio Macrì | Shared interfaces, models, enums and UI components for the MentorAgent family.… |
| 2026-10-13 15:24:11 | [Novior.MentorAgent.Blazor](https://www.nuget.org/packages/Novior.MentorAgent.Blazor) | 1.0.0 | Emanuele Longo, Antonio Macrì | Blazor WebAssembly client for MentorAgent. Install in your Blazor WASM / Blazor… |
| 2026-10-13 15:24:12 | [Novior.MentorAgent.Server](https://www.nuget.org/packages/Novior.MentorAgent.Server) | 1.0.0 | Emanuele Longo, Antonio Macrì | Expose MentorAgent as a universal AI backend from any ASP.NET Core application.… |
| 2026-10-13 15:24:13 | [Novior.MentorAgent.Declarative](https://www.nuget.org/packages/Novior.MentorAgent.Declarative) | 1.0.0 | Emanuele Longo, Antonio Macrì | Define MentorAgent Level-2 specialist agents in YAML instead of C#. Wraps the A… |
| 2026-10-13 15:24:14 | [Novior.MentorAgent](https://www.nuget.org/packages/Novior.MentorAgent) | 1.0.0 | Emanuele Longo, Antonio Macrì | A Blazor Razor Class Library that adds an AI-powered floating chat assistant to… |
| 2026-10-13 15:30:53 | [CodeRestraint](https://www.nuget.org/packages/CodeRestraint) | 0.0.1 | CodeRestraint | Syntax-based C# implementation size and parameter limits. |
| 2026-10-13 15:31:27 | [Skyline.DataMiner.Utils.EntityIdentifier](https://www.nuget.org/packages/Skyline.DataMiner.Utils.EntityIdentifier) | 2.0.1-prerelease1 | SkylineCommunications | [Minimum Required DataMiner: 10.4.11] Helper for resolving entity identifiers t… |
| 2026-10-13 15:32:14 | [SqlLookout](https://www.nuget.org/packages/SqlLookout) | 0.0.1-alpha | Derek | Reserved package id for SqlLookout, a SQL Server monitoring tool. Work in progr… |
| 2026-10-13 15:33:47 | [kokos-me-dotnet-evodoc-ai-orchestrator.Shared](https://www.nuget.org/packages/kokos-me-dotnet-evodoc-ai-orchestrator.Shared) | 1.0.0 | Smeup BSA s.r.l. | Contratti condivisi (DTO degli endpoint /ai/*, configurazione e costanti) del M… |
| 2026-10-13 15:34:34 | [kokos-me-dotnet-evodoc-ai-orchestrator.SDK](https://www.nuget.org/packages/kokos-me-dotnet-evodoc-ai-orchestrator.SDK) | 1.0.0 | Smeup BSA s.r.l. | Client .NET del MEX AI Orchestrator di EvoDoc: AiPortalClient per evoPortal e A… |
| 2026-10-13 15:39:30 | [Cronitor.Coravel](https://www.nuget.org/packages/Cronitor.Coravel) | 6.0.77 | gonace | Reports Coravel scheduled jobs to Cronitor: run when they start, complete when… |
| 2026-10-13 15:47:05 | [PanoramicData.IssueAssessment](https://www.nuget.org/packages/PanoramicData.IssueAssessment) | 1.0.19 | Panoramic Data Limited | Schema-agnostic issue and ticket quality assessment for .NET: score Jira, GitHu… |
| 2026-10-13 15:55:19 | [Yoyo.WeCom](https://www.nuget.org/packages/Yoyo.WeCom) | 10.5.8 | Yoyo | 独立 .NET 企业微信客户端：连接隔离、token、目录、消息、待办与安全回调。 |
| 2026-10-13 15:55:34 | [Nethermind.RocksDbBindings](https://www.nuget.org/packages/Nethermind.RocksDbBindings) | 11.8.1.153 | Nethermind | C# bindings for RocksDB. |
| 2026-10-13 15:58:02 | [VectorPulse.StatelessGateway](https://www.nuget.org/packages/VectorPulse.StatelessGateway) | 1.1.0 | VectorPulse Software | High-performance, memory-optimized stateless webhook proxy and concurrent multi… |
| 2026-10-13 15:58:44 | [TingPush.Maui](https://www.nuget.org/packages/TingPush.Maui) | 1.0.0 | TingPush | .NET MAUI SDK for TingPush push notifications and incoming calls (CallKit on iO… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
