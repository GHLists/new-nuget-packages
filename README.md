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

## Latest list — 2026-11-21 23:19 UTC

New packages created between 2026-11-21 22:18 UTC and 2026-11-21 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T23-19-22-315257Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 22:24:17 | [BorrowedTorch.Engine.AdditionalFeatures](https://www.nuget.org/packages/BorrowedTorch.Engine.AdditionalFeatures) | 1.1.3 | Vladyslav Pysarenko | Kindling, Borrowed Torch's game engine: its additional features - sound, post e… |
| 2026-11-21 22:24:22 | [Bashka.Plugins.Themes.TurboVisionDark](https://www.nuget.org/packages/Bashka.Plugins.Themes.TurboVisionDark) | 1.0.8 | Evgeny Gorbovoy | Dark theme for Bashka based on Turbo Vision compatible theme. |
| 2026-11-21 22:39:34 | [Subrange](https://www.nuget.org/packages/Subrange) | 0.1.1 | Qluxzz | Subrange types for .NET: a number type that only holds values within its bounds… |
| 2026-11-21 22:39:34 | [Subrange.Swashbuckle](https://www.nuget.org/packages/Subrange.Swashbuckle) | 0.1.1 | Qluxzz | Documents Subrange types in Swashbuckle OpenAPI schemas as the integers and num… |
| 2026-11-21 22:47:03 | [ResultUnion.FluentValidation](https://www.nuget.org/packages/ResultUnion.FluentValidation) | 0.2.0 | Giorgi Kaldani | FluentValidation integration for ResultUnion: a ValidationResult becomes a Resu… |
| 2026-11-21 22:47:04 | [CefKit](https://www.nuget.org/packages/CefKit) | 0.1.0 | CefKit contributors | .NET binding to the Chromium Embedded Framework C API for Windows and Linux x64… |
| 2026-11-21 23:00:59 | [Meziantou.Framework.Email](https://www.nuget.org/packages/Meziantou.Framework.Email) | 1.0.0 | meziantou | Reads and writes email, contact and calendar files. Outlook data files (PST and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
