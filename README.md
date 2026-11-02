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

## Latest list — 2026-11-02 07:20 UTC

New packages created between 2026-11-02 06:19 UTC and 2026-11-02 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T07-20-35-435739Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 06:20:53 | [FS.GG.Algorithms](https://www.nuget.org/packages/FS.GG.Algorithms) | 0.1.0 | FS-GG | Shared algorithms for FS.GG: a frozen-order binary and indexed heap, Q16.16 fix… |
| 2026-11-02 06:31:10 | [Sachssoft.Sasogine.Controls](https://www.nuget.org/packages/Sachssoft.Sasogine.Controls) | 0.13.0-alpha | Tobias Sachs | UI controls and layout infrastructure for the Sasogine game engine, including s… |
| 2026-11-02 06:56:30 | [Soenneker.Docusign.OpenApiClientUtil](https://www.nuget.org/packages/Soenneker.Docusign.OpenApiClientUtil) | 11.0.2 | Jake Soenneker | A thread-safe utility for obtaining Docusign's OpenApiClient singleton. |
| 2026-11-02 07:08:38 | [Caveman.IAWebCrawler](https://www.nuget.org/packages/Caveman.IAWebCrawler) | 0.1.0 | Francesco Paolo Passaro | Web crawler for .NET 10 that downloads a complete website and produces three co… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
