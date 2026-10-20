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

## Latest list — 2026-10-20 21:20 UTC

New packages created between 2026-10-20 20:21 UTC and 2026-10-20 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T21-20-43-12021Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 20:28:43 | [LATec.MAUI.Yandex.Ads](https://www.nuget.org/packages/LATec.MAUI.Yandex.Ads) | 1.0.1 | Aleh Ladyka | Yandex Mobile Ads banner control (AdBannerView) for .NET MAUI on Android and iO… |
| 2026-10-20 20:32:42 | [Capastrum.Acp.Protocol](https://www.nuget.org/packages/Capastrum.Acp.Protocol) | 1.0.0 | Capastrum contributors | Agent Client Protocol v1 contracts for Capastrum. |
| 2026-10-20 20:32:43 | [Capastrum.Mcp.Protocol](https://www.nuget.org/packages/Capastrum.Mcp.Protocol) | 1.0.0 | Capastrum contributors | Model Context Protocol 2026-07-28 contracts for Capastrum. |
| 2026-10-20 20:32:44 | [Capastrum.Mcp](https://www.nuget.org/packages/Capastrum.Mcp) | 1.0.0 | Capastrum contributors | MCP server with tools, resources and prompts. |
| 2026-10-20 20:32:45 | [Capastrum.JsonRpc](https://www.nuget.org/packages/Capastrum.JsonRpc) | 1.0.0 | Capastrum contributors | JSON-RPC 2.0 peer, message model and transports for Capastrum. |
| 2026-10-20 20:32:46 | [Capastrum.Mcp.Client](https://www.nuget.org/packages/Capastrum.Mcp.Client) | 1.0.0 | Capastrum contributors | MCP client for connecting C# applications to external tool servers. |
| 2026-10-20 20:32:46 | [Capastrum.Acp.Server](https://www.nuget.org/packages/Capastrum.Acp.Server) | 1.0.0 | Capastrum contributors | ACP agent server for exposing a C# application as an agent. |
| 2026-10-20 20:32:47 | [Capastrum.Acp](https://www.nuget.org/packages/Capastrum.Acp) | 1.0.0 | Capastrum contributors | ACP host for launching and orchestrating AI agents with human-in-the-loop contr… |
| 2026-10-20 20:47:27 | [Programaris.Tenancy.Http](https://www.nuget.org/packages/Programaris.Tenancy.Http) | 0.2.0 | PROGRAMARIS | Opt-in, destination-restricted outbound tenant context propagation for HttpClie… |
| 2026-10-20 20:55:43 | [SlipeServer.Net.Managed](https://www.nuget.org/packages/SlipeServer.Net.Managed) | 0.1.0-CI-20261020-2… | Slipe | A managed C# implementation of the MTA San Andreas net layer for Slipe Server,… |
| 2026-10-20 20:56:02 | [Incursa.Platform.Sqlite](https://www.nuget.org/packages/Incursa.Platform.Sqlite) | 6.0.10 | Incursa | Single-host SQLite provider for Incursa Platform scheduling, messaging, coordin… |
| 2026-10-20 21:02:16 | [Archevolt](https://www.nuget.org/packages/Archevolt) | 0.1.0 | Stephan van Stekelenburg | A standalone, Bevy-inspired entity component system for .NET 10 and C# 14. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
