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

## Latest list — 2026-10-28 23:20 UTC

New packages created between 2026-10-28 22:19 UTC and 2026-10-28 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T23-20-17-726897Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 22:33:59 | [Maplibre.NativeFfi.Runtime.Metal](https://www.nuget.org/packages/Maplibre.NativeFfi.Runtime.Metal) | 0.202610.3 | MapLibre | Metal native runtime assets for MapLibre Native .NET. |
| 2026-10-28 22:34:00 | [Maplibre.NativeFfi](https://www.nuget.org/packages/Maplibre.NativeFfi) | 0.202610.3 | MapLibre | Low-level .NET bindings for the MapLibre Native C API. |
| 2026-10-28 22:34:03 | [Maplibre.NativeFfi.Runtime.Vulkan](https://www.nuget.org/packages/Maplibre.NativeFfi.Runtime.Vulkan) | 0.202610.3 | MapLibre | Vulkan native runtime assets for MapLibre Native .NET. |
| 2026-10-28 22:34:05 | [Maplibre.NativeFfi.Runtime.OpenGL](https://www.nuget.org/packages/Maplibre.NativeFfi.Runtime.OpenGL) | 0.202610.3 | MapLibre | OpenGL native runtime assets for MapLibre Native .NET. |
| 2026-10-28 23:07:26 | [Gravicode.OfficeNet.Mcp](https://www.nuget.org/packages/Gravicode.OfficeNet.Mcp) | 2.0.0 | Gravicode Studios | An MCP server that lets AI assistants create, edit, convert and preview Word, E… |
| 2026-10-28 23:07:58 | [OneLobby.Core](https://www.nuget.org/packages/OneLobby.Core) | 0.6.0 | OneLobby contributors | Engine-agnostic OneLobby client: lobbies, lockstep, voice and text chat. |
| 2026-10-28 23:07:59 | [OneLobby.Replication](https://www.nuget.org/packages/OneLobby.Replication) | 0.6.0 | OneLobby contributors | Engine-agnostic host-authoritative state replication over a OneLobby raw-mode l… |
| 2026-10-28 23:07:59 | [OneLobby.Direct](https://www.nuget.org/packages/OneLobby.Direct) | 0.6.0 | OneLobby contributors | Host and join OneLobby lobbies by IP address: the host's game runs the signalin… |
| 2026-10-28 23:08:00 | [OneLobby.Hub](https://www.nuget.org/packages/OneLobby.Hub) | 0.6.0 | OneLobby contributors | OneLobby signaling hub (protocol lk1): lobbies, join codes, signaling relay. Us… |
| 2026-10-28 23:08:00 | [OneLobby.Godot](https://www.nuget.org/packages/OneLobby.Godot) | 0.6.0 | OneLobby contributors | Godot 4 transport (WebRTC data channels, WebSocket), microphone capture and pla… |
| 2026-10-28 23:08:01 | [OneLobby.DataChannel](https://www.nuget.org/packages/OneLobby.DataChannel) | 0.6.0 | OneLobby contributors | Engine-agnostic ITransport for OneLobby over libdatachannel (WebRTC data channe… |
| 2026-10-28 23:08:01 | [OneLobby.Opus](https://www.nuget.org/packages/OneLobby.Opus) | 0.6.0 | OneLobby contributors | IVoiceCodec for OneLobby using Concentus, a managed Opus port (BSD-3-Clause). |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
