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

## Latest list — 2026-10-04 02:21 UTC

New packages created between 2026-10-04 01:19 UTC and 2026-10-04 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T02-21-39-84468Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 01:28:16 | [Syntrony.EntityFrameworkCore.Repositories](https://www.nuget.org/packages/Syntrony.EntityFrameworkCore.Repositories) | 1.0.0 | Syntrony Technologies Inc. | EF Core implementation of the Syntrony.Repositories contract: EfCoreRepositoryB… |
| 2026-10-04 01:30:33 | [Themia.Storage.Cloudflare](https://www.nuget.org/packages/Themia.Storage.Cloudflare) | 0.30.3 | Sarawut Phaekuntod | Cloudflare cache-purge implementation of Themia.Storage's ICdnPurger: after a p… |
| 2026-10-04 01:37:20 | [Patware.Pipeline.Persistence.EntityFrameworkCore](https://www.nuget.org/packages/Patware.Pipeline.Persistence.EntityFrameworkCore) | 0.1.0 | Patware | Persist .NET workflow history and execution state in SQL Server with Entity Fra… |
| 2026-10-04 01:37:57 | [Patware.Pipeline.Hangfire](https://www.nuget.org/packages/Patware.Pipeline.Hangfire) | 0.1.0 | Patware | Power .NET workflows with Hangfire processing, scheduled polling, and recovery… |
| 2026-10-04 01:38:21 | [Patware.Pipeline.Blazor](https://www.nuget.org/packages/Patware.Pipeline.Blazor) | 0.1.0 | Patware | Bring .NET workflows into view with Blazor pages for pipeline run history, job… |
| 2026-10-04 01:40:08 | [Nimblesite.DataProvider.Migration.SqlServer](https://www.nuget.org/packages/Nimblesite.DataProvider.Migration.SqlServer) | 0.10.0-beta | ChristianFindlay | SQL Server DDL generator and schema inspector for Nimblesite.DataProvider.Migra… |
| 2026-10-04 01:49:00 | [CISS.SideMenu.Oqtane](https://www.nuget.org/packages/CISS.SideMenu.Oqtane) | 2.2.23 | Dao Hung | Build polished Oqtane 10.2.1 sites with the ACME theme, CISS Menu Builder, Auto… |
| 2026-10-04 02:02:27 | [ova.EntityNexus.Abstractions](https://www.nuget.org/packages/ova.EntityNexus.Abstractions) | 10.7.1 | ovaataaridotru | Domain model for EntityNexus DSL Framework is absract model for implementing by… |
| 2026-10-04 02:12:11 | [Elsa.Bpmn](https://www.nuget.org/packages/Elsa.Bpmn) | 3.9.0 | Elsa Workflows Community | Provides BPMN execution support by wiring the Bpmn.Model and Bpmn.Semantics lib… |
| 2026-10-04 02:12:11 | [Elsa.Bpmn.Interchange](https://www.nuget.org/packages/Elsa.Bpmn.Interchange) | 3.9.0 | Elsa Workflows Community | Provides BPMN XML interchange support by wiring the Bpmn.Interchange library in… |
| 2026-10-04 02:12:13 | [Elsa.Diagnostics.ConsoleLogs](https://www.nuget.org/packages/Elsa.Diagnostics.ConsoleLogs) | 3.9.0 | Elsa Workflows Community | Provides live raw console log streaming for Elsa hosts. |
| 2026-10-04 02:12:35 | [Elsa.UserTasks](https://www.nuget.org/packages/Elsa.UserTasks) | 3.9.0 | Elsa Workflows Community | Provides identity-neutral, workflow-bound human user tasks. |
| 2026-10-04 02:12:36 | [Elsa.UserTasks.Persistence.EFCore](https://www.nuget.org/packages/Elsa.UserTasks.Persistence.EFCore) | 3.9.0 | Elsa Workflows Community | Provides Entity Framework Core persistence for Elsa user tasks. |
| 2026-10-04 02:12:36 | [Elsa.UserTasks.Persistence.EFCore.MySql](https://www.nuget.org/packages/Elsa.UserTasks.Persistence.EFCore.MySql) | 3.9.0 | Elsa Workflows Community | Provides MySQL EF Core persistence for Elsa user tasks. |
| 2026-10-04 02:12:37 | [Elsa.UserTasks.Persistence.EFCore.Oracle](https://www.nuget.org/packages/Elsa.UserTasks.Persistence.EFCore.Oracle) | 3.9.0 | Elsa Workflows Community | Provides Oracle EF Core persistence for Elsa user tasks. |
| 2026-10-04 02:12:37 | [Elsa.UserTasks.Persistence.EFCore.PostgreSql](https://www.nuget.org/packages/Elsa.UserTasks.Persistence.EFCore.PostgreSql) | 3.9.0 | Elsa Workflows Community | Provides PostgreSQL EF Core persistence for Elsa user tasks. |
| 2026-10-04 02:12:37 | [Elsa.UserTasks.Persistence.EFCore.SqlServer](https://www.nuget.org/packages/Elsa.UserTasks.Persistence.EFCore.SqlServer) | 3.9.0 | Elsa Workflows Community | Provides SQL Server EF Core persistence for Elsa user tasks. |
| 2026-10-04 02:12:37 | [Elsa.UserTasks.Persistence.EFCore.Sqlite](https://www.nuget.org/packages/Elsa.UserTasks.Persistence.EFCore.Sqlite) | 3.9.0 | Elsa Workflows Community | Provides SQLite EF Core persistence for Elsa user tasks. |
| 2026-10-04 02:12:38 | [Elsa.UserTasks.Persistence.VNext](https://www.nuget.org/packages/Elsa.UserTasks.Persistence.VNext) | 3.9.0 | Elsa Workflows Community | Provides provider-neutral experimental persistence for Elsa user tasks. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
