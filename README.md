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

## Latest list — 2026-11-21 06:19 UTC

New packages created between 2026-11-21 05:21 UTC and 2026-11-21 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T06-19-11-571613Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 05:25:42 | [Moonwell.Stats](https://www.nuget.org/packages/Moonwell.Stats) | 0.21.0 | mdlsvensson | The effects of Moonwell's ready-made stats: crit, hit chance, evasion, parry, b… |
| 2026-11-21 05:39:10 | [SkyRender.Wpf](https://www.nuget.org/packages/SkyRender.Wpf) | 4.0.0 | Piranha91, Synthesis Collecti… | WPF view host for SkyRender: a paced live view (native child window, or a share… |
| 2026-11-21 05:43:03 | [NonBoxingUnions.Generator](https://www.nuget.org/packages/NonBoxingUnions.Generator) | 1.0.0 | Nathan Davis | A source generator for creating non-boxing unions |
| 2026-11-21 05:45:20 | [Hubtech](https://www.nuget.org/packages/Hubtech) | 1.0.0 | Hub Tech — medical website re… | Hub Tech medical website redesign Pakistan constants. Official: https://hubtech… |
| 2026-11-21 05:48:14 | [VirtoCommerce.AuditLog.Data.Search](https://www.nuget.org/packages/VirtoCommerce.AuditLog.Data.Search) | 3.1005.0 | VirtoCommerce.AuditLog.Data.S… | Package Description |
| 2026-11-21 05:54:04 | [CodeWF.Avalonia.Markdown.Core](https://www.nuget.org/packages/CodeWF.Avalonia.Markdown.Core) | 12.1.6.9 | Vex Contributors | Markdown 块编辑核心：块模型与编辑操作（拆块/合并/空文档首块），零 UI 依赖。Block editing core for the markdow… |
| 2026-11-21 05:57:45 | [Arcodiant.Empyrean.Dev](https://www.nuget.org/packages/Arcodiant.Empyrean.Dev) | 0.133.1 | Arcodiant/Andrew Armstrong | Development tools for a windowed Empyrean game: a run shell that loads a named… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
