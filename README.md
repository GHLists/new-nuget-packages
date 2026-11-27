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

## Latest list — 2026-11-27 02:20 UTC

New packages created between 2026-11-27 01:21 UTC and 2026-11-27 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T02-20-25-820861Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 01:33:49 | [BYO.Plugin.Infrastructure](https://www.nuget.org/packages/BYO.Plugin.Infrastructure) | 1.44.0-gceec1e4b5e | softwareworkercom | Infrastructure plugin for SoftwareWorker BYO (Build Your Own) CLI, including SQ… |
| 2026-11-27 01:34:09 | [Quick.EntityFrameworkCore.Plus.MongoDB](https://www.nuget.org/packages/Quick.EntityFrameworkCore.Plus.MongoDB) | 2026.11.0 | scbeta | Quick.EntityFrameworkCore.Plus的MongoDB数据库支持。 |
| 2026-11-27 01:46:51 | [Clc.Authentication](https://www.nuget.org/packages/Clc.Authentication) | 1.0.1 | Central Library Consortium | Microsoft Entra ID sign-in and CLC membership authorization for ASP.NET Core we… |
| 2026-11-27 01:47:34 | [Devinno.UI.Wpf](https://www.nuget.org/packages/Devinno.UI.Wpf) | 0.9.2 | Devinno | WPF adapter for Devinno.UI: ViewControl puts a DvApp in a WPF window (IME text… |
| 2026-11-27 01:58:32 | [MvcThrottle2](https://www.nuget.org/packages/MvcThrottle2) | 3.0.1 | John J Scott | MvcThrottle2 filter is designed for controlling the rate of requests that clien… |
| 2026-11-27 01:59:55 | [XH.OA.UTILS](https://www.nuget.org/packages/XH.OA.UTILS) | 6.26.600 | XhLab | XH实验室管理通用方法代码库 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
