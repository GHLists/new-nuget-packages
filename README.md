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

## Latest list — 2026-11-03 02:20 UTC

New packages created between 2026-11-03 01:19 UTC and 2026-11-03 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T02-20-19-436277Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 01:46:42 | [ISL.NetFramework.Payment](https://www.nuget.org/packages/ISL.NetFramework.Payment) | 1.0.1 | ISL.com | Core abstractions, models, enums, and bootstrap options for the ISL multi-gatew… |
| 2026-11-03 02:03:26 | [IxIFlow](https://www.nuget.org/packages/IxIFlow) | 1.0.0 | HumanHub LLC | Durable workflow engine for .NET with typed activities, recovery, sagas, waits… |
| 2026-11-03 02:07:37 | [IxIFlow.Abstractions](https://www.nuget.org/packages/IxIFlow.Abstractions) | 1.0.0 | HumanHub LLC | Activity, recovery, scope and data-mapping contracts for IxIFlow workflow autho… |
| 2026-11-03 02:07:38 | [IxIFlow.AspNetCore](https://www.nuget.org/packages/IxIFlow.AspNetCore) | 1.0.0 | HumanHub LLC | Authorized HTTP triggers, CloudEvents ingress and workflow operations for IxIFl… |
| 2026-11-03 02:07:39 | [IxIFlow.Authoring](https://www.nuget.org/packages/IxIFlow.Authoring) | 1.0.0 | HumanHub LLC | Workflow document validation and activity catalogs for IxIFlow. |
| 2026-11-03 02:07:40 | [IxIFlow.Coordinator](https://www.nuget.org/packages/IxIFlow.Coordinator) | 1.0.0 | HumanHub LLC | Stateless workflow matching and host links over JSON gRPC streams. |
| 2026-11-03 02:07:40 | [IxIFlow.Debugging](https://www.nuget.org/packages/IxIFlow.Debugging) | 1.0.0 | HumanHub LLC | Optional pure C# breakpoint conditions for IxIFlow. |
| 2026-11-03 02:07:41 | [IxIFlow.Generators](https://www.nuget.org/packages/IxIFlow.Generators) | 1.0.0 | HumanHub LLC | Workflow YAML document models, validation, translation and source generation fo… |
| 2026-11-03 02:07:42 | [IxIFlow.PostgreSql](https://www.nuget.org/packages/IxIFlow.PostgreSql) | 1.0.0 | HumanHub LLC | PostgreSQL store for IxIFlow: instances, inbox, waits, traces, the completion o… |
| 2026-11-03 02:07:43 | [IxIFlow.Relational](https://www.nuget.org/packages/IxIFlow.Relational) | 1.0.0 | HumanHub LLC | Shared protocol with internal extension points for the first-party IxIFlow rela… |
| 2026-11-03 02:07:44 | [IxIFlow.Sqlite](https://www.nuget.org/packages/IxIFlow.Sqlite) | 1.0.0 | HumanHub LLC | SQLite store for single-host durable IxIFlow workflows. |
| 2026-11-03 02:07:45 | [IxIFlow.SqlServer](https://www.nuget.org/packages/IxIFlow.SqlServer) | 1.0.0 | HumanHub LLC | SQL Server store for IxIFlow: instances, inbox, waits, traces and the completio… |
| 2026-11-03 02:07:46 | [IxIFlow.Templates](https://www.nuget.org/packages/IxIFlow.Templates) | 1.0.0 | HumanHub LLC | Versioned templates for IxIFlow: the RenderTemplate and SendTemplateMessage act… |
| 2026-11-03 02:07:47 | [IxIFlow.Templates.Liquid](https://www.nuget.org/packages/IxIFlow.Templates.Liquid) | 1.0.0 | HumanHub LLC | Liquid template engine for IxIFlow templates, built on Fluid. |
| 2026-11-03 02:07:47 | [IxIFlow.Webhooks](https://www.nuget.org/packages/IxIFlow.Webhooks) | 1.0.0 | HumanHub LLC | Standard Webhooks publisher for IxIFlow workflow outbox events. |
| 2026-11-03 02:08:08 | [VpnHood.AppLib.App.WindowsTun](https://www.nuget.org/packages/VpnHood.AppLib.App.WindowsTun) | 9.1.864 | VpnHood.AppLib.App.WindowsTun | Shared library for VpnHood Windows Clients |
| 2026-11-03 02:08:12 | [VpnHood.AppLib.Stores.GalaxyStore.Core](https://www.nuget.org/packages/VpnHood.AppLib.Stores.GalaxyStore.Core) | 9.1.864 | VpnHood.AppLib.Stores.GalaxyS… | VpnHood Galaxy Store updates, which any Galaxy Store app can use. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
