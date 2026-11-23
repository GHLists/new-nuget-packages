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

## Latest list — 2026-11-23 10:21 UTC

New packages created between 2026-11-23 09:21 UTC and 2026-11-23 10:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T10-21-13-799751Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 09:23:33 | [Orkeon.Interop.AgentCli](https://www.nuget.org/packages/Orkeon.Interop.AgentCli) | 1.4.0 | Orkeon Contributors | Experimental agent CLI provider for Orkeon (ADR-020): an Orkeon agent answered… |
| 2026-11-23 09:24:35 | [Fleans.Plugins.JavaScript](https://www.nuget.org/packages/Fleans.Plugins.JavaScript) | 0.15.0 | nightBaker | Fleans JavaScript plugin — runs <scriptTask scriptFormat="javascript"> out of t… |
| 2026-11-23 09:42:53 | [UEditorNetCore10](https://www.nuget.org/packages/UEditorNetCore10) | 1.0.0 | UEditorNetCore | Package Description |
| 2026-11-23 09:45:48 | [GizmoSDK.GPF.Common](https://www.nuget.org/packages/GizmoSDK.GPF.Common) | 2.12.352.1 | GizmoSDK team (gizmosdk@saabg… | Toolkit-independent managed GPF module contracts, properties, notifications, re… |
| 2026-11-23 09:45:52 | [GizmoSDK.GPF](https://www.nuget.org/packages/GizmoSDK.GPF) | 2.12.352.1 | GizmoSDK team (gizmosdk@saabg… | Managed C# contracts, Avalonia presentation, native bridge and GPFMain host for… |
| 2026-11-23 09:45:59 | [GizmoSDK.CCT](https://www.nuget.org/packages/GizmoSDK.CCT) | 2.12.352.1 | GizmoSDK team (gizmosdk@saabg… | Managed CCT plugin components for the GizmoSDK Plugin Framework. The package co… |
| 2026-11-23 09:47:28 | [ISL.NetFramework.Booking.Application](https://www.nuget.org/packages/ISL.NetFramework.Booking.Application) | 2.6.1 | ISL.com | Availability engine, holiday rules, and booking orchestration for the ISL appoi… |
| 2026-11-23 09:47:32 | [ISL.NetFramework.Booking.Infrastructure](https://www.nuget.org/packages/ISL.NetFramework.Booking.Infrastructure) | 2.6.3 | ISL.com | Vendor adapters (Microsoft Bookings via Graph), token acquisition, persistence,… |
| 2026-11-23 09:48:30 | [ISL.NetFramework.QrCode.Application](https://www.nuget.org/packages/ISL.NetFramework.QrCode.Application) | 2.5.0 | ISL.com | Generation orchestrator and request validation for the ISL QR code framework. |
| 2026-11-23 09:48:34 | [ISL.NetFramework.QrCode.Infrastructure](https://www.nuget.org/packages/ISL.NetFramework.QrCode.Infrastructure) | 2.5.0 | ISL.com | Renderers (QRCoder, ZXing.Net), logo compositors, and the FileUpload-backed sto… |
| 2026-11-23 09:48:39 | [ISL.NetFramework.Scheduling](https://www.nuget.org/packages/ISL.NetFramework.Scheduling) | 1.0.0 | ISL.com | Scheduling core: database-driven schedule reconciler, generic job dispatcher, h… |
| 2026-11-23 09:48:47 | [ISL.NetFramework.Scheduling.Abstractions](https://www.nuget.org/packages/ISL.NetFramework.Scheduling.Abstractions) | 1.0.0 | ISL.com | Scheduling contracts: handler interface, execution context, schedule descriptor… |
| 2026-11-23 09:49:33 | [Vercel.AI.Mistral.LiveKit](https://www.nuget.org/packages/Vercel.AI.Mistral.LiveKit) | 0.4.0 | hardkoded | LiveKit adapter for the Mistral realtime transport of the community .NET port o… |
| 2026-11-23 09:54:32 | [Modellkapitaene.BasicLibrary.Data](https://www.nuget.org/packages/Modellkapitaene.BasicLibrary.Data) | 0.0.1.52-pre | Modellkapitaene.net | Package Description |
| 2026-11-23 09:59:56 | [SabakaLang.AspNet](https://www.nuget.org/packages/SabakaLang.AspNet) | 0.1.0 | sabaka-chabaka | Write ASP.NET Minimal API controllers in SabakaLang. |
| 2026-11-23 10:02:02 | [Credfeto.ChangeLog.Cmd.any](https://www.nuget.org/packages/Credfeto.ChangeLog.Cmd.any) | 1.10.219.2997-pack-… | Mark Ridgwell | Changelog manager dotnet tool. |
| 2026-11-23 10:12:05 | [H.OxyPlot.Uno.WinUI](https://www.nuget.org/packages/H.OxyPlot.Uno.WinUI) | 0.9.1 | havendv, OxyPlot contributors… | OxyPlot is a plotting library for .NET. This is package contains the UWP/WinUI/… |
| 2026-11-23 10:17:04 | [VirtoCommerce.SiteBuilder.Data.SqlServer](https://www.nuget.org/packages/VirtoCommerce.SiteBuilder.Data.SqlServer) | 3.1000.0 | VirtoCommerce.SiteBuilder.Dat… | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
