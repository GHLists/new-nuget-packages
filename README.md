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

## Latest list — 2026-09-28 17:22 UTC

New packages created between 2026-09-28 16:19 UTC and 2026-09-28 17:22 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T17-22-30-163726Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 16:23:08 | [MDD4All.DME.Views](https://www.nuget.org/packages/MDD4All.DME.Views) | 2.0.0.1 | Dr. Oliver Alt, mDuckLab | The Blazor components of MDD4All.DME, the object graph editor: a card per objec… |
| 2026-09-28 16:32:29 | [CasCap.Common.AI.Evaluation](https://www.nuget.org/packages/CasCap.Common.AI.Evaluation) | 4.14.3 | Alex Vincent | Evaluation harness for Microsoft Agent Framework agents built with CasCap.Commo… |
| 2026-09-28 16:32:40 | [EdoardoTona.Rustino](https://www.nuget.org/packages/EdoardoTona.Rustino) | 0.4.1 | Edoardo Tona | Cross-platform native webview windows powered by Rust (wry/tao). Drop-in replac… |
| 2026-09-28 16:32:41 | [EdoardoTona.Rustino.Blazor](https://www.nuget.org/packages/EdoardoTona.Rustino.Blazor) | 0.4.1 | Edoardo Tona | Blazor Hybrid for Rustino.NET: host Razor components in a native Rustino window… |
| 2026-09-28 16:32:42 | [EdoardoTona.Rustino.Reactive](https://www.nuget.org/packages/EdoardoTona.Rustino.Reactive) | 0.4.1 | Edoardo Tona | System.Reactive extensions for Rustino.NET window events. |
| 2026-09-28 16:52:09 | [Eryri.FileDistributedCache](https://www.nuget.org/packages/Eryri.FileDistributedCache) | 1.0.0 | Osian Linton | Local filesystem-backed IDistributedCache and IBufferedDistributedCache for sin… |
| 2026-09-28 17:02:53 | [MESCIUS.ActiveReports.AI.Web](https://www.nuget.org/packages/MESCIUS.ActiveReports.AI.Web) | 20.2.1 | MESCIUS inc. | ActiveReports AI Web provides ASP.NET Core middleware that integrates AI-powere… |
| 2026-09-28 17:03:36 | [MESCIUS.ActiveReports.Design.AI.Reporting](https://www.nuget.org/packages/MESCIUS.ActiveReports.Design.AI.Reporting) | 20.2.0 | MESCIUS inc. | ActiveReports is a set of assemblies that enable you to create, render, print,… |
| 2026-09-28 17:08:49 | [QueryCache.Core](https://www.nuget.org/packages/QueryCache.Core) | 0.1.0 | Gabriel Matte | Async query-result cache primitives (in-process LRU or any HybridCache, per-ite… |
| 2026-09-28 17:08:49 | [QueryCache.Dapper](https://www.nuget.org/packages/QueryCache.Dapper) | 0.1.0 | Gabriel Matte | Cache Dapper query results in-process or in any HybridCache, keyed by SQL text,… |
| 2026-09-28 17:08:50 | [QueryCache.EFCore](https://www.nuget.org/packages/QueryCache.EFCore) | 0.1.0 | Gabriel Matte | Cache Entity Framework Core query results in-process or in any HybridCache, wit… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
