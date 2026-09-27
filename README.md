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

## Latest list — 2026-09-27 16:20 UTC

New packages created between 2026-09-27 15:20 UTC and 2026-09-27 16:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-27T16-20-23-053772Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-27 15:23:07 | [Soenneker.Facebook.OpenApiClientUtil](https://www.nuget.org/packages/Soenneker.Facebook.OpenApiClientUtil) | 4.0.2 | Jake Soenneker | A thread-safe utility for obtaining Facebook's OpenApiClient singleton. |
| 2026-09-27 15:23:42 | [Soenneker.Instagram.OpenApiClientUtil](https://www.nuget.org/packages/Soenneker.Instagram.OpenApiClientUtil) | 4.0.2 | Jake Soenneker | A thread-safe utility for obtaining Instagram's OpenApiClient singleton. |
| 2026-09-27 15:32:44 | [AbacusBusinessSoftware.AbaReport](https://www.nuget.org/packages/AbacusBusinessSoftware.AbaReport) | 0.0.5 | ABACUS | ABACUS AbaReport REST API SDK module for .NET. |
| 2026-09-27 15:32:49 | [AbacusBusinessSoftware.DependencyInjection](https://www.nuget.org/packages/AbacusBusinessSoftware.DependencyInjection) | 0.0.5 | ABACUS | Registers all packaged ABACUS SDK module clients for dependency injection. |
| 2026-09-27 15:32:58 | [AbacusBusinessSoftware.Testing](https://www.nuget.org/packages/AbacusBusinessSoftware.Testing) | 0.0.5 | ABACUS | Test helpers for ABACUS .NET SDK (capturing/fake HTTP handlers, OData response… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
