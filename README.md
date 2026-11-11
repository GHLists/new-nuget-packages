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

## Latest list — 2026-11-11 16:19 UTC

New packages created between 2026-11-11 15:20 UTC and 2026-11-11 16:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T16-19-37-105898Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 15:21:22 | [GtG.Open.HC.SelectionAwarePaging](https://www.nuget.org/packages/GtG.Open.HC.SelectionAwarePaging) | 16.6.0 | GtG Open Maintainers | Selection-aware offset paging for Hot Chocolate: execute only the item, count a… |
| 2026-11-11 15:31:47 | [Noosh24.OpenApi](https://www.nuget.org/packages/Noosh24.OpenApi) | 0.1.0 | Noosh24 | Official .NET client for the Noosh24 Open API: menu, reservations, orders, paym… |
| 2026-11-11 15:32:27 | [HoneyDrunk.Agents.Operations](https://www.nuget.org/packages/HoneyDrunk.Agents.Operations) | 0.2.0 | HoneyDrunk Studios | The shared, versioned HTTP operations contract for HoneyDrunk Grid agent hosts… |
| 2026-11-11 15:32:41 | [SuperAdmin.Rbac](https://www.nuget.org/packages/SuperAdmin.Rbac) | 0.1.0.1 | Super Admin | Role-based authentication, URL-based permissions and a role-aware sidebar menu… |
| 2026-11-11 15:35:39 | [FaceCrop.NET](https://www.nuget.org/packages/FaceCrop.NET) | 1.0.0 | airtaxi | Face-aware maximum square cropping with an embedded BlazeFace short-range face… |
| 2026-11-11 15:36:09 | [Blueprint.Testing.HttpClient](https://www.nuget.org/packages/Blueprint.Testing.HttpClient) | 3.1.1 | Symprex | A test double of a Blueprint typed client's upstream for Blueprint.Testing: ans… |
| 2026-11-11 15:48:01 | [Cike.Security](https://www.nuget.org/packages/Cike.Security) | 1.0.12 | Lemon.Li | Package Description |
| 2026-11-11 15:48:02 | [Cike.MultiTenancy](https://www.nuget.org/packages/Cike.MultiTenancy) | 1.0.12 | Lemon.Li | Package Description |
| 2026-11-11 15:52:27 | [DynamicAuthorization.AspNetCore](https://www.nuget.org/packages/DynamicAuthorization.AspNetCore) | 2.0.0-beta-1 | Mohsen Esmailpour | Dynamic, permission-based authorization for ASP.NET Core MVC, Razor Pages and M… |
| 2026-11-11 15:52:28 | [DynamicAuthorization.AspNetCore.HybridCache](https://www.nuget.org/packages/DynamicAuthorization.AspNetCore.HybridCache) | 2.0.0-beta-1 | Mohsen Esmailpour | HybridCache store for DynamicAuthorization.AspNetCore. Shares cached user roles… |
| 2026-11-11 15:52:29 | [DynamicAuthorization.AspNetCore.EntityFrameworkCore](https://www.nuget.org/packages/DynamicAuthorization.AspNetCore.EntityFrameworkCore) | 2.0.0-beta-1 | Mohsen Esmailpour | Entity Framework Core store for DynamicAuthorization.AspNetCore. Keeps the perm… |
| 2026-11-11 15:52:30 | [DynamicAuthorization.AspNetCore.Dashboard](https://www.nuget.org/packages/DynamicAuthorization.AspNetCore.Dashboard) | 2.0.0-beta-1 | Mohsen Esmailpour | A dashboard for DynamicAuthorization.AspNetCore, built with Razor Pages: manage… |
| 2026-11-11 15:54:30 | [Nullean.Snapshots.Images.Assertions](https://www.nuget.org/packages/Nullean.Snapshots.Images.Assertions) | 0.9.0 | Nullean and contributors | AwesomeAssertions extensions for Nullean.Snapshots.Images: MatchImageSnapshot f… |
| 2026-11-11 15:57:14 | [SI.Rosetta.Aggregates.PostgreSQL](https://www.nuget.org/packages/SI.Rosetta.Aggregates.PostgreSQL) | 1.36.0 | SI.Rosetta.Aggregates.Postgre… | Package Description |
| 2026-11-11 15:59:11 | [Slugger](https://www.nuget.org/packages/Slugger) | 1.2.0 | Reefact | The slugger command: human-readable random names, Docker- and Heroku-style (hum… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
