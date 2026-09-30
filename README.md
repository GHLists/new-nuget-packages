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

## Latest list — 2026-09-30 02:21 UTC

New packages created between 2026-09-30 01:20 UTC and 2026-09-30 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T02-21-39-064801Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 01:20:55 | [reflgen](https://www.nuget.org/packages/reflgen) | 1.0.0 | 29thnight | Macro-free, attribute-driven C++20 reflection for Visual C++ projects. Installi… |
| 2026-09-30 01:24:33 | [WASU.Plugin.Minio](https://www.nuget.org/packages/WASU.Plugin.Minio) | 26.930.9 | WASU.Plugin.Minio | Package Description |
| 2026-09-30 01:26:34 | [polanes.project.Domain](https://www.nuget.org/packages/polanes.project.Domain) | 0.0.1-alphabeta1 | polanes.project.Domain | Package Description |
| 2026-09-30 01:36:50 | [Sitecore.XmCloud.XA.JSS.Foundation.Theming](https://www.nuget.org/packages/Sitecore.XmCloud.XA.JSS.Foundation.Theming) | 1.10.13 | Sitecore Corporation A/S | Sitecore Experience Accelerator 40.5.54 |
| 2026-09-30 01:37:07 | [Sitecore.XmCloud.XA.JSS.Foundation.JSONLD](https://www.nuget.org/packages/Sitecore.XmCloud.XA.JSS.Foundation.JSONLD) | 1.10.13 | Sitecore Corporation A/S | Sitecore Experience Accelerator 40.5.54 |
| 2026-09-30 01:37:45 | [FrameFlow.Inference.OpenVino](https://www.nuget.org/packages/FrameFlow.Inference.OpenVino) | 0.13.0 | Charles Lee | FrameFlow — cross-platform FFmpeg media pipelines for .NET: decode, encode, pla… |
| 2026-09-30 01:40:27 | [Sitecore.XmCloud.LayoutService.AgenticContext](https://www.nuget.org/packages/Sitecore.XmCloud.LayoutService.AgenticContext) | 1.10.13 | Sitecore | Sitecore Layout Service Agentic Context |
| 2026-09-30 01:41:32 | [Kjt.DotNet.AzureAppServices.Extension.Splunk](https://www.nuget.org/packages/Kjt.DotNet.AzureAppServices.Extension.Splunk) | 1.16.0 | Kyle Tully | Zero-code tracing, metrics and logs for .NET and .NET Framework apps on Windows… |
| 2026-09-30 01:41:34 | [Kjt.DotNet.AzureAppServices.Extension](https://www.nuget.org/packages/Kjt.DotNet.AzureAppServices.Extension) | 1.17.0 | Kyle Tully | Zero-code tracing, metrics and logs for .NET and .NET Framework apps on Windows… |
| 2026-09-30 01:47:31 | [DanceRudiments](https://www.nuget.org/packages/DanceRudiments) | 0.2.0 | Kieran Simkin | C# bindings to the DanceFlow C++ rhythmic motion library. Music: https://kieran… |
| 2026-09-30 01:53:39 | [TKWF.Ext.Authentication](https://www.nuget.org/packages/TKWF.Ext.Authentication) | 0.1.0 | LoongBa.cn 龙爸出品 | TKWF 扩展：认证中心——令牌体系（手写 RS256 JWT + kid 轮换 + 黑名单落库 + Refresh rotation）/ 认证矩阵 Prov… |
| 2026-09-30 01:59:59 | [GtkSharp4.Sdk](https://www.nuget.org/packages/GtkSharp4.Sdk) | 4.22.4.26273 | 'GtkSharp Contributors' | GtkSharp SDK. Enabled via the net8.0-gtk TFM. |
| 2026-09-30 02:00:21 | [Net4x.Vb6ToCSharp.XamarinGtk.UpgradeHelpers](https://www.nuget.org/packages/Net4x.Vb6ToCSharp.XamarinGtk.UpgradeHelpers) | 1.0.0.26273 | Vb6ToCSharp.XamarinGtk.Upgrad… | WPF controls, helpers and common dialogs for VB6 programs converted to C# by Vb… |
| 2026-09-30 02:00:29 | [Net4x.Xamarin.Forms.Gtk3.Controls.Tests](https://www.nuget.org/packages/Net4x.Xamarin.Forms.Gtk3.Controls.Tests) | 5.0.0.1 | Microsoft | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
