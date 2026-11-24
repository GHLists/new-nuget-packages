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

## Latest list — 2026-11-24 07:22 UTC

New packages created between 2026-11-24 06:18 UTC and 2026-11-24 07:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T07-22-00-379863Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 06:21:30 | [Jtext103.CFET2.Things.S7ClientThing](https://www.nuget.org/packages/Jtext103.CFET2.Things.S7ClientThing) | 1.0.0 | Jtext103 | Siemens S7 PLC communication for CFET2. |
| 2026-11-24 06:26:30 | [Jtext103.CFET2.Things.InfluxDBThing](https://www.nuget.org/packages/Jtext103.CFET2.Things.InfluxDBThing) | 1.0.0 | Jtext103 | InfluxDB data storage for CFET2. |
| 2026-11-24 06:41:50 | [Ombrevix.Billing.Sdk](https://www.nuget.org/packages/Ombrevix.Billing.Sdk) | 0.1.0 | ombrevix | Ombrevix Billing SDK for .NET: subscriptions, customers, products and usage bil… |
| 2026-11-24 06:45:57 | [Aiursoft.EsrpSign.SDK](https://www.nuget.org/packages/Aiursoft.EsrpSign.SDK) | 10.0.0 | Aiursoft.EsrpSign.SDK | Create company OpenPGP keys, sign release manifests, and download verification… |
| 2026-11-24 06:51:31 | [MafLabs.Notifications](https://www.nuget.org/packages/MafLabs.Notifications) | 0.1.0 | MafLabs contributors | Send a notification to a person by mail (SMTP with STARTTLS, password read from… |
| 2026-11-24 06:56:03 | [HealthMgr.david.202611](https://www.nuget.org/packages/HealthMgr.david.202611) | 1.1.2 | HealthMgr | Package Description |
| 2026-11-24 06:58:57 | [GroveGames.SecureStorage](https://www.nuget.org/packages/GroveGames.SecureStorage) | 0.3.0 | Grove Games | Secure key-value storage for games on .NET and Unity, backed by the iOS Keychai… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
