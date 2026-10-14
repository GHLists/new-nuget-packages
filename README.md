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

## Latest list — 2026-10-14 20:19 UTC

New packages created between 2026-10-14 19:20 UTC and 2026-10-14 20:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T20-19-59-165776Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 19:22:08 | [BorrowedTorch.InputBinder](https://www.nuget.org/packages/BorrowedTorch.InputBinder) | 2.0.1 | Vladyslav Pysarenko | Class library for managing various types of input binding to game actions. |
| 2026-10-14 19:22:50 | [Fuuga.Server.cpu](https://www.nuget.org/packages/Fuuga.Server.cpu) | 1.0.41 | Tuomas Hietanen | This package contains OpenAI and Anthropic compatible HTTP server for Fuuga, to… |
| 2026-10-14 19:23:04 | [Flip7](https://www.nuget.org/packages/Flip7) | 0.1.0 | Leo Conforti | The card game Flip 7 in F#: a rules engine that plays whole games, the odds a h… |
| 2026-10-14 19:23:38 | [Fuuga.Server.cpu.linux-x64](https://www.nuget.org/packages/Fuuga.Server.cpu.linux-x64) | 1.0.41 | Tuomas Hietanen | This package contains OpenAI and Anthropic compatible HTTP server for Fuuga, to… |
| 2026-10-14 19:24:25 | [Fuuga.Server.cpu.osx-arm64](https://www.nuget.org/packages/Fuuga.Server.cpu.osx-arm64) | 1.0.41 | Tuomas Hietanen | This package contains OpenAI and Anthropic compatible HTTP server for Fuuga, to… |
| 2026-10-14 19:24:59 | [Fuuga.Server.cpu.win-x64](https://www.nuget.org/packages/Fuuga.Server.cpu.win-x64) | 1.0.41 | Tuomas Hietanen | This package contains OpenAI and Anthropic compatible HTTP server for Fuuga, to… |
| 2026-10-14 19:26:08 | [TechStyle.JsonCompress.Cli](https://www.nuget.org/packages/TechStyle.JsonCompress.Cli) | 1.0.3 | Ejaz Hussain Arain | Command line for json-compress: compress, restore, measure, minify, beautify an… |
| 2026-10-14 19:27:58 | [TrustList.Badge](https://www.nuget.org/packages/TrustList.Badge) | 0.1.0 | TrustList | Show your TrustList rank badge on your website: builds the badge image URL, the… |
| 2026-10-14 19:30:28 | [TechStyle.SecureKeystore.Cli](https://www.nuget.org/packages/TechStyle.SecureKeystore.Cli) | 3.0.0 | Ejaz Hussain Arain | Command line for secure-keystore: encrypted secrets at rest, with no service to… |
| 2026-10-14 19:31:03 | [TechStyle.SecureKeystore](https://www.nuget.org/packages/TechStyle.SecureKeystore) | 3.0.0 | Ejaz Hussain Arain | Encrypted secrets at rest for .NET, with no service to run. Two-layer AES-256-G… |
| 2026-10-14 19:47:20 | [ZeroFactor.Aspire.Hosting](https://www.nuget.org/packages/ZeroFactor.Aspire.Hosting) | 0.1.0 | Caleb Bertsch | Aspire hosting integration for 0factor, a mock OIDC provider for local developm… |
| 2026-10-14 19:50:46 | [SkyBellSharp](https://www.nuget.org/packages/SkyBellSharp) | 0.1.1 | Xavier A. | Unofficial .NET client for the SkyBell Gen5 cloud API (devices, live WebRTC ses… |
| 2026-10-14 20:13:47 | [Vali-Bucket](https://www.nuget.org/packages/Vali-Bucket) | 1.0.0 | Felipe Rafael Montenegro Morr… | Vali-Bucket groups timestamps into fixed-size time buckets for reporting and an… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
