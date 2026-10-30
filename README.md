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

## Latest list — 2026-10-30 04:20 UTC

New packages created between 2026-10-30 03:19 UTC and 2026-10-30 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T04-20-22-384616Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 03:35:59 | [ClaudeUsage.NockMon](https://www.nuget.org/packages/ClaudeUsage.NockMon) | 1.0.0 | nockawa | NockMon widget: your Claude subscription's weekly usage — used vs. elapsed, on… |
| 2026-10-30 03:46:28 | [docs-boilerplate](https://www.nuget.org/packages/docs-boilerplate) | 1.0.1 | Spooffit | Offline-capable Markdown-first documentation initialization CLI |
| 2026-10-30 03:49:59 | [Algebrakit.Sdk](https://www.nuget.org/packages/Algebrakit.Sdk) | 1.0.0 | Algebrakit | Official .NET SDK for the Algebrakit Webservice API — create exercise sessions,… |
| 2026-10-30 03:57:19 | [TCMProject.Jurisdictions](https://www.nuget.org/packages/TCMProject.Jurisdictions) | 26.10.30.2 | TCMProject.Jurisdictions | Contratos de jurisdicción (país) para la plataforma TCM: identificadores, histo… |
| 2026-10-30 03:57:21 | [TCMProject.Jurisdictions.PE](https://www.nuget.org/packages/TCMProject.Jurisdictions.PE) | 26.10.30.2 | TCMProject.Jurisdictions.PE | Perú para TCMProject.Jurisdictions: DNI, carné de extranjería y pasaporte; hist… |
| 2026-10-30 04:00:56 | [SpawnDev.Codecs](https://www.nuget.org/packages/SpawnDev.Codecs) | 1.0.0 | LostBeard | GPU-accelerated, patent-clean codecs for .NET where the codec work runs on the… |
| 2026-10-30 04:01:00 | [SpawnDev.Codecs.References](https://www.nuget.org/packages/SpawnDev.Codecs.References) | 1.0.0 | LostBeard | CPU reference implementations of the codecs that ship in SpawnDev.Codecs. Used… |
| 2026-10-30 04:09:54 | [Johnwikix.ScottPlot](https://www.nuget.org/packages/Johnwikix.ScottPlot) | 5.1.60.1 | Scott Harden | ScottPlot is a free and open-source plotting library for .NET. This package can… |
| 2026-10-30 04:10:04 | [Johnwikix.ScottPlot.D3D12.Core](https://www.nuget.org/packages/Johnwikix.ScottPlot.D3D12.Core) | 5.1.60.1 | ScottPlot contributors | Hardware D3D12 full Figure rendering for ScottPlot using Skia GPU, native MSAA,… |
| 2026-10-30 04:10:07 | [Johnwikix.ScottPlot.WPF](https://www.nuget.org/packages/Johnwikix.ScottPlot.WPF) | 5.1.60.1 | Scott Harden | User controls for displaying interactive plots in WPF applications |
| 2026-10-30 04:10:10 | [Johnwikix.ScottPlot.D3D12](https://www.nuget.org/packages/Johnwikix.ScottPlot.D3D12) | 5.1.60.1 | ScottPlot contributors | Complete ScottPlot WPF Figures rendered with hardware D3D12 through D3DImage, w… |
| 2026-10-30 04:10:12 | [Johnwikix.ScottPlot.D3D12.WinUI](https://www.nuget.org/packages/Johnwikix.ScottPlot.D3D12.WinUI) | 5.1.60.1 | ScottPlot contributors | Complete ScottPlot Figures on native WinUI 3 SwapChainPanel through shared D3D1… |
| 2026-10-30 04:10:13 | [Johnwikix.ScottPlot.D3D12.UWP](https://www.nuget.org/packages/Johnwikix.ScottPlot.D3D12.UWP) | 5.1.60.1 | ScottPlot contributors | Complete ScottPlot Figures on native Windows.UI.Xaml SwapChainPanel through sha… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
