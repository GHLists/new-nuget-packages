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

## Latest list — 2026-10-07 20:22 UTC

New packages created between 2026-10-07 19:20 UTC and 2026-10-07 20:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T20-22-13-900913Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 19:21:06 | [Coree.Analyzers.CodeClarity](https://www.nuget.org/packages/Coree.Analyzers.CodeClarity) | 0.1.4 | Carsten Riedel | Roslyn analyzer for C# readability. CCCRC001 flags a return expression that exc… |
| 2026-10-07 19:34:53 | [ShotDetector.Native.linux-arm64](https://www.nuget.org/packages/ShotDetector.Native.linux-arm64) | 0.7.0 | Jakob Boman | FFmpeg 8.1.3's shared libraries for linux-arm64, built for decoding only (no en… |
| 2026-10-07 19:34:54 | [ShotDetector.Native.linux-musl-x64](https://www.nuget.org/packages/ShotDetector.Native.linux-musl-x64) | 0.7.0 | Jakob Boman | FFmpeg 8.1.3's shared libraries for linux-musl-x64, built for decoding only (no… |
| 2026-10-07 19:34:55 | [ShotDetector.Native.linux-x64](https://www.nuget.org/packages/ShotDetector.Native.linux-x64) | 0.7.0 | Jakob Boman | FFmpeg 8.1.3's shared libraries for linux-x64, built for decoding only (no enco… |
| 2026-10-07 19:34:56 | [ShotDetector.Native.osx-arm64](https://www.nuget.org/packages/ShotDetector.Native.osx-arm64) | 0.7.0 | Jakob Boman | FFmpeg 8.1.3's shared libraries for osx-arm64, built for decoding only (no enco… |
| 2026-10-07 19:34:57 | [ShotDetector.Native.win-x64](https://www.nuget.org/packages/ShotDetector.Native.win-x64) | 0.7.0 | Jakob Boman | FFmpeg 8.1.3's shared libraries for win-x64, built for decoding only (no encode… |
| 2026-10-07 19:50:20 | [OpenFeature.Providers.Flagd.Core](https://www.nuget.org/packages/OpenFeature.Providers.Flagd.Core) | 1.0.0 | Todd Baert | In-process flagd flag evaluation engine for .NET, for use by flagd providers |
| 2026-10-07 19:51:31 | [CodeBrix.Platform.PlayTest.OpenGL.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.Platform.PlayTest.OpenGL.ApacheLicenseForever) | 1.0.280.1176 | Jeremy Ellis and contributors | Real OpenGL contexts for PlayTest runs of applications that use the Graphics3DG… |
| 2026-10-07 19:51:47 | [CQRSharp.RabbitMQ](https://www.nuget.org/packages/CQRSharp.RabbitMQ) | 5.1.0 | BisocM | A Native-AOT-compatible RabbitMQ transport for CQRSharp. Durable notifications… |
| 2026-10-07 19:51:59 | [MobiOne.Security.Contracts](https://www.nuget.org/packages/MobiOne.Security.Contracts) | 5.0.1 | MobiOne.Security.Contracts | MobiOne application role and authorization contracts. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
