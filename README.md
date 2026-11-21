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

## Latest list — 2026-11-21 03:19 UTC

New packages created between 2026-11-21 02:19 UTC and 2026-11-21 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T03-19-35-082073Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 02:27:15 | [AdaskoTheBeAsT.Interop.Execution.AspNetCore](https://www.nuget.org/packages/AdaskoTheBeAsT.Interop.Execution.AspNetCore) | 3.0.0 | Adam "AdaskoTheBeAsT" Plucińs… | ASP.NET Core minimal-API and diagnostics integration for AdaskoTheBeAsT.Interop… |
| 2026-11-21 02:50:15 | [fynydd.umbraco.search.postgres](https://www.nuget.org/packages/fynydd.umbraco.search.postgres) | 18.0.0 | Fynydd LLC | Postgres and pgvector storage for Umbraco semantic search. |
| 2026-11-21 02:52:53 | [Nedo.Agentic.Policy](https://www.nuget.org/packages/Nedo.Agentic.Policy) | 0.1.0 | PT. Sinergi Dimensi Informati… | Tool-policy decision of the Nedo Agentic platform: allow, deny or hold one tool… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
