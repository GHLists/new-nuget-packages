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

## Latest list — 2026-11-10 01:20 UTC

New packages created between 2026-11-10 00:19 UTC and 2026-11-10 01:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T01-20-34-090507Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 00:25:57 | [Universal.Operative.Sdk.Discrete.Databricks](https://www.nuget.org/packages/Universal.Operative.Sdk.Discrete.Databricks) | 1.0.0 | Andrew Ong | Databricks Unity Gateway adapters for Universal.Operative.Sdk.Discrete. |
| 2026-11-10 00:42:10 | [Taba.Pulumi](https://www.nuget.org/packages/Taba.Pulumi) | 0.3.11 | rafaelpontani | Queues, distributors and access tokens of the Taba messaging system. |
| 2026-11-10 00:42:11 | [Kaminari.Sazanami](https://www.nuget.org/packages/Kaminari.Sazanami) | 1.1.0 | ErrorLSC | Shared infrastructure for the Kaminari projects. |
| 2026-11-10 00:42:21 | [Kaminari.Samidare](https://www.nuget.org/packages/Kaminari.Samidare) | 1.1.0 | ErrorLSC | The query compiler of the Kaminari projects. |
| 2026-11-10 00:44:25 | [HPD-Agent.AspNetCore.Evaluations](https://www.nuget.org/packages/HPD-Agent.AspNetCore.Evaluations) | 0.9.5 | HPD-Research,Einstein Essibu | Optional evaluation API endpoints for HPD-Agent ASP.NET hosts. |
| 2026-11-10 00:44:26 | [HPD-Agent.AspNetCore.OpenApi](https://www.nuget.org/packages/HPD-Agent.AspNetCore.OpenApi) | 0.9.5 | HPD-Research,Einstein Essibu | OpenAPI document generation for the HPD-Agent HTTP and committed SSE API. |
| 2026-11-10 00:44:27 | [HPD-Agent.Audio.LiveKit](https://www.nuget.org/packages/HPD-Agent.Audio.LiveKit) | 0.9.5 | HPD-Research,Einstein Essibu | Managed LiveKit audio transport for HPD Agent Audio. |
| 2026-11-10 00:44:32 | [HPD-Agent.Client](https://www.nuget.org/packages/HPD-Agent.Client) | 0.9.5 | HPD-Research,Einstein Essibu | Invariant HTTP, retry, error, and resumable SSE runtime for generated HPD Agent… |
| 2026-11-10 00:44:34 | [HPD-Agent.Evaluations.HpdBase](https://www.nuget.org/packages/HPD-Agent.Evaluations.HpdBase) | 0.9.5 | HPD-Research,Einstein Essibu | HPD Base-backed durable score, run, dataset, and evaluation result storage for… |
| 2026-11-10 00:44:40 | [HPD-Agent.MultiAgent.AspNetCore](https://www.nuget.org/packages/HPD-Agent.MultiAgent.AspNetCore) | 0.9.5 | HPD-Research,Einstein Essibu | ASP.NET Core projection API for durable HPD multi-agent graph activations. |
| 2026-11-10 00:44:40 | [HPD-Agent.MultiAgent.HpdBase](https://www.nuget.org/packages/HPD-Agent.MultiAgent.HpdBase) | 0.9.5 | HPD-Research,Einstein Essibu | HPD Base adapter for durable HPD multi-agent graph activations. |
| 2026-11-10 00:44:59 | [HPD-Agent.Sandbox](https://www.nuget.org/packages/HPD-Agent.Sandbox) | 0.9.5 | HPD-Research,Einstein Essibu | Backend-neutral Agent sandbox composition, capability admission, and logical wo… |
| 2026-11-10 00:45:00 | [HPD-Agent.Sandbox.HostContainers](https://www.nuget.org/packages/HPD-Agent.Sandbox.HostContainers) | 0.9.5 | HPD-Research,Einstein Essibu | Agent adapter for retained HPD Environment Host Containers sandbox sessions. |
| 2026-11-10 00:45:01 | [HPD-Agent.Sandbox.HostProcess](https://www.nuget.org/packages/HPD-Agent.Sandbox.HostProcess) | 0.9.5 | HPD-Research,Einstein Essibu | Thin Agent adapter for the HPD Environment Host Process backend. |
| 2026-11-10 00:45:02 | [HPD-Agent.Sandbox.VirtualMachine](https://www.nuget.org/packages/HPD-Agent.Sandbox.VirtualMachine) | 0.9.5 | HPD-Research,Einstein Essibu | Agent-facing Apple Virtualization sandbox integration for HPD Agent. |
| 2026-11-10 00:45:03 | [HPD-Agent.Stores.HpdBase](https://www.nuget.org/packages/HPD-Agent.Stores.HpdBase) | 0.9.5 | HPD-Research,Einstein Essibu | HPD Base-backed durable stores for HPD Agent definitions, sessions, and thread… |
| 2026-11-10 00:55:16 | [Polars.FSharp](https://www.nuget.org/packages/Polars.FSharp) | 1.1.0 | ErrorLSC | Idiomatic F# API for Polars DataFrame library with strict type safety and pipel… |
| 2026-11-10 01:01:41 | [Identvia.AspNetCore](https://www.nuget.org/packages/Identvia.AspNetCore) | 0.1.3 | Identvia | AddIdentvia(): Sign in with Identvia for ASP.NET Core, the OpenID Connect handl… |
| 2026-11-10 01:01:42 | [Identvia](https://www.nuget.org/packages/Identvia) | 0.1.3 | Identvia | Sign in with Identvia for .NET apps (MAUI, WinUI, WPF, console): OpenID Connect… |
| 2026-11-10 01:04:51 | [SharpDTLS](https://www.nuget.org/packages/SharpDTLS) | 0.0.1 | Lukas Volf | DTLS 1.0-1.3 and TLS 1.0-1.3 client and server written in C#. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
