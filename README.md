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

## Latest list — 2026-11-28 02:20 UTC

New packages created between 2026-11-28 01:21 UTC and 2026-11-28 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-28T02-20-55-274521Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-28 01:44:57 | [Proxeno.Kiln.Audio](https://www.nuget.org/packages/Proxeno.Kiln.Audio) | 1.0.0 | Proxeno | Pure-managed SIMD Opus (RFC 6716) encoder and decoder for real-time voice. No n… |
| 2026-11-28 02:05:34 | [Provident.Foundations.SqlServer](https://www.nuget.org/packages/Provident.Foundations.SqlServer) | 11.98.3 | Sam Jones | A general-purpose, portable .NET class library for SQL Server database developm… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
