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

## Latest list — 2026-10-07 09:19 UTC

New packages created between 2026-10-07 08:20 UTC and 2026-10-07 09:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T09-19-50-539293Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 08:24:45 | [DotGuard.Cli](https://www.nuget.org/packages/DotGuard.Cli) | 0.1.4 | DotGuard | .NET Production Readiness and Security Auditor |
| 2026-10-07 08:25:30 | [Corner49.Infra.AzureCosmosDB](https://www.nuget.org/packages/Corner49.Infra.AzureCosmosDB) | 10.0.146 | Frank Vanderlinden | Opinionated repository layer for Azure Cosmos DB: automatic container creation,… |
| 2026-10-07 08:25:31 | [Corner49.Infra.AzureServiceBus](https://www.nuget.org/packages/Corner49.Infra.AzureServiceBus) | 10.0.146 | Frank Vanderlinden | Opinionated messaging on Azure Service Bus: auto-provisioned queues and topics,… |
| 2026-10-07 08:25:32 | [Corner49.Infra.AzureStorage](https://www.nuget.org/packages/Corner49.Infra.AzureStorage) | 10.0.146 | Frank Vanderlinden | Opinionated wrappers for Azure Blob Storage and Azure File Shares. Part of the… |
| 2026-10-07 08:25:32 | [Corner49.Infra.CLI](https://www.nuget.org/packages/Corner49.Infra.CLI) | 10.0.146 | Frank Vanderlinden | Opinionated bootstrap for .NET console apps, workers and containerised jobs: co… |
| 2026-10-07 08:25:33 | [Corner49.Infra.Core](https://www.nuget.org/packages/Corner49.Infra.Core) | 10.0.146 | Frank Vanderlinden | Shared abstractions and utilities for the Corner49.Infra packages, a set of pac… |
| 2026-10-07 08:33:09 | [Expresso.Rendering.Linq](https://www.nuget.org/packages/Expresso.Rendering.Linq) | 0.10.0 | itorgashov | Render Expresso expression trees to LINQ predicates and sort keys for IQueryabl… |
| 2026-10-07 08:33:39 | [Expresso.Rendering.EntityFramework](https://www.nuget.org/packages/Expresso.Rendering.EntityFramework) | 0.10.0 | itorgashov | Render Expresso filters and sorts to Entity Framework 6 predicates and sort key… |
| 2026-10-07 08:33:53 | [Expresso.Rendering.EntityFrameworkCore](https://www.nuget.org/packages/Expresso.Rendering.EntityFrameworkCore) | 0.10.0 | itorgashov | Render Expresso filters and sorts to EF Core predicates and sort keys, with pro… |
| 2026-10-07 08:41:31 | [Testinium.DevicePark](https://www.nuget.org/packages/Testinium.DevicePark) | 1.0.0 | Device Park Team | Official .NET SDK for the Device Park public APIs. Discover devices, manage poo… |
| 2026-10-07 08:46:13 | [Nexus.Casp.Sdk](https://www.nuget.org/packages/Nexus.Casp.Sdk) | 2026.10.7 | Quantoz Technology | .NET client and dependency injection support for the Quantoz Nexus CASP API. |
| 2026-10-07 09:02:32 | [Moberg.Beacon.AI](https://www.nuget.org/packages/Moberg.Beacon.AI) | 4.5.0.2 | Moberg | Beacon AI extensions library providing LLM-powered documentation generation, al… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
