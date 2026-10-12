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

## Latest list — 2026-10-12 03:20 UTC

New packages created between 2026-10-12 02:20 UTC and 2026-10-12 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T03-20-34-968717Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 02:28:59 | [HoistDotnet](https://www.nuget.org/packages/HoistDotnet) | 0.1.1 | drezni01 | HoistDotnet: the hoist-core server endpoints hoist-react apps need, as a plugin… |
| 2026-10-12 02:51:25 | [Components.Maui.Controls](https://www.nuget.org/packages/Components.Maui.Controls) | 1.49.0 | machi_pon | Controls for MAUI application |
| 2026-10-12 02:52:57 | [IcebergDb](https://www.nuget.org/packages/IcebergDb) | 0.1.0 | Ankush, Iceberg DB | Official .NET C# client for Iceberg Vector Database |
| 2026-10-12 03:02:43 | [ArchiGeoSharp.Basic](https://www.nuget.org/packages/ArchiGeoSharp.Basic) | 0.1.1 | ArchiFrog | Cross-platform C# geometry kernel for architectural and computational design (.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
