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

## Latest list — 2026-10-04 00:18 UTC

New packages created between 2026-10-03 23:21 UTC and 2026-10-04 00:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T00-18-54-708052Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 23:23:13 | [SunamoSlnGen](https://www.nuget.org/packages/SunamoSlnGen) | 26.10.4.2 | www.sunamo.cz | Helper for reading project paths from Visual Studio solution files via Microsof… |
| 2026-10-03 23:24:08 | [AlienFx.Api](https://www.nuget.org/packages/AlienFx.Api) | 1.0.1 | Panoramic Data Limited | A .NET API client for controlling AlienFX lighting zones on Alienware devices. |
| 2026-10-03 23:24:22 | [SunamoNTextCat](https://www.nuget.org/packages/SunamoNTextCat) | 26.10.4.1 | www.sunamo.cz | Language detection (Czech/English) built on NTextCat with an embedded Wikipedia… |
| 2026-10-03 23:26:00 | [AgencyDotNet.Indexer](https://www.nuget.org/packages/AgencyDotNet.Indexer) | 0.1.207-g22b1d0f8ed | Emre Aydinceren | Command-line semantic indexer for agents: incrementally indexes a folder of tex… |
| 2026-10-03 23:27:07 | [Beetech.OmniAutoId.Client](https://www.nuget.org/packages/Beetech.OmniAutoId.Client) | 1.0.0 | Beetech Auto-ID Engineering T… | Official .NET client library for Beetech OmniAuto-ID and Adv.SmartSdk Edge Gate… |
| 2026-10-03 23:27:12 | [Beetech.OmniAutoId.Templates](https://www.nuget.org/packages/Beetech.OmniAutoId.Templates) | 1.0.0 | Beetech Auto-ID Engineering T… | Official dotnet new templates for scaffolding high-speed Beetech OmniAuto-ID an… |
| 2026-10-03 23:28:29 | [SunamoTranslate](https://www.nuget.org/packages/SunamoTranslate) | 26.10.4.1 | www.sunamo.cz | Translation helpers (Google Cloud Translation, cache of translated sentences, d… |
| 2026-10-03 23:43:40 | [ClaudeCodeBridge](https://www.nuget.org/packages/ClaudeCodeBridge) | 1.0.0 | Isaias Gomes | Integrates any .NET 8 application with the Claude Code CLI via subprocess. Prov… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
