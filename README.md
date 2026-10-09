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

## Latest list — 2026-10-09 00:21 UTC

New packages created between 2026-10-08 23:20 UTC and 2026-10-09 00:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T00-21-45-501345Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 23:26:39 | [OpenRecite](https://www.nuget.org/packages/OpenRecite) | 1.0.0 | ArabidopsisDev | Platform-independent study review SDK with FSRS-6, SM-2, Leitner, project persi… |
| 2026-10-09 00:04:26 | [diegoschagas.api.infrastructure](https://www.nuget.org/packages/diegoschagas.api.infrastructure) | 1.5.43 | Diego Struk Chagas | Infrastructure services, authentication integration and technical implementatio… |
| 2026-10-09 00:12:34 | [AlphaQuantum.SellDataToAI](https://www.nuget.org/packages/AlphaQuantum.SellDataToAI) | 1.0.0 | Alpha Quantum | .NET client for the Data Asset Score API from selldatatoai.com: score company d… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
