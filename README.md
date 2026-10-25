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

## Latest list — 2026-10-25 12:19 UTC

New packages created between 2026-10-25 11:21 UTC and 2026-10-25 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T12-19-50-84498Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 11:23:55 | [dotVault.Configuration](https://www.nuget.org/packages/dotVault.Configuration) | 2026.10.25.95 | software.tirol | Lokale Entwicklungs-Settings aus dem Secrets-Tresor dotVault: IConfiguration-Qu… |
| 2026-10-25 11:24:37 | [Fakturnaut.Sdk](https://www.nuget.org/packages/Fakturnaut.Sdk) | 1.0.1 | Fakturnaut | Fakturnaut API client: issue, validate, deliver and check EN 16931 e-invoices (… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
