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

## Latest list — 2026-11-11 02:20 UTC

New packages created between 2026-11-11 01:20 UTC and 2026-11-11 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T02-20-08-408468Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 01:23:24 | [RecursiveAI.OnePhysics.Interchange](https://www.nuget.org/packages/RecursiveAI.OnePhysics.Interchange) | 1.0.0 | Recursive AI, LLC | Importers for RecursiveAI.OnePhysics: URDF and MJCF robots become articulation… |
| 2026-11-11 01:23:24 | [RecursiveAI.OnePhysics](https://www.nuget.org/packages/RecursiveAI.OnePhysics) | 1.0.0 | Recursive AI, LLC | Deterministic 2D and 3D physics for .NET with identical results on every platfo… |
| 2026-11-11 01:23:25 | [RecursiveAI.OnePhysics.Tools](https://www.nuget.org/packages/RecursiveAI.OnePhysics.Tools) | 1.0.0 | Recursive AI, LLC | Authoring-time geometry for RecursiveAI.OnePhysics: 3D convex decomposition, hu… |
| 2026-11-11 01:23:37 | [Universal.Operative.Sdk.ModelContextProtocol](https://www.nuget.org/packages/Universal.Operative.Sdk.ModelContextProtocol) | 1.0.0 | Andrew Ong | Model Context Protocol tool discovery, native Operative tool adapters, and MCP… |
| 2026-11-11 01:28:55 | [NLNet.UiDebug.Light.SDK](https://www.nuget.org/packages/NLNet.UiDebug.Light.SDK) | 1.0.0 | NLNet | Lightweight optional debug module contract for .NET applications. |
| 2026-11-11 01:34:21 | [BootstrapBlazor.SignalR.Client](https://www.nuget.org/packages/BootstrapBlazor.SignalR.Client) | 11.0.0 | Argo(argo@live.ca),BootstrapB… | Optional SignalR client transport for BootstrapBlazor dispatch and connection s… |
| 2026-11-11 01:54:32 | [FireMQ.Client](https://www.nuget.org/packages/FireMQ.Client) | 0.1.0 | FireMQ | .NET client for FireMQ, a RabbitMQ-compatible message broker. Speaks the native… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
