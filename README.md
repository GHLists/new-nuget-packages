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

## Latest list — 2026-10-20 07:21 UTC

New packages created between 2026-10-20 06:21 UTC and 2026-10-20 07:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T07-21-28-474517Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 06:21:15 | [WebFilez.Storage.AmazonS3](https://www.nuget.org/packages/WebFilez.Storage.AmazonS3) | 1.0.0 | Matt Gordon | Amazon S3 provider for WebFilez. Register it with AddWebFilezAmazonS3(). |
| 2026-10-20 06:21:29 | [WebFilez.Storage.AzureBlob](https://www.nuget.org/packages/WebFilez.Storage.AzureBlob) | 1.0.0 | Matt Gordon | Azure Blob Storage provider for WebFilez. Register it with AddWebFilezAzureBlob… |
| 2026-10-20 06:21:46 | [WebFilez.Storage.GoogleCloud](https://www.nuget.org/packages/WebFilez.Storage.GoogleCloud) | 1.0.0 | Matt Gordon | Google Cloud Storage provider for WebFilez. Register it with AddWebFilezGoogleC… |
| 2026-10-20 06:22:05 | [WebFilez.Plugins.FileRobot](https://www.nuget.org/packages/WebFilez.Plugins.FileRobot) | 1.0.0 | Matt Gordon | Optional FileRobot image editor for WebFilez. Load filerobot.js and map its id… |
| 2026-10-20 06:22:22 | [WebFilez.Plugins.FortuneSheet](https://www.nuget.org/packages/WebFilez.Plugins.FortuneSheet) | 1.0.0 | Matt Gordon | Optional Fortune Sheet editor for WebFilez. Load fortunesheet.js and map its id… |
| 2026-10-20 06:22:37 | [WebFilez.Plugins.SuperDoc](https://www.nuget.org/packages/WebFilez.Plugins.SuperDoc) | 1.0.0 | Matt Gordon | Optional SuperDoc editor for WebFilez. Load superdoc.js and map its id with the… |
| 2026-10-20 06:37:20 | [Frontmatec.UpdateManagement](https://www.nuget.org/packages/Frontmatec.UpdateManagement) | 0.1.1 | Frontmatec | Updates of an installed app, whatever installed it: check, download, apply and… |
| 2026-10-20 06:37:21 | [Frontmatec.UpdateManagement.Velopack](https://www.nuget.org/packages/Frontmatec.UpdateManagement.Velopack) | 0.1.1 | Frontmatec | Updates of an app installed with Velopack, from its update feed in the Frontmat… |
| 2026-10-20 06:37:22 | [Frontmatec.UpdateManagement.Windows](https://www.nuget.org/packages/Frontmatec.UpdateManagement.Windows) | 0.1.1 | Frontmatec | The update check, question and progress of a WPF app, in English and Danish. |
| 2026-10-20 06:45:58 | [Majo.Command](https://www.nuget.org/packages/Majo.Command) | 0.0.1 | Sweety Majo | A lightweight, typed command-tree library for .NET. |
| 2026-10-20 06:48:46 | [NewLife.JT1078](https://www.nuget.org/packages/NewLife.JT1078) | 1.0.2026.1020-beta0… | 新生命开发团队 | JT/T 1078 视频通讯协议核心实现，包括RTP报文解析、音视频编解码、H.264解析 |
| 2026-10-20 06:48:47 | [NewLife.JT1078.Server](https://www.nuget.org/packages/NewLife.JT1078.Server) | 1.0.2026.1020-beta0… | 新生命开发团队 | 基于NewLife.Net的JT1078 TCP服务端，支持RTP分包合并和设备会话管理 |
| 2026-10-20 06:59:28 | [NewLife.JT808](https://www.nuget.org/packages/NewLife.JT808) | 1.1.2026.1020-beta0… | 新生命开发团队 | JT/T 808车辆定位协议完整实现，支持2011/2013/2019版本 |
| 2026-10-20 07:06:09 | [ClamChart](https://www.nuget.org/packages/ClamChart) | 1.0.0 | machi_pon | MAUI charts for dashboards and widgets rendered with SkiaSharp |
| 2026-10-20 07:12:52 | [devdeer.Libraries.AspNetCore.Blazor](https://www.nuget.org/packages/devdeer.Libraries.AspNetCore.Blazor) | 0.1.0-alpha | DEVDEER GmbH | Initialization and configuration including useful base types for ASP.NET Core B… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
