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

## Latest list — 2026-11-24 09:19 UTC

New packages created between 2026-11-24 08:19 UTC and 2026-11-24 09:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T09-19-33-801915Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 08:28:17 | [ZeroCSharp.SDL3](https://www.nuget.org/packages/ZeroCSharp.SDL3) | 0.11.0 | Zero C# contributors | SDL 3 for zero-mode C# programs: windows, 2D drawing, keyboard and mouse. Windo… |
| 2026-11-24 08:57:23 | [Polhem.Chat](https://www.nuget.org/packages/Polhem.Chat) | 0.1.0 | Polhem contributors | An observable conversation model for AI chat user interfaces: turns the streame… |
| 2026-11-24 08:57:25 | [Polhem.Chat.Avalonia](https://www.nuget.org/packages/Polhem.Chat.Avalonia) | 0.1.0 | Polhem contributors | An AI chat control for Avalonia: streamed replies rendered as Markdown, reasoni… |
| 2026-11-24 08:59:43 | [AutoSettingUI.Avalonia12](https://www.nuget.org/packages/AutoSettingUI.Avalonia12) | 2.0.0 | Sakuya Starry | Avalonia 12 UI implementation for AutoSettingUI |
| 2026-11-24 08:59:45 | [AutoSettingUI.DynamicLocalization](https://www.nuget.org/packages/AutoSettingUI.DynamicLocalization) | 2.0.0 | Sakuya Starry | Optional DynamicLocalization adapter for AutoSettingUI |
| 2026-11-24 09:07:56 | [Reglet.Validation](https://www.nuget.org/packages/Reglet.Validation) | 1.6.0 | Maik Rehder | Document validator for Reglet: checks DOCX, XLSX, ODF and PDF files for what Wo… |
| 2026-11-24 09:07:57 | [Reglet.Xlsx](https://www.nuget.org/packages/Reglet.Xlsx) | 1.6.0 | Maik Rehder | XLSX (SpreadsheetML, ECMA-376) workbook writer and reader for Reglet. |
| 2026-11-24 09:11:59 | [SelectView.FSharp.SystemTextJson.OpenApi](https://www.nuget.org/packages/SelectView.FSharp.SystemTextJson.OpenApi) | 0.1.0 | SelectView | OpenAPI schemas for F# types serialized with FSharp.SystemTextJson. Schema and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
