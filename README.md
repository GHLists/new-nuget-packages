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

## Latest list — 2026-10-01 02:21 UTC

New packages created between 2026-10-01 01:21 UTC and 2026-10-01 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T02-21-30-36002Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 01:27:22 | [ZeroAgent.Dialog](https://www.nuget.org/packages/ZeroAgent.Dialog) | 1.1.0 | Phong Võ | Deterministic Semantic Task-Oriented Dialogue System and Multi-Tier Agentic Mem… |
| 2026-10-01 01:27:23 | [ZeroAgent.Tools](https://www.nuget.org/packages/ZeroAgent.Tools) | 1.1.0 | Phong Võ | Industrial and Operational Toolset for ZeroAgent (PLC Modbus, Gorilla TSDB Quer… |
| 2026-10-01 01:35:07 | [Novolis.Avalonia.Packaging.Inno](https://www.nuget.org/packages/Novolis.Avalonia.Packaging.Inno) | 2026.1.6.194 | Novolis | Inno Setup script generation helpers for Novolis Avalonia installers. |
| 2026-10-01 01:35:08 | [Novolis.Avalonia.Raylib](https://www.nuget.org/packages/Novolis.Avalonia.Raylib) | 2026.1.6.194 | Novolis | Avalonia host control for embedded Raylib viewports (hidden GLFW + RGBA streami… |
| 2026-10-01 01:35:09 | [Novolis.Avalonia.Rendering](https://www.nuget.org/packages/Novolis.Avalonia.Rendering) | 2026.1.6.194 | Novolis | Avalonia hosts for Novolis.Rendering.TwoD (OpenGL) and CPU RGBA frames. |
| 2026-10-01 01:35:11 | [Novolis.Avalonia.Ship](https://www.nuget.org/packages/Novolis.Avalonia.Ship) | 2026.1.6.194 | Novolis | Ship Designer Avalonia chrome: validate ship, hatch helpers, airtight overlay,… |
| 2026-10-01 01:35:13 | [Novolis.Avalonia.Ship.Design](https://www.nuget.org/packages/Novolis.Avalonia.Ship.Design) | 2026.1.6.194 | Novolis | Object-first Ship Designer Avalonia UI: PLAN/MODEL/PRESENT, ShipDesignSession,… |
| 2026-10-01 01:35:15 | [Novolis.Avalonia.Speech](https://www.nuget.org/packages/Novolis.Avalonia.Speech) | 2026.1.6.194 | Novolis | Application speech front for device voice playback and user-owned Azure Speech… |
| 2026-10-01 01:35:16 | [Novolis.Avalonia.StarMap](https://www.nuget.org/packages/Novolis.Avalonia.StarMap) | 2026.1.6.194 | Novolis | Avalonia pan/zoom star map control for catalog points and route edges. |
| 2026-10-01 01:35:17 | [Novolis.Avalonia.Studio](https://www.nuget.org/packages/Novolis.Avalonia.Studio) | 2026.1.6.194 | Novolis | Studio chrome for Avalonia editors: status, flash, busy overlay, three-column l… |
| 2026-10-01 01:35:18 | [Novolis.Avalonia.ThreeD](https://www.nuget.org/packages/Novolis.Avalonia.ThreeD) | 2026.1.6.194 | Novolis | Avalonia ThreeD editor surface: scene hierarchy, OpenGL wireframe viewport, mes… |
| 2026-10-01 01:35:20 | [Novolis.Avalonia.Torrent](https://www.nuget.org/packages/Novolis.Avalonia.Torrent) | 2026.1.6.194 | Novolis | Avalonia torrent session chrome bound to Novolis.Transports.Torrent — not a pro… |
| 2026-10-01 01:35:21 | [Novolis.Avalonia.Video](https://www.nuget.org/packages/Novolis.Avalonia.Video) | 2026.1.6.194 | Novolis | Avalonia video surface, storyboard strip, and Movie Maker preview session. |
| 2026-10-01 01:35:22 | [Novolis.Avalonia.Voice](https://www.nuget.org/packages/Novolis.Avalonia.Voice) | 2026.1.6.194 | Novolis | Avalonia controls for Novolis voice preset design, preview, and C# export. |
| 2026-10-01 01:48:05 | [Entitler](https://www.nuget.org/packages/Entitler) | 0.0.1 | 1843 Inc. | Official Entitler SDK for .NET (not yet available) |
| 2026-10-01 02:08:25 | [EmptyEngine.Serialization](https://www.nuget.org/packages/EmptyEngine.Serialization) | 0.3.1 | FriendSea | Package Description |
| 2026-10-01 02:08:26 | [EmptyEngine.Serialization.Editor](https://www.nuget.org/packages/EmptyEngine.Serialization.Editor) | 0.3.1 | FriendSea | Package Description |
| 2026-10-01 02:08:28 | [EmptyEngine.Serialization.Generator](https://www.nuget.org/packages/EmptyEngine.Serialization.Generator) | 0.3.1 | FriendSea | Package Description |
| 2026-10-01 02:08:32 | [EmptyEngine.TypeCatalog](https://www.nuget.org/packages/EmptyEngine.TypeCatalog) | 0.3.1 | FriendSea | Package Description |
| 2026-10-01 02:12:14 | [Meziantou.Framework.Language.Css](https://www.nuget.org/packages/Meziantou.Framework.Language.Css) | 1.0.0 | meziantou | A Roslyn-style immutable CSS syntax tree with lossless parsing and diagnostics:… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
