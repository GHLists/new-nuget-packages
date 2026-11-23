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

## Latest list — 2026-11-23 04:21 UTC

New packages created between 2026-11-23 03:21 UTC and 2026-11-23 04:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T04-21-25-255858Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 03:27:14 | [DZen.Adiantum](https://www.nuget.org/packages/DZen.Adiantum) | 1.0.0 | Joe Dluzen | Pure managed C# implementation of the Adiantum length-preserving encryption con… |
| 2026-11-23 03:29:14 | [GameVoice](https://www.nuget.org/packages/GameVoice) | 1.0.0 | djaus2 | Reusable Blazor Server voice chat: push-to-talk speech recognition, text-to-spe… |
| 2026-11-23 03:34:06 | [DbnSuite.Fetch.linux-arm64](https://www.nuget.org/packages/DbnSuite.Fetch.linux-arm64) | 0.5.0 | SquidEyes | DbnFetch (dbnf): download raw and processed market data from a DbnSync archive… |
| 2026-11-23 03:34:10 | [DbnSuite.Fetch.osx-x64](https://www.nuget.org/packages/DbnSuite.Fetch.osx-x64) | 0.5.0 | SquidEyes | DbnFetch (dbnf): download raw and processed market data from a DbnSync archive… |
| 2026-11-23 03:44:23 | [Dimina.Desktop](https://www.nuget.org/packages/Dimina.Desktop) | 1.9.0 | Dimina Contributors | Standalone Dimina mini-program windows for desktop .NET hosts |
| 2026-11-23 04:01:04 | [CodeBrix.WebPlatform.Backend.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.Backend.ApacheLicenseForever) | 1.0.327.240 | Jeremy Ellis | The ASP.NET Core plumbing of a CodeBrix.WebPlatform backend, in one services ca… |
| 2026-11-23 04:01:26 | [CodeBrix.WebPlatform.BackendMapper.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.BackendMapper.ApacheLicenseForever) | 1.0.327.240 | Jeremy Ellis | A build-time library that reads the REST controllers and SignalR hubs of a comp… |
| 2026-11-23 04:01:45 | [CodeBrix.WebPlatform.Core.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.Core.ApacheLicenseForever) | 1.0.327.240 | Jeremy Ellis | The shared definitions of the CodeBrix.WebPlatform web application platform: th… |
| 2026-11-23 04:03:01 | [CodeBrix.WebPlatform.FrontendBuilder.LinuxArm64.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.FrontendBuilder.LinuxArm64.ApacheLicenseForever) | 1.0.327.240 | Jeremy Ellis | The prebuilt build tools of the CodeBrix.WebPlatform web application platform f… |
| 2026-11-23 04:03:27 | [CodeBrix.WebPlatform.FrontendBuilder.LinuxX64.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.FrontendBuilder.LinuxX64.ApacheLicenseForever) | 1.0.327.240 | Jeremy Ellis | The prebuilt build tools of the CodeBrix.WebPlatform web application platform f… |
| 2026-11-23 04:04:21 | [CodeBrix.WebPlatform.FrontendBuilder.MacOSArm64.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.FrontendBuilder.MacOSArm64.ApacheLicenseForever) | 1.0.327.240 | Jeremy Ellis | The prebuilt build tools of the CodeBrix.WebPlatform web application platform f… |
| 2026-11-23 04:04:50 | [CodeBrix.WebPlatform.FrontendBuilder.MacOSX64.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.FrontendBuilder.MacOSX64.ApacheLicenseForever) | 1.0.327.240 | Jeremy Ellis | The prebuilt build tools of the CodeBrix.WebPlatform web application platform f… |
| 2026-11-23 04:05:23 | [CodeBrix.WebPlatform.FrontendBuilder.WindowsX64.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.FrontendBuilder.WindowsX64.ApacheLicenseForever) | 1.0.327.240 | Jeremy Ellis | The prebuilt build tools of the CodeBrix.WebPlatform web application platform f… |
| 2026-11-23 04:08:36 | [PalORM.Sqlite](https://www.nuget.org/packages/PalORM.Sqlite) | 6.9.0 | PalDDD | PalORM SQLite Provider — Microsoft.Data.Sqlite.Core + SQLite3MC 适配 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
