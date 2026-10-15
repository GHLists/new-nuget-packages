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

## Latest list — 2026-10-15 01:22 UTC

New packages created between 2026-10-15 00:19 UTC and 2026-10-15 01:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T01-22-36-327924Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 00:30:35 | [Spek.NET](https://www.nuget.org/packages/Spek.NET) | 0.1.0 | Derek Yang | Spek's spectrogram analysis for .NET. Decodes audio with ffmpeg and turns it in… |
| 2026-10-15 00:30:36 | [Spek.NET.WinUI](https://www.nuget.org/packages/Spek.NET.WinUI) | 0.1.0 | Derek Yang | A WinUI 3 control that draws Spek's spectrogram of an audio file with Win2D as… |
| 2026-10-15 00:35:57 | [OdinsHand.Templates](https://www.nuget.org/packages/OdinsHand.Templates) | 0.3.1 | n8daniels | dotnet new template that adds an Odin's Hand in-game test harness plugin to a V… |
| 2026-10-15 00:36:00 | [OdinsHand](https://www.nuget.org/packages/OdinsHand) | 0.3.1 | n8daniels | An in-game test harness for Valheim (BepInEx 5) mods. Launches the real game, l… |
| 2026-10-15 00:50:05 | [Gori.Common.Roslyn](https://www.nuget.org/packages/Gori.Common.Roslyn) | 1.0.0 | Gori.Common.Roslyn | Package Description |
| 2026-10-15 00:50:25 | [Gori.Common.Roslyn.Test](https://www.nuget.org/packages/Gori.Common.Roslyn.Test) | 1.0.0 | Gori.Common.Roslyn.Test | Package Description |
| 2026-10-15 01:12:35 | [Webority.Analyzers](https://www.nuget.org/packages/Webority.Analyzers) | 0.2.0 | Webority Technologies | The fleet's banned-API rules at build time: one list of banned types, members a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
