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

## Latest list — 2026-11-03 05:19 UTC

New packages created between 2026-11-03 04:20 UTC and 2026-11-03 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T05-19-07-16881Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 04:26:41 | [NewLife.Office.Cli](https://www.nuget.org/packages/NewLife.Office.Cli) | 1.5.2026.1103-beta0… | 新生命开发团队 | NewLife.Office 命令行工具（office）：办公文档转 Markdown、结构快照、锚点补丁与 MCP 服务端，供 AI/Agent 直接调用 |
| 2026-11-03 04:32:11 | [Enlitt](https://www.nuget.org/packages/Enlitt) | 0.1.0 | Enlitt | Enlitt SDK for .NET: sessions, standard and premium model accounting, usage, an… |
| 2026-11-03 04:32:12 | [Enlitt.AspNetCore](https://www.nuget.org/packages/Enlitt.AspNetCore) | 0.1.0 | Enlitt | ASP.NET Core bindings for the Enlitt SDK: session middleware and sign-in endpoi… |
| 2026-11-03 04:32:13 | [Enlitt.Extensions.AI](https://www.nuget.org/packages/Enlitt.Extensions.AI) | 0.1.0 | Enlitt | Microsoft.Extensions.AI IChatClient adapter for Enlitt standard and premium mod… |
| 2026-11-03 04:52:00 | [GodotXaml.Cli](https://www.nuget.org/packages/GodotXaml.Cli) | 0.1.0 | Leftos Aslanoglou | Checks, converts and formats Godot scenes and resources written as XAML. |
| 2026-11-03 04:52:01 | [GodotXaml.Core](https://www.nuget.org/packages/GodotXaml.Core) | 0.1.0 | Leftos Aslanoglou | The godot-xaml core for reading and writing .xscn and .xres, and converting God… |
| 2026-11-03 05:04:42 | [OODD.CrossPrint.Core](https://www.nuget.org/packages/OODD.CrossPrint.Core) | 1.0.0 | OODD CrossPrint Contributors | CrossPrint 模板模型、单位换算与 JSON 序列化（无 UI 依赖）。 |
| 2026-11-03 05:04:43 | [OODD.CrossPrint.Designer](https://www.nuget.org/packages/OODD.CrossPrint.Designer) | 1.0.0 | OODD CrossPrint Contributors | CrossPrint 设计器内核：视口、命中测试、交互状态机、命令、属性描述符与叠加层绘制。不引用任何宿主 UI 框架。 |
| 2026-11-03 05:04:45 | [OODD.CrossPrint.Engine](https://www.nuget.org/packages/OODD.CrossPrint.Engine) | 1.0.0 | OODD CrossPrint Contributors | CrossPrint 渲染引擎：SkiaSharp 元素渲染、PDF/PNG 导出、数据绑定。无 UI 框架依赖。 |
| 2026-11-03 05:04:46 | [OODD.CrossPrint.Hosts.Avalonia](https://www.nuget.org/packages/OODD.CrossPrint.Hosts.Avalonia) | 1.0.0 | OODD CrossPrint Contributors | Package Description |
| 2026-11-03 05:04:47 | [OODD.CrossPrint.Hosts.Eto](https://www.nuget.org/packages/OODD.CrossPrint.Hosts.Eto) | 1.0.0 | OODD CrossPrint Contributors | CrossPrint Eto.Forms 宿主适配层：DesignerControl（设计画布）与 PreviewControl（打印预览），共用同一渲染路径。 |
| 2026-11-03 05:04:48 | [OODD.CrossPrint.Hosts.Uno](https://www.nuget.org/packages/OODD.CrossPrint.Hosts.Uno) | 1.0.0 | OODD CrossPrint Contributors | CrossPrint Uno Platform 宿主适配层：DesignerControl（设计画布）与 PreviewControl（打印预览），共用同一渲… |
| 2026-11-03 05:04:49 | [OODD.CrossPrint.Hosts.WinForms](https://www.nuget.org/packages/OODD.CrossPrint.Hosts.WinForms) | 1.0.0 | OODD CrossPrint Contributors | CrossPrint WinForms 宿主适配层：DesignerControl（设计画布）与 PreviewControl（打印预览），共用同一渲染路径。 |
| 2026-11-03 05:04:50 | [OODD.CrossPrint.Hosts.WinUi](https://www.nuget.org/packages/OODD.CrossPrint.Hosts.WinUi) | 1.0.0 | OODD CrossPrint Contributors | CrossPrint WinUI 3 宿主适配层：DesignerControl（设计画布）与 PreviewControl（打印预览），共用同一渲染路径。 |
| 2026-11-03 05:04:51 | [OODD.CrossPrint.Hosts.Wpf](https://www.nuget.org/packages/OODD.CrossPrint.Hosts.Wpf) | 1.0.0 | OODD CrossPrint Contributors | CrossPrint WPF 宿主适配层：DesignerControl（设计画布）与 PreviewControl（打印预览），共用同一渲染路径。 |
| 2026-11-03 05:04:53 | [OODD.CrossPrint.Printing](https://www.nuget.org/packages/OODD.CrossPrint.Printing) | 1.0.0 | OODD CrossPrint Contributors | CrossPrint 打印目标抽象层：把渲染引擎的产物送出去的统一出口。v0.1 提供 PdfFilePrintTarget（PDF 落盘，FR-PRT-01… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
