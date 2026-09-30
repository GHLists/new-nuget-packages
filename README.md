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

## Latest list — 2026-09-30 20:20 UTC

New packages created between 2026-09-30 19:21 UTC and 2026-09-30 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T20-20-51-234116Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 19:25:16 | [NetPdf](https://www.nuget.org/packages/NetPdf) | 1.1.0 | Roland Aroche and NetPdf cont… | Convert HTML + CSS to PDF in pure C# / .NET 10 — no browser engine, no Chromium… |
| 2026-09-30 19:32:47 | [ZeroI18n](https://www.nuget.org/packages/ZeroI18n) | 1.0.0 | Summpot | High-performance, zero-overhead compile-time i18n source generator for .NET. Su… |
| 2026-09-30 19:35:42 | [UniFFISharp](https://www.nuget.org/packages/UniFFISharp) | 0.1.0 | Summpot | Zero-CLI, zero-boilerplate UniFFI binding generator and runtime for Rust + C# i… |
| 2026-09-30 19:39:42 | [Aluna.net](https://www.nuget.org/packages/Aluna.net) | 1.0.0 | Aluna Contributors | Aluna is a .NET event sourcing toolkit with abstractions, repositories, and eve… |
| 2026-09-30 19:41:05 | [DarkWS.Testing](https://www.nuget.org/packages/DarkWS.Testing) | 5.0.0 | Bobsans | Transportless handler testing for DarkWS |
| 2026-09-30 19:45:25 | [s0rent.Milsymbol.Cli](https://www.nuget.org/packages/s0rent.Milsymbol.Cli) | 0.1.1 | s0rent | Spatialillusions' milsymbol JS library repackaged as a CLI application |
| 2026-09-30 19:45:40 | [aicb-roslyn-mcp](https://www.nuget.org/packages/aicb-roslyn-mcp) | 0.5.465.11 | Gregor Dadera | Roslyn-based code intelligence for C#/.NET coding agents. This MCP server and c… |
| 2026-09-30 19:51:56 | [Natrix.Swr](https://www.nuget.org/packages/Natrix.Swr) | 0.14.1 | miroljub1995 | Stale-while-revalidate data fetching for Natrix — a port of React SWR built on… |
| 2026-09-30 20:03:33 | [Gulla.Optimizely.DdsExplorer](https://www.nuget.org/packages/Gulla.Optimizely.DdsExplorer) | 2.0.0 | Tomas Hensrud Gulla | Browse, inspect, edit and delete Dynamic Data Store stores and items from the S… |
| 2026-09-30 20:05:05 | [SkiaGameRendering.Core.D3D12](https://www.nuget.org/packages/SkiaGameRendering.Core.D3D12) | 0.17.1 | SkiaGameRendering.Core.D3D12 | Engine-agnostic D3D12/Skia interop shared by D3D12-based SkiaGameRendering back… |
| 2026-09-30 20:05:12 | [SkiaGameRendering.Stride.D3D12](https://www.nuget.org/packages/SkiaGameRendering.Stride.D3D12) | 0.17.1-beta | SkiaGameRendering.Stride.D3D12 | GPU SkiaSharp rendering into Stride Texture targets via Skia's Direct3D 12 back… |
| 2026-09-30 20:13:30 | [Componyx.Data](https://www.nuget.org/packages/Componyx.Data) | 1.0.0 | Componyx - E.H. Daanen | A lightweight, database-first ORM for .NET built directly on ADO.NET. Write que… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
