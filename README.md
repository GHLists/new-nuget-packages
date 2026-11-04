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

## Latest list — 2026-11-04 18:19 UTC

New packages created between 2026-11-04 17:21 UTC and 2026-11-04 18:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T18-19-52-814538Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 17:26:48 | [si-engine](https://www.nuget.org/packages/si-engine) | 1.1.0 | LuPaLa-Coder | Software Intelligence Engine: analizza applicazioni ASP.NET Core e database SQL… |
| 2026-11-04 17:29:50 | [Nantuc.Common](https://www.nuget.org/packages/Nantuc.Common) | 0.8.2 | RomanyPe | Package Description |
| 2026-11-04 17:29:51 | [Nantuc.Compiler](https://www.nuget.org/packages/Nantuc.Compiler) | 0.8.2 | RomanyPe | Frontend и Backend компилятора платформы Nantuc. Frontend принимает исходник на… |
| 2026-11-04 17:29:52 | [Nantuc.Contracts](https://www.nuget.org/packages/Nantuc.Contracts) | 0.8.2 | RomanyPe | Package Description |
| 2026-11-04 17:29:53 | [Nantuc.Diagnostics](https://www.nuget.org/packages/Nantuc.Diagnostics) | 0.8.2 | RomanyPe | Package Description |
| 2026-11-04 17:29:54 | [Nantuc.Kernel](https://www.nuget.org/packages/Nantuc.Kernel) | 0.8.2 | RomanyPe | Package Description |
| 2026-11-04 17:29:55 | [Nantuc.VmApplication](https://www.nuget.org/packages/Nantuc.VmApplication) | 0.8.2 | RomanyPe | Package Description |
| 2026-11-04 17:29:57 | [Nantuc.VmApplication.Extensions](https://www.nuget.org/packages/Nantuc.VmApplication.Extensions) | 0.8.2 | RomanyPe | Package Description |
| 2026-11-04 17:41:40 | [Beryl.Outlook](https://www.nuget.org/packages/Beryl.Outlook) | 2.0.0 | Data TB Software | Enterprise-grade Outlook PST/OST Forensic Analysis, Deep NDB/LTP Carving, B-Tre… |
| 2026-11-04 17:42:05 | [Unicom360](https://www.nuget.org/packages/Unicom360) | 0.1.0 | Techrode Solutions Limited | The official .NET client for the Unicom360 API: SMS, email and WhatsApp messagi… |
| 2026-11-04 17:45:37 | [SmsTunnel](https://www.nuget.org/packages/SmsTunnel) | 1.0.0 | Narcis Bodea | Send texts from your own .NET apps through your own Android phone, from your ow… |
| 2026-11-04 17:45:39 | [SmsTunnel.Extensions.DependencyInjection](https://www.nuget.org/packages/SmsTunnel.Extensions.DependencyInjection) | 1.0.0 | Narcis Bodea | services.AddSmsTunnel() for ASP.NET Core, worker services and other apps with d… |
| 2026-11-04 17:51:54 | [Cartovia.WinForms](https://www.nuget.org/packages/Cartovia.WinForms) | 1.0.0 | Nicolas Estebe | Cartovia Windows Forms map control: vector maps with MapLibre GL JS (no account… |
| 2026-11-04 17:51:54 | [Cartovia.WebView2](https://www.nuget.org/packages/Cartovia.WebView2) | 1.0.0 | Nicolas Estebe | Microsoft Edge WebView2 host of Cartovia: serves the map page, bridges messages… |
| 2026-11-04 17:51:55 | [Cartovia.Wpf](https://www.nuget.org/packages/Cartovia.Wpf) | 1.0.0 | Nicolas Estebe | Cartovia WPF map control: vector maps with MapLibre GL JS (no account needed) o… |
| 2026-11-04 17:51:56 | [Cartovia.Core](https://www.nuget.org/packages/Cartovia.Core) | 1.0.0 | Nicolas Estebe | UI-agnostic core of Cartovia, vector maps for .NET desktop apps: strongly-typed… |
| 2026-11-04 17:51:56 | [Cartovia.Mapbox.Services](https://www.nuget.org/packages/Cartovia.Mapbox.Services) | 1.0.0 | Nicolas Estebe | Optional Mapbox extension of Cartovia: strongly-typed .NET client for the Mapbo… |
| 2026-11-04 17:54:11 | [XDev.OpenWrt.uBus.Client.Net](https://www.nuget.org/packages/XDev.OpenWrt.uBus.Client.Net) | 0.0.1-alpha001 | jasells,XDevApps | Client for the OpenWrt ubus HTTP JSON-RPC API (uhttpd-mod-ubus + rpcd): session… |
| 2026-11-04 18:00:43 | [BRIDGES](https://www.nuget.org/packages/BRIDGES) | 0.1.0 | Nicolas MONTAGNE, Romain MESN… | Tools from the Build'in platform for Geometry and Structural Design. |
| 2026-11-04 18:03:56 | [Descope.Maui](https://www.nuget.org/packages/Descope.Maui) | 1.1.0 | Descope | The Descope SDK for .NET MAUI signs users in with Descope Flows through the sys… |
| 2026-11-04 18:08:08 | [Puppetty](https://www.nuget.org/packages/Puppetty) | 1.0.0 | Tom Laird-McConnell | The puppetty tool: drive CLI/TUI programs in a real terminal from the shell, wi… |
| 2026-11-04 18:08:09 | [Puppetty.NET](https://www.nuget.org/packages/Puppetty.NET) | 1.0.0 | Tom Laird-McConnell | Drive CLI/TUI programs in a real pseudo-terminal from code: type, press keys, c… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
