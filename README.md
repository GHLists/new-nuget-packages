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

## Latest list — 2026-10-12 04:19 UTC

New packages created between 2026-10-12 03:20 UTC and 2026-10-12 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T04-19-27-798788Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 03:44:10 | [VL.PRC](https://www.nuget.org/packages/VL.PRC) | 1.0.0-rc1 | Amir Bastan | Parametric Robot Control (PRC) for vvvv gamma. |
| 2026-10-12 03:50:09 | [NanoBus.Transports.Demo](https://www.nuget.org/packages/NanoBus.Transports.Demo) | 0.1.0 | Wayland Young | Lightweight, AOT-first demo/learning transport for NanoBus. |
| 2026-10-12 03:50:29 | [NanoBus.Transports.InMemory](https://www.nuget.org/packages/NanoBus.Transports.InMemory) | 0.1.0 | Wayland Young | Lightweight, AOT-first in-memory transport for NanoBus. |
| 2026-10-12 03:54:01 | [LibFuseSharp](https://www.nuget.org/packages/LibFuseSharp) | 1.0.0 | PureLogicCode.com | FUSE 3 high-level mount library for .NET on Linux (libfuse3) and macOS (macFUSE… |
| 2026-10-12 04:00:05 | [TCIS.Consul.Registration](https://www.nuget.org/packages/TCIS.Consul.Registration) | 1.0.2 | TCIS Core Community and Contr… | TCIS Core Framework is an application framework for building modular, multi-ten… |
| 2026-10-12 04:00:12 | [MainframeEngine](https://www.nuget.org/packages/MainframeEngine) | 1.1.1 | Mainframe Games | A modular C# game engine on Vulkan: Godot-style scene tree with source-generate… |
| 2026-10-12 04:00:13 | [MainframeEngine.Templates](https://www.nuget.org/packages/MainframeEngine.Templates) | 1.1.1 | Mainframe Games | dotnet new templates for Mainframe Engine games: mfgame (game library + GameHos… |
| 2026-10-12 04:07:04 | [SkiaExtensions](https://www.nuget.org/packages/SkiaExtensions) | 0.0.1 | machi_pon | Extensions for SkiaSharp. This is a placeholder release and contains no functio… |
| 2026-10-12 04:12:22 | [Kite.Abp](https://www.nuget.org/packages/Kite.Abp) | 2.2.0 | SpringLee | 基于.NET10 and Abp Vnext 10.x |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
