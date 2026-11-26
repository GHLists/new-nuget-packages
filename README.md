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

## Latest list — 2026-11-26 18:19 UTC

New packages created between 2026-11-26 17:19 UTC and 2026-11-26 18:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T18-19-23-565504Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 17:30:23 | [Iconclass.Core](https://www.nuget.org/packages/Iconclass.Core) | 0.0.1 | Daniele Fusi | Iconclass core module. |
| 2026-11-26 17:30:26 | [Iconclass.Import](https://www.nuget.org/packages/Iconclass.Import) | 0.0.1 | Daniele Fusi | Iconclass data import module. |
| 2026-11-26 17:30:29 | [Iconclass.PgSql](https://www.nuget.org/packages/Iconclass.PgSql) | 0.0.1 | Daniele Fusi | Iconclass PostgreSQL module. |
| 2026-11-26 17:30:33 | [Iconclass.Api.Controllers](https://www.nuget.org/packages/Iconclass.Api.Controllers) | 0.0.1 | Daniele Fusi | Iconclass API controllers module. |
| 2026-11-26 17:38:11 | [LineTen.Authentication.Hmac.Signing](https://www.nuget.org/packages/LineTen.Authentication.Hmac.Signing) | 4.0.0 | LineTen | LineTen Hmac request signing (LineTen-Hmac-1 / LineTen-Hmac-2), no ASP.NET Core… |
| 2026-11-26 17:45:02 | [TestPacket](https://www.nuget.org/packages/TestPacket) | 1.0.0 | shurdukov.ad | Package Description |
| 2026-11-26 17:55:51 | [Gravicode.Science.DaskNet.Geo](https://www.nuget.org/packages/Gravicode.Science.DaskNet.Geo) | 2.3.0 | Gravicode Studios | Geospatial operations for Dask.Net (a dask-geopandas analogue): geohashes, spat… |
| 2026-11-26 17:55:52 | [Gravicode.Science.DaskNet.Lakehouse](https://www.nuget.org/packages/Gravicode.Science.DaskNet.Lakehouse) | 2.3.0 | Gravicode Studios | Delta Lake and Apache Iceberg readers for Dask.Net: tables become partitioned D… |
| 2026-11-26 17:55:53 | [Gravicode.Science.DaskNet.ML](https://www.nuget.org/packages/Gravicode.Science.DaskNet.ML) | 2.3.0 | Gravicode Studios | Distributed machine learning for Dask.Net (a dask-ml analogue): grid and random… |
| 2026-11-26 17:55:54 | [Gravicode.Science.DaskNet.Streaming](https://www.nuget.org/packages/Gravicode.Science.DaskNet.Streaming) | 2.3.0 | Gravicode Studios | Micro-batch streaming for Dask.Net: filters, projections and SQL per batch on a… |
| 2026-11-26 17:59:00 | [Eternet.TestPlanner.Artifacts](https://www.nuget.org/packages/Eternet.TestPlanner.Artifacts) | 2.8.7 | Eternet | Bounded offline ETP artifact descriptors and producer-owned snapshot compatibil… |
| 2026-11-26 18:00:07 | [AntChain.SDK.INSURANCESAAS](https://www.nuget.org/packages/AntChain.SDK.INSURANCESAAS) | 1.1.0 | Ant Chain, Inc | Ant Chain INSURANCESAAS SDK Library for .NET |
| 2026-11-26 18:06:20 | [Jiron.Umbraco.FormBuilder.Core](https://www.nuget.org/packages/Jiron.Umbraco.FormBuilder.Core) | 17.0.0 | Jiron | The domain of Jiron Form Builder for Umbraco 17: form definitions, rules, valid… |
| 2026-11-26 18:06:21 | [Jiron.Umbraco.FormBuilder.AI](https://www.nuget.org/packages/Jiron.Umbraco.FormBuilder.AI) | 17.0.0 | Jiron | An optional add-on for Jiron Form Builder on Umbraco 17: editors draft a form f… |
| 2026-11-26 18:06:21 | [Jiron.Umbraco.FormBuilder.Web](https://www.nuget.org/packages/Jiron.Umbraco.FormBuilder.Web) | 17.0.0 | Jiron | The public and management APIs, form rendering, themes and the Forms section of… |
| 2026-11-26 18:06:22 | [Jiron.Umbraco.FormBuilder](https://www.nuget.org/packages/Jiron.Umbraco.FormBuilder) | 17.0.0 | Jiron | A form builder for Umbraco 17: editors design forms with pages, rules and actio… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
