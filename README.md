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

## Latest list — 2026-10-04 07:20 UTC

New packages created between 2026-10-04 06:20 UTC and 2026-10-04 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T07-20-48-482866Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 06:34:54 | [JKToolKit.CodexSDK.Runtime.linux-arm64](https://www.nuget.org/packages/JKToolKit.CodexSDK.Runtime.linux-arm64) | 0.160.0 | JKamsker,OpenAI | Optional Codex CLI 0.160.0 runtime for linux-arm64. Contains OpenAI Codex and i… |
| 2026-10-04 06:34:59 | [JKToolKit.CodexSDK.Runtime.linux-x64](https://www.nuget.org/packages/JKToolKit.CodexSDK.Runtime.linux-x64) | 0.160.0 | JKamsker,OpenAI | Optional Codex CLI 0.160.0 runtime for linux-x64. Contains OpenAI Codex and its… |
| 2026-10-04 06:35:05 | [JKToolKit.CodexSDK.Runtime.osx-arm64](https://www.nuget.org/packages/JKToolKit.CodexSDK.Runtime.osx-arm64) | 0.160.0 | JKamsker,OpenAI | Optional Codex CLI 0.160.0 runtime for osx-arm64. Contains OpenAI Codex and its… |
| 2026-10-04 06:35:12 | [JKToolKit.CodexSDK.Runtime.osx-x64](https://www.nuget.org/packages/JKToolKit.CodexSDK.Runtime.osx-x64) | 0.160.0 | JKamsker,OpenAI | Optional Codex CLI 0.160.0 runtime for osx-x64. Contains OpenAI Codex and its b… |
| 2026-10-04 06:35:17 | [JKToolKit.CodexSDK.Runtime.win-arm64](https://www.nuget.org/packages/JKToolKit.CodexSDK.Runtime.win-arm64) | 0.160.0 | JKamsker,OpenAI | Optional Codex CLI 0.160.0 runtime for win-arm64. Contains OpenAI Codex and its… |
| 2026-10-04 06:35:24 | [JKToolKit.CodexSDK.Runtime.win-x64](https://www.nuget.org/packages/JKToolKit.CodexSDK.Runtime.win-x64) | 0.160.0 | JKamsker,OpenAI | Optional Codex CLI 0.160.0 runtime for win-x64. Contains OpenAI Codex and its b… |
| 2026-10-04 06:38:04 | [Knmdb.TrackAndTrace](https://www.nuget.org/packages/Knmdb.TrackAndTrace) | 1.0.0 | KNMDB | Кроссплатформенный SDK и DI-сервис для Track and Trace API системы KNMDB / KNDD… |
| 2026-10-04 07:02:09 | [StdMrrDetector](https://www.nuget.org/packages/StdMrrDetector) | 1.0.0 | Nornion | Library to check whether STDF file has MRR record. |
| 2026-10-04 07:10:57 | [Webority.Domain.Abstractions](https://www.nuget.org/packages/Webority.Domain.Abstractions) | 0.1.0 | Webority Technologies | Shared domain contracts for Webority products, with no dependencies so a produc… |
| 2026-10-04 07:10:58 | [Webority.Domain.EntityFrameworkCore](https://www.nuget.org/packages/Webority.Domain.EntityFrameworkCore) | 0.1.0 | Webority Technologies | Entity Framework Core companion to Webority.Domain.Abstractions: the AuditInter… |
| 2026-10-04 07:12:52 | [Orvano](https://www.nuget.org/packages/Orvano) | 0.2.0 | Orvano | The Orvano SDK for .NET: server code for Orvano, the open source backend you ho… |
| 2026-10-04 07:13:43 | [ReactiveUI.Validation.AndroidX.Reactive](https://www.nuget.org/packages/ReactiveUI.Validation.AndroidX.Reactive) | 8.0.0 | ReactiveUI and Contributors | Provides ReactiveUI.Validation.Reactive extensions for the AndroidX Library, fo… |
| 2026-10-04 07:13:44 | [ReactiveUI.Validation.Reactive](https://www.nuget.org/packages/ReactiveUI.Validation.Reactive) | 8.0.0 | ReactiveUI and Contributors | Validations library for ReactiveUI.Reactive, the System.Reactive flavour of Rea… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
