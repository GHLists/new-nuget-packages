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

## Latest list — 2026-10-29 01:19 UTC

New packages created between 2026-10-29 00:20 UTC and 2026-10-29 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T01-19-28-327219Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 00:50:49 | [Plugin.Maui.SharedTransitions](https://www.nuget.org/packages/Plugin.Maui.SharedTransitions) | 0.1.0 | Wilson Vargas | Shared element transitions between pages for .NET MAUI (Shell and NavigationPag… |
| 2026-10-29 00:58:37 | [GalForge](https://www.nuget.org/packages/GalForge) | 1.0.0 | sillycowvalley | CUPL-subset logic compiler for GAL16V8, GAL20V8 and GAL22V10. |
| 2026-10-29 01:08:56 | [ToolUp.Facts.Presentation](https://www.nuget.org/packages/ToolUp.Facts.Presentation) | 0.36.0 | Andrew J. Willshire | ToolUp.Facts.Presentation — from a gated fact series to a Fuaran-UI node. A pre… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
