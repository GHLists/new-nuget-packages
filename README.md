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

## Latest list — 2026-10-03 20:19 UTC

New packages created between 2026-10-03 19:21 UTC and 2026-10-03 20:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T20-19-54-453079Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 19:31:28 | [SqlChangeTrackingHelper](https://www.nuget.org/packages/SqlChangeTrackingHelper) | 1.0.0 | Tommy Torenius | Makes it easier to read changes from SQL Server Change Tracking the right way:… |
| 2026-10-03 19:36:23 | [Serinus1.Chess](https://www.nuget.org/packages/Serinus1.Chess) | 1.3.0 | Geras1mleo, Serinus1 | A fork of the Gera.Chess library by Geras1mleo. This fork is maintained by Seri… |
| 2026-10-03 20:13:56 | [Entuity.Api](https://www.nuget.org/packages/Entuity.Api) | 2.0.257-ge2e9f8b436 | Panoramic Data Limited | A .NET API for Entuity |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
