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

## Latest list — 2026-11-19 06:21 UTC

New packages created between 2026-11-19 05:21 UTC and 2026-11-19 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T06-21-38-730046Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 05:30:11 | [Wartakopi](https://www.nuget.org/packages/Wartakopi) | 1.0.0 | Warta Kopi — media ulasan ked… | Warta Kopi Indonesian coffee shop reviews constants. Official: https://www.wart… |
| 2026-11-19 05:33:12 | [Vidfomo.FrameGeometry](https://www.nuget.org/packages/Vidfomo.FrameGeometry) | 0.1.0 | js-upup | Integer geometry helpers for planning video frame resizing and centered crops. |
| 2026-11-19 05:45:59 | [EasyReasy.Auth.Testing](https://www.nuget.org/packages/EasyReasy.Auth.Testing) | 1.0.0 | Adam Tovatt | A software WebAuthn authenticator for testing passkey and security-key endpoint… |
| 2026-11-19 05:52:15 | [Compze.Teventive.MemoryImageStateStore](https://www.nuget.org/packages/Compze.Teventive.MemoryImageStateStore) | 0.1.0-alpha | Lidbom Solutions AB | A memory image of taggregates: every taggregate held in memory for the containe… |
| 2026-11-19 05:52:19 | [Compze.Teventive.MemoryImageStateStore.MemoryPack](https://www.nuget.org/packages/Compze.Teventive.MemoryImageStateStore.MemoryPack) | 0.1.0-alpha | Lidbom Solutions AB | A MemoryPack cache for Compze.Teventive.MemoryImageStateStore's JSON files, so… |
| 2026-11-19 06:02:31 | [Eleris.RawNet](https://www.nuget.org/packages/Eleris.RawNet) | 0.1.0 | Sébastien Putier | Pure managed .NET library to read camera raw files (Nikon NEF first): metadata,… |
| 2026-11-19 06:05:54 | [OpenDCP.Framework.Connections.Datasource.MSSQL](https://www.nuget.org/packages/OpenDCP.Framework.Connections.Datasource.MSSQL) | 0.4.0 | OpenDCP.Framework.Connections… | Package Description |
| 2026-11-19 06:06:44 | [CodeBrix.WebPlatform.WasmShrink.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.WasmShrink.ApacheLicenseForever) | 1.0.323.365 | Jeremy Ellis | The WebAssembly size optimizer for the CodeBrix.WebPlatform web application pla… |
| 2026-11-19 06:10:36 | [Curiosity.CLI.linux-arm64](https://www.nuget.org/packages/Curiosity.CLI.linux-arm64) | 26.11.8242 | Curiosity GmbH | The official .NET command line tool for Curiosity Studio (https://curiosity.ai). |
| 2026-11-19 06:11:45 | [Curiosity.CLI.win-arm64](https://www.nuget.org/packages/Curiosity.CLI.win-arm64) | 26.11.8242 | Curiosity GmbH | The official .NET command line tool for Curiosity Studio (https://curiosity.ai). |
| 2026-11-19 06:11:57 | [Curiosity.CLI.win-x64](https://www.nuget.org/packages/Curiosity.CLI.win-x64) | 26.11.8242 | Curiosity GmbH | The official .NET command line tool for Curiosity Studio (https://curiosity.ai). |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
