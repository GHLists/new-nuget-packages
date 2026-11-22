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

## Latest list — 2026-11-22 22:20 UTC

New packages created between 2026-11-22 21:19 UTC and 2026-11-22 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T22-20-20-146262Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 21:47:20 | [Synergit.Data.SqLite](https://www.nuget.org/packages/Synergit.Data.SqLite) | 3.1.0 | Synergit s.r.o. | Library of SQLite DB Thin Client for Synergit s.r.o. company |
| 2026-11-22 21:53:30 | [Lunate.Decisions.Model](https://www.nuget.org/packages/Lunate.Decisions.Model) | 1.18.0 | Lunate.Decisions.Model | The one decision model of Lunate: DecisionRequest, DecisionQuestion and its kin… |
| 2026-11-22 21:54:58 | [TxGold.Business](https://www.nuget.org/packages/TxGold.Business) | 0.3.0 | TxGold | TxGold Business API client: signed requests, payments, payment requests, holds,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
