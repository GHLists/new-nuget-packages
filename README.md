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

## Latest list — 2026-11-18 08:22 UTC

New packages created between 2026-11-18 07:19 UTC and 2026-11-18 08:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T08-22-13-748574Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 07:24:09 | [Jens.EntityMapper](https://www.nuget.org/packages/Jens.EntityMapper) | 0.1.0 | Jens | Convention-based object-to-object mapper with mapping profiles and IQueryable p… |
| 2026-11-18 07:27:37 | [NettyApps.Platform.API](https://www.nuget.org/packages/NettyApps.Platform.API) | 10.0.0 | NettyApps Enterprise Architec… | Database-agnostic ASP.NET Core (.NET 10 & .NET 11) headless REST API SDK for al… |
| 2026-11-18 07:30:30 | [Eplicta.Ipx](https://www.nuget.org/packages/Eplicta.Ipx) | 1.0.0 | Eplicta AB | Reads, writes and validates IPX, the Information Plan Exchange format for infor… |
| 2026-11-18 07:30:31 | [Eplicta.Ipx.Tool](https://www.nuget.org/packages/Eplicta.Ipx.Tool) | 1.0.0 | Eplicta AB | The ipx command-line tool: validate IPX documents, and compare the retention of… |
| 2026-11-18 07:32:41 | [OpenDCP.Framework.Connections.Datasource.Snowflake](https://www.nuget.org/packages/OpenDCP.Framework.Connections.Datasource.Snowflake) | 0.3.0 | OpenDCP.Framework.Connections… | Package Description |
| 2026-11-18 07:33:44 | [NettyApps.Platform.AspNetCore](https://www.nuget.org/packages/NettyApps.Platform.AspNetCore) | 10.0.0 | NettyApps Enterprise Architec… | Database-agnostic ASP.NET Core (.NET 10 & .NET 11) security and multi-tenancy S… |
| 2026-11-18 07:33:53 | [NanoFlags.OpenFeature](https://www.nuget.org/packages/NanoFlags.OpenFeature) | 0.1.0 | NanoFlags | OpenFeature (https://openfeature.dev) provider for the NanoFlags .NET server SD… |
| 2026-11-18 07:33:53 | [NanoFlags](https://www.nuget.org/packages/NanoFlags) | 0.1.0 | NanoFlags | NanoFlags feature flags for .NET servers: local, synchronous evaluation (a port… |
| 2026-11-18 07:34:30 | [NettyApps.Platform.Primitives](https://www.nuget.org/packages/NettyApps.Platform.Primitives) | 10.0.0 | NettyApps Enterprise Architec… | Universal zero-dependency enterprise primitives for .NET 10 and .NET 11 across… |
| 2026-11-18 07:37:21 | [Mafesoft.VimeoClient.Extensions.DependencyInjection](https://www.nuget.org/packages/Mafesoft.VimeoClient.Extensions.DependencyInjection) | 3.4.2 | Federico Mazzanti | Registers Mafesoft.VimeoClient in the Microsoft.Extensions dependency injection… |
| 2026-11-18 07:45:53 | [Hlibz.MinimalApi.Endpoints.FluentValidation](https://www.nuget.org/packages/Hlibz.MinimalApi.Endpoints.FluentValidation) | 1.0.0 | Hlib Zinchenko | Automatic FluentValidation for Hlibz.MinimalApi.Endpoints: options.AddFluentVal… |
| 2026-11-18 07:45:53 | [Hlibz.MinimalApi.Endpoints](https://www.nuget.org/packages/Hlibz.MinimalApi.Endpoints) | 1.0.0 | Hlib Zinchenko | One class per minimal API endpoint, discovered and mapped for you: implement IE… |
| 2026-11-18 07:46:13 | [Hlibz.Paging](https://www.nuget.org/packages/Hlibz.Paging) | 1.0.0 | Hlib Zinchenko | Paging and sorting for list endpoints: [Sortable] marks which DTO properties a… |
| 2026-11-18 07:46:14 | [Hlibz.Paging.EntityFrameworkCore](https://www.nuget.org/packages/Hlibz.Paging.EntityFrameworkCore) | 1.0.0 | Hlib Zinchenko | PaginateAsync for Entity Framework Core: sorts an IQueryable by Hlibz.Paging's… |
| 2026-11-18 07:53:22 | [Hlibz.OpenApi.AspNetCore](https://www.nuget.org/packages/Hlibz.OpenApi.AspNetCore) | 1.0.0 | Hlib Zinchenko | Transformers for Microsoft.AspNetCore.OpenApi: XML summaries as descriptions, r… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
