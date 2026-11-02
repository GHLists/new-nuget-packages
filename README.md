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

## Latest list — 2026-11-02 09:21 UTC

New packages created between 2026-11-02 08:20 UTC and 2026-11-02 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T09-21-42-196664Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 08:23:52 | [Kokhan.DriveTrack.Domain](https://www.nuget.org/packages/Kokhan.DriveTrack.Domain) | 1.0.0 | Anatolii Kokhan | Domain model of the DriveTrack delivery tracking system. |
| 2026-11-02 08:33:58 | [Pycom.Graph](https://www.nuget.org/packages/Pycom.Graph) | 0.1.0 | Pycom | Domain-side client for projecting business objects into the Pycom Neo4j graph. |
| 2026-11-02 08:34:36 | [Components.Blazor](https://www.nuget.org/packages/Components.Blazor) | 1.0.0 | machi_pon | Components for Blazor application |
| 2026-11-02 08:55:55 | [unitofwork.hm](https://www.nuget.org/packages/unitofwork.hm) | 1.10.0 | UnitOfWork | Package Description |
| 2026-11-02 08:57:22 | [ModelBase.hm](https://www.nuget.org/packages/ModelBase.hm) | 1.10.0 | ModelsBase | Package Description |
| 2026-11-02 09:06:24 | [keyseal](https://www.nuget.org/packages/keyseal) | 0.1.0 | keyseal | Encrypt and decrypt files for a recipient using P-256 and AES-256-GCM. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
