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

## Latest list — 2026-11-23 19:20 UTC

New packages created between 2026-11-23 18:21 UTC and 2026-11-23 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T19-20-25-189391Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 18:25:18 | [Webority.Webhooks.Inbound.Abstractions](https://www.nuget.org/packages/Webority.Webhooks.Inbound.Abstractions) | 0.26.0 | Webority Technologies | Webority.Webhooks.Inbound.Abstractions holds the inbound request and the signat… |
| 2026-11-23 18:32:27 | [Openlayer](https://www.nuget.org/packages/Openlayer) | 0.1.0 | Openlayer | The official C# / .NET library for the Openlayer API, the Evaluation Platform f… |
| 2026-11-23 18:32:52 | [DocsRagMcp](https://www.nuget.org/packages/DocsRagMcp) | 0.1.0 | Ahmed Manai | MCP server that lets Claude, GitHub Copilot and Cursor search your own document… |
| 2026-11-23 18:33:28 | [Sstv.EndpointEol](https://www.nuget.org/packages/Sstv.EndpointEol) | 1.0.0 | Sstv | Endpoint end-of-life management for ASP.NET Core: sunset headers, warnings, met… |
| 2026-11-23 18:33:30 | [Sstv.EndpointEol.Swashbuckle](https://www.nuget.org/packages/Sstv.EndpointEol.Swashbuckle) | 1.0.0 | Sstv | Swashbuckle/OpenAPI annotations for Sstv.EndpointEol: deprecated flag, sunset n… |
| 2026-11-23 18:34:37 | [Aiursoft.BadgeProxy](https://www.nuget.org/packages/Aiursoft.BadgeProxy) | 10.0.0 | Aiursoft | BadgeProxy is a proxy service for GitLab pipeline status and coverage badge SVG… |
| 2026-11-23 18:40:34 | [ShingZhanho.FRConjugation](https://www.nuget.org/packages/ShingZhanho.FRConjugation) | 5.1.1 | ShingZhanho | French conjugation using a bundled catalogue of spelling rules. |
| 2026-11-23 18:50:40 | [Iwxxm.Net.Validation.Saxon](https://www.nuget.org/packages/Iwxxm.Net.Validation.Saxon) | 1.0.0 | 0neTX | Optional Iwxxm.Net add-on that runs the complete, unmodified official WMO IWXXM… |
| 2026-11-23 18:50:40 | [Iwxxm.Net](https://www.nuget.org/packages/Iwxxm.Net) | 1.0.0 | 0neTX | Zero-dependency .NET Standard 2.0 & 2.1 library for ICAO/WMO IWXXM 2025-2: XSD… |
| 2026-11-23 18:54:02 | [SinkSharp.Sinks.Slack](https://www.nuget.org/packages/SinkSharp.Sinks.Slack) | 1.0.0 | SinkSharp | Slack alerting sink for SinkSharp. Posts Error/Critical log events to a Slack c… |
| 2026-11-23 18:57:39 | [AIKernel.Contracts.Reranking](https://www.nuget.org/packages/AIKernel.Contracts.Reranking) | 0.1.4 | Takuya Sogawa | AIKernel text reranking and capability contracts using the shared provider scor… |
| 2026-11-23 18:57:45 | [SinkSharp.Sinks.MicrosoftTeams](https://www.nuget.org/packages/SinkSharp.Sinks.MicrosoftTeams) | 1.0.0 | SinkSharp | Microsoft Teams alerting sink for SinkSharp. Posts Error/Critical log events to… |
| 2026-11-23 18:58:09 | [Glazor](https://www.nuget.org/packages/Glazor) | 1.1.0 | Valentino Proietti and Ilaria… | A specialized Razor Class Library for .NET 10 Blazor applications, offering hig… |
| 2026-11-23 18:58:23 | [Glazor.EntityFrameworkCore](https://www.nuget.org/packages/Glazor.EntityFrameworkCore) | 1.1.0 | Valentino Proietti and Ilaria… | Entity Framework Core paged data models for the Glazor data grids. |
| 2026-11-23 19:03:54 | [AbpAdmin.Cli](https://www.nuget.org/packages/AbpAdmin.Cli) | 0.1.0 | ABP Admin contributors | Adds ABP Admin to an ABP application: detects its .NET and ABP versions and its… |
| 2026-11-23 19:06:40 | [AIKernel.Providers.Reranker](https://www.nuget.org/packages/AIKernel.Providers.Reranker) | 0.1.4 | Takuya Sogawa | Local CPU text reranking with the pinned mMARCO MiniLM FP32 ONNX model. |
| 2026-11-23 19:08:29 | [GroveGames.Notifications](https://www.nuget.org/packages/GroveGames.Notifications) | 0.1.0 | Grove Games | Local notifications for mobile games: scheduling, permission, channels and the… |
| 2026-11-23 19:10:11 | [GroveGames.Haptics](https://www.nuget.org/packages/GroveGames.Haptics) | 0.1.0 | Grove Games | Haptic feedback with intensity, sharpness and duration for .NET and Unity, with… |
| 2026-11-23 19:11:54 | [GroveGames.Input](https://www.nuget.org/packages/GroveGames.Input) | 0.1.0 | Grove Games | Prioritized pointer and keyboard events with handled state for .NET and Unity |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
