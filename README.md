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

## Latest list — 2026-10-10 19:20 UTC

New packages created between 2026-10-10 18:21 UTC and 2026-10-10 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T19-20-41-251255Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 18:39:13 | [CodeBrix.Audio.Vorbis.BsdLicenseForever](https://www.nuget.org/packages/CodeBrix.Audio.Vorbis.BsdLicenseForever) | 1.0.283.1118 | Jeremy Ellis | Ogg Vorbis encoding for CodeBrix.Audio. OggVorbisEncoder turns float samples in… |
| 2026-10-10 18:44:58 | [Janglim](https://www.nuget.org/packages/Janglim) | 0.3.0 | AJ-comp | Janglim is an embeddable LALR(1) parser-generator engine for .NET. Define gramm… |
| 2026-10-10 18:45:16 | [FrameReader](https://www.nuget.org/packages/FrameReader) | 1.4.1-preview | Jakob Boman | Fast in-process video and audio for .NET through FFmpeg's libraries: frames at… |
| 2026-10-10 18:59:41 | [Coworkee.CodeGen](https://www.nuget.org/packages/Coworkee.CodeGen) | 0.0.1.13 | fgilde | Optional DTO and mapping generation for entities with Nextended.CodeGen, mapped… |
| 2026-10-10 18:59:55 | [Coworkee.Client.Blazor.ClientEntities](https://www.nuget.org/packages/Coworkee.Client.Blazor.ClientEntities) | 0.0.1.13 | fgilde | Client entities for Blazor WebAssembly: mirror OData sets in the browser and fi… |
| 2026-10-10 19:02:26 | [AIntelA.Agents.Gcp](https://www.nuget.org/packages/AIntelA.Agents.Gcp) | 0.20.0 | Envision Tecnologia | AIA Agents SDK on Google Cloud: the Cloud Tasks run bus and compaction schedule… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
