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

## Latest list — 2026-10-21 22:20 UTC

New packages created between 2026-10-21 21:21 UTC and 2026-10-21 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T22-20-21-87183Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 21:47:13 | [Code2.Net.Dns](https://www.nuget.org/packages/Code2.Net.Dns) | 0.1.5 | 2code | Minimal DNS library (rfc1035) |
| 2026-10-21 21:51:45 | [Brows.DirectoryListing](https://www.nuget.org/packages/Brows.DirectoryListing) | 1.0.0 | Ken Yourek | A .NET library for parsing FTP server directory listings into structured entrie… |
| 2026-10-21 22:00:52 | [HCS.UmbCustomHeader](https://www.nuget.org/packages/HCS.UmbCustomHeader) | 1.0.0 | Nik Rimington | Group Umbraco backoffice sections into dropdowns in the top navigation, configu… |
| 2026-10-21 22:04:55 | [Chd.DesignTimeServices](https://www.nuget.org/packages/Chd.DesignTimeServices) | 10.0.0 | Mehmet Yoldaş | Chd (Cleverly Handle Difficulty) packages are easy to use. This package plugs T… |
| 2026-10-21 22:08:01 | [Ikonym](https://www.nuget.org/packages/Ikonym) | 0.1.0 | Numera11y | Deterministic geometric SVG avatars generated from a stable identifier. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
