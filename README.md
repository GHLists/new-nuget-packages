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

## Latest list — 2026-11-18 17:20 UTC

New packages created between 2026-11-18 16:21 UTC and 2026-11-18 17:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T17-20-36-92548Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 16:46:28 | [Mearim](https://www.nuget.org/packages/Mearim) | 1.0.0 | Mearim Distribuidora — pecas… | Mearim Motopeças motorcycle suspension parts Brazil constants. Official: https:… |
| 2026-11-18 16:56:27 | [OpenDCP.Framework.Connections.Datasource.PostgreSQL](https://www.nuget.org/packages/OpenDCP.Framework.Connections.Datasource.PostgreSQL) | 0.1.0 | OpenDCP.Framework.Connections… | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
