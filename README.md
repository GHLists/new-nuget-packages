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

## Latest list — 2026-11-09 12:20 UTC

New packages created between 2026-11-09 11:21 UTC and 2026-11-09 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T12-20-42-765455Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 11:49:46 | [PollySdk.Documents](https://www.nuget.org/packages/PollySdk.Documents) | 0.2.0 | Chengchao Zhu | Provider-neutral document processing and bounded native PDF and OpenXML structu… |
| 2026-11-09 11:49:47 | [PollySdk.Documents.Services](https://www.nuget.org/packages/PollySdk.Documents.Services) | 0.2.0 | Chengchao Zhu | Optional, explicitly configured PaddleOCR worker and ONLYOFFICE Docs conversion… |
| 2026-11-09 11:50:00 | [PollySdk.AgentFramework.Extensions.Knowledge.PostgreSql](https://www.nuget.org/packages/PollySdk.AgentFramework.Extensions.Knowledge.PostgreSql) | 0.2.0 | Chengchao Zhu | PostgreSQL full-text and pgvector search projection for Polly Knowledge. |
| 2026-11-09 11:50:01 | [PollySdk.WebUI](https://www.nuget.org/packages/PollySdk.WebUI) | 0.2.0 | Chengchao Zhu | Environment-neutral Polly WebUI static assets and standalone ASP.NET Core hosti… |
| 2026-11-09 11:50:02 | [PollySdk.AgentFramework.Extensions.Knowledge.Sqlite](https://www.nuget.org/packages/PollySdk.AgentFramework.Extensions.Knowledge.Sqlite) | 0.2.0 | Chengchao Zhu | SQLite FTS5 search projection for Polly Knowledge. |
| 2026-11-09 12:02:48 | [LHFD.CleanArch.Infrastructure.Sdk](https://www.nuget.org/packages/LHFD.CleanArch.Infrastructure.Sdk) | 1.0.4 | Lucas Henrique Faria de Deus | SDK completo de Arquitetura Limpa contendo Domínio Base, Repositório Genérico e… |
| 2026-11-09 12:07:09 | [Lowline.Extensions.AI](https://www.nuget.org/packages/Lowline.Extensions.AI) | 0.12.0 | iyulab | The Lowline engine's model over a Microsoft.Extensions.AI chat client: filling… |
| 2026-11-09 12:09:38 | [RuneForBlazor.Charts](https://www.nuget.org/packages/RuneForBlazor.Charts) | 0.12.0 | kenconnet666 | Rune.UI 的图表：折线、面积、柱状、组合、散点、环形、雷达、漏斗、矩形树图、瀑布、桑基、弦图、网络图、时间线、地图，C# 输出 SVG。 |
| 2026-11-09 12:09:39 | [RuneForBlazor.Charts.Maps](https://www.nuget.org/packages/RuneForBlazor.Charts.Maps) | 0.12.0 | kenconnet666 | Rune.Charts 的 MapChart 用的地理数据：中国省份与世界各国（TopoJSON）。 |
| 2026-11-09 12:09:40 | [RuneForBlazor](https://www.nuget.org/packages/RuneForBlazor) | 0.12.0 | kenconnet666 | Blazor 组件库底座：信号式的响应式状态（[State] 生成器）、可逐层覆盖的属性合并、强类型的运行时样式与主题。 |
| 2026-11-09 12:09:41 | [RuneForBlazor.UI](https://www.nuget.org/packages/RuneForBlazor.UI) | 0.12.0 | kenconnet666 | 基于 Rune 的 Blazor 组件库：主题与 tokens、组件默认值与按部件的样式定制、组件。 |
| 2026-11-09 12:09:42 | [RuneForBlazor.Icons](https://www.nuget.org/packages/RuneForBlazor.Icons) | 0.12.0 | kenconnet666 | Rune.UI 的 Lucide 图标全集：Lucide.Plus 等强类型静态属性，配合 Icon 组件使用；发布到 WebAssembly 时自动裁剪未用… |
| 2026-11-09 12:09:43 | [RuneForBlazor.UI.Area](https://www.nuget.org/packages/RuneForBlazor.UI.Area) | 0.12.0 | kenconnet666 | Rune.UI 的省市区数据：按 6 位代码的省、市、区县，给 Cascader、TreeSelect 做地址选择。 |
| 2026-11-09 12:09:44 | [RuneForBlazor.UI.Dates](https://www.nuget.org/packages/RuneForBlazor.UI.Dates) | 0.12.0 | kenconnet666 | Rune.UI 的日期组件：DateField、TimeField、Calendar、DatePicker、DateRangePicker、RelativeT… |
| 2026-11-09 12:12:49 | [Nova.API](https://www.nuget.org/packages/Nova.API) | 0.5.0 | Soan | API publique des plugins Nova pour le serveur dedie Unturned (U3DS) : INovaPlug… |
| 2026-11-09 12:12:50 | [Nova.Sdk](https://www.nuget.org/packages/Nova.Sdk) | 0.5.0 | Soan | SDK MSBuild des plugins Nova pour Unturned : Nova.API, generateurs de commandes… |
| 2026-11-09 12:12:51 | [Nova.Templates](https://www.nuget.org/packages/Nova.Templates) | 0.5.0 | Soan | Modeles dotnet new pour les plugins Nova (Unturned) : dotnet new nova-plugin. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
