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

## Latest list — 2026-10-24 06:20 UTC

New packages created between 2026-10-24 05:21 UTC and 2026-10-24 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T06-20-23-304602Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 05:27:00 | [Douze.any](https://www.nuget.org/packages/Douze.any) | 0.2.0 | Sebastien Ros | Stupidly simple, blazing fast static site generator. |
| 2026-10-24 05:27:02 | [Douze.linux-arm64](https://www.nuget.org/packages/Douze.linux-arm64) | 0.2.0 | Sebastien Ros | Stupidly simple, blazing fast static site generator. |
| 2026-10-24 05:27:04 | [Douze.linux-x64](https://www.nuget.org/packages/Douze.linux-x64) | 0.2.0 | Sebastien Ros | Stupidly simple, blazing fast static site generator. |
| 2026-10-24 05:27:06 | [Douze.osx-arm64](https://www.nuget.org/packages/Douze.osx-arm64) | 0.2.0 | Sebastien Ros | Stupidly simple, blazing fast static site generator. |
| 2026-10-24 05:27:08 | [Douze.osx-x64](https://www.nuget.org/packages/Douze.osx-x64) | 0.2.0 | Sebastien Ros | Stupidly simple, blazing fast static site generator. |
| 2026-10-24 05:27:14 | [Douze.win-arm64](https://www.nuget.org/packages/Douze.win-arm64) | 0.2.0 | Sebastien Ros | Stupidly simple, blazing fast static site generator. |
| 2026-10-24 05:27:16 | [Douze.win-x64](https://www.nuget.org/packages/Douze.win-x64) | 0.2.0 | Sebastien Ros | Stupidly simple, blazing fast static site generator. |
| 2026-10-24 05:27:17 | [Douze](https://www.nuget.org/packages/Douze) | 0.2.0 | Sebastien Ros | Stupidly simple, blazing fast static site generator. |
| 2026-10-24 05:57:53 | [Qualithm.Platform](https://www.nuget.org/packages/Qualithm.Platform) | 0.1.0 | Qualithm | C# client for the Qualithm Platform API, generated from its OpenAPI spec. |
| 2026-10-24 06:06:01 | [Tickwork.Utilities](https://www.nuget.org/packages/Tickwork.Utilities) | 1.0.0 | Xavier Klausener | The entities, managers and contracts of Tickwork, a background job scheduler fo… |
| 2026-10-24 06:06:01 | [Tickwork.Instrumentation.OpenTelemetry](https://www.nuget.org/packages/Tickwork.Instrumentation.OpenTelemetry) | 1.0.0 | Xavier Klausener | OpenTelemetry tracing for Tickwork jobs. Forked from TickerQ 10.4.0. |
| 2026-10-24 06:06:02 | [Tickwork](https://www.nuget.org/packages/Tickwork) | 1.0.0 | Xavier Klausener | Tickwork is a background job scheduler for .NET: cron and time-based jobs, retr… |
| 2026-10-24 06:10:32 | [Webority.Delivery.SpaHost](https://www.nuget.org/packages/Webority.Delivery.SpaHost) | 0.19.0 | Webority Technologies | A shared host for React single-page apps: serves the app's built files and appl… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
