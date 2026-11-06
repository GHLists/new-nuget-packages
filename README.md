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

## Latest list — 2026-11-06 07:19 UTC

New packages created between 2026-11-06 06:20 UTC and 2026-11-06 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T07-19-57-805854Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 06:33:40 | [Stride.Dependencies.Assimp](https://www.nuget.org/packages/Stride.Dependencies.Assimp) | 6.0.5.2 | Stride Contributors | Assimp shared library for the Stride 3D importer. Built from assimp/assimp v6.0… |
| 2026-11-06 06:37:04 | [Vocab.Sdk.Maui](https://www.nuget.org/packages/Vocab.Sdk.Maui) | 0.0.2501.11908 | vo.cab | Sign in with vo.cab from a .NET MAUI app: AddVocab() wires the authorization co… |
| 2026-11-06 06:38:08 | [MasterX.Logging.FileSystem](https://www.nuget.org/packages/MasterX.Logging.FileSystem) | 3.0.6 | master-X (Marco Sena) | Configurable file system logging provider for master-X applications. |
| 2026-11-06 06:40:03 | [BIMPlugins.Bars](https://www.nuget.org/packages/BIMPlugins.Bars) | 2.0.1 | Samir Shibliev | Revit Package BIMPlugins.Bars |
| 2026-11-06 07:01:48 | [StaticNorth.Uhp.Harnesses.ClaudeCode](https://www.nuget.org/packages/StaticNorth.Uhp.Harnesses.ClaudeCode) | 1.2.0 | uhp-dotnet contributors | Native AOT-compatible Claude Code provider for UHP hosts. |
| 2026-11-06 07:01:50 | [StaticNorth.Uhp.Harnesses.Codex](https://www.nuget.org/packages/StaticNorth.Uhp.Harnesses.Codex) | 1.2.0 | uhp-dotnet contributors | Native AOT-compatible Codex App Server provider for UHP hosts. |
| 2026-11-06 07:01:51 | [StaticNorth.Uhp.Harnesses.OpenCode](https://www.nuget.org/packages/StaticNorth.Uhp.Harnesses.OpenCode) | 1.2.0 | uhp-dotnet contributors | Native AOT-compatible OpenCode provider for UHP hosts. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
