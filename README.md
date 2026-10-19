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

## Latest list — 2026-10-19 12:20 UTC

New packages created between 2026-10-19 11:22 UTC and 2026-10-19 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T12-20-01-501829Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 11:24:09 | [SatorImaging.Threading](https://www.nuget.org/packages/SatorImaging.Threading) | 1.9.0 | Sator Imaging | SatorImaging.Threading from Sator Imaging |
| 2026-10-19 11:26:24 | [Astrea.DataTables](https://www.nuget.org/packages/Astrea.DataTables) | 1.0.0 | Gautam Soni | DataTables for ASP.NET Core |
| 2026-10-19 11:43:30 | [UnicoreSoftwareSolutions.Tool.GenCRUD](https://www.nuget.org/packages/UnicoreSoftwareSolutions.Tool.GenCRUD) | 1.0.0 | Unicore Software Solutions | A tool for generating CRUD UI and API code for ASP.NET Core applications. |
| 2026-10-19 11:43:55 | [Arc56.Generated.HashMapsData2Value.zebgen](https://www.nuget.org/packages/Arc56.Generated.HashMapsData2Value.zebgen) | 1.0.1.2026101911 | HashMapsData2Value | Generated ARC-56 Algorand smart-contract clients for HashMapsData2Value/zebgen. |
| 2026-10-19 11:48:03 | [WopiServer](https://www.nuget.org/packages/WopiServer) | 0.1.0 | https://github.com/Papyrine/W… | The host side of the Web Application Open Platform Interface (WOPI) for ASP.NET… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
