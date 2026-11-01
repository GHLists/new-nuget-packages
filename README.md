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

## Latest list — 2026-11-01 07:19 UTC

New packages created between 2026-11-01 06:20 UTC and 2026-11-01 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T07-19-04-224405Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 06:50:35 | [Element-Plus.Admin.Template](https://www.nuget.org/packages/Element-Plus.Admin.Template) | 0.12.1 | Element-Plus Blazor (Smart) | dotnet new template that scaffolds an Element-Plus Blazor WebAssembly admin sta… |
| 2026-11-01 06:53:38 | [ManagedCodecs.Thumbnails](https://www.nuget.org/packages/ManagedCodecs.Thumbnails) | 0.5.0 | Jakob Boman | Thumbnails (PNG or RGBA) and the basic facts (duration, displayed size, codecs,… |
| 2026-11-01 06:53:40 | [ManagedCodecs.Unity](https://www.nuget.org/packages/ManagedCodecs.Unity) | 0.5.0 | Jakob Boman | The ManagedCodecs decoders (H.264, MJPEG, AAC LC and HE-AAC; AVI, MP4 and ADTS)… |
| 2026-11-01 07:11:42 | [ArtificialFlow.Sdk](https://www.nuget.org/packages/ArtificialFlow.Sdk) | 1.2.0 | ArtificialFlow contributors | REST SDK for the ArtificialFlow gateway API. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
