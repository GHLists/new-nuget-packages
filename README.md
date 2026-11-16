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

## Latest list — 2026-11-16 13:19 UTC

New packages created between 2026-11-16 12:21 UTC and 2026-11-16 13:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T13-19-45-633945Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 12:32:33 | [Geekmotors.Crucible](https://www.nuget.org/packages/Geekmotors.Crucible) | 0.1.0 | Geekmotors | Semantic assertions for code that calls LLMs: an AI judge checks that a reply m… |
| 2026-11-16 12:32:35 | [Geekmotors.Crucible.Xunit](https://www.nuget.org/packages/Geekmotors.Crucible.Xunit) | 0.1.0 | Geekmotors | xUnit v3 adapter for Crucible: [CrucibleFact] and [CrucibleTheory] run a test N… |
| 2026-11-16 12:37:05 | [NE.Standard.UI.Desktop](https://www.nuget.org/packages/NE.Standard.UI.Desktop) | 2.10.0 | Aki Evans | The Windows desktop WebView2 host of the NE.Standard UI framework: runs the ful… |
| 2026-11-16 12:42:30 | [LogDrop.Api](https://www.nuget.org/packages/LogDrop.Api) | 0.1.0-alpha1 | LogDrop | Optional custom spans, flush, export status and key update for .NET services tr… |
| 2026-11-16 12:52:21 | [AdorablePepchik.CommandPipeline](https://www.nuget.org/packages/AdorablePepchik.CommandPipeline) | 1.0.0 | LaPeregrin | Building flow for handling some process. |
| 2026-11-16 12:55:10 | [Consolonia.Imaging](https://www.nuget.org/packages/Consolonia.Imaging) | 12.1.4.17 | https://github.com/consolonia… | Shows pictures as real pixels in terminals that support the kitty graphics prot… |
| 2026-11-16 12:59:05 | [Ekvip.Cinnamon.Semi.SubstrateMap](https://www.nuget.org/packages/Ekvip.Cinnamon.Semi.SubstrateMap) | 5.0.0 | ekvip automation GmbH | A TwinCAT HMI control that renders SEMI substrate maps (wafers, panels and othe… |
| 2026-11-16 13:02:06 | [VisioForge.DotNet.Core.Redist.MP4.arm64](https://www.nuget.org/packages/VisioForge.DotNet.Core.Redist.MP4.arm64) | 2026.11.16 | VisioForge | MP4, MPEG-TS, MKV and HLS output for the VisioForge .NET SDKs (Windows engines)… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
