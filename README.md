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

## Latest list — 2026-10-04 05:20 UTC

New packages created between 2026-10-04 04:20 UTC and 2026-10-04 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T05-20-25-213732Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 04:22:38 | [jaytwo.Ergonomics.Images](https://www.nuget.org/packages/jaytwo.Ergonomics.Images) | 0.1.0-beta-20261003… | jaytwo.Ergonomics.Images | Ergonomic resize and rotation for still images, on NetVips. |
| 2026-10-04 04:40:48 | [SyntaxCircus.Cmsify.Infrastructure.Sqlite](https://www.nuget.org/packages/SyntaxCircus.Cmsify.Infrastructure.Sqlite) | 0.8.8 | Syntax Circus LLC | Optional SQLite persistence registration and schema-only migrations for Cmsify. |
| 2026-10-04 04:49:29 | [LibTab](https://www.nuget.org/packages/LibTab) | 0.1.0 | Scott J Guyton | Pure C# libtab reader/writer for Plan 9 ndb-shaped tables with compatible HASHE… |
| 2026-10-04 04:51:36 | [UE.Toolkit.SandfallTypes](https://www.nuget.org/packages/UE.Toolkit.SandfallTypes) | 1.0.2 | Rirurin | UE Toolkit generated classes and structs for Clair Obscur: Expedition 33 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
