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

## Latest list — 2026-10-10 13:21 UTC

New packages created between 2026-10-10 12:19 UTC and 2026-10-10 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T13-21-33-148473Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 12:22:51 | [Kusachius.QueryMapper](https://www.nuget.org/packages/Kusachius.QueryMapper) | 1.4.1 | Aldis Arust | LINQ-style SQL query mapping extensions for Entity Framework Core and PostgreSQ… |
| 2026-10-10 12:25:14 | [CodeWF.Avalonia.Controls](https://www.nuget.org/packages/CodeWF.Avalonia.Controls) | 12.1.4 | 沙漠尽头的狼 | Avalonia 基础自定义控件库：控件 API、状态模型、绘制逻辑、标记扩展与转换器，内置 Semi 主题资源（引导、传输列表、状态徽标、标题栏等）。Cor… |
| 2026-10-10 12:25:15 | [CodeWF.Avalonia.DataGrid](https://www.nuget.org/packages/CodeWF.Avalonia.DataGrid) | 12.1.4 | 沙漠尽头的狼 | 官方 Avalonia DataGrid 的增强扩展：三态排序（升/降/取消）、自然排序比较器与智能 ToolTip，内置 Semi 主题入口。Enhance… |
| 2026-10-10 12:25:16 | [CodeWF.Avalonia.Dock](https://www.nuget.org/packages/CodeWF.Avalonia.Dock) | 12.1.4 | 沙漠尽头的狼 | 基于开源 Dock.Avalonia 的布局扩展控件与 Semi 风格主题：GridDock 布局适配、梯形页签与中英文本地化资源。Dock layout e… |
| 2026-10-10 12:25:18 | [CodeWF.Avalonia.Lang.Generator](https://www.nuget.org/packages/CodeWF.Avalonia.Lang.Generator) | 12.1.4 | 沙漠尽头的狼 | Avalonia 多语言方案的编译期源生成器：从语言资源生成强类型资源 Key。Compile-time source generator producing… |
| 2026-10-10 12:25:18 | [CodeWF.Avalonia.Lang](https://www.nuget.org/packages/CodeWF.Avalonia.Lang) | 12.1.4 | 沙漠尽头的狼 | Avalonia 插件化多语言方案：I18n 标记扩展、运行时切换文化、父文化回退，内置 Json/Xml/Resx 三种资源加载器，附强类型 Key 源生成… |
| 2026-10-10 12:25:20 | [CodeWF.Avalonia.Markdown](https://www.nuget.org/packages/CodeWF.Avalonia.Markdown) | 12.1.4 | 沙漠尽头的狼 | Markdown 完整包：在 Lite 渲染引擎之上提供图片（GIF/SVG/预览）、数学公式、Mermaid 图表、TextMate 代码高亮、PNG/PD… |
| 2026-10-10 12:25:21 | [CodeWF.Avalonia.Markdown.Lite](https://www.nuget.org/packages/CodeWF.Avalonia.Markdown.Lite) | 12.1.4 | 沙漠尽头的狼 | Markdown 渲染基础包：基于 Avalonia 与 Markdig 的解析渲染引擎，只渲染常规元素（标题/段落/列表/引用/表格/链接/代码块单色/图片… |
| 2026-10-10 12:25:25 | [CodeWF.Avalonia.TreeDataGrid](https://www.nuget.org/packages/CodeWF.Avalonia.TreeDataGrid) | 12.1.4 | 沙漠尽头的狼 | 社区版 TreeDataGrid.Avalonia 的增强扩展：三态排序（升/降/取消）、Ctrl+A 全选与智能 ToolTip，内置 Semi 主题（本地… |
| 2026-10-10 12:53:07 | [RAGToolkit.AI.Evaluation](https://www.nuget.org/packages/RAGToolkit.AI.Evaluation) | 0.1.0 | gimmick | Offline retrieval evaluation for RAG: Hit, Recall@K, Precision@K, MRR, nDCG@K a… |
| 2026-10-10 13:01:48 | [BringYourOwnAgent](https://www.nuget.org/packages/BringYourOwnAgent) | 0.0.2 | ultrathinker | Early draft reference implementation of BYOA (Bring Your Own Agent): manifest v… |
| 2026-10-10 13:03:31 | [LanDX.Templates](https://www.nuget.org/packages/LanDX.Templates) | 1.0.0 | LanDX | LanDX .NET project templates |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
