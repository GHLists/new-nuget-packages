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

## Latest list — 2026-10-11 12:21 UTC

New packages created between 2026-10-11 11:19 UTC and 2026-10-11 12:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T12-21-16-680031Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 11:19:21 | [ELF.Modules.Hosting.Sidecar](https://www.nuget.org/packages/ELF.Modules.Hosting.Sidecar) | 0.8.0 | ELF INTERNATIONAL EXPRESS CO.… | 讓 ASP.NET Core 宿主以桌面殼（Tauri、Electron）子行程執行：127.0.0.1 隨機埠、stdout 交握埠號、stdin 關閉或父… |
| 2026-10-11 11:19:23 | [GameFrameX.Foundation.Logger.GrafanaLoki](https://www.nuget.org/packages/GameFrameX.Foundation.Logger.GrafanaLoki) | 5.0.0 | AlianBlank,GameFrameX,Blank | GameFrameX.Foundation.Logger.GrafanaLoki,GameFrameX 框架的基础设施框架库,提供日志的 Grafana Lo… |
| 2026-10-11 11:19:24 | [GameFrameX.Foundation.Logger.MongoDB](https://www.nuget.org/packages/GameFrameX.Foundation.Logger.MongoDB) | 5.0.0 | AlianBlank,GameFrameX,Blank | GameFrameX.Foundation.Logger.MongoDB,GameFrameX 框架的基础设施框架库,提供日志的 MongoDB Sink 组… |
| 2026-10-11 11:26:01 | [ZYC.Framework.Core](https://www.nuget.org/packages/ZYC.Framework.Core) | 1.5.5 | ZYC.Framework.Core | Package Description |
| 2026-10-11 11:36:36 | [BIDS.Server](https://www.nuget.org/packages/BIDS.Server) | 6.6.3-commit-b25682… | Performa Software Pty Ltd | PowerShell module for managing BIDS Servers |
| 2026-10-11 11:36:38 | [BIDS.Studio](https://www.nuget.org/packages/BIDS.Studio) | 6.6.3-commit-b25682… | Performa Software Pty Ltd | PowerShell module for installing BIDS Studio |
| 2026-10-11 11:48:19 | [CodoMetis.TypeKit.Serilog](https://www.nuget.org/packages/CodoMetis.TypeKit.Serilog) | 1.5.0 | CaffeinatedCoder | Serilog integration for CodoMetis.TypeKit: value objects are logged as what the… |
| 2026-10-11 11:48:20 | [CodoMetis.TypeKit.Testing](https://www.nuget.org/packages/CodoMetis.TypeKit.Testing) | 1.5.0 | CaffeinatedCoder | Test assertions for CodoMetis.TypeKit's Option and Result: hand a test the valu… |
| 2026-10-11 11:52:50 | [SjolystInnovation.AppKit.Vipps](https://www.nuget.org/packages/SjolystInnovation.AppKit.Vipps) | 0.1.1 | Sjølyst Innovation AS | A client for the Vipps MobilePay Recurring, ePayment, Userinfo and Webhooks API… |
| 2026-10-11 11:55:29 | [Arc56.Generated.tolgazorlu.nftmap](https://www.nuget.org/packages/Arc56.Generated.tolgazorlu.nftmap) | 1.0.1.2026101111 | tolgazorlu | Generated ARC-56 Algorand smart-contract clients for tolgazorlu/nftmap. |
| 2026-10-11 12:15:51 | [GaussStylization](https://www.nuget.org/packages/GaussStylization) | 0.1.0 | Nicholas Chieppa | Managed C# port of Gauss Stylization (mesh stylization from preferred surface n… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
