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

## Latest list — 2026-11-23 07:19 UTC

New packages created between 2026-11-23 06:19 UTC and 2026-11-23 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T07-19-11-075232Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 06:22:29 | [FreeType.Net](https://www.nuget.org/packages/FreeType.Net) | 0.1.0 | FreeType.Net contributors | .NET bindings for FreeType 2.13.2, with FreeType built for win-x64, win-arm64,… |
| 2026-11-23 06:24:43 | [Nextorm.Extensions.Gitea](https://www.nuget.org/packages/Nextorm.Extensions.Gitea) | 1.0.0 | Nextorm.Extensions.Gitea | Nextorm repository context for the Gitea 1.24.7 SQLite schema. |
| 2026-11-23 06:24:44 | [Nextorm.Extensions.Mastodon](https://www.nuget.org/packages/Nextorm.Extensions.Mastodon) | 1.0.0 | Nextorm.Extensions.Mastodon | Nextorm repository context for the Mastodon PostgreSQL tags schema. |
| 2026-11-23 06:24:47 | [Nextorm.Extensions.WordPress](https://www.nuget.org/packages/Nextorm.Extensions.WordPress) | 1.0.0 | Nextorm.Extensions.WordPress | Nextorm repository context for the WordPress terms schema. |
| 2026-11-23 07:06:58 | [Tralys.Analyzers](https://www.nuget.org/packages/Tralys.Analyzers) | 0.1.0 | Tralys.Analyzers contributors | Roslyn analyzers for rules that hold in any C# codebase, starting with no null-… |
| 2026-11-23 07:12:25 | [BIMPlugins.AvalonEdit](https://www.nuget.org/packages/BIMPlugins.AvalonEdit) | 6.3.1 | Samir Shibliev, AvalonEdit co… | AvalonEdit for Revit add-ins, under an assembly name of its own: it never clash… |
| 2026-11-23 07:13:02 | [GoogleColabClient](https://www.nuget.org/packages/GoogleColabClient) | 0.1.0 | Enari | Unofficial .NET client for google-colab-cli 0.7.5 (strict port). Unofficial, no… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
