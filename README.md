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

## Latest list — 2026-11-06 06:20 UTC

New packages created between 2026-11-06 05:20 UTC and 2026-11-06 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T06-20-35-33444Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 05:30:25 | [RhythmBase.RhythmDoctor.Lang](https://www.nuget.org/packages/RhythmBase.RhythmDoctor.Lang) | 1.3.13 | RhythmBase.RhythmDoctor.Lang | Expression language (ANTLR grammar, evaluators and the ExpressionContext sandbo… |
| 2026-11-06 05:30:26 | [RhythmBase.RhythmDoctor.Playhead](https://www.nuget.org/packages/RhythmBase.RhythmDoctor.Playhead) | 1.3.13 | RhythmBase.RhythmDoctor.Playh… | Read-only level simulation (playhead, event scheduler, condition evaluation and… |
| 2026-11-06 05:44:10 | [Hawkynt.FileFormats.Video](https://www.nuget.org/packages/Hawkynt.FileFormats.Video) | 1.0.0.223 | Hawkynt | Pure-C# library for reading video containers and decoding video codecs. Demuxin… |
| 2026-11-06 05:54:15 | [links-notation](https://www.nuget.org/packages/links-notation) | 0.31.2 | Konstantin Diachenko | Link.Foundation's Links Notation parser and formatter for .NET |
| 2026-11-06 05:55:18 | [Meziantou.Framework.Imaging.Charts](https://www.nuget.org/packages/Meziantou.Framework.Imaging.Charts) | 1.0.0 | meziantou | Renders the charts of Meziantou.Framework.Charts with Meziantou.Framework.Imagi… |
| 2026-11-06 05:55:18 | [Meziantou.Framework.Charts](https://www.nuget.org/packages/Meziantou.Framework.Charts) | 1.0.0 | meziantou | Grammar-of-graphics chart library that renders deterministic SVG: bar, line, ar… |
| 2026-11-06 06:10:13 | [Beep.PDF.BarCodes](https://www.nuget.org/packages/Beep.PDF.BarCodes) | 1.0.1 | Beep.PDF.BarCodes | Package Description |
| 2026-11-06 06:10:14 | [Beep.PDF.System](https://www.nuget.org/packages/Beep.PDF.System) | 1.0.1 | Beep.PDF.System | Package Description |
| 2026-11-06 06:10:14 | [Beep.PDF.Charting](https://www.nuget.org/packages/Beep.PDF.Charting) | 1.0.1 | Beep.PDF.Charting | Package Description |
| 2026-11-06 06:10:15 | [Beep.PDF.Shared](https://www.nuget.org/packages/Beep.PDF.Shared) | 1.0.1 | Beep.PDF.Shared | Package Description |
| 2026-11-06 06:11:56 | [MFiles.Grpc](https://www.nuget.org/packages/MFiles.Grpc) | 26.11.0 | M-Files | Client for the M-Files gRPC API: the generated client classes of every service,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
