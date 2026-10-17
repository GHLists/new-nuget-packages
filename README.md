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

## Latest list — 2026-10-17 14:21 UTC

New packages created between 2026-10-17 13:21 UTC and 2026-10-17 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T14-21-49-925263Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 13:34:24 | [Fuaran.UI.Design](https://www.nuget.org/packages/Fuaran.UI.Design) | 0.95.0 | Andrew J. Willshire | Fuaran UI described as a design system: one call renders a preview card per IDL… |
| 2026-10-17 13:34:55 | [Fuaran.UI.Validator.Certification](https://www.nuget.org/packages/Fuaran.UI.Validator.Certification) | 0.95.0 | Andrew J. Willshire | Fuaran recipe / fragment certification: proves a parameterised fragment emits a… |
| 2026-10-17 13:35:29 | [Kododo.Way.Shell](https://www.nuget.org/packages/Kododo.Way.Shell) | 2.0.0 | Kododo | Shared UI shell for Kododo Way libraries (ConfigWay, CultureWay, RunWay, LogWay… |
| 2026-10-17 13:36:21 | [Pinqponq.Observability.Abstractions](https://www.nuget.org/packages/Pinqponq.Observability.Abstractions) | 1.0.0 | Pinqponq | ILogService, the logging contract of Pinqponq.Observability, without any depend… |
| 2026-10-17 13:36:22 | [Pinqponq.Observability](https://www.nuget.org/packages/Pinqponq.Observability) | 1.0.0 | Pinqponq | Pinqloq logging for ASP.NET Core: one structured record per request (redacted r… |
| 2026-10-17 13:36:23 | [Pinqponq.Contracts](https://www.nuget.org/packages/Pinqponq.Contracts) | 1.0.0 | Pinqponq | Shared API contracts: the base response and error envelope (compatible with dev… |
| 2026-10-17 13:36:23 | [Brows.Win32.STAThreadPool.Contracts](https://www.nuget.org/packages/Brows.Win32.STAThreadPool.Contracts) | 1.3.0 | Ken Yourek | Contracts for a reusable single-threaded apartment thread pool. The contracts a… |
| 2026-10-17 13:36:23 | [Pinqponq.Database.Postgres.EntityFrameworkCore](https://www.nuget.org/packages/Pinqponq.Database.Postgres.EntityFrameworkCore) | 1.0.0 | Pinqponq | Registers an EF Core DbContext on PostgreSQL (Npgsql) with one shared NpgsqlDat… |
| 2026-10-17 13:36:24 | [Pinqponq.ErrorHandling.Postgres](https://www.nuget.org/packages/Pinqponq.ErrorHandling.Postgres) | 1.0.0 | Pinqponq | PostgreSQL error mapping for Pinqponq.ErrorHandling: turns Npgsql PostgresExcep… |
| 2026-10-17 13:38:50 | [ComPeter.PrimeNGTable](https://www.nuget.org/packages/ComPeter.PrimeNGTable) | 8.1.3 | Alex Ibrahim Ojea,ComPeter | Community-maintained fork of ECS.PrimeNGTable, based on the original project by… |
| 2026-10-17 13:40:22 | [ForbiddenChars](https://www.nuget.org/packages/ForbiddenChars) | 0.1.0 | ryuchan00 | A C# source generator that turns a string field into a property whose setter re… |
| 2026-10-17 13:45:20 | [Prowl.Graphite.Rendering](https://www.nuget.org/packages/Prowl.Graphite.Rendering) | 3.8.0 | Prowl Contributors | The high level renderer of Prowl.Graphite: worlds, meshes, materials, views and… |
| 2026-10-17 13:46:30 | [Kododo.CultureWay](https://www.nuget.org/packages/Kododo.CultureWay) | 2.0.0 | Kododo | Runtime localization editor for ASP.NET Core. Persist and edit translated strin… |
| 2026-10-17 13:46:31 | [Kododo.CultureWay.Core](https://www.nuget.org/packages/Kododo.CultureWay.Core) | 2.0.0 | Kododo | Core abstractions for CultureWay: the IStore and IReadOnlySource interfaces and… |
| 2026-10-17 13:46:31 | [Kododo.CultureWay.PostgreSQL](https://www.nuget.org/packages/Kododo.CultureWay.PostgreSQL) | 2.0.0 | Kododo | PostgreSQL persistence store for CultureWay. Keeps translations, added language… |
| 2026-10-17 13:46:31 | [Kododo.CultureWay.UI](https://www.nuget.org/packages/Kododo.CultureWay.UI) | 2.0.0 | Kododo | Embedded web UI for CultureWay. Adds a React-based localization editor served d… |
| 2026-10-17 13:47:13 | [Vestigium.Helpers.Kql.AppMgmt](https://www.nuget.org/packages/Vestigium.Helpers.Kql.AppMgmt) | 1.0.0 | Vestigium | AppMgmt field catalogs and sessions for Vestigium.Helpers.Kql. |
| 2026-10-17 13:49:04 | [Xunit.SharedExamples](https://www.nuget.org/packages/Xunit.SharedExamples) | 0.1.0 | ryuchan00 | RSpec-style shared examples for xUnit.net v3, built on default interface method… |
| 2026-10-17 14:06:13 | [Minos.NET.Evaluation](https://www.nuget.org/packages/Minos.NET.Evaluation) | 1.2.0 | Marcel Roozekrans | Labelled decision datasets for Minos.NET: a versioned JSONL format that pairs e… |
| 2026-10-17 14:06:17 | [Minos.NET.Tool](https://www.nuget.org/packages/Minos.NET.Tool) | 1.2.0 | Marcel Roozekrans | The minos command line tool for Minos.NET: calibrates a decision model against… |
| 2026-10-17 14:06:28 | [Lokad.Image](https://www.nuget.org/packages/Lokad.Image) | 0.1.0 | Lokad | Safe managed image codecs and basic image editing for .NET. |
| 2026-10-17 14:13:20 | [ThorstenSauter.Azure.Cosmos.Migrations](https://www.nuget.org/packages/ThorstenSauter.Azure.Cosmos.Migrations) | 0.1.0 | Thorsten Sauter | Versioned, reversible migrations for Azure Cosmos DB (NoSQL): ordered C# migrat… |
| 2026-10-17 14:13:20 | [ThorstenSauter.Azure.Cosmos.Migrations.Tool](https://www.nuget.org/packages/ThorstenSauter.Azure.Cosmos.Migrations.Tool) | 0.1.0 | Thorsten Sauter | Command-line tool for ThorstenSauter.Azure.Cosmos.Migrations: apply, roll back,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
