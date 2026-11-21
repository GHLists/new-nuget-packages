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

## Latest list — 2026-11-21 20:21 UTC

New packages created between 2026-11-21 19:20 UTC and 2026-11-21 20:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T20-21-01-191662Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 19:28:03 | [GSharp.CodeAnalysis.Transformations](https://www.nuget.org/packages/GSharp.CodeAnalysis.Transformations) | 0.5.767 | David Obando | Data-defined code fixes for GSharp (ADR-0227 D6): transformation programs, thei… |
| 2026-11-21 19:29:55 | [ResultUnion](https://www.nuget.org/packages/ResultUnion) | 0.1.0 | Giorgi Kaldani | A Result pattern for .NET built on C# 15 unions: Result<T>, Result and Error wi… |
| 2026-11-21 19:29:56 | [ResultUnion.Grpc](https://www.nuget.org/packages/ResultUnion.Grpc) | 0.1.0 | Giorgi Kaldani | gRPC integration for ResultUnion: Error to and from google.rpc.Status (ErrorInf… |
| 2026-11-21 19:29:57 | [ResultUnion.AspNetCore](https://www.nuget.org/packages/ResultUnion.AspNetCore) | 0.1.0 | Giorgi Kaldani | ASP.NET Core integration for ResultUnion: typed Minimal API results (Results<Ok… |
| 2026-11-21 19:47:52 | [MusicTheory.Abc](https://www.nuget.org/packages/MusicTheory.Abc) | 3.0.0 | phmatray | ABC notation for MusicTheory: reads single-voice ABC tunes into spelled notes,… |
| 2026-11-21 19:47:54 | [MusicTheory.ChordPro](https://www.nuget.org/packages/MusicTheory.ChordPro) | 3.0.0 | phmatray | ChordPro for MusicTheory: parses chord sheets into lines and chord segments and… |
| 2026-11-21 19:47:58 | [MusicTheory.Midi](https://www.nuget.org/packages/MusicTheory.Midi) | 3.0.0 | phmatray | Standard MIDI files for MusicTheory: writes measures, a tempo map and a key as… |
| 2026-11-21 19:48:00 | [MusicTheory.MusicXml](https://www.nuget.org/packages/MusicTheory.MusicXml) | 3.0.0 | phmatray | MusicXML for MusicTheory: writes measures, key, meter and title as partwise Mus… |
| 2026-11-21 20:11:06 | [MinimalRabbit.FanOperations.FileBased](https://www.nuget.org/packages/MinimalRabbit.FanOperations.FileBased) | 0.0.14-alpha | dotnetKyle | Add fan operations to MinimalRabbit. This package adds fan operations that are… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
