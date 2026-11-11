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

## Latest list — 2026-11-11 17:21 UTC

New packages created between 2026-11-11 16:19 UTC and 2026-11-11 17:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T17-21-23-377763Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 16:25:14 | [Starward.SharpSevenZip](https://www.nuget.org/packages/Starward.SharpSevenZip) | 2.0.130 | Joel Ahlgren, Markovtsev Vadi… | 7-zip native library wrapper. Managed 7-zip library written in C# that provides… |
| 2026-11-11 16:27:48 | [RecursiveAI.OneScope.Tool](https://www.nuget.org/packages/RecursiveAI.OneScope.Tool) | 1.0.0 | Recursive AI, LLC | onescope: a viewer for the Recursive AI family's deterministic libraries. Scrub… |
| 2026-11-11 16:30:58 | [Isotopes](https://www.nuget.org/packages/Isotopes) | 10.0.0 | Max Eroshkin | This package contains most common targets for fallout.build. |
| 2026-11-11 16:47:39 | [Lengko.Chart.Wpf](https://www.nuget.org/packages/Lengko.Chart.Wpf) | 1.0.0 | LengkoDev, Cas | Modern, high-performance charting and data visualization library for WPF with z… |
| 2026-11-11 16:48:06 | [OpenDCP.Framework.AdminActions](https://www.nuget.org/packages/OpenDCP.Framework.AdminActions) | 0.3.1 | OpenDCP.Framework.AdminActions | Package Description |
| 2026-11-11 16:49:38 | [OpenDCP.Framework.Cleanup](https://www.nuget.org/packages/OpenDCP.Framework.Cleanup) | 0.1.0 | OpenDCP.Framework.Cleanup | Package Description |
| 2026-11-11 16:50:01 | [Kebechet.Maui.YouTubeEmbed](https://www.nuget.org/packages/Kebechet.Maui.YouTubeEmbed) | 1.0.0 | Kebechet | Plays YouTube videos inside a .NET MAUI Blazor Hybrid app without YouTube's Err… |
| 2026-11-11 16:51:41 | [OpenDCP.Framework.ServiceDiscovery](https://www.nuget.org/packages/OpenDCP.Framework.ServiceDiscovery) | 0.1.0 | OpenDCP.Framework.ServiceDisc… | Package Description |
| 2026-11-11 16:54:05 | [OpenDCP.Framework.Dashboard](https://www.nuget.org/packages/OpenDCP.Framework.Dashboard) | 0.1.0 | OpenDCP.Framework.Dashboard | Package Description |
| 2026-11-11 16:55:50 | [OpenDCP.Framework.HttpClient](https://www.nuget.org/packages/OpenDCP.Framework.HttpClient) | 0.2.0 | OpenDCP.Framework.HttpClient | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
