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

## Latest list — 2026-10-30 08:21 UTC

New packages created between 2026-10-30 07:21 UTC and 2026-10-30 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T08-21-01-862462Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 07:32:32 | [RKNNSharp](https://www.nuget.org/packages/RKNNSharp) | 0.1.0 | sqk0232 | RK3588 DMA-frame RKNN inference with RGA preprocessing. |
| 2026-10-30 07:41:37 | [Extrode.Pare](https://www.nuget.org/packages/Extrode.Pare) | 0.6.1 | Extrode | TypeScript type stripper: overwrites type syntax with spaces, so the JavaScript… |
| 2026-10-30 07:41:38 | [Extrode.Pare.AspNetCore](https://www.nuget.org/packages/Extrode.Pare.AspNetCore) | 0.6.1 | Extrode | Re-strips changed TypeScript (wwwroot, PareServeAt sources, referenced Razor cl… |
| 2026-10-30 07:41:39 | [Extrode.Pare.Build](https://www.nuget.org/packages/Extrode.Pare.Build) | 0.6.1 | Extrode | Strips TypeScript type syntax to JavaScript during dotnet build. No Node. |
| 2026-10-30 07:53:59 | [Sdcb.SimdCodecs.Pnm](https://www.nuget.org/packages/Sdcb.SimdCodecs.Pnm) | 1.2.0 | sdcb | Pure-managed Netpbm decoder and encoder for .NET: PBM, PGM and PPM (P1-P6, plai… |
| 2026-10-30 07:54:08 | [Sdcb.SimdCodecs.Qoi](https://www.nuget.org/packages/Sdcb.SimdCodecs.Qoi) | 1.2.0 | sdcb | Pure-managed QOI ("Quite OK Image") decoder and encoder for .NET, written from… |
| 2026-10-30 07:57:39 | [Doka.EntityFrameworkCore.NestedSet.MySql](https://www.nuget.org/packages/Doka.EntityFrameworkCore.NestedSet.MySql) | 10.1.0 | Dominic Kalkbrenner | Nested-set hierarchy integration for the MySql Entity Framework Core provider. |
| 2026-10-30 07:57:45 | [Doka.EntityFrameworkCore.NestedSet.Postgres](https://www.nuget.org/packages/Doka.EntityFrameworkCore.NestedSet.Postgres) | 10.1.0 | Dominic Kalkbrenner | Nested-set hierarchy integration for the Postgres Entity Framework Core provide… |
| 2026-10-30 07:57:51 | [Doka.EntityFrameworkCore.NestedSet.Sqlite](https://www.nuget.org/packages/Doka.EntityFrameworkCore.NestedSet.Sqlite) | 10.1.0 | Dominic Kalkbrenner | Nested-set hierarchy integration for the Sqlite Entity Framework Core provider. |
| 2026-10-30 07:57:58 | [Doka.EntityFrameworkCore.NestedSet.SqlServer](https://www.nuget.org/packages/Doka.EntityFrameworkCore.NestedSet.SqlServer) | 10.1.0 | Dominic Kalkbrenner | Nested-set hierarchy integration for the SqlServer Entity Framework Core provid… |
| 2026-10-30 07:59:05 | [Iyu.Lowline](https://www.nuget.org/packages/Iyu.Lowline) | 0.46.0 | iyulab | iyu-framework-v5: OData + GraphQL runtime framework for .NET 10. |
| 2026-10-30 08:03:53 | [Aurionpro.PaymentFramework.Core10.0](https://www.nuget.org/packages/Aurionpro.PaymentFramework.Core10.0) | 10.0.0 | Core10 | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
