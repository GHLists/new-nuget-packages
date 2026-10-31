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

## Latest list — 2026-10-31 02:20 UTC

New packages created between 2026-10-31 01:19 UTC and 2026-10-31 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T02-20-43-110085Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 01:33:26 | [JBOpale.LicenceManager.Cpp](https://www.nuget.org/packages/JBOpale.LicenceManager.Cpp) | 1.0.1 | JB-Opale | Dependency-free C++ validator (x64 static library, MSVC) for JBOpale.LicenceMan… |
| 2026-10-31 01:38:11 | [JBOpale.LicenceManager](https://www.nuget.org/packages/JBOpale.LicenceManager) | 1.0.1 | JB-Opale | Compact, offline software licence keys signed with ECDSA P-256: issue and valid… |
| 2026-10-31 01:58:50 | [LuminaUI.Charts](https://www.nuget.org/packages/LuminaUI.Charts) | 0.6.10 | LuminaUI Contributors | Lumina-themed chart controls for Avalonia and LuminaUI. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
