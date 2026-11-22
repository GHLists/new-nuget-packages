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

## Latest list — 2026-11-22 21:19 UTC

New packages created between 2026-11-22 20:19 UTC and 2026-11-22 21:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T21-19-46-004873Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 20:24:07 | [VisioForge.CrossPlatform.OpenCV.Windows.arm64](https://www.nuget.org/packages/VisioForge.CrossPlatform.OpenCV.Windows.arm64) | 2026.11.16 | VisioForge | OpenCV computer vision libraries package for VisioForge .NET SDKs. Enables adva… |
| 2026-11-22 20:24:23 | [CUDAPython.Dotnet.win-x64](https://www.nuget.org/packages/CUDAPython.Dotnet.win-x64) | 0.1.1 | CUDAPython.Dotnet.Nuget | Self-contained Windows x64 .NET wrapper for CUDA Python, including CPython and… |
| 2026-11-22 20:30:43 | [Cyberdot.Jotter](https://www.nuget.org/packages/Cyberdot.Jotter) | 1.0.0 | cyberdot | Jotter is an F# static site generator for Markdown blogs with paginated indexes… |
| 2026-11-22 20:34:04 | [Chris82111.GitManager.GitWrapper.Static.LinuxX64](https://www.nuget.org/packages/Chris82111.GitManager.GitWrapper.Static.LinuxX64) | 1.0.0 | Chris82111 | Plugin to extend the Core solution for using Git in a portable form. Supports:… |
| 2026-11-22 20:35:24 | [Chris82111.GitManager.GitWrapper.Static.WindowsX64](https://www.nuget.org/packages/Chris82111.GitManager.GitWrapper.Static.WindowsX64) | 1.0.0 | Chris82111 | Plugin to extend the Core solution for using Git in a portable form. Supports:… |
| 2026-11-22 20:42:42 | [Agilis.Ads](https://www.nuget.org/packages/Agilis.Ads) | 0.1.0 | Agilis Dating Ltd | Official .NET client for the Agilis Advertising REST API: Offers, Events, webho… |
| 2026-11-22 20:47:58 | [Zharp](https://www.nuget.org/packages/Zharp) | 0.1.0 | Zharp | Zharp for .NET: errors with the code that ran, traces, failed queries, request… |
| 2026-11-22 20:48:00 | [Zharp.AspNet](https://www.nuget.org/packages/Zharp.AspNet) | 0.1.0 | Zharp | Zharp for classic ASP.NET on .NET Framework (MVC 5, Web API 2, WebForms) on IIS… |
| 2026-11-22 20:48:01 | [Zharp.AspNet.WebApi](https://www.nuget.org/packages/Zharp.AspNet.WebApi) | 0.1.0 | Zharp | Zharp for ASP.NET Web API 2 on .NET Framework: config.AddZharp() reports what c… |
| 2026-11-22 20:48:02 | [Zharp.AspNetCore](https://www.nuget.org/packages/Zharp.AspNetCore) | 0.1.0 | Zharp | Zharp for ASP.NET Core: builder.Services.AddZharp() traces every request by its… |
| 2026-11-22 20:48:03 | [Zharp.AwsLambda](https://www.nuget.org/packages/Zharp.AwsLambda) | 0.1.0 | Zharp | Zharp for .NET on AWS Lambda: ZharpLambda.Wrap(handler) traces each invocation… |
| 2026-11-22 20:48:04 | [Zharp.Build](https://www.nuget.org/packages/Zharp.Build) | 0.1.0 | Zharp | Zharp's MSBuild step: after a Release build, uploads the project's sources as a… |
| 2026-11-22 20:48:05 | [Zharp.GoogleCloudFunctions](https://www.nuget.org/packages/Zharp.GoogleCloudFunctions) | 0.1.0 | Zharp | Zharp for .NET on Google Cloud Run functions (Cloud Functions): one assembly at… |
| 2026-11-22 20:50:22 | [Chris82111.GitManager.GitWrapper.Static.Any](https://www.nuget.org/packages/Chris82111.GitManager.GitWrapper.Static.Any) | 1.0.0 | Chris82111 | Plugin to extend the Core solution for using Git in a portable form. Supports:… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
