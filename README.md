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

## Latest list — 2026-10-28 21:20 UTC

New packages created between 2026-10-28 20:20 UTC and 2026-10-28 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T21-20-43-562433Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 20:20:27 | [Fluxer.Net.Voice](https://www.nuget.org/packages/Fluxer.Net.Voice) | 3.9.0 | Nexfinity | Voice channel support for Fluxer.Net bots: joining voice channels and sending a… |
| 2026-10-28 20:22:42 | [TencentCloudSDKIntlEN.Adp](https://www.nuget.org/packages/TencentCloudSDKIntlEN.Adp) | 3.0.1417 | Tencent Cloud API Team | Tencent Cloud API 3.0 SDK for .NET |
| 2026-10-28 20:31:51 | [Messaia.Net.MailService.Abstractions](https://www.nuget.org/packages/Messaia.Net.MailService.Abstractions) | 10.2.0-beta04 | Fouad Messaia | Mail Service Abstractions |
| 2026-10-28 20:31:56 | [Messaia.Net.MailService.Observers](https://www.nuget.org/packages/Messaia.Net.MailService.Observers) | 10.2.0-beta04 | Fouad Messaia | Mail Service Observers |
| 2026-10-28 20:33:34 | [Lavalink4NET.Fluxer](https://www.nuget.org/packages/Lavalink4NET.Fluxer) | 0.1.1 | SylveonDeko | Lavalink4NET integration for Fluxer.Net bots, playing Lavalink audio into Fluxe… |
| 2026-10-28 20:47:57 | [CSweet.ConnectionService.Protocol](https://www.nuget.org/packages/CSweet.ConnectionService.Protocol) | 0.3.0 | C-Sweet | Provider-neutral managed connection protocol and deployment proof client. |
| 2026-10-28 20:58:13 | [Neph.GenericLibs.Net.HangFireLib](https://www.nuget.org/packages/Neph.GenericLibs.Net.HangFireLib) | 0.1.0 | Neph | Generic Hangfire helpers and service registration extensions for ASP.NET Core a… |
| 2026-10-28 20:59:22 | [zstd-c](https://www.nuget.org/packages/zstd-c) | 1.5.7 | Yann Collet, Meta Platforms,… | Zstandard, a fast lossless compression algorithm, built with vcpkg. |
| 2026-10-28 21:01:46 | [CSweet.Plugins.Platform.YouTube](https://www.nuget.org/packages/CSweet.Plugins.Platform.YouTube) | 0.2.1 | C-Sweet | Deterministic, broker-enforced YouTube connection contracts for C-Sweet. |
| 2026-10-28 21:12:37 | [Neph.GenericLibs.Net.RedisLib](https://www.nuget.org/packages/Neph.GenericLibs.Net.RedisLib) | 0.1.0 | Neph | Generic Redis helpers and service registration extensions for .NET applications. |
| 2026-10-28 21:13:06 | [Neph.GenericLibs.Net.LiveboxLib](https://www.nuget.org/packages/Neph.GenericLibs.Net.LiveboxLib) | 0.1.0 | Neph | Generic Orange Livebox client helpers and service registration extensions for .… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
