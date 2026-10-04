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

## Latest list — 2026-10-04 16:20 UTC

New packages created between 2026-10-04 15:21 UTC and 2026-10-04 16:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T16-20-41-518944Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 15:29:06 | [Plugin.Maui.NativeContextMenus](https://www.nuget.org/packages/Plugin.Maui.NativeContextMenus) | 1.0.0 | Ed Giardina | Plugin.Maui.NativeContextMenus provides the ability to create native context me… |
| 2026-10-04 15:37:18 | [DeltaNetcode](https://www.nuget.org/packages/DeltaNetcode) | 0.0.2 | DeltaNetcode | Engine-independent networking for .NET applications. |
| 2026-10-04 15:37:39 | [Banned.CodeDiff](https://www.nuget.org/packages/Banned.CodeDiff) | 0.1.0 | banned | Core Git diff parsing, models, transformations, and syntax highlighting. |
| 2026-10-04 15:37:40 | [Banned.CodeDiff.Avalonia](https://www.nuget.org/packages/Banned.CodeDiff.Avalonia) | 0.1.0 | banned | Avalonia controls for rendering unified diffs in split and unified layouts. |
| 2026-10-04 15:45:11 | [Vestigium.Controls.QueryBar](https://www.nuget.org/packages/Vestigium.Controls.QueryBar) | 1.0.0 | Vestigium | WPF query bar for a KQL session: text, clear, saved queries, and completion. |
| 2026-10-04 16:04:32 | [Shells.Endpoints.Swachbuckle](https://www.nuget.org/packages/Shells.Endpoints.Swachbuckle) | 3.0.0 | Ignjat Koicki | Swagger integration for Shells.Endpoints. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
