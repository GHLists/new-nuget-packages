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

## Latest list — 2026-11-06 16:19 UTC

New packages created between 2026-11-06 15:19 UTC and 2026-11-06 16:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T16-19-43-714768Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 15:36:22 | [Suwagcms.Sdk](https://www.nuget.org/packages/Suwagcms.Sdk) | 0.1.0 | Piotr Gugnowski | The SDK of a .NET bot built on Suwagcms: the definition format, its validator a… |
| 2026-11-06 15:36:36 | [Enbrea.Cron.Descriptor](https://www.nuget.org/packages/Enbrea.Cron.Descriptor) | 0.2.0 | STÜBER SYSTEMS GmbH | Human-readable descriptions for Enbrea.Cron expressions and schedules. |
| 2026-11-06 15:51:12 | [Sunder.Sdk.Avalonia](https://www.nuget.org/packages/Sunder.Sdk.Avalonia) | 1.0.0 | Younics | Avalonia-specific public contracts and Sunder theme resources for package App v… |
| 2026-11-06 15:51:17 | [Sunder.Sdk.Stacks](https://www.nuget.org/packages/Sunder.Sdk.Stacks) | 1.0.0 | Younics | Public contracts for contributing package data to Sunder Stack discovery, expor… |
| 2026-11-06 15:51:21 | [Sunder.Sdk.Worker](https://www.nuget.org/packages/Sunder.Sdk.Worker) | 1.0.0 | Younics | Standalone .NET worker authoring support for the Sunder Worker V1 process proto… |
| 2026-11-06 15:51:44 | [WIJI.Core.Types](https://www.nuget.org/packages/WIJI.Core.Types) | 1.0.0 | DGDIW | Package Description |
| 2026-11-06 15:55:30 | [Omega3065.RaCustomMenu](https://www.nuget.org/packages/Omega3065.RaCustomMenu) | 0.2.0 | OMEGA3065,Bankokwak | Package Description |
| 2026-11-06 15:56:08 | [Greatminds.Arqi.win-x64](https://www.nuget.org/packages/Greatminds.Arqi.win-x64) | 0.2.26 | Greatminds | Architecture as Code CLI for defining, validating and generating architecture a… |
| 2026-11-06 15:56:10 | [Greatminds.Arqi.linux-x64](https://www.nuget.org/packages/Greatminds.Arqi.linux-x64) | 0.2.26 | Greatminds | Architecture as Code CLI for defining, validating and generating architecture a… |
| 2026-11-06 15:56:12 | [Greatminds.Arqi.osx-x64](https://www.nuget.org/packages/Greatminds.Arqi.osx-x64) | 0.2.26 | Greatminds | Architecture as Code CLI for defining, validating and generating architecture a… |
| 2026-11-06 15:56:14 | [Greatminds.Arqi.osx-arm64](https://www.nuget.org/packages/Greatminds.Arqi.osx-arm64) | 0.2.26 | Greatminds | Architecture as Code CLI for defining, validating and generating architecture a… |
| 2026-11-06 15:56:24 | [Greatminds.Arqi](https://www.nuget.org/packages/Greatminds.Arqi) | 0.2.26 | Greatminds | Architecture as Code CLI for defining, validating and generating architecture a… |
| 2026-11-06 16:01:23 | [ILNumerics.Community.SceneEditor.WPF](https://www.nuget.org/packages/ILNumerics.Community.SceneEditor.WPF) | 7.4.0.310 | Thilo Viereck | Properties editor for ILNumerics (http://ilnumerics.net/) scene graphs and plot… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
