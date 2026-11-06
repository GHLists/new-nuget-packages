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

## Latest list — 2026-11-06 19:21 UTC

New packages created between 2026-11-06 18:20 UTC and 2026-11-06 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T19-21-55-760252Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 18:20:42 | [Malitor.Sdk](https://www.nuget.org/packages/Malitor.Sdk) | 1.0.0 | dotnarmafzar | Package Description |
| 2026-11-06 18:22:00 | [PeachDrawing.CoreGraphics](https://www.nuget.org/packages/PeachDrawing.CoreGraphics) | 0.9.26 | PeachDrawing.CoreGraphics | A CoreGraphics Canvas for PeachDrawing.Core - draw shapes, gradients, clips, la… |
| 2026-11-06 18:22:52 | [ScrubTest.Debug.WinUI](https://www.nuget.org/packages/ScrubTest.Debug.WinUI) | 1.1.0 | Orthosilicate | WinUI 3 Controls for Icons and Settings |
| 2026-11-06 18:24:54 | [PeachBrackets.Apple](https://www.nuget.org/packages/PeachBrackets.Apple) | 0.9.26 | PeachBrackets.Apple | A macOS (AppKit) and iOS (UIKit) view that shows an HTML document laid out by P… |
| 2026-11-06 18:53:03 | [SeoApiLens](https://www.nuget.org/packages/SeoApiLens) | 0.2.1 | Yong Seo | ASP.NET Core integration for SeoApiLens: MapSeoApiLens() mounts a self-containe… |
| 2026-11-06 18:55:27 | [BleedingOnTheEdge.Razor.Sdk](https://www.nuget.org/packages/BleedingOnTheEdge.Razor.Sdk) | 1.0.0 | BleedingOnTheEdge, Sina Vali | Public SDK for developing Razor extensions. Contains only contracts, hooks, slo… |
| 2026-11-06 18:55:33 | [AvaAdwaita.Controls](https://www.nuget.org/packages/AvaAdwaita.Controls) | 1.10.0.7 | drasticactions | Controls that libadwaita and GTK have and Avalonia does not, drawn by AvaAdwait… |
| 2026-11-06 19:08:08 | [PulseTrade.Comm.ResourceNode.LegacyBridge](https://www.nuget.org/packages/PulseTrade.Comm.ResourceNode.LegacyBridge) | 0.1.1 | PulseTrade.Comm.ResourceNode.… | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
