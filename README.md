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

## Latest list — 2026-11-06 13:19 UTC

New packages created between 2026-11-06 12:19 UTC and 2026-11-06 13:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T13-19-40-357997Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 12:21:33 | [StepHighlighter.ReqnrollPlugin](https://www.nuget.org/packages/StepHighlighter.ReqnrollPlugin) | 0.1.0 | Kamil Marek | Reqnroll runtime plugin that streams step results (JSON Lines) while tests run,… |
| 2026-11-06 12:25:11 | [PureGate.Socket](https://www.nuget.org/packages/PureGate.Socket) | 1.0.1 | Ahmed Yasin Koculu | A dependency-free TCP messaging fabric for .NET: multiplexed request/response,… |
| 2026-11-06 12:27:01 | [Dockview.Core](https://www.nuget.org/packages/Dockview.Core) | 1.0.0 | Dockview.Core | Package Description |
| 2026-11-06 12:41:35 | [Umbraco.Community.NodeIcons](https://www.nuget.org/packages/Umbraco.Community.NodeIcons) | 18.0.0-rc1 | Søren Kottal | Choose individual document icons in the native Umbraco content tree and documen… |
| 2026-11-06 12:50:58 | [HuntApi](https://www.nuget.org/packages/HuntApi) | 0.1.0 | HuntAPI | Official .NET SDK for the HuntAPI media download API. |
| 2026-11-06 12:51:42 | [Piloterr](https://www.nuget.org/packages/Piloterr) | 0.1.0 | Piloterr | Official .NET SDK for the Piloterr web scraping API. |
| 2026-11-06 12:51:45 | [Autom](https://www.nuget.org/packages/Autom) | 0.1.0 | Autom | Official .NET SDK for the Autom SERP API. |
| 2026-11-06 12:51:51 | [CaptureKit](https://www.nuget.org/packages/CaptureKit) | 0.1.0 | CaptureKit | Official .NET SDK for the CaptureKit screenshot API. |
| 2026-11-06 12:51:54 | [Veille](https://www.nuget.org/packages/Veille) | 0.1.0 | Veille | Official .NET SDK for the Veille fraud prevention API. |
| 2026-11-06 12:51:57 | [ChartQuery](https://www.nuget.org/packages/ChartQuery) | 0.1.0 | ChartQuery | Official .NET SDK for the ChartQuery chart and QR code API. |
| 2026-11-06 12:52:00 | [BrowserSolver](https://www.nuget.org/packages/BrowserSolver) | 0.1.0 | BrowserSolver | Official .NET SDK for the BrowserSolver web unlocker API. |
| 2026-11-06 12:52:03 | [Asin](https://www.nuget.org/packages/Asin) | 0.1.0 | Asin | Official .NET SDK for the Asin Amazon price tracking API. |
| 2026-11-06 13:08:28 | [Indigina.Tms.TikTokEdge.WebApi](https://www.nuget.org/packages/Indigina.Tms.TikTokEdge.WebApi) | 1.0.0 | Indigina | Package contains web api for Tms.TikTokEdge service. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
