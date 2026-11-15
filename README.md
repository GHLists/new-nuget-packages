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

## Latest list — 2026-11-15 17:21 UTC

New packages created between 2026-11-15 16:21 UTC and 2026-11-15 17:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T17-21-13-237976Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 16:22:43 | [VL.Audio.BeatTracking](https://www.nuget.org/packages/VL.Audio.BeatTracking) | 0.2.0-alpha | Matthias Husinsky, Claude | Common parts of the beat trackers VL.Audio.BeatNet and VL.Audio.BTrack for vvvv… |
| 2026-11-15 16:22:49 | [VL.Audio.BeatNet](https://www.nuget.org/packages/VL.Audio.BeatNet) | 0.2.0-alpha | Matthias Husinsky, Claude | Real-time beat and downbeat tracker nodes for vvvv gamma and VL.Audio, working… |
| 2026-11-15 16:22:56 | [VL.Audio.BTrack](https://www.nuget.org/packages/VL.Audio.BTrack) | 0.2.0-alpha | Matthias Husinsky, Claude | Real-time beat tracker node for vvvv gamma and VL.Audio, working at 44.1 and 48… |
| 2026-11-15 16:29:03 | [Xui.Middleware.EmulatorLegacy](https://www.nuget.org/packages/Xui.Middleware.EmulatorLegacy) | 0.0.252-alpha | Xui Apps | Package Description |
| 2026-11-15 16:41:51 | [DotNetAgentSurface.Hosting](https://www.nuget.org/packages/DotNetAgentSurface.Hosting) | 0.1.75-preview | dotnet-agent-surface contribu… | Dual-surface Microsoft.Extensions.Hosting application for DotNetAgentSurface: o… |
| 2026-11-15 16:42:27 | [DocuVieware.runtimes.macos](https://www.nuget.org/packages/DocuVieware.runtimes.macos) | 3.4.12 | Nutrient | The Nutrient Scanning Connector's macOS installer, which DocuVieware serves to… |
| 2026-11-15 16:42:34 | [DocuVieware.runtimes.windows](https://www.nuget.org/packages/DocuVieware.runtimes.windows) | 3.4.12 | Nutrient | The Nutrient Scanning Connector's Windows installer, which DocuVieware serves t… |
| 2026-11-15 17:05:05 | [CallFlowViewer](https://www.nuget.org/packages/CallFlowViewer) | 0.1.0 | Ahmad Nedal | Press Ctrl+. on any C# method and choose "Show call flow to this method" to ope… |
| 2026-11-15 17:11:35 | [WebAwesome.Blazor.Extensions](https://www.nuget.org/packages/WebAwesome.Blazor.Extensions) | 3.14.0.4 | BoldBrick | Optional extras for the WebAwesome.Blazor bindings: features that add behavior… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
