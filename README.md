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

## Latest list — 2026-10-12 00:20 UTC

New packages created between 2026-10-11 23:19 UTC and 2026-10-12 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T00-20-43-706893Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 23:38:19 | [Shaunebu.MAUI.Navigation.Analyzers](https://www.nuget.org/packages/Shaunebu.MAUI.Navigation.Analyzers) | 1.0.0 | Shaunebu | Roslyn analyzers and code fixes for enforcing safe navigation practices in .NET… |
| 2026-10-11 23:38:21 | [Shaunebu.MAUI.Navigation.CodeFixes](https://www.nuget.org/packages/Shaunebu.MAUI.Navigation.CodeFixes) | 1.0.0 | Shaunebu | Roslyn code fixes for Shaunebu.MAUI.Navigation analyzers. |
| 2026-10-11 23:38:22 | [Shaunebu.MAUI.Navigation](https://www.nuget.org/packages/Shaunebu.MAUI.Navigation) | 1.0.0 | Shaunebu | Enterprise-grade typed navigation orchestration for .NET MAUI. Provides strongl… |
| 2026-10-11 23:38:24 | [Shaunebu.MAUI.Navigation.Debugger](https://www.nuget.org/packages/Shaunebu.MAUI.Navigation.Debugger) | 1.0.0 | Shaunebu | Optional navigation diagnostics platform for Shaunebu.MAUI.Navigation. Provides… |
| 2026-10-11 23:38:26 | [Shaunebu.MAUI.Navigation.Generators](https://www.nuget.org/packages/Shaunebu.MAUI.Navigation.Generators) | 1.0.0 | Shaunebu | Incremental source generators for strongly typed navigation infrastructure in .… |
| 2026-10-11 23:50:33 | [NGB.Platform.Templates](https://www.nuget.org/packages/NGB.Platform.Templates) | 3.2.0 | NGB Platform | Official independently buildable NGB application template with API, Migrator, B… |
| 2026-10-11 23:58:55 | [ModRelease](https://www.nuget.org/packages/ModRelease) | 1.0.0 | nianeyna | Release pipeline for BepInEx mods: clean build against the installed game, meta… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
