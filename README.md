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

## Latest list — 2026-11-26 20:20 UTC

New packages created between 2026-11-26 19:20 UTC and 2026-11-26 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T20-20-38-071274Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 19:21:01 | [Hyperplane.NET](https://www.nuget.org/packages/Hyperplane.NET) | 0.1.3 | David Obando | Vector Decision Model (VDM) library for .NET written in G#: typed Choice, Score… |
| 2026-11-26 19:21:02 | [Hyperplane.Cider](https://www.nuget.org/packages/Hyperplane.Cider) | 0.1.3 | David Obando | Optional reader adapter for Hyperplane.NET: CiderEmbedder turns any Cider.NET I… |
| 2026-11-26 19:21:07 | [Hyperplane.Server](https://www.nuget.org/packages/Hyperplane.Server) | 0.1.3 | David Obando | Local HTTP server for Hyperplane vector decision models: the Decisions API (/ap… |
| 2026-11-26 19:30:16 | [Kitpymes.Core.Mapper](https://www.nuget.org/packages/Kitpymes.Core.Mapper) | 1.0.0 | Kitpymes, Sebastian R Ferrari | Mapeo explícito sin reflexión: cada mapeo es una clase escrita a mano (IMapper… |
| 2026-11-26 19:32:54 | [Croner](https://www.nuget.org/packages/Croner) | 1.0.0 | Hexagon | Cron for .NET: parse cron expressions (seconds, years, L, W, #, +), find next a… |
| 2026-11-26 19:41:21 | [Casazium.License](https://www.nuget.org/packages/Casazium.License) | 0.1.0 | Casazium | The .NET SDK for the Casazium License Server: activate and verify license keys,… |
| 2026-11-26 19:44:09 | [EdsDcfNet.Checker](https://www.nuget.org/packages/EdsDcfNet.Checker) | 1.17.0 | Dietmar Borgards | edsdcf-check: command-line validator for CiA 306 EDS and DCF files, built on th… |
| 2026-11-26 19:44:23 | [Hyperbee.Expressions.Abstractions](https://www.nuget.org/packages/Hyperbee.Expressions.Abstractions) | 1.7.0 | Stillpoint Software, Inc. | Compiler and coroutine contracts shared by Hyperbee.Expressions and its compile… |
| 2026-11-26 19:48:52 | [BitMagic.Cc65Lib](https://www.nuget.org/packages/BitMagic.Cc65Lib) | 0.1.92 | Yazwh0 | X16 Emulator and Debugger |
| 2026-11-26 19:48:54 | [BitMagic.ZiModem.Net](https://www.nuget.org/packages/BitMagic.ZiModem.Net) | 0.1.92 | Yazwh0 | C# binding for zimodem running as a host library, giving a Hayes-compatible Wi-… |
| 2026-11-26 19:49:05 | [BitMagic.X16Debugger](https://www.nuget.org/packages/BitMagic.X16Debugger) | 0.1.92 | Yazwh0 | X16 Emulator and Debugger |
| 2026-11-26 19:49:49 | [CrCore.Maui](https://www.nuget.org/packages/CrCore.Maui) | 11.0.0 | apptade | CrCore.Maui is a .NET MAUI library: controls, converters, and more, built with… |
| 2026-11-26 20:12:51 | [EgyptianId](https://www.nuget.org/packages/EgyptianId) | 1.0.0 | Ahmed Mohamed Gaber | Offline validation and parsing of the 14-digit Egyptian national ID number (الر… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
