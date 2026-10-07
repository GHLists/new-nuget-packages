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

## Latest list — 2026-10-07 04:21 UTC

New packages created between 2026-10-07 03:22 UTC and 2026-10-07 04:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T04-21-43-363776Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 03:33:58 | [Mibo.Markup](https://www.nuget.org/packages/Mibo.Markup) | 6.0.0 | Mibo.Markup | Package Description |
| 2026-10-07 03:38:19 | [SmartPipe.Extensions.Channels](https://www.nuget.org/packages/SmartPipe.Extensions.Channels) | 2.2.0 | SmartPipe | Channel merge primitives for SmartPipe.Core. |
| 2026-10-07 03:38:21 | [SmartPipe.Extensions.Transforms](https://www.nuget.org/packages/SmartPipe.Extensions.Transforms) | 2.2.0 | SmartPipe | Composable transforms for SmartPipe.Core. |
| 2026-10-07 03:38:22 | [SmartPipe.Extensions.Logging](https://www.nuget.org/packages/SmartPipe.Extensions.Logging) | 2.2.0 | SmartPipe | Logging sinks for SmartPipe.Core. |
| 2026-10-07 03:38:24 | [SmartPipe.Extensions.Csv](https://www.nuget.org/packages/SmartPipe.Extensions.Csv) | 2.2.0 | SmartPipe | Strict, bounded CSV sources and sinks for SmartPipe.Core. |
| 2026-10-07 03:38:25 | [SmartPipe.Extensions.Dapper](https://www.nuget.org/packages/SmartPipe.Extensions.Dapper) | 2.2.0 | SmartPipe | Explicit-SQL Dapper sources and sinks for SmartPipe.Core. |
| 2026-10-07 03:38:26 | [SmartPipe.Extensions.EntityFrameworkCore](https://www.nuget.org/packages/SmartPipe.Extensions.EntityFrameworkCore) | 2.2.0 | SmartPipe | Provider-neutral Entity Framework Core query sources for SmartPipe.Core. |
| 2026-10-07 03:38:28 | [SmartPipe.Extensions.Mapster](https://www.nuget.org/packages/SmartPipe.Extensions.Mapster) | 2.2.0 | SmartPipe | Mapster object-mapping transforms for SmartPipe.Core with composition-time conf… |
| 2026-10-07 03:38:29 | [SmartPipe.Extensions.Polly](https://www.nuget.org/packages/SmartPipe.Extensions.Polly) | 2.2.0 | SmartPipe | Polly resilience decorator for SmartPipe.Core transforms with explicit inner-tr… |
| 2026-10-07 03:38:30 | [SmartPipe.Extensions.Http](https://www.nuget.org/packages/SmartPipe.Extensions.Http) | 2.2.0 | SmartPipe | Streaming HTTP sources and sinks for SmartPipe.Core. |
| 2026-10-07 03:38:32 | [SmartPipe.Testing](https://www.nuget.org/packages/SmartPipe.Testing) | 2.2.0 | SmartPipe | Framework-neutral helpers for testing SmartPipe.Core sources and activations. |
| 2026-10-07 03:38:33 | [SmartPipe.Extensions.Http.Json](https://www.nuget.org/packages/SmartPipe.Extensions.Http.Json) | 2.2.0 | SmartPipe | Source-generated JSON codecs for streaming SmartPipe.Core HTTP pipelines. |
| 2026-10-07 03:38:34 | [SmartPipe.Extensions.DependencyInjection](https://www.nuget.org/packages/SmartPipe.Extensions.DependencyInjection) | 2.2.0 | SmartPipe | SmartPipe framework integration package for SmartPipe.Extensions.DependencyInje… |
| 2026-10-07 03:38:35 | [SmartPipe.Extensions.OpenTelemetry](https://www.nuget.org/packages/SmartPipe.Extensions.OpenTelemetry) | 2.2.0 | SmartPipe | Exporter-neutral OpenTelemetry registration for SmartPipe pipeline metrics and… |
| 2026-10-07 03:38:37 | [SmartPipe.Extensions.Hosting](https://www.nuget.org/packages/SmartPipe.Extensions.Hosting) | 2.2.0 | SmartPipe | SmartPipe host integration package for SmartPipe.Extensions.Hosting. |
| 2026-10-07 03:38:38 | [SmartPipe.Extensions.HealthChecks](https://www.nuget.org/packages/SmartPipe.Extensions.HealthChecks) | 2.2.0 | SmartPipe | Key-based liveness and readiness health checks for canonical SmartPipe pipeline… |
| 2026-10-07 03:38:39 | [SmartPipe.Extensions.DataAnnotations](https://www.nuget.org/packages/SmartPipe.Extensions.DataAnnotations) | 2.2.0 | SmartPipe | DataAnnotations validation transforms for SmartPipe.Core. |
| 2026-10-07 03:38:42 | [SmartPipe.Extensions.PostgreSql](https://www.nuget.org/packages/SmartPipe.Extensions.PostgreSql) | 2.2.0 | SmartPipe | PostgreSQL-native SmartPipe components: binary COPY streaming source, binary CO… |
| 2026-10-07 03:55:26 | [CrestronHomeDevTools.Automation](https://www.nuget.org/packages/CrestronHomeDevTools.Automation) | 1.25.0 | Neil Colvin | Durable Crestron Home submission workflow and shared test-session implementatio… |
| 2026-10-07 03:56:02 | [Carbon.WebAuthn](https://www.nuget.org/packages/Carbon.WebAuthn) | 0.1.0 | Carbon.WebAuthn | Package Description |
| 2026-10-07 03:57:43 | [CrestronHomeDevTools.SubmissionTests](https://www.nuget.org/packages/CrestronHomeDevTools.SubmissionTests) | 1.25.0 | Neil Colvin | Shared NUnit 5 submission fixture for running the same Crestron driver tests in… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
