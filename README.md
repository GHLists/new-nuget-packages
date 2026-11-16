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

## Latest list — 2026-11-16 05:20 UTC

New packages created between 2026-11-16 04:19 UTC and 2026-11-16 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T05-20-28-309611Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 04:34:47 | [AurorisNet.Umbraco.DisableTelemetry](https://www.nuget.org/packages/AurorisNet.Umbraco.DisableTelemetry) | 18.3.1.1 | Auroris | Stops Umbraco's telemetry beacon, installer reporting and dashboard news reques… |
| 2026-11-16 04:43:22 | [WebSharper.TensorFlowJs](https://www.nuget.org/packages/WebSharper.TensorFlowJs) | 10.1.0.752 | IntelliFactory | WebSharper bindings for TensorFlow.js 4.x (4.22.0+) |
| 2026-11-16 04:45:11 | [Vane.Container](https://www.nuget.org/packages/Vane.Container) | 1.0.0 | wangqingsong | Dependency injection container for .NET with MEF-style attribute composition, k… |
| 2026-11-16 04:46:06 | [Vane.Container.AspNetCore](https://www.nuget.org/packages/Vane.Container.AspNetCore) | 1.0.0 | wangqingsong | ASP.NET Core host integration for Vane.Container. Adds UseVaneContainer on IHos… |
| 2026-11-16 04:46:35 | [Vane.Container.Prism](https://www.nuget.org/packages/Vane.Container.Prism) | 1.0.0 | wangqingsong | Prism 8 IContainerExtension adapter for Vane.Container. Routes PrismApplication… |
| 2026-11-16 05:04:06 | [SqlChat.Client](https://www.nuget.org/packages/SqlChat.Client) | 0.1.0 | Drew Coogan | SqlChat public API: ISqlChatClient, SqlChatBuilder and dependency-injection reg… |
| 2026-11-16 05:04:06 | [SqlChat.Ai](https://www.nuget.org/packages/SqlChat.Ai) | 0.1.0 | Drew Coogan | Natural language to validated, read-only SQL for PostgreSQL and SQL Server, pow… |
| 2026-11-16 05:04:07 | [SqlChat.Domain](https://www.nuget.org/packages/SqlChat.Domain) | 0.1.0 | Drew Coogan | Core abstractions, domain models and result types for SqlChat. Referenced by th… |
| 2026-11-16 05:04:08 | [SqlChat.Service](https://www.nuget.org/packages/SqlChat.Service) | 0.1.0 | Drew Coogan | SqlChat orchestration engine and read-only SQL security validation. Referenced… |
| 2026-11-16 05:04:08 | [SqlChat.Data](https://www.nuget.org/packages/SqlChat.Data) | 0.1.0 | Drew Coogan | SqlChat schema providers (PostgreSQL, SQL Server, EF Core, DDL/JSON/YAML) and r… |
| 2026-11-16 05:10:02 | [Universal.Operative.Sdk.Databricks](https://www.nuget.org/packages/Universal.Operative.Sdk.Databricks) | 1.0.0 | Andrew Ong | REST-backed Databricks Genie tools for Operative, supporting multiple spaces an… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
