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

## Latest list — 2026-11-09 13:21 UTC

New packages created between 2026-11-09 12:20 UTC and 2026-11-09 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T13-21-32-185692Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 12:23:30 | [AngleSharp.Browser](https://www.nuget.org/packages/AngleSharp.Browser) | 0.1.0 | AngleSharp | A UI-agnostic browser engine bringing the AngleSharp ecosystem together. |
| 2026-11-09 12:23:32 | [AngleSharp.Browser.Avalonia](https://www.nuget.org/packages/AngleSharp.Browser.Avalonia) | 0.1.0 | AngleSharp | An Avalonia control displaying web pages with AngleSharp.Browser. |
| 2026-11-09 12:38:15 | [OsuSv](https://www.nuget.org/packages/OsuSv) | 0.1.0 | lEttEr93 | osu! mania 谱面的变速（SV）评估：把滚动速度变化拆成不等时、极端度、背谱度、不适度、夸张度几个独立的量，不合成单一分数。输入是 .osu 文本，纯… |
| 2026-11-09 12:38:17 | [OsuSv.Cli](https://www.nuget.org/packages/OsuSv.Cli) | 0.1.0 | lEttEr93 | osu-sv 命令行：算 osu! mania 谱面的 SV 评估量（osu-sv compute chart.osu --json）。 |
| 2026-11-09 12:40:12 | [Bintiny.Umbraco](https://www.nuget.org/packages/Bintiny.Umbraco) | 0.1.0 | B. Gunnarsson | Compresses images with bintiny as Umbraco saves them. |
| 2026-11-09 12:59:08 | [PosInformatique.Foundations.EntityFramework.Converters](https://www.nuget.org/packages/PosInformatique.Foundations.EntityFramework.Converters) | 1.4.0 | Gilles TOURREAU | Provides a collection of basic Entity Framework Core value converters, includin… |
| 2026-11-09 13:00:17 | [Inceptus.DiagramEngine.Bpmn](https://www.nuget.org/packages/Inceptus.DiagramEngine.Bpmn) | 1.0.0 | Robert Prokopczuk | BPMN notation semantics, commands, validation, and plugin contributions for the… |
| 2026-11-09 13:00:19 | [Inceptus.DiagramEngine.Bpmn.Blazor](https://www.nuget.org/packages/Inceptus.DiagramEngine.Bpmn.Blazor) | 1.0.0 | Robert Prokopczuk | BPMN modeler components and browser presentation integration for the Inceptus D… |
| 2026-11-09 13:00:20 | [Inceptus.DiagramEngine.Canvas2D](https://www.nuget.org/packages/Inceptus.DiagramEngine.Canvas2D) | 1.0.0 | Robert Prokopczuk | Canvas2D browser editing session, interaction, scene, and renderer integration… |
| 2026-11-09 13:00:20 | [Universal.Databricks.Client](https://www.nuget.org/packages/Universal.Databricks.Client) | 1.0.0 | Andrew Ong | .NET client for the Databricks Unity Gateway: unified Chat Completions and Resp… |
| 2026-11-09 13:00:21 | [Inceptus.DiagramEngine.Contracts](https://www.nuget.org/packages/Inceptus.DiagramEngine.Contracts) | 1.0.0 | Robert Prokopczuk | Immutable contracts and extension APIs for the Inceptus Diagram Engine. |
| 2026-11-09 13:00:22 | [Inceptus.DiagramEngine.Organizational](https://www.nuget.org/packages/Inceptus.DiagramEngine.Organizational) | 1.0.0 | Robert Prokopczuk | Organizational Profile semantics and plugin contributions for the Inceptus Diag… |
| 2026-11-09 13:00:24 | [Inceptus.DiagramEngine.Runtime](https://www.nuget.org/packages/Inceptus.DiagramEngine.Runtime) | 1.0.0 | Robert Prokopczuk | Headless document, command, history, projection, layout, routing, validation, a… |
| 2026-11-09 13:04:22 | [OpenSoundControl.Core](https://www.nuget.org/packages/OpenSoundControl.Core) | 0.1.0-dev2 | Agash | Open Sound Control for .NET: OSC 1.0 and 1.1 codec (messages, bundles, time tag… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
