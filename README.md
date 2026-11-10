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

## Latest list — 2026-11-10 03:20 UTC

New packages created between 2026-11-10 02:20 UTC and 2026-11-10 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T03-20-10-725221Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 02:24:22 | [Meziantou.Framework.VectorGraphics](https://www.nuget.org/packages/Meziantou.Framework.VectorGraphics) | 1.0.0 | meziantou | Retained vector scene (shapes, paths, texts, groups, gradients), deterministic… |
| 2026-11-10 02:24:22 | [Meziantou.Framework.Imaging.VectorGraphics](https://www.nuget.org/packages/Meziantou.Framework.Imaging.VectorGraphics) | 1.0.0 | meziantou | Draws the scenes of Meziantou.Framework.VectorGraphics (charts, diagrams) with… |
| 2026-11-10 02:24:22 | [Meziantou.Framework.Mermaid](https://www.nuget.org/packages/Meziantou.Framework.Mermaid) | 1.0.0 | meziantou | Reads and writes the Mermaid text format: the 25 diagram types of Meziantou.Fra… |
| 2026-11-10 02:24:22 | [Meziantou.Framework.Diagrams](https://www.nuget.org/packages/Meziantou.Framework.Diagrams) | 1.0.0 | meziantou | Diagrams written as deterministic SVG, inspired by Mermaid: 25 diagram types of… |
| 2026-11-10 02:29:56 | [LiteDriver](https://www.nuget.org/packages/LiteDriver) | 0.1.0 | cnefan31 | 面向工业 SOCKET 设备的轻量 TCP 连接管理库：断线重连、运行时增改删设备与监听端点、可插拔帧编解码、显式命令结果语义，零 NuGet 依赖核心并支持… |
| 2026-11-10 02:29:57 | [LiteDriver.Hosting](https://www.nuget.org/packages/LiteDriver.Hosting) | 0.1.0 | cnefan31 | LiteDriver 的 .NET 通用主机集成：把驱动作为 IHostedService 托管，并从 DI 容器解析依赖。核心包保持零依赖。 |
| 2026-11-10 02:32:50 | [Plex.Core.Http](https://www.nuget.org/packages/Plex.Core.Http) | 1.0.0 | Manuel Saleta | Modern, lightweight, high-performance .NET HttpClient library for Plex Media Se… |
| 2026-11-10 02:32:52 | [RDCore.SDK](https://www.nuget.org/packages/RDCore.SDK) | 0.1.0-alpha | 9562-7303 Québec inc. | The RDCore language model and the plumbing every process and extension of the p… |
| 2026-11-10 02:34:41 | [NulliBehaviour](https://www.nuget.org/packages/NulliBehaviour) | 1.0.0 | NulliBehaviour | Package Description |
| 2026-11-10 02:47:58 | [Blasphemous.CheatConsoleExtended](https://www.nuget.org/packages/Blasphemous.CheatConsoleExtended) | 1.0.0 | NewbieElton | Mod for Blasphemous 1 that adds extended cheat console functionality |
| 2026-11-10 02:58:45 | [Sevencat.ImageFacade](https://www.nuget.org/packages/Sevencat.ImageFacade) | 0.1.0 | ImageFacade contributors | 与后端无关的图像处理门面：统一的加载/保存、Resize 六模式、绘制与中英文文字 API，换后端不换调用代码。本包是核心抽象，不含任何编解码或渲染依赖。 |
| 2026-11-10 02:58:50 | [Sevencat.ImageFacade.ImageSharp](https://www.nuget.org/packages/Sevencat.ImageFacade.ImageSharp) | 0.1.0 | ImageFacade contributors | ImageFacade 的 ImageSharp 3.x 后端：纯托管、格式全，适合服务端批处理。使用方需自行确认 Six Labors Split Lice… |
| 2026-11-10 02:58:56 | [Sevencat.ImageFacade.ImageSharp2](https://www.nuget.org/packages/Sevencat.ImageFacade.ImageSharp2) | 0.1.0 | ImageFacade contributors | ImageFacade 的 ImageSharp 2.x 后端：纯托管、格式全，适合服务端批处理。使用方需自行确认 Six Labors Split Lice… |
| 2026-11-10 02:59:01 | [Sevencat.ImageFacade.OpenCvSharp](https://www.nuget.org/packages/Sevencat.ImageFacade.OpenCvSharp) | 0.1.0 | ImageFacade contributors | ImageFacade 的 OpenCvSharp4 后端：BGRA Mat 直接进出，原生绘制；半透明形状与虚线不支持，文字用核心字形光栅化（含中文）。 |
| 2026-11-10 02:59:08 | [Sevencat.ImageFacade.OpenCvSharp5](https://www.nuget.org/packages/Sevencat.ImageFacade.OpenCvSharp5) | 0.1.0 | ImageFacade contributors | ImageFacade 的 OpenCvSharp5 后端：BGRA Mat 直接进出，原生绘制；半透明形状与虚线不支持，文字用核心字形光栅化（含中文）。 |
| 2026-11-10 02:59:14 | [Sevencat.ImageFacade.SdcbSimdCodecs](https://www.nuget.org/packages/Sevencat.ImageFacade.SdcbSimdCodecs) | 0.1.0 | ImageFacade contributors | ImageFacade 的纯托管后端：Sdcb.SimdCodecs 编解码 + 自绘渲染，无原生依赖、AOT 友好，输出确定。 |
| 2026-11-10 02:59:18 | [Sevencat.ImageFacade.SkiaSharp](https://www.nuget.org/packages/Sevencat.ImageFacade.SkiaSharp) | 0.1.0 | ImageFacade contributors | ImageFacade 的 SkiaSharp 4.x 后端：原生绘制、文字与 alpha 混合，视频帧叠加的首选后端。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
