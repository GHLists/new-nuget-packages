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

## Latest list — 2026-11-18 01:19 UTC

New packages created between 2026-11-18 00:20 UTC and 2026-11-18 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T01-19-25-08302Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 00:23:50 | [FsToolkit.ErrorHandling.Sources](https://www.nuget.org/packages/FsToolkit.ErrorHandling.Sources) | 6.0.0-beta007 | demystifyfp, TheAngryByrd | The source code of FsToolkit.ErrorHandling as F# files that compile inside your… |
| 2026-11-18 00:44:54 | [Nodda.Client](https://www.nuget.org/packages/Nodda.Client) | 1.2.1 | Nodda | Cliente oficial de la API de Nodda para emitir y consultar facturas VERI*FACTU… |
| 2026-11-18 00:57:11 | [Ritten.Bitwarden](https://www.nuget.org/packages/Ritten.Bitwarden) | 0.31.0 | Tom Wolfe | Bitwarden and Vaultwarden for Ritten workflows: secrets read by bw:// reference… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
