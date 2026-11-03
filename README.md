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

## Latest list — 2026-11-03 17:20 UTC

New packages created between 2026-11-03 16:21 UTC and 2026-11-03 17:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T17-20-22-5094Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 16:25:58 | [Semifreddo](https://www.nuget.org/packages/Semifreddo) | 0.1.0 | Mark Hammond | Persistent (immutable, structurally shared) collections for .NET: vectors, RRB… |
| 2026-11-03 16:32:02 | [Cs2Play.Sdk](https://www.nuget.org/packages/Cs2Play.Sdk) | 1.9.0 | cs2play | The SDK of cs2play for modes of Counter-Strike 2: a mode is a CounterStrikeShar… |
| 2026-11-03 16:32:03 | [Cs2Play.Templates](https://www.nuget.org/packages/Cs2Play.Templates) | 1.9.0 | cs2play | Templates of cs2play for dotnet new: dotnet new cs2play-mode makes a small work… |
| 2026-11-03 16:35:25 | [Shirasagi0012.MaterialSymbols.Avalonia](https://www.nuget.org/packages/Shirasagi0012.MaterialSymbols.Avalonia) | 0.1.2-alpha | Shirasagi0012 | Icons from Material Symbols variable font. Support variable axis. |
| 2026-11-03 16:35:27 | [Shirasagi0012.MaterialSymbols.Avalonia.Outlined](https://www.nuget.org/packages/Shirasagi0012.MaterialSymbols.Avalonia.Outlined) | 0.1.2-alpha | Shirasagi0012 | Material Symbols variable font for Shirasagi0012.MaterialSymbols.Avalonia. |
| 2026-11-03 16:35:29 | [Shirasagi0012.MaterialSymbols.Avalonia.Rounded](https://www.nuget.org/packages/Shirasagi0012.MaterialSymbols.Avalonia.Rounded) | 0.1.2-alpha | Shirasagi0012 | Icons from Material Symbols variable font. Support variable axis. |
| 2026-11-03 16:35:31 | [Shirasagi0012.MaterialSymbols.Avalonia.Sharp](https://www.nuget.org/packages/Shirasagi0012.MaterialSymbols.Avalonia.Sharp) | 0.1.2-alpha | Shirasagi0012 | Material Symbols variable font for Shirasagi0012.MaterialSymbols.Avalonia. |
| 2026-11-03 16:46:42 | [BorrowedTorch.MonoGame.Framework.Compute.WindowsDX](https://www.nuget.org/packages/BorrowedTorch.MonoGame.Framework.Compute.WindowsDX) | 3.8.3.2 | Elzianor, cpt-max, MonoGame T… | The MonoGame runtime for Windows using DirectX API's, with compute, tessellatio… |
| 2026-11-03 16:58:04 | [Heliograph.Engine](https://www.nuget.org/packages/Heliograph.Engine) | 0.1.0 | Heliograph contributors | The pure rules engine for Heliograph, a board game of mirrors and light: move l… |
| 2026-11-03 17:14:42 | [Extrode.NativeWeb.Scaffold](https://www.nuget.org/packages/Extrode.NativeWeb.Scaffold) | 0.1.0 | Extrode LLC | NativeWeb framework: scaffolding attributes and the store contract the generate… |
| 2026-11-03 17:14:42 | [Extrode.NativeWeb.Render](https://www.nuget.org/packages/Extrode.NativeWeb.Render) | 0.1.0 | Extrode LLC | NativeWeb framework: compiled-template render runtime (TemplateWriter, Html, IR… |
| 2026-11-03 17:14:46 | [Extrode.NativeWeb.Permissions](https://www.nuget.org/packages/Extrode.NativeWeb.Permissions) | 0.1.0 | Extrode LLC | NativeWeb framework: model permissions, groups, and the store contract the perm… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
