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

## Latest list — 2026-10-03 07:21 UTC

New packages created between 2026-10-03 06:21 UTC and 2026-10-03 07:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T07-21-25-866517Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 06:34:55 | [BuildMonitor](https://www.nuget.org/packages/BuildMonitor) | 1.0.0 | https://github.com/SimonCropp… | Cross platform build/CI monitor that runs in the system tray. |
| 2026-10-03 06:38:53 | [SwartBerg.Mediator.SourceGenerator](https://www.nuget.org/packages/SwartBerg.Mediator.SourceGenerator) | 3.1.0 | SwartBerg Studio | Compile-time handler registration for SwartBerg.Mediator. Generates AddMediator… |
| 2026-10-03 06:48:51 | [ChromaDotNet.Client.DependencyInjection](https://www.nuget.org/packages/ChromaDotNet.Client.DependencyInjection) | 2.0.0-ci-37105313564 | ChromaDB.Client.DependencyInj… | .NET SDK for Chroma database |
| 2026-10-03 06:48:52 | [ChromaDotNet.Client](https://www.nuget.org/packages/ChromaDotNet.Client) | 2.0.0-ci-37105313564 | ChromaDB.Client | .NET SDK for Chroma database |
| 2026-10-03 07:09:05 | [RefurbishedDinosaurs.LegacyFormats](https://www.nuget.org/packages/RefurbishedDinosaurs.LegacyFormats) | 1.0.0 | kibertoad | Bounded decoders for file formats commonly found in legacy games. |
| 2026-10-03 07:09:06 | [RefurbishedDinosaurs.Media.Fli](https://www.nuget.org/packages/RefurbishedDinosaurs.Media.Fli) | 1.0.0 | kibertoad | Bounded indexed FLI animation decoding. |
| 2026-10-03 07:09:06 | [RefurbishedDinosaurs.Media.Smacker](https://www.nuget.org/packages/RefurbishedDinosaurs.Media.Smacker) | 1.0.0 | kibertoad | Bounded managed Smacker container, video and packed audio decoders. |
| 2026-10-03 07:09:07 | [RefurbishedDinosaurs.Media.Playback](https://www.nuget.org/packages/RefurbishedDinosaurs.Media.Playback) | 1.0.0 | kibertoad | Presentation clocks and sequential frame coordination. |
| 2026-10-03 07:09:08 | [RefurbishedDinosaurs.Core](https://www.nuget.org/packages/RefurbishedDinosaurs.Core) | 1.0.0 | kibertoad | Reusable clean-room game restoration primitives. |
| 2026-10-03 07:09:08 | [RefurbishedDinosaurs.Media.Avi](https://www.nuget.org/packages/RefurbishedDinosaurs.Media.Avi) | 1.0.0 | kibertoad | Bounded AVI, Cinepak, RLE8 and Microsoft ADPCM decoders. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
