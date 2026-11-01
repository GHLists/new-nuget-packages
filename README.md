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

## Latest list — 2026-11-01 18:18 UTC

New packages created between 2026-11-01 17:20 UTC and 2026-11-01 18:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T18-18-29-245422Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 17:49:22 | [Karya.Core.Identity](https://www.nuget.org/packages/Karya.Core.Identity) | 1.0.0 | Ramazan Karagoz | Karya Core Identity Layer - Authentication and Authorization for .NET 10 |
| 2026-11-01 17:55:06 | [PostgresStudio.Diagnostics](https://www.nuget.org/packages/PostgresStudio.Diagnostics) | 0.11.0 | Marko Lahma | The diagnostics engine of Postgres Studio and Marten Studio, with no ASP.NET Co… |
| 2026-11-01 17:59:55 | [Pondhawk.Utilities](https://www.nuget.org/packages/Pondhawk.Utilities) | 1.0.0 | Pond Hawk Technologies Inc. | Configuration-driven DI modules, service startup, pipelines and type helpers fo… |
| 2026-11-01 18:01:01 | [Pondhawk.Exceptions](https://www.nuget.org/packages/Pondhawk.Exceptions) | 1.0.0 | Pond Hawk Technologies Inc. | Transport-agnostic error model and common exception types for .NET. |
| 2026-11-01 18:01:02 | [Pondhawk.Mediator](https://www.nuget.org/packages/Pondhawk.Mediator) | 1.0.0 | Pond Hawk Technologies Inc. | Lightweight CQRS-style request/response mediator with pipeline behaviors and a… |
| 2026-11-01 18:01:15 | [Packata.Http](https://www.nuget.org/packages/Packata.Http) | 1.25.0 | Cédric L. Charlier | Optional embeddable HTTP hosting and row representations for selected Packata c… |
| 2026-11-01 18:01:16 | [Packata.Http.Arrow](https://www.nuget.org/packages/Packata.Http.Arrow) | 1.25.0 | Cédric L. Charlier | Optional Arrow IPC representation for Packata HTTP asset hosting. |
| 2026-11-01 18:07:53 | [FIAP.TechChallenge.Execution.Application.Messaging](https://www.nuget.org/packages/FIAP.TechChallenge.Execution.Application.Messaging) | 0.1.0 | João Victor Maieru Teixeira | Integration message contracts published by the Execution service. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
