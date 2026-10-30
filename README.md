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

## Latest list — 2026-10-30 03:19 UTC

New packages created between 2026-10-30 02:20 UTC and 2026-10-30 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T03-19-33-81706Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 02:21:00 | [LocalSharp](https://www.nuget.org/packages/LocalSharp) | 0.1.1 | Michael Smith | A .NET client for local LLM servers (LM Studio, Ollama, llama.cpp, vLLM), built… |
| 2026-10-30 02:23:15 | [MiniTui](https://www.nuget.org/packages/MiniTui) | 1.0.0 | Discover Edge LLC | A minimal, immediate-mode TUI framework for .NET inspired by ratatui |
| 2026-10-30 02:43:37 | [OODD.Charts.Adapters.Avalonia](https://www.nuget.org/packages/OODD.Charts.Adapters.Avalonia) | 1.0.0 | OODD | Avalonia 宿主适配器：Raster/SKPicture 到 WriteableBitmap 的像素桥 + ChartControl。 |
| 2026-10-30 02:43:51 | [OODD.Charts.Adapters.Eto](https://www.nuget.org/packages/OODD.Charts.Adapters.Eto) | 1.0.0 | OODD | Eto.Forms 宿主适配器：Raster/SKPicture 到 Eto.Drawing.Bitmap 的像素桥 + ChartControl（Drawa… |
| 2026-10-30 02:44:05 | [OODD.Charts.Adapters.Maui](https://www.nuget.org/packages/OODD.Charts.Adapters.Maui) | 1.0.0 | OODD | MAUI 宿主适配器：Chart/Raster 到 ImageSource 的编码桥 + ChartImage、ChartCanvasView。 |
| 2026-10-30 02:44:18 | [OODD.Charts.Adapters.Uno](https://www.nuget.org/packages/OODD.Charts.Adapters.Uno) | 1.0.0 | OODD | Uno Platform 宿主适配器：Raster/SKPicture 到 Uno WinUI 契约 WriteableBitmap 的像素桥 + Chart… |
| 2026-10-30 02:44:33 | [OODD.Charts.Adapters.WinForms](https://www.nuget.org/packages/OODD.Charts.Adapters.WinForms) | 1.0.0 | OODD | WinForms 宿主适配器：Raster/SKPicture 到 GDI+ Bitmap 的像素桥 + ChartControl。 |
| 2026-10-30 02:44:44 | [OODD.Charts.Adapters.WinUi](https://www.nuget.org/packages/OODD.Charts.Adapters.WinUi) | 1.0.0 | OODD | WinUI 3 宿主适配器：Raster/SKPicture 到 Microsoft.UI.Xaml WriteableBitmap 的像素桥 + Chart… |
| 2026-10-30 02:44:54 | [OODD.Charts.Adapters.Wpf](https://www.nuget.org/packages/OODD.Charts.Adapters.Wpf) | 1.0.0 | OODD | WPF 宿主适配器：Raster/SKPicture 到 WriteableBitmap 的像素桥 + ChartControl。 |
| 2026-10-30 02:45:19 | [OODD.Charts.Core](https://www.nuget.org/packages/OODD.Charts.Core) | 1.0.0 | OODD | 跨平台刚性网格表单渲染引擎（SkiaSharp 内核）。不含任何 UI 框架依赖。 |
| 2026-10-30 02:45:31 | [OODD.Charts.Engineering](https://www.nuget.org/packages/OODD.Charts.Engineering) | 1.0.0 | OODD | 工程表单：测井成果图（多轨 + 倒置深度轴 + 图样道）、变压器油色谱大卫三角形（三角坐标 + 包线）。基于 OODD.Charts.Core 引擎。 |
| 2026-10-30 02:45:44 | [OODD.Charts.Geoscience](https://www.nuget.org/packages/OODD.Charts.Geoscience) | 1.0.0 | OODD | 地学与气象表单：地面/高空天气图（站点填图 + 风杆）、T-lnP 温度对数压力图（斜交网格 + 五族线）。基于 OODD.Charts.Core 引擎。 |
| 2026-10-30 02:45:55 | [OODD.Charts.Medical](https://www.nuget.org/packages/OODD.Charts.Medical) | 1.0.0 | OODD | 医疗表单：三测单（体温单）、产程图、疼痛评估、保护性约束巡视、输血反应，以及 19 张专科/事件/设备/科室运营记录单。基于 OODD.Charts.Core… |
| 2026-10-30 02:46:04 | [OODD.Charts.Radar](https://www.nuget.org/packages/OODD.Charts.Radar) | 1.0.0 | OODD | 雷达态势图（PPI）：360°/180° 盘面、量程环、方位线、扫描扇、目标与轨迹、可配置信息面板。基于 OODD.Charts.Core 引擎。 |
| 2026-10-30 02:46:15 | [OODD.Charts.Tickets](https://www.nuget.org/packages/OODD.Charts.Tickets) | 1.0.0 | OODD | 凭证家族：电气工作票（三联）、八类特殊作业票、增值税专用发票（多联 + 密码区 + 压印大写）。基于 OODD.Charts.Core 引擎。 |
| 2026-10-30 02:46:24 | [OODD.Charts.Transit](https://www.nuget.org/packages/OODD.Charts.Transit) | 1.0.0 | OODD | 交通运输表单：列车运行图、载重平衡与重心包线、集装箱积载图、危险货物联单、超限运输许可附图。基于 OODD.Charts.Core 引擎。 |
| 2026-10-30 02:47:33 | [NSail.Storage.Git](https://www.nuget.org/packages/NSail.Storage.Git) | 0.1.412 | Leonardo Porro,Emmanuel Arias | NSail.Storage.Git, part of NSail Stack: a .NET modular-monolith framework (mess… |
| 2026-10-30 02:48:56 | [FroxstReader](https://www.nuget.org/packages/FroxstReader) | 1.0.0 | Fr0xst | FroxstReader is a package used to read memory. |
| 2026-10-30 02:49:20 | [XiaoYou.Game.AI.Api](https://www.nuget.org/packages/XiaoYou.Game.AI.Api) | 1.0.0 | XiaoYou.Game.AI.Api | Package Description |
| 2026-10-30 02:53:45 | [C1.Blazor.ColorPicker](https://www.nuget.org/packages/C1.Blazor.ColorPicker) | 10.0.20262.62-beta | MESCIUS inc. | Using ComponentOne ColorPicker™ for Blazor, select colors from professionally-d… |
| 2026-10-30 02:53:51 | [C1.Blazor.Diagram](https://www.nuget.org/packages/C1.Blazor.Diagram) | 10.0.20262.62-beta | MESCIUS inc. | FlexChart is a Cartesian chart control. Supports line, area, scatter, bubble, c… |
| 2026-10-30 03:05:59 | [ResponseResultHandler.FluentValidation](https://www.nuget.org/packages/ResponseResultHandler.FluentValidation) | 15.0.0 | Yahya Erdogan | FluentValidation integration for ResponseResultHandler: turns validation result… |
| 2026-10-30 03:12:30 | [AIFunctionSetMatcher](https://www.nuget.org/packages/AIFunctionSetMatcher) | 1.0.0 | AIFunctionSetMatcher | MEAI 函数声明集合的语义匹配库。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
