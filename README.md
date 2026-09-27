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

## Latest list — 2026-09-27 09:04 UTC

New packages created between 2026-09-27 08:04 UTC and 2026-09-27 09:04 UTC.

[Full CSV](data/new-nuget-packages-2026-09-27T09-04-37-184845Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-27 08:08:48 | [BravoDev.AppointMe.Templates](https://www.nuget.org/packages/BravoDev.AppointMe.Templates) | 1.2.1 | BravoDev | A production-grade modular-monolith .NET 10 + React 19 SaaS foundation: multi-t… |
| 2026-09-27 08:10:59 | [QuickDraw.Pict](https://www.nuget.org/packages/QuickDraw.Pict) | 0.1.0 | Lars Dytterud | Dependency-free reader and writer for Apple QuickDraw PICT pictures (v1, v2 and… |
| 2026-09-27 08:11:00 | [QuickDraw.Pict.ImageSharp](https://www.nuget.org/packages/QuickDraw.Pict.ImageSharp) | 0.1.0 | Lars Dytterud | SixLabors.ImageSharp format plugin for Apple QuickDraw PICT pictures, QuickTime… |
| 2026-09-27 08:13:18 | [Stride.Dependencies.Naga](https://www.nuget.org/packages/Stride.Dependencies.Naga) | 2026.9.27 | Stride Contributors | naga, the SPIR-V to WGSL converter, for Stride's WebGPU/browser shader path. Bu… |
| 2026-09-27 08:30:14 | [NextGenSoftware.OASIS.MCP.Server](https://www.nuget.org/packages/NextGenSoftware.OASIS.MCP.Server) | 2.0.2 | David Ellams (NextGen Softwar… | The OASIS Model Context Protocol (MCP) Server — exposes 250 typed named tools a… |
| 2026-09-27 08:33:24 | [Stride.Dependencies.Tint](https://www.nuget.org/packages/Stride.Dependencies.Tint) | 2026.9.27 | Stride Contributors | Tint, the WGSL validator from Dawn, for Stride's WebGPU/browser shader path. Re… |
| 2026-09-27 08:43:03 | [ChunkShift](https://www.nuget.org/packages/ChunkShift) | 0.1.0 | MrFr3di | Deterministic content-defined chunking, streaming binary manifests and verifica… |
| 2026-09-27 08:48:45 | [Paradise.Hexa.NET.ImGui](https://www.nuget.org/packages/Paradise.Hexa.NET.ImGui) | 3.1.0 | Juna Meinhold | A .NET wrapper for the Dear ImGui library. (1.92.9b) |
| 2026-09-27 08:48:46 | [Paradise.Hexa.NET.ImGuizmo](https://www.nuget.org/packages/Paradise.Hexa.NET.ImGuizmo) | 3.1.0 | Juna Meinhold | A .NET wrapper for the ImGuizmo library. (1.92.5 WIP / commit dc25afb) (for ImG… |
| 2026-09-27 08:48:46 | [Paradise.Hexa.NET.ImNodes](https://www.nuget.org/packages/Paradise.Hexa.NET.ImNodes) | 3.1.0 | Juna Meinhold | A .NET wrapper for the ImNodes library. (0.5.0 / commit c9bb8e9) (for ImGui 1.9… |
| 2026-09-27 08:48:47 | [Paradise.Hexa.NET.ImGui.Backends.GLFW](https://www.nuget.org/packages/Paradise.Hexa.NET.ImGui.Backends.GLFW) | 3.1.0 | Juna Meinhold | A .NET wrapper for the Dear ImGui (1.92.9b) library backend GLFW. |
| 2026-09-27 08:48:48 | [Paradise.Hexa.NET.ImGui.Backends.SDL2](https://www.nuget.org/packages/Paradise.Hexa.NET.ImGui.Backends.SDL2) | 3.1.0 | Juna Meinhold | A .NET wrapper for the Dear ImGui (1.92.9b) library backend SDL2. |
| 2026-09-27 08:48:50 | [Paradise.Hexa.NET.ImPlot3D](https://www.nuget.org/packages/Paradise.Hexa.NET.ImPlot3D) | 3.1.0 | Juna Meinhold | A .NET wrapper for the ImPlot3D library. (0.4 / commit 41ae3e4) (for ImGui 1.92… |
| 2026-09-27 08:48:51 | [Paradise.Hexa.NET.ImPlot](https://www.nuget.org/packages/Paradise.Hexa.NET.ImPlot) | 3.1.0 | Juna Meinhold | A .NET wrapper for the ImPlot library. (1.1 WIP / commit 1351ab2) (for ImGui 1.… |
| 2026-09-27 08:48:52 | [Paradise.Hexa.NET.ImGui.Backends](https://www.nuget.org/packages/Paradise.Hexa.NET.ImGui.Backends) | 3.1.0 | Juna Meinhold | A .NET wrapper for the Dear ImGui (1.92.9b) library backends (Win32, Vulkan, Op… |
| 2026-09-27 08:48:53 | [Paradise.Hexa.NET.ImGui.Backends.SDL3](https://www.nuget.org/packages/Paradise.Hexa.NET.ImGui.Backends.SDL3) | 3.1.0 | Juna Meinhold | A .NET wrapper for the Dear ImGui (1.92.9b) library backend SDL3. |
| 2026-09-27 08:56:23 | [Podargus.UI.WinForms](https://www.nuget.org/packages/Podargus.UI.WinForms) | 1.0.0 | Podargus | The official, all-in-one Podargus UI component suite. Stop importing piecemeal… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
