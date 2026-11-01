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

## Latest list — 2026-11-01 15:20 UTC

New packages created between 2026-11-01 14:18 UTC and 2026-11-01 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T15-20-53-573559Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 14:39:27 | [EveShipFit.EsfFormat](https://www.nuget.org/packages/EveShipFit.EsfFormat) | 1.0.0 | EVEShipFit Team | Read and write esf/1, the plain-text format for EVE Online ship fits |
| 2026-11-01 14:55:58 | [Maieru.FiapTechChallenge.Messaging.Kafka](https://www.nuget.org/packages/Maieru.FiapTechChallenge.Messaging.Kafka) | 0.1.1 | João Victor Maieru Teixeira | Kafka publisher for the FIAP Tech Challenge messaging interface. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
