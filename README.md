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

## Latest list — 2026-09-30 01:20 UTC

New packages created between 2026-09-30 00:19 UTC and 2026-09-30 01:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T01-20-25-776926Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 00:34:22 | [VoxScript2](https://www.nuget.org/packages/VoxScript2) | 2.0.0 | Redvoxel Games | Easily embeddable scripting language |
| 2026-09-30 00:39:43 | [NGB.Platform.PostgreSql.AspNetCore](https://www.nuget.org/packages/NGB.Platform.PostgreSql.AspNetCore) | 3.0.0 | NGB Platform | ASP.NET Core health checks and canonical HTTP exception mapping for the NGB Pos… |
| 2026-09-30 00:39:45 | [NGB.Platform.Runtime.Hosting](https://www.nuget.org/packages/NGB.Platform.Runtime.Hosting) | 3.0.0 | NGB Platform | Generic-host lifecycle adapters for NGB Platform Runtime, including fail-fast s… |
| 2026-09-30 00:39:46 | [NGB.Platform.Hosting.AspNetCore](https://www.nuget.org/packages/NGB.Platform.Hosting.AspNetCore) | 3.0.0 | NGB Platform | Provider-neutral ASP.NET Core hosting, authentication, branding, health, CORS,… |
| 2026-09-30 00:39:49 | [NGB.Platform.BackgroundJobs.PostgreSql](https://www.nuget.org/packages/NGB.Platform.BackgroundJobs.PostgreSql) | 3.0.0 | NGB Platform | PostgreSQL Hangfire storage adapter and batched recurring-job inspection for NG… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
