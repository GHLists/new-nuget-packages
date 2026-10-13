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

## Latest list — 2026-10-13 12:21 UTC

New packages created between 2026-10-13 11:19 UTC and 2026-10-13 12:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T12-21-09-847368Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 11:55:33 | [SU2.C15e.Infrastructure.Http](https://www.nuget.org/packages/SU2.C15e.Infrastructure.Http) | 2.0.3 | SU2 Platform | External HTTP client foundation with destination validation and safe transport… |
| 2026-10-13 11:56:11 | [SU2.C15e.UseCases.Data](https://www.nuget.org/packages/SU2.C15e.UseCases.Data) | 2.0.3 | SU2 Platform | Opt-in EF Core and Dapper application data ports. |
| 2026-10-13 12:00:18 | [aio](https://www.nuget.org/packages/aio) | 0.3.0 | asantamariaplainconcepts | AI Orchestrator: the loop that takes an issue to a merged pull request, in your… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
