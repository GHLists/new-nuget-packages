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

## Latest list — 2026-11-25 06:19 UTC

New packages created between 2026-11-25 05:19 UTC and 2026-11-25 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T06-19-52-227517Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 05:34:56 | [NCode.Coordination](https://www.nuget.org/packages/NCode.Coordination) | 0.3.0 | NCode Group | The composition of NCode.Coordination: providers registered on one builder and… |
| 2026-11-25 05:49:17 | [Instancium.Trust](https://www.nuget.org/packages/Instancium.Trust) | 1.7.5 | Instancium | Crypto-agile trust library for the Instancium ecosystem: Ed25519 signing, Argon… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
