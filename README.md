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

## Latest list — 2026-11-21 10:20 UTC

New packages created between 2026-11-21 09:21 UTC and 2026-11-21 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T10-20-14-926308Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 09:40:22 | [Sevencat.ImageFacade.Avalonia.Win64Aio](https://www.nuget.org/packages/Sevencat.ImageFacade.Avalonia.Win64Aio) | 0.6.0 | ImageFacade contributors | ImageFacade 的 Avalonia.Win64Aio 后端：Avalonia 宿主已经合并了真 SkiaSharp（含原生 libSkiaSharp… |
| 2026-11-21 09:40:44 | [Sevencat.ImageFacade.SimdSkia](https://www.nuget.org/packages/Sevencat.ImageFacade.SimdSkia) | 0.6.0 | ImageFacade contributors | ImageFacade 的 SimdSkia 后端：纯托管的 SkiaSharp 兼容实现，不依赖 SkiaSharp / HarfBuzz 原生库，适合 A… |
| 2026-11-21 09:40:47 | [GameBananaSdk](https://www.nuget.org/packages/GameBananaSdk) | 1.0.0 | ArchLeaders | Semi-dynamic SDK for the GameBanana API |
| 2026-11-21 09:43:19 | [SiemensS7.NetCore](https://www.nuget.org/packages/SiemensS7.NetCore) | 2.0.0 | Giant | Communicate with Siemens PLC using the S7 protocol. 使用S7协议与西门子PLC通讯 |
| 2026-11-21 09:44:30 | [Cratis.Showrunner.Operations](https://www.nuget.org/packages/Cratis.Showrunner.Operations) | 2.17.1 | Cratis | Operations for Showrunner — a reusable watchdog that checks a Kubernetes deploy… |
| 2026-11-21 09:44:33 | [Cratis.Showrunner.StageManager.Pulumi](https://www.nuget.org/packages/Cratis.Showrunner.StageManager.Pulumi) | 2.17.1 | Cratis | Stage Manager for Pulumi — typed Pulumi components that declare the Stage Manag… |
| 2026-11-21 09:57:37 | [HTLLeonding.Utility.LeoUnion](https://www.nuget.org/packages/HTLLeonding.Utility.LeoUnion) | 1.0.0 | M. Haslinger | Generic ad-hoc union types for C# 15: Union<T1, ..., T10>, plus marker types fo… |
| 2026-11-21 10:02:11 | [NpgsqlRest.Mcp](https://www.nuget.org/packages/NpgsqlRest.Mcp) | 1.2.1 | Vedran Bilopavlović | MCP (Model Context Protocol) server for NpgsqlRest — projects opted-in PostgreS… |
| 2026-11-21 10:09:26 | [Suwbackkit.Testing](https://www.nuget.org/packages/Suwbackkit.Testing) | 0.3.0 | Manomenu | Test helpers for ASP.NET Core backends: recreate and drop a PostgreSQL test dat… |
| 2026-11-21 10:15:10 | [FM.Dotgit.osx-arm64](https://www.nuget.org/packages/FM.Dotgit.osx-arm64) | 0.1.0 | Fakhrulhilal Maktum | Git repository toolkit: clone and update many repositories at once. |
| 2026-11-21 10:15:17 | [FM.Dotclock.linux-x64](https://www.nuget.org/packages/FM.Dotclock.linux-x64) | 0.1.0 | Fakhrulhilal Maktum | Clockify from the command line: bulk-add time entries and view timesheets. |
| 2026-11-21 10:15:20 | [FM.Dotclock.osx-arm64](https://www.nuget.org/packages/FM.Dotclock.osx-arm64) | 0.1.0 | Fakhrulhilal Maktum | Clockify from the command line: bulk-add time entries and view timesheets. |
| 2026-11-21 10:15:21 | [FM.Dotclock](https://www.nuget.org/packages/FM.Dotclock) | 0.1.0 | Fakhrulhilal Maktum | Clockify from the command line: bulk-add time entries and view timesheets. |
| 2026-11-21 10:15:22 | [FM.Dotkafka](https://www.nuget.org/packages/FM.Dotkafka) | 0.1.0 | Fakhrulhilal Maktum | Kafka and Schema Registry toolkit: produce messages and manage topics. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
