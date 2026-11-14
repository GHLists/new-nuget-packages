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

## Latest list — 2026-11-14 15:20 UTC

New packages created between 2026-11-14 14:19 UTC and 2026-11-14 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T15-20-07-926868Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 14:33:50 | [SwiftDispatch.Contracts](https://www.nuget.org/packages/SwiftDispatch.Contracts) | 1.0.0 | Kamyab Valipour | Contracts for SwiftDispatch requests, pipelines, and notifications. |
| 2026-11-14 14:33:50 | [SwiftDispatch](https://www.nuget.org/packages/SwiftDispatch) | 1.0.0 | Kamyab Valipour | A free, source-generated, Native AOT-friendly mediator with ordered pipelines a… |
| 2026-11-14 14:46:41 | [Helix.Templates](https://www.nuget.org/packages/Helix.Templates) | 0.4.0 | arflisch | Project templates for Helix UI: a Blazor WebAssembly app and a WPF app with the… |
| 2026-11-14 14:46:42 | [Helix.Export](https://www.nuget.org/packages/Helix.Export) | 0.4.0 | arflisch | Excel (.xlsx), Word (.docx) and CSV files from your lists in a few lines: typed… |
| 2026-11-14 14:46:44 | [Helix.Avalonia](https://www.nuget.org/packages/Helix.Avalonia) | 0.4.0 | arflisch | Clean, modern Avalonia controls where every visual part is a property: buttons,… |
| 2026-11-14 14:46:53 | [Tempo.Blazor.AI](https://www.nuget.org/packages/Tempo.Blazor.AI) | 2.11.0 | ptyll | AI conversation components for Tempo.Blazor: a safe Markdig markdown view, mess… |
| 2026-11-14 14:47:08 | [Tempo.Blazor.EmailTemplates.Engine](https://www.nuget.org/packages/Tempo.Blazor.EmailTemplates.Engine) | 2.11.0 | ptyll | Local render engine for the Tempo.Blazor email template editor: the sandboxed S… |
| 2026-11-14 14:47:16 | [Tempo.Blazor.Modeling.BpmnXml](https://www.nuget.org/packages/Tempo.Blazor.Modeling.BpmnXml) | 2.11.0 | ptyll | Headless BPMN 2.0 XML converter for Tempo.Blazor Modeling: deterministic, loss-… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
