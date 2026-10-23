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

## Latest list — 2026-10-23 12:20 UTC

New packages created between 2026-10-23 11:20 UTC and 2026-10-23 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T12-20-13-220548Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 11:24:02 | [Codai](https://www.nuget.org/packages/Codai) | 2.0.0 | Codai contributors | Run Codai from anywhere with `dotnet tool install --global Codai`, or grab a se… |
| 2026-10-23 11:24:03 | [Codai.Adapters](https://www.nuget.org/packages/Codai.Adapters) | 2.0.0 | Codai contributors | Codai integrations for configuration, providers, tools, analysis, pricing, stor… |
| 2026-10-23 11:24:04 | [Codai.Application](https://www.nuget.org/packages/Codai.Application) | 2.0.0 | Codai contributors | Host-neutral application runtime shared by the Codai CLI, VS Code integration,… |
| 2026-10-23 11:24:06 | [Codai.Core](https://www.nuget.org/packages/Codai.Core) | 2.0.0 | Codai contributors | Domain types, abstractions and first-party services that every other Codai pack… |
| 2026-10-23 11:24:42 | [KirillMaster.QualityGates.Build](https://www.nuget.org/packages/KirillMaster.QualityGates.Build) | 0.1.0 | KirillMaster | Quality gates for modern .NET: warnings-as-errors, curated third-party analyzer… |
| 2026-10-23 11:24:43 | [KirillMaster.QualityGates.Architecture](https://www.nuget.org/packages/KirillMaster.QualityGates.Architecture) | 0.1.0 | KirillMaster | ArchUnitNET-based hexagonal layering test base with config-driven rules and rep… |
| 2026-10-23 11:36:21 | [Alexpivo394.Revit.Export](https://www.nuget.org/packages/Alexpivo394.Revit.Export) | 2027.1.0 | Alexpivo394 | UI-free Revit model export to RVT and NWC: detached opening, link handling, cle… |
| 2026-10-23 11:36:27 | [Alexpivo394.Revit.Export.Sources](https://www.nuget.org/packages/Alexpivo394.Revit.Export.Sources) | 1.0.0 | Alexpivo394 | Revit model sources without the Revit API: Revit Server REST tree, folder tree,… |
| 2026-10-23 11:41:58 | [Idora.NET](https://www.nuget.org/packages/Idora.NET) | 1.0.0 | Jake Seracino | Idora generates prefixed, time-ordered entity identifiers such as usr_01k2f9v8t… |
| 2026-10-23 11:44:44 | [RecursiveAI.OnePdf](https://www.nuget.org/packages/RecursiveAI.OnePdf) | 1.0.0 | Recursive AI, LLC | A pure-managed, read-only .NET PDF library with no dependencies beyond the base… |
| 2026-10-23 11:44:45 | [RecursiveAI.OnePdf.Fonts](https://www.nuget.org/packages/RecursiveAI.OnePdf.Fonts) | 1.0.0 | Recursive AI, LLC | Substitute fonts for OnePDF, for documents that use the standard 14 fonts witho… |
| 2026-10-23 11:46:16 | [Arc56.Generated.colauttilorenzo.Web3Service](https://www.nuget.org/packages/Arc56.Generated.colauttilorenzo.Web3Service) | 1.0.1.2026102310 | colauttilorenzo | Generated ARC-56 Algorand smart-contract clients for colauttilorenzo/Web3Servic… |
| 2026-10-23 11:46:53 | [Snail.Toolkit.Documents](https://www.nuget.org/packages/Snail.Toolkit.Documents) | 0.1.0 | orldev | Reads PDF, Word, Excel, PowerPoint, HTML, CSV, JSON, Markdown and text into one… |
| 2026-10-23 11:55:36 | [AssemblyMeta.AssemblyInfo](https://www.nuget.org/packages/AssemblyMeta.AssemblyInfo) | 1.0.0-preview | Skymly | 把 SDK 默认的 9 个程序集特性生成为 AssemblyMeta.Info 编译期常量。 |
| 2026-10-23 11:55:37 | [AssemblyMeta.Constants](https://www.nuget.org/packages/AssemblyMeta.Constants) | 1.0.0-preview | Skymly | 把 Constant 与 FileConstant MSBuild 项生成为 AssemblyMeta.Constants 强类型常量。 |
| 2026-10-23 11:55:37 | [Flatmate](https://www.nuget.org/packages/Flatmate) | 1.0.0 | Matt Gordon | Multi-tenancy for ASP.NET Core. Resolve a tenant for each request, inject it, a… |
| 2026-10-23 11:55:38 | [AssemblyMeta.Project](https://www.nuget.org/packages/AssemblyMeta.Project) | 1.0.0-preview | Skymly | 把 opt-in 的项目属性生成为 AssemblyMeta.Project 编译期常量。 |
| 2026-10-23 11:55:39 | [AssemblyMeta.Metadata](https://www.nuget.org/packages/AssemblyMeta.Metadata) | 1.0.0-preview | Skymly | 把 AssemblyMetadata 项生成为 AssemblyMeta.Metadata 编译期常量，不重复生成程序集特性。 |
| 2026-10-23 11:55:40 | [AssemblyMeta.Git](https://www.nuget.org/packages/AssemblyMeta.Git) | 1.0.0-preview | Skymly | 把 SourceLink 与 CI 环境中的 Git 信息生成为 AssemblyMeta.Git 编译期常量。 |
| 2026-10-23 11:55:41 | [Flatmate.EntityFrameworkCore](https://www.nuget.org/packages/Flatmate.EntityFrameworkCore) | 1.0.0 | Matt Gordon | Entity Framework Core query filters for Flatmate tenants. |
| 2026-10-23 11:55:41 | [AssemblyMeta.Resources](https://www.nuget.org/packages/AssemblyMeta.Resources) | 1.0.0-preview | Skymly | 把 EmbeddedResource 生成为 AssemblyMeta.Resources，提供 Text、GetBytes 与 GetStream。 |
| 2026-10-23 11:55:42 | [AssemblyMeta.Strings](https://www.nuget.org/packages/AssemblyMeta.Strings) | 1.0.0-preview | Skymly | 把中性 resx 生成为 AssemblyMeta.Strings 编译期字符串常量。 |
| 2026-10-23 11:55:44 | [AssemblyMeta](https://www.nuget.org/packages/AssemblyMeta) | 1.0.0-preview | Skymly | AssemblyMeta 元包，聚合 AssemblyInfo、Constants、Project、Metadata、Git、Resources 与 Stri… |
| 2026-10-23 12:11:45 | [Goo.Gestures](https://www.nuget.org/packages/Goo.Gestures) | 0.8.1 | Xaz | Shared gesture recognizers for Goo core input arbitration. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
