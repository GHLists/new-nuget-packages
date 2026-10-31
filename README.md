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

## Latest list — 2026-10-31 08:20 UTC

New packages created between 2026-10-31 07:18 UTC and 2026-10-31 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T08-20-59-889681Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 07:32:44 | [X.Toolkits.PDF](https://www.nuget.org/packages/X.Toolkits.PDF) | 1.0.0 | X | X.Toolkits PDF 扩展 |
| 2026-10-31 07:39:41 | [Nexttag.Chat.EfCore](https://www.nuget.org/packages/Nexttag.Chat.EfCore) | 1.0.0 | Nexttag - Jonathan Schenker | Persistencia do chat unificado (Nexttag.Chat) no PostgreSQL com EF Core: conver… |
| 2026-10-31 07:57:08 | [Runic.Desktop.Kestrel](https://www.nuget.org/packages/Runic.Desktop.Kestrel) | 0.15.0 | RunicArtifex | Serves Runic Desktop surfaces from ASP.NET Core Kestrel. |
| 2026-10-31 07:57:09 | [Runic.Desktop.NativeServer](https://www.nuget.org/packages/Runic.Desktop.NativeServer) | 0.15.0 | RunicArtifex | Serves Runic Desktop surfaces from a native Rust (axum) HTTP and WebSocket serv… |
| 2026-10-31 07:57:11 | [Runic.Desktop.NativeServer.Static.linux-arm64](https://www.nuget.org/packages/Runic.Desktop.NativeServer.Static.linux-arm64) | 0.15.0 | RunicArtifex | The static library of the native Runic Desktop server for NativeAOT on linux-ar… |
| 2026-10-31 07:57:13 | [Runic.Desktop.NativeServer.Static.linux-musl-arm64](https://www.nuget.org/packages/Runic.Desktop.NativeServer.Static.linux-musl-arm64) | 0.15.0 | RunicArtifex | The static library of the native Runic Desktop server for NativeAOT on linux-mu… |
| 2026-10-31 07:57:15 | [Runic.Desktop.NativeServer.Static.linux-musl-x64](https://www.nuget.org/packages/Runic.Desktop.NativeServer.Static.linux-musl-x64) | 0.15.0 | RunicArtifex | The static library of the native Runic Desktop server for NativeAOT on linux-mu… |
| 2026-10-31 07:57:16 | [Runic.Desktop.NativeServer.Static.linux-x64](https://www.nuget.org/packages/Runic.Desktop.NativeServer.Static.linux-x64) | 0.15.0 | RunicArtifex | The static library of the native Runic Desktop server for NativeAOT on linux-x6… |
| 2026-10-31 07:57:18 | [Runic.Desktop.NativeServer.Static.osx-arm64](https://www.nuget.org/packages/Runic.Desktop.NativeServer.Static.osx-arm64) | 0.15.0 | RunicArtifex | The static library of the native Runic Desktop server for NativeAOT on osx-arm6… |
| 2026-10-31 07:57:19 | [Runic.Desktop.NativeServer.Static.win-arm64](https://www.nuget.org/packages/Runic.Desktop.NativeServer.Static.win-arm64) | 0.15.0 | RunicArtifex | The static library of the native Runic Desktop server for NativeAOT on win-arm6… |
| 2026-10-31 07:57:21 | [Runic.Desktop.NativeServer.Static.win-x64](https://www.nuget.org/packages/Runic.Desktop.NativeServer.Static.win-x64) | 0.15.0 | RunicArtifex | The static library of the native Runic Desktop server for NativeAOT on win-x64.… |
| 2026-10-31 08:03:05 | [KirillMaster.QualityGates.Cli](https://www.nuget.org/packages/KirillMaster.QualityGates.Cli) | 0.5.0 | KirillMaster | qg dotnet tool: PR and new-code gates, baseline ratchet, coverage, duplication,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
