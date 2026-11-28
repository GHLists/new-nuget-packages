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

## Latest list — 2026-11-28 09:19 UTC

New packages created between 2026-11-28 08:21 UTC and 2026-11-28 09:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-28T09-19-17-341915Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-28 08:22:16 | [OneGTMLab.GtmToolFinder](https://www.nuget.org/packages/OneGTMLab.GtmToolFinder) | 1.0.0 | OneGTMLab | Small .NET client for the free, read-only GTM Tool Finder API: API reviews of s… |
| 2026-11-28 08:22:18 | [OneGTMLab.GtmToolFinder.Cli](https://www.nuget.org/packages/OneGTMLab.GtmToolFinder.Cli) | 1.0.0 | OneGTMLab | gtmfind: command-line search of the free GTM Tool Finder directory (tool API re… |
| 2026-11-28 08:26:52 | [OmegaAOL.Bifrost](https://www.nuget.org/packages/OmegaAOL.Bifrost) | 1.0.0 | OmegaAOL and EAZY BLACK | A drop-in HTTP/1.1 handler and WebSocket client for .NET that perform TLS with… |
| 2026-11-28 08:36:35 | [dabuzmakov.MoodCover](https://www.nuget.org/packages/dabuzmakov.MoodCover) | 0.1.0 | dabuzmakov | Fractal flame PNG generator with multithreaded rendering. |
| 2026-11-28 08:40:07 | [NativeLang.Classify](https://www.nuget.org/packages/NativeLang.Classify) | 0.2.0 | NativeLang contributors | Classify text locally using categories supplied by your application. |
| 2026-11-28 08:44:16 | [CoreOCRRuntime.OpenVino.linux-x64](https://www.nuget.org/packages/CoreOCRRuntime.OpenVino.linux-x64) | 4.3.0-beta02 | PaddleOCRCore | CoreOCROnnx OpenVINO CPU and Intel GPU runtime package for Linux x64. |
| 2026-11-28 08:45:04 | [CoreOCRRuntime.OpenVino.win-x64](https://www.nuget.org/packages/CoreOCRRuntime.OpenVino.win-x64) | 4.3.0-beta02 | PaddleOCRCore | CoreOCROnnx OpenVINO CPU and Intel GPU runtime package for Windows x64. |
| 2026-11-28 08:58:40 | [OctopusLiveWire](https://www.nuget.org/packages/OctopusLiveWire) | 1.0.0 | Katamba Martin | OCTOPUS Live Engine for .NET: runs YAML workflow blueprints in memory behind AS… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
