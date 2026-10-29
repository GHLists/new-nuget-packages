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

## Latest list — 2026-10-29 22:19 UTC

New packages created between 2026-10-29 21:19 UTC and 2026-10-29 22:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T22-19-29-93933Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 21:24:57 | [HttpConnectionCore.Shared](https://www.nuget.org/packages/HttpConnectionCore.Shared) | 1.0.0 | By Mx | Librería optimizada en .NET 6 para el consumo de Web APIs utilizando SocketsHtt… |
| 2026-10-29 21:31:53 | [Qwips.Core.ClientSdk.MultiCase](https://www.nuget.org/packages/Qwips.Core.ClientSdk.MultiCase) | 1.0.1 | Qwips.Core.ClientSdk.MultiCase | Package Description |
| 2026-10-29 21:34:27 | [Qwips.ClientSdk.QwipsIntegration](https://www.nuget.org/packages/Qwips.ClientSdk.QwipsIntegration) | 1.0.0 | Qwips.ClientSdk.QwipsIntegrat… | Package Description |
| 2026-10-29 21:40:11 | [Colonise](https://www.nuget.org/packages/Colonise) | 0.2.0 | Simon Jefferies | A read-only engineering colony with asynchronous residents, durable inboxes, an… |
| 2026-10-29 22:10:22 | [NymBroker.Scheduling.MySql](https://www.nuget.org/packages/NymBroker.Scheduling.MySql) | 0.15.0 | nymankla@gmail.com | Durable MySQL / MariaDB schedule store for NymBroker: named scheduled actions r… |
| 2026-10-29 22:10:24 | [NymBroker.Scheduling.Sqlite](https://www.nuget.org/packages/NymBroker.Scheduling.Sqlite) | 0.15.0 | nymankla@gmail.com | Durable SQLite schedule store for NymBroker: named scheduled actions catch up m… |
| 2026-10-29 22:10:26 | [NymBroker.Scheduling.SqlServer](https://www.nuget.org/packages/NymBroker.Scheduling.SqlServer) | 0.15.0 | nymankla@gmail.com | Durable SQL Server schedule store for NymBroker: named scheduled actions run on… |
| 2026-10-29 22:10:26 | [NymBroker.Scheduling.Postgres](https://www.nuget.org/packages/NymBroker.Scheduling.Postgres) | 0.15.0 | nymankla@gmail.com | Durable PostgreSQL schedule store for NymBroker: named scheduled actions run on… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
