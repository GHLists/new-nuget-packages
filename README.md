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

## Latest list — 2026-10-17 13:21 UTC

New packages created between 2026-10-17 12:20 UTC and 2026-10-17 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T13-21-37-022996Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 12:35:47 | [RodriOliveira.AdrGuard.Mcp](https://www.nuget.org/packages/RodriOliveira.AdrGuard.Mcp) | 1.0.0 | Rodrigo de Oliveira | Expose bounded, read-only Architecture Decision Record discovery, validation, i… |
| 2026-10-17 12:39:28 | [VL.AdvancedGlassWindow](https://www.nuget.org/packages/VL.AdvancedGlassWindow) | 1.0.0 | murxylink; torinos-yt | Transparent Stride and Skia windows for vvvv gamma 7.4. Includes SceneWindow (G… |
| 2026-10-17 12:39:38 | [cheqi-sdk](https://www.nuget.org/packages/cheqi-sdk) | 3.0.0 | Cheqi | Official .NET SDK for Cheqi - End-to-end encrypted digital receipt processing |
| 2026-10-17 12:45:06 | [Mpgsql.Protocol](https://www.nuget.org/packages/Mpgsql.Protocol) | 1.0.0 | Belov Ilya and contributors | Minimalistic standalone PostgreSQL protocol 3.0 message codecs, binary type con… |
| 2026-10-17 12:45:23 | [WpfDesignGuard.Cli](https://www.nuget.org/packages/WpfDesignGuard.Cli) | 0.2.1 | WpfDesignGuard contributors | WpfDesignGuard governance CLI: dual-layer ratchet gate (hard-zero domains + glo… |
| 2026-10-17 12:45:23 | [WpfDesignGuard.Analyzers](https://www.nuget.org/packages/WpfDesignGuard.Analyzers) | 0.2.1 | WpfDesignGuard contributors | WPF design-system violations at compile time: XAML incremental generator consum… |
| 2026-10-17 12:45:24 | [WpfDesignGuard.Core](https://www.nuget.org/packages/WpfDesignGuard.Core) | 0.2.1 | WpfDesignGuard contributors | WpfDesignGuard rule engine: XAML model parsing, designguard.json model, exempti… |
| 2026-10-17 12:53:38 | [GerardSmit.FtpServer.Sockets](https://www.nuget.org/packages/GerardSmit.FtpServer.Sockets) | 0.0.1 | Gerard Smit | Raw-socket hosting for GerardSmit.FtpServer.Core, as an IHostedService. |
| 2026-10-17 12:53:38 | [GerardSmit.FtpServer.Core](https://www.nuget.org/packages/GerardSmit.FtpServer.Core) | 0.0.1 | Gerard Smit | FTP(S) server protocol implementation for .NET: commands, sessions, data connec… |
| 2026-10-17 12:53:39 | [GerardSmit.FtpServer.Kestrel](https://www.nuget.org/packages/GerardSmit.FtpServer.Kestrel) | 0.0.1 | Gerard Smit | Kestrel hosting for GerardSmit.FtpServer.Core: serve FTP from an ASP.NET Core a… |
| 2026-10-17 12:58:38 | [Prowl.Graphite.Debugger](https://www.nuget.org/packages/Prowl.Graphite.Debugger) | 3.8.0 | Prowl Contributors | Records Graphite graph executions into a serializable trace and replays them do… |
| 2026-10-17 12:58:42 | [Prowl.Prism](https://www.nuget.org/packages/Prowl.Prism) | 3.8.0 | Prowl Contributors | A GLSL to SPIR-V compiler for the Prowl engine. Parses GLSL (preprocessor, toke… |
| 2026-10-17 13:01:23 | [EluciusFTW.SpectreTuff.Elmish](https://www.nuget.org/packages/EluciusFTW.SpectreTuff.Elmish) | 0.14.14 | Guy Buss, Daniel Muckelbauer | Run Elmish applications on SpectreTuff: key and tick subscriptions, terminal se… |
| 2026-10-17 13:01:47 | [Corvo.Nfse](https://www.nuget.org/packages/Corvo.Nfse) | 0.1.1 | Corvo Technology | .NET SDK for the Corvo NFS-e API: issue Brazilian service invoices, calculate t… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
