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

## Latest list — 2026-10-22 06:19 UTC

New packages created between 2026-10-22 05:20 UTC and 2026-10-22 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T06-19-48-795082Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 05:23:36 | [HamsterWheel.HLinq.Lang.Pl](https://www.nuget.org/packages/HamsterWheel.HLinq.Lang.Pl) | 0.13.0 | HamsterWheel.HLinq.Lang.Pl | Package Description |
| 2026-10-22 05:23:37 | [HamsterWheel.HLinq.SqlServer](https://www.nuget.org/packages/HamsterWheel.HLinq.SqlServer) | 0.13.0 | HamsterWheel.HLinq.SqlServer | Package Description |
| 2026-10-22 05:23:38 | [HamsterWheel.HLinq.Sqlite](https://www.nuget.org/packages/HamsterWheel.HLinq.Sqlite) | 0.13.0 | HamsterWheel.HLinq.Sqlite | Package Description |
| 2026-10-22 05:23:39 | [HamsterWheel.HLinq.MariaDb](https://www.nuget.org/packages/HamsterWheel.HLinq.MariaDb) | 0.13.0 | HamsterWheel.HLinq.MariaDb | Package Description |
| 2026-10-22 05:23:40 | [HamsterWheel.HLinq.MySql](https://www.nuget.org/packages/HamsterWheel.HLinq.MySql) | 0.13.0 | HamsterWheel.HLinq.MySql | Package Description |
| 2026-10-22 05:34:11 | [JvmBridge.Logging](https://www.nuget.org/packages/JvmBridge.Logging) | 26.10.22.2987 | void-community | Microsoft.Extensions.Logging adapters for JvmBridge agents: an ILogger that wri… |
| 2026-10-22 05:52:21 | [Runic.CommandLine](https://www.nuget.org/packages/Runic.CommandLine) | 0.8.0 | RunicArtifex | Parser-neutral command catalog, execution, host integration, and output kernel… |
| 2026-10-22 05:52:22 | [Runic.CommandLine.Processes](https://www.nuget.org/packages/Runic.CommandLine.Processes) | 0.8.0 | RunicArtifex | Bounded and cancellable local process execution for command-line clients. |
| 2026-10-22 05:52:23 | [Runic.CommandLine.Spectre](https://www.nuget.org/packages/Runic.CommandLine.Spectre) | 0.8.0 | RunicArtifex | Spectre.Console presentation for Runic Command Line applications. |
| 2026-10-22 05:52:24 | [Runic.CommandLine.Testing](https://www.nuget.org/packages/Runic.CommandLine.Testing) | 0.8.0 | RunicArtifex | Deterministic test helpers for Runic Command Line applications. |
| 2026-10-22 06:06:16 | [Tern.Cli.win-arm64](https://www.nuget.org/packages/Tern.Cli.win-arm64) | 0.1.2 | Mark Gibbons | Drop-in, Native AOT replacement for the Sitecore CLI. |
| 2026-10-22 06:06:19 | [Tern.Cli.linux-arm64](https://www.nuget.org/packages/Tern.Cli.linux-arm64) | 0.1.2 | Mark Gibbons | Drop-in, Native AOT replacement for the Sitecore CLI. |
| 2026-10-22 06:06:22 | [Tern.Cli.osx-arm64](https://www.nuget.org/packages/Tern.Cli.osx-arm64) | 0.1.2 | Mark Gibbons | Drop-in, Native AOT replacement for the Sitecore CLI. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
