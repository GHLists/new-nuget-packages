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

## Latest list — 2026-11-13 06:20 UTC

New packages created between 2026-11-13 05:21 UTC and 2026-11-13 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T06-20-40-684059Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 05:23:54 | [GraphitiNet.PostgreSql](https://www.nuget.org/packages/GraphitiNet.PostgreSql) | 0.1.0 | graphiti-net contributors | PostgreSQL storage for graphiti-net through EF Core, with pgvector for vector s… |
| 2026-11-13 05:23:54 | [GraphitiNet](https://www.nuget.org/packages/GraphitiNet) | 0.1.0 | graphiti-net contributors | Temporal knowledge graphs for AI agents in .NET: an independent C# rewrite of G… |
| 2026-11-13 05:23:55 | [GraphitiNet.SqlServer](https://www.nuget.org/packages/GraphitiNet.SqlServer) | 0.1.0 | graphiti-net contributors | SQL Server 2025 and Azure SQL storage for graphiti-net through EF Core, with th… |
| 2026-11-13 05:42:13 | [Arcodiant.Vulkan](https://www.nuget.org/packages/Arcodiant.Vulkan) | 0.2.1 | Arcodiant/Andrew Armstrong | A thin, hand-extended C# binding for Vulkan 1.3 and GLFW 3.4, with the GLFW nat… |
| 2026-11-13 05:48:13 | [Arcodiant.Empyrean](https://www.nuget.org/packages/Arcodiant.Empyrean) | 0.125.0 | Arcodiant/Andrew Armstrong | Core of the Empyrean C# game engine: scene-scoped ECS, game loop, time, content… |
| 2026-11-13 05:48:15 | [Arcodiant.Empyrean.Animation](https://www.nuget.org/packages/Arcodiant.Empyrean.Animation) | 0.125.0 | Arcodiant/Andrew Armstrong | Skeletal animation for the Empyrean engine: play clips on rigged glTF character… |
| 2026-11-13 05:48:17 | [Arcodiant.Empyrean.Audio](https://www.nuget.org/packages/Arcodiant.Empyrean.Audio) | 0.125.0 | Arcodiant/Andrew Armstrong | Audio abstraction for the Empyrean engine: mixer, buses, voice priority, SFX, m… |
| 2026-11-13 05:48:19 | [Arcodiant.Empyrean.Audio.OpenAL](https://www.nuget.org/packages/Arcodiant.Empyrean.Audio.OpenAL) | 0.125.0 | Arcodiant/Andrew Armstrong | OpenAL output backend for the Empyrean engine audio abstraction. |
| 2026-11-13 05:48:21 | [Arcodiant.Empyrean.Audio.Vorbis](https://www.nuget.org/packages/Arcodiant.Empyrean.Audio.Vorbis) | 0.125.0 | Arcodiant/Andrew Armstrong | Ogg Vorbis decoder for the Empyrean engine audio abstraction. |
| 2026-11-13 05:48:23 | [Arcodiant.Empyrean.Diagnostics](https://www.nuget.org/packages/Arcodiant.Empyrean.Diagnostics) | 0.125.0 | Arcodiant/Andrew Armstrong | Metrics and a debug HUD for the Empyrean game engine. |
| 2026-11-13 05:48:26 | [Arcodiant.Empyrean.Geometry](https://www.nuget.org/packages/Arcodiant.Empyrean.Geometry) | 0.125.0 | Arcodiant/Andrew Armstrong | CPU mesh geometry for the Empyrean engine: vertex layout, glTF and OBJ parsing,… |
| 2026-11-13 05:48:28 | [Arcodiant.Empyrean.Graphics](https://www.nuget.org/packages/Arcodiant.Empyrean.Graphics) | 0.125.0 | Arcodiant/Andrew Armstrong | Vulkan rendering for the Empyrean engine: window, cameras, meshes, sprites, lig… |
| 2026-11-13 05:48:30 | [Arcodiant.Empyrean.Hosting](https://www.nuget.org/packages/Arcodiant.Empyrean.Hosting) | 0.125.0 | Arcodiant/Andrew Armstrong | Standard host for the Empyrean engine: EmpyreanHostBuilder, configuration, depe… |
| 2026-11-13 05:48:33 | [Arcodiant.Empyrean.Hosting.Glfw](https://www.nuget.org/packages/Arcodiant.Empyrean.Hosting.Glfw) | 0.125.0 | Arcodiant/Andrew Armstrong | Game host for the Empyrean engine: composes the GLFW window, Vulkan renderer an… |
| 2026-11-13 05:48:37 | [Arcodiant.Empyrean.Input](https://www.nuget.org/packages/Arcodiant.Empyrean.Input) | 0.125.0 | Arcodiant/Andrew Armstrong | Input abstraction for the Empyrean engine: actions, axes, gestures and input mo… |
| 2026-11-13 05:48:40 | [Arcodiant.Empyrean.Input.Glfw](https://www.nuget.org/packages/Arcodiant.Empyrean.Input.Glfw) | 0.125.0 | Arcodiant/Andrew Armstrong | GLFW input backend for the Empyrean engine input abstraction. |
| 2026-11-13 05:48:43 | [Arcodiant.Empyrean.Navigation](https://www.nuget.org/packages/Arcodiant.Empyrean.Navigation) | 0.125.0 | Arcodiant/Andrew Armstrong | Navigation for the Empyrean engine: navmesh baking, agent steering and doorway… |
| 2026-11-13 05:48:47 | [Arcodiant.Empyrean.Physics](https://www.nuget.org/packages/Arcodiant.Empyrean.Physics) | 0.125.0 | Arcodiant/Andrew Armstrong | Physics query abstraction for the Empyrean engine: raycast, overlap and sweep o… |
| 2026-11-13 05:48:49 | [Arcodiant.Empyrean.Physics.Jolt](https://www.nuget.org/packages/Arcodiant.Empyrean.Physics.Jolt) | 0.125.0 | Arcodiant/Andrew Armstrong | Jolt Physics query backend for the Empyrean engine physics abstraction (win-x64… |
| 2026-11-13 05:48:52 | [Arcodiant.Empyrean.Ui](https://www.nuget.org/packages/Arcodiant.Empyrean.Ui) | 0.125.0 | Arcodiant/Andrew Armstrong | Retained and immediate-mode UI for the Empyrean engine: panels, labels, buttons… |
| 2026-11-13 05:48:54 | [Arcodiant.Empyrean.Ui.Handlers](https://www.nuget.org/packages/Arcodiant.Empyrean.Ui.Handlers) | 0.125.0 | Arcodiant/Andrew Armstrong | Opt-in built-in UI action handlers for the Empyrean engine: open and close scre… |
| 2026-11-13 05:48:58 | [Arcodiant.Empyrean.Xr](https://www.nuget.org/packages/Arcodiant.Empyrean.Xr) | 0.125.0 | Arcodiant/Andrew Armstrong | XR (VR) runtime seam for the Empyrean engine: per-eye presentation, head and co… |
| 2026-11-13 05:49:00 | [Arcodiant.Empyrean.Xr.OpenXr](https://www.nuget.org/packages/Arcodiant.Empyrean.Xr.OpenXr) | 0.125.0 | Arcodiant/Andrew Armstrong | OpenXR backend for the Empyrean engine XR runtime seam, with the Khronos loader… |
| 2026-11-13 06:03:07 | [SpaceCG.Standard.LedRenderer](https://www.nuget.org/packages/SpaceCG.Standard.LedRenderer) | 1.1.0 | huangmin@spacecg.cn | Led灯带渲染 |
| 2026-11-13 06:03:25 | [SpaceCG.Standard.LedRenderer.Wpf](https://www.nuget.org/packages/SpaceCG.Standard.LedRenderer.Wpf) | 1.0.0 | SpaceCG.Standard.LedRenderer.… | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
