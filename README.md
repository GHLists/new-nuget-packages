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

## Latest list — 2026-10-28 02:18 UTC

New packages created between 2026-10-28 01:20 UTC and 2026-10-28 02:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T02-18-56-756764Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 01:25:29 | [JBOpale.MathAdvanced](https://www.nuget.org/packages/JBOpale.MathAdvanced) | 2.0.0 | Jérôme FRANCOIS, JB-OPale Tea… | Ensemble de méthodes et de classes mathématiques |
| 2026-10-28 01:32:50 | [Dogvane.WeTextNet](https://www.nuget.org/packages/Dogvane.WeTextNet) | 0.1.8 | dogvane | Pure C# TN/ITN text normalization runtime for WeTextProcessing: loads the pre-b… |
| 2026-10-28 01:35:46 | [IronHive.Providers.Declarations](https://www.nuget.org/packages/IronHive.Providers.Declarations) | 0.73.0 | iyulab | IronHive provider declarations - an endpoint, a wire format, a credential place… |
| 2026-10-28 01:36:24 | [CleanLambdaFunction.Template](https://www.nuget.org/packages/CleanLambdaFunction.Template) | 2026.10.28.36 | Stephen Walsh | A template for an API using a streamlined version of Clean Architecture and .NE… |
| 2026-10-28 01:40:55 | [PaperSharp](https://www.nuget.org/packages/PaperSharp) | 1.0.1 | SpringHgui | 要出分页文档，不必再为它养一个浏览器：一行 Renderer.RenderPdf(html, css) 就在 .NET 进程内产出矢量 PDF —— 文字可选… |
| 2026-10-28 01:51:55 | [Fipc](https://www.nuget.org/packages/Fipc) | 1.0.0 | Hayden Donnelly | Shared-memory IPC for .NET: streams, broadcasts, work queues and services betwe… |
| 2026-10-28 02:05:14 | [DanfeSharp.Next](https://www.nuget.org/packages/DanfeSharp.Next) | 3.2.1 | Ricardo Brito,Allan Ferreira | Gerador em PDF do DANFE (NF-e), DANFE NFC-e, documentos de eventos (carta de co… |
| 2026-10-28 02:12:35 | [SignalHouseSms.Sdk](https://www.nuget.org/packages/SignalHouseSms.Sdk) | 1.5.1 | Signal House LLC | Official .NET SDK for the SignalHouse platform |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
