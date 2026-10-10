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

## Latest list — 2026-10-10 08:21 UTC

New packages created between 2026-10-10 07:20 UTC and 2026-10-10 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T08-21-45-06642Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 07:30:07 | [SinkSharp.Sinks.Console](https://www.nuget.org/packages/SinkSharp.Sinks.Console) | 1.0.0 | SinkSharp | Coloured console sink for SinkSharp — high-performance structured logging for .… |
| 2026-10-10 07:31:09 | [Lycen.Abstractions](https://www.nuget.org/packages/Lycen.Abstractions) | 0.4.6 | NRTH | Stable licensed-product contracts for Lycen. |
| 2026-10-10 07:31:10 | [Lycen.DependencyInjection](https://www.nuget.org/packages/Lycen.DependencyInjection) | 0.4.6 | NRTH | Dependency injection helpers for licensed Lycen products. |
| 2026-10-10 07:31:48 | [SinkSharp.Sinks.Dashboard](https://www.nuget.org/packages/SinkSharp.Sinks.Dashboard) | 1.0.0-preview | SinkSharp | Embedded real-time log dashboard for SinkSharp. Mounts on your existing ASP.NET… |
| 2026-10-10 07:32:56 | [SinkSharp.Sinks.File](https://www.nuget.org/packages/SinkSharp.Sinks.File) | 1.0.0 | SinkSharp | Rolling daily JSONL file sink for SinkSharp. Compact Log Event Format (CLEF) co… |
| 2026-10-10 07:39:19 | [Webority.Email.Content](https://www.nuget.org/packages/Webority.Email.Content) | 0.41.0 | Webority Technologies | Email Studio content store: templates authored as content, their versions with… |
| 2026-10-10 07:39:21 | [Webority.Email.Content.Ai](https://www.nuget.org/packages/Webority.Email.Content.Ai) | 0.41.0 | Webority Technologies | AI drafting for Email Studio over Webority.Ai: writes a new draft, improves the… |
| 2026-10-10 07:39:43 | [Webority.Email.Studio](https://www.nuget.org/packages/Webority.Email.Studio) | 0.41.0 | Webority Technologies | Email Studio, the shared admin pages for editable email: the email list and the… |
| 2026-10-10 08:01:02 | [Bfs.Seed.Auth](https://www.nuget.org/packages/Bfs.Seed.Auth) | 0.2.0 | Black Forest Sentinel | Token-Prüfung für Azure Functions (dotnet-isolated) in Sentinel-Seed-Projekten:… |
| 2026-10-10 08:02:59 | [ShotDetector.Native.Gpl.linux-arm64](https://www.nuget.org/packages/ShotDetector.Native.Gpl.linux-arm64) | 1.3.0 | Jakob Boman | ShotDetector.Native's FFmpeg 8.1.3 libraries for linux-arm64 with x264 added, s… |
| 2026-10-10 08:03:00 | [ShotDetector.Native.Gpl.linux-musl-x64](https://www.nuget.org/packages/ShotDetector.Native.Gpl.linux-musl-x64) | 1.3.0 | Jakob Boman | ShotDetector.Native's FFmpeg 8.1.3 libraries for linux-musl-x64 with x264 added… |
| 2026-10-10 08:03:01 | [ShotDetector.Native.Gpl.linux-x64](https://www.nuget.org/packages/ShotDetector.Native.Gpl.linux-x64) | 1.3.0 | Jakob Boman | ShotDetector.Native's FFmpeg 8.1.3 libraries for linux-x64 with x264 added, so… |
| 2026-10-10 08:03:02 | [ShotDetector.Native.Gpl.osx-arm64](https://www.nuget.org/packages/ShotDetector.Native.Gpl.osx-arm64) | 1.3.0 | Jakob Boman | ShotDetector.Native's FFmpeg 8.1.3 libraries for osx-arm64 with x264 added, so… |
| 2026-10-10 08:03:04 | [ShotDetector.Native.Gpl.win-x64](https://www.nuget.org/packages/ShotDetector.Native.Gpl.win-x64) | 1.3.0 | Jakob Boman | ShotDetector.Native's FFmpeg 8.1.3 libraries for win-x64 with x264 added, so Fr… |
| 2026-10-10 08:04:42 | [Webority.Store](https://www.nuget.org/packages/Webority.Store) | 0.1.2 | Webority Technologies | App store presence for Webority products: the store app, review, reply draft, l… |
| 2026-10-10 08:04:44 | [Webority.Store.Admin](https://www.nuget.org/packages/Webority.Store.Admin) | 0.1.2 | Webority Technologies | The marketing team's store pages for Webority admin portals: the reviews inbox… |
| 2026-10-10 08:04:46 | [Webority.Store.Ai](https://www.nuget.org/packages/Webority.Store.Ai) | 0.1.2 | Webority Technologies | AI for Webority store work: drafts review replies from each app's reply guide,… |
| 2026-10-10 08:04:48 | [Webority.Store.EntityFrameworkCore](https://www.nuget.org/packages/Webority.Store.EntityFrameworkCore) | 0.1.2 | Webority Technologies | Stores Webority store data in the product's own database: the entity configurat… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
