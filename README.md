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

## Latest list — 2026-11-24 00:20 UTC

New packages created between 2026-11-23 23:21 UTC and 2026-11-24 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T00-20-41-609715Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 23:30:00 | [AIKernel.Providers.Stt](https://www.nuget.org/packages/AIKernel.Providers.Stt) | 0.1.4 | Takuya Sogawa | Local CPU WAV transcription with the pinned multilingual Whisper small model. |
| 2026-11-23 23:31:39 | [Svg.Editor.Skia.Uno](https://www.nuget.org/packages/Svg.Editor.Skia.Uno) | 7.0.5 | Wiesław Šoltés | Reusable SVG editor workspace and accelerated canvas for Uno Platform. |
| 2026-11-23 23:31:43 | [Svg.Editor.Mcp](https://www.nuget.org/packages/Svg.Editor.Mcp) | 5.2.4 | Wiesław Šoltés | Shared MCP protocol and automation adapters for the SVG editor. |
| 2026-11-23 23:31:55 | [Svg.Editor.Mcp.Hosting](https://www.nuget.org/packages/Svg.Editor.Mcp.Hosting) | 5.2.4 | Wiesław Šoltés | Local MCP hosting and browser relay for the SVG editor. |
| 2026-11-23 23:32:02 | [EaseFilter.FileSecurity](https://www.nuget.org/packages/EaseFilter.FileSecurity) | 5.8.8.1 | EaseFilter | The EaseFilter File Security SDK is a comprehensive, modular framework designed… |
| 2026-11-23 23:48:52 | [DotReticulum.Applications](https://www.nuget.org/packages/DotReticulum.Applications) | 1.5.7.158 | DotReticulum contributors | DotReticulum runtime host (ReticulumNode) and Reticulum utility implementations. |
| 2026-11-23 23:48:54 | [DotReticulum.Core](https://www.nuget.org/packages/DotReticulum.Core) | 1.5.7.158 | DotReticulum contributors | Reticulum identities, destinations, packet codec and interface manager for DotR… |
| 2026-11-23 23:48:55 | [DotReticulum.Crypto](https://www.nuget.org/packages/DotReticulum.Crypto) | 1.5.7.158 | DotReticulum contributors | Ed25519, X25519, HKDF-SHA256 and Reticulum token primitives for DotReticulum. |
| 2026-11-23 23:48:57 | [DotReticulum.Interfaces](https://www.nuget.org/packages/DotReticulum.Interfaces) | 1.5.7.158 | DotReticulum contributors | Reticulum UDP, TCP, serial and other network interfaces for DotReticulum. |
| 2026-11-23 23:48:58 | [DotReticulum.Transport](https://www.nuget.org/packages/DotReticulum.Transport) | 1.5.7.158 | DotReticulum contributors | Reticulum announces, routing, path discovery, links, channels and resources for… |
| 2026-11-23 23:58:28 | [GameEventScript.Network](https://www.nuget.org/packages/GameEventScript.Network) | 0.6.0 | Stephan Schlöpke | Portable, synchronous Game Event Script network sessions over schema-declared r… |
| 2026-11-23 23:58:29 | [GameEventScript.Network.Sockets](https://www.nuget.org/packages/GameEventScript.Network.Sockets) | 0.6.0 | Stephan Schlöpke | TCP, WebSocket and UDP transports for Game Event Script network sessions. Backg… |
| 2026-11-24 00:02:05 | [Winche.Integrity](https://www.nuget.org/packages/Winche.Integrity) | 1.0.0 | Ehsan Rashidi | Winche Integrity: a project's apps prove they're its own (App Attest, Play Inte… |
| 2026-11-24 00:02:06 | [Winche.Integrity.AspNetCore](https://www.nuget.org/packages/Winche.Integrity.AspNetCore) | 1.0.0 | Ehsan Rashidi | Winche Integrity for ASP.NET Core: the apps' token exchange (/integrity/v1/exch… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
