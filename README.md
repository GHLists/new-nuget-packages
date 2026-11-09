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

## Latest list — 2026-11-09 04:20 UTC

New packages created between 2026-11-09 03:18 UTC and 2026-11-09 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T04-20-25-63538Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 03:52:54 | [Cratis.Arc.Mcp](https://www.nuget.org/packages/Cratis.Arc.Mcp) | 22.177.0 | Cratis | Model Context Protocol serving for Cratis Arc: explicitly declared commands and… |
| 2026-11-09 03:54:09 | [BSGameLib.Core](https://www.nuget.org/packages/BSGameLib.Core) | 1.0.3-preview | Burningstorm Studios | The types every BSGameLib package and a game's shared code agree on: IIdentifia… |
| 2026-11-09 03:54:09 | [BSGameLib.Chat](https://www.nuget.org/packages/BSGameLib.Chat) | 1.0.4-preview | Burningstorm Studios | A chat and slash-command engine for games: commands from a fluent builder or at… |
| 2026-11-09 03:54:10 | [BSGameLib.MsQuic.Native](https://www.nuget.org/packages/BSGameLib.MsQuic.Native) | 1.0.3-preview | Burningstorm Studios | Native msquic for .NET's QUIC on Linux and macOS, copied beside a game's execut… |
| 2026-11-09 03:54:12 | [BSGameLib.Networking](https://www.nuget.org/packages/BSGameLib.Networking) | 1.0.4-preview | Burningstorm Studios | Client and server networking for games over QUIC: plain-class packets, reliable… |
| 2026-11-09 03:54:14 | [BSGameLib.Server](https://www.nuget.org/packages/BSGameLib.Server) | 1.0.4-preview | Burningstorm Studios | A dedicated game server host on Microsoft.Extensions.Hosting: finds your game's… |
| 2026-11-09 03:54:16 | [BSGameLib.Sdl3.Native](https://www.nuget.org/packages/BSGameLib.Sdl3.Native) | 1.0.3-preview | Burningstorm Studios | Native SDL3, SDL3_image and SDL3_mixer for Windows, Linux and macOS, copied bes… |
| 2026-11-09 03:54:17 | [BSGameLib.MoltenVK.Native](https://www.nuget.org/packages/BSGameLib.MoltenVK.Native) | 1.0.3-preview | Burningstorm Studios | MoltenVK, Vulkan for macOS, copied beside a game's executable. Added automatica… |
| 2026-11-09 03:54:18 | [BSGameLib.Sdl3.Interop](https://www.nuget.org/packages/BSGameLib.Sdl3.Interop) | 1.0.4-preview | Burningstorm Studios | .NET bindings for SDL3, SDL3_image and SDL3_mixer, generated from the SDL heade… |
| 2026-11-09 03:54:19 | [BSGameLib.Game](https://www.nuget.org/packages/BSGameLib.Game) | 1.0.11-preview | Burningstorm Studios | A 2D game engine for .NET on SDL3, with Vulkan and OpenGL renderers, shaders co… |
| 2026-11-09 03:54:20 | [BSGameLib.Game.ShaderCompiler](https://www.nuget.org/packages/BSGameLib.Game.ShaderCompiler) | 1.0.4-preview | Burningstorm Studios | Compiles GLSL to SPIR-V at runtime for BSGameLib.Game's Vulkan renderer, with a… |
| 2026-11-09 03:54:20 | [BSGameLib.UI](https://www.nuget.org/packages/BSGameLib.UI) | 1.0.4-preview | Burningstorm Studios | The UI layer for BSGameLib.Game: views in XML or C#, bound to view-models, with… |
| 2026-11-09 03:58:44 | [Weave.WebSharper](https://www.nuget.org/packages/Weave.WebSharper) | 0.1.0 | Weave contributors | A component library for building F# web applications with WebSharper. |
| 2026-11-09 04:05:21 | [Sokuro](https://www.nuget.org/packages/Sokuro) | 1.0.0 | Pdawg | A fast, multi-threaded logging library for .NET designed for low latency and th… |
| 2026-11-09 04:10:26 | [PiSharp.Chord.Hosting](https://www.nuget.org/packages/PiSharp.Chord.Hosting) | 1.5.0.1 | PiSharp contributors | EXPERIMENTAL. Native Chord plugin, HTTP and process-worker hosting. Requires th… |
| 2026-11-09 04:10:28 | [PiSharp.Env.Protocol](https://www.nuget.org/packages/PiSharp.Env.Protocol) | 1.5.0.1 | PiSharp contributors | EXPERIMENTAL. Bounded frame codec for the PiSharp remote environment protocol.… |
| 2026-11-09 04:10:30 | [PiSharp.Chord](https://www.nuget.org/packages/PiSharp.Chord) | 1.5.0.1 | PiSharp contributors | EXPERIMENTAL. Native Chord host, state, jobs, registries and versioned links. R… |
| 2026-11-09 04:10:31 | [PiSharp.Env](https://www.nuget.org/packages/PiSharp.Env) | 1.5.0.1 | PiSharp contributors | EXPERIMENTAL. Remote execution, filesystem, watch and SSH environment client. D… |
| 2026-11-09 04:10:32 | [PiSharp.Durable.Store](https://www.nuget.org/packages/PiSharp.Durable.Store) | 1.5.0.1 | PiSharp contributors | EXPERIMENTAL. Durable storage and registry adapters for Chord with SQLite. Supp… |
| 2026-11-09 04:13:19 | [Weave.WebSharper.Templates](https://www.nuget.org/packages/Weave.WebSharper.Templates) | 0.1.0 | Weave contributors | Project templates for Weave and WebSharper. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
