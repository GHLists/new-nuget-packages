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

## Latest list — 2026-10-27 03:20 UTC

New packages created between 2026-10-27 02:20 UTC and 2026-10-27 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T03-20-23-862583Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 02:43:57 | [udpi30-mcp](https://www.nuget.org/packages/udpi30-mcp) | 1.15.1 | UDP | MCP server exposing UDPI30 operations as tools for Claude Code, Cursor, and oth… |
| 2026-10-27 02:43:57 | [udpi30](https://www.nuget.org/packages/udpi30) | 1.15.1 | UDP | Project definition for Microsoft Unified Data Platform — declarative CI/CD for… |
| 2026-10-27 02:47:14 | [nugetgo.github.com.spf13.cobra](https://www.nuget.org/packages/nugetgo.github.com.spf13.cobra) | 1.10.2 | go2cs conversion | unofficial go2cs C# conversion of github.com/spf13/cobra v1.10.2, built on the… |
| 2026-10-27 02:53:05 | [Soenneker.QrCodes.Generator](https://www.nuget.org/packages/Soenneker.QrCodes.Generator) | 11.0.1 | Jake Soenneker | A utility for generating QR codes. |
| 2026-10-27 02:53:44 | [AppPortal.Abstractions](https://www.nuget.org/packages/AppPortal.Abstractions) | 3.0.384 | AvantiPoint | Shared contracts for AppPortal consent, application context, and telemetry capa… |
| 2026-10-27 02:53:58 | [Soenneker.QrCodes.Reader](https://www.nuget.org/packages/Soenneker.QrCodes.Reader) | 11.0.1 | Jake Soenneker | A utility for reading QR codes. |
| 2026-10-27 02:54:13 | [AppPortal.Telemetry.Maui](https://www.nuget.org/packages/AppPortal.Telemetry.Maui) | 3.0.384 | AvantiPoint | AppPortal telemetry integration for .NET MAUI, including dependency injection a… |
| 2026-10-27 02:54:40 | [AppPortal.Telemetry](https://www.nuget.org/packages/AppPortal.Telemetry) | 3.0.384 | AvantiPoint | AppPortal analytics, crash reporting, structured logs, sessions, and real user… |
| 2026-10-27 02:54:57 | [AppPortal.Telemetry.Prism.Logging](https://www.nuget.org/packages/AppPortal.Telemetry.Prism.Logging) | 3.0.384 | AvantiPoint | AppPortal telemetry provider for Prism Plugin Logging. |
| 2026-10-27 02:55:12 | [AppPortal.Telemetry.Prism.Navigation](https://www.nuget.org/packages/AppPortal.Telemetry.Prism.Navigation) | 3.0.384 | AvantiPoint | AppPortal screen analytics and navigation performance monitoring for Prism regi… |
| 2026-10-27 02:55:31 | [AppPortal.Telemetry.Uno](https://www.nuget.org/packages/AppPortal.Telemetry.Uno) | 3.0.384 | AvantiPoint | AppPortal telemetry integration for Uno Platform applications using the Skia re… |
| 2026-10-27 02:55:47 | [AppPortal.TestKit](https://www.nuget.org/packages/AppPortal.TestKit) | 3.0.384 | AvantiPoint | AppPortal test doubles and recorded-call assertions for unit testing .NET appli… |
| 2026-10-27 02:59:12 | [RecursiveAI.OneAudio.Devices](https://www.nuget.org/packages/RecursiveAI.OneAudio.Devices) | 1.2.0 | Recursive AI, LLC | Audio device playback and capture for OneAudio: WASAPI, Core Audio and ALSA ove… |
| 2026-10-27 03:02:46 | [LogVue.Providers.Abstractions](https://www.nuget.org/packages/LogVue.Providers.Abstractions) | 1.1.0 | Matt Gordon | Contracts for writing events into the LogVue log dashboard. A provider package… |
| 2026-10-27 03:02:50 | [LogVue.Providers.Serilog](https://www.nuget.org/packages/LogVue.Providers.Serilog) | 1.1.0 | Matt Gordon | Serilog sink for the LogVue log dashboard. Reference this only when the host lo… |
| 2026-10-27 03:06:04 | [Meziantou.Framework.SnapshotTesting.Pdf](https://www.nuget.org/packages/Meziantou.Framework.SnapshotTesting.Pdf) | 1.0.0 | meziantou | Enables verification of PDF documents using file-based snapshots: each page is… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
