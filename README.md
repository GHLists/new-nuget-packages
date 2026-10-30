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

## Latest list — 2026-10-30 01:21 UTC

New packages created between 2026-10-30 00:20 UTC and 2026-10-30 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T01-21-47-785526Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 00:50:59 | [UniversalOffice.Core](https://www.nuget.org/packages/UniversalOffice.Core) | 0.9.1 | Eric Kono | Shared base of the UniversalOffice libraries: lossless OPC (ZIP) package access… |
| 2026-10-30 00:52:28 | [UniversalOffice.Docx](https://www.nuget.org/packages/UniversalOffice.Docx) | 0.9.1 | Eric Kono | Word documents in pure .NET: lossless .docx reading and editing (sanitizing unt… |
| 2026-10-30 01:01:57 | [victor-wiki.FastDtwSharp](https://www.nuget.org/packages/victor-wiki.FastDtwSharp) | 1.0.0 | victor-wiki | C# implementation of fastdtw, which is an approximate Dynamic Time Warping (DTW… |
| 2026-10-30 01:08:11 | [victor-wiki.SharpUtility](https://www.nuget.org/packages/victor-wiki.SharpUtility) | 1.0.0 | victor-wiki | Helper classes and Extension methods. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
