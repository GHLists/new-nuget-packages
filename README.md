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

## Latest list — 2026-10-11 23:19 UTC

New packages created between 2026-10-11 22:21 UTC and 2026-10-11 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T23-19-32-807624Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 22:22:25 | [KatzibuildParser](https://www.nuget.org/packages/KatzibuildParser) | 1.0.0 | AaronoLW | Simple library for parsing KATZIBUILD files |
| 2026-10-11 22:37:03 | [VetCore.FDMV.Importer](https://www.nuget.org/packages/VetCore.FDMV.Importer) | 0.1.1 | VetCoreSolution | Une bibliothèque .NET qui lit les fichiers tarif au format FDMV (« Gestion des… |
| 2026-10-11 22:38:01 | [SqlBlame](https://www.nuget.org/packages/SqlBlame) | 0.0.1 | Uros Milic | Interactive terminal tool for browsing the change history of SQL Server stored… |
| 2026-10-11 22:40:08 | [QuanticDigit.Common.Utility.Model](https://www.nuget.org/packages/QuanticDigit.Common.Utility.Model) | 9.1.0 | Quantic Digit S.R.L. | Libreria di utility comuni: contratti dei modelli di trasporto (marcatori, invo… |
| 2026-10-11 22:48:00 | [Qubic.WalletConnect](https://www.nuget.org/packages/Qubic.WalletConnect) | 1.0.0 | Qubic.NET Contributors | WalletConnect v2 wallet side for Qubic (namespace "qubic"): pairing, session ap… |
| 2026-10-11 23:02:13 | [Stormancer.Server.Plugins.Analytics.Outputs.Elasticsearch](https://www.nuget.org/packages/Stormancer.Server.Plugins.Analytics.Outputs.Elasticsearch) | 1.0.0-pre | Stormancer | Stores analytics in elasticsearch. |
| 2026-10-11 23:08:28 | [hippo.osx-arm64](https://www.nuget.org/packages/hippo.osx-arm64) | 0.1.0 | Alister Pineda | Indexes a markdown workspace into a local SQLite cache and answers structural q… |
| 2026-10-11 23:08:28 | [hippo.osx-x64](https://www.nuget.org/packages/hippo.osx-x64) | 0.1.0 | Alister Pineda | Indexes a markdown workspace into a local SQLite cache and answers structural q… |
| 2026-10-11 23:08:29 | [hippo.linux-x64](https://www.nuget.org/packages/hippo.linux-x64) | 0.1.0 | Alister Pineda | Indexes a markdown workspace into a local SQLite cache and answers structural q… |
| 2026-10-11 23:08:30 | [hippo.linux-musl-x64](https://www.nuget.org/packages/hippo.linux-musl-x64) | 0.1.0 | Alister Pineda | Indexes a markdown workspace into a local SQLite cache and answers structural q… |
| 2026-10-11 23:08:30 | [hippo.win-x64](https://www.nuget.org/packages/hippo.win-x64) | 0.1.0 | Alister Pineda | Indexes a markdown workspace into a local SQLite cache and answers structural q… |
| 2026-10-11 23:08:32 | [hippo](https://www.nuget.org/packages/hippo) | 0.1.0 | Alister Pineda | Indexes a markdown workspace into a local SQLite cache and answers structural q… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
