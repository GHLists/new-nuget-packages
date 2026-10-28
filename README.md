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

## Latest list — 2026-10-28 01:20 UTC

New packages created between 2026-10-28 00:18 UTC and 2026-10-28 01:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T01-20-22-328154Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 00:32:25 | [LiteBus.Commands.Recurring](https://www.nuget.org/packages/LiteBus.Commands.Recurring) | 7.0.0 | A. Shafie | Recurring commands: a hosted loop that sends a configured command through the c… |
| 2026-10-28 00:32:26 | [LiteBus.Commands.Recurring.Storage.PostgreSql](https://www.nuget.org/packages/LiteBus.Commands.Recurring.Storage.PostgreSql) | 7.0.0 | A. Shafie | Storage adapter and registration APIs for the LiteBus.Commands.Recurring.Storag… |
| 2026-10-28 00:32:28 | [LiteBus.Commands.Storage.Marten](https://www.nuget.org/packages/LiteBus.Commands.Storage.Marten) | 7.0.0 | A. Shafie | Storage adapter and registration APIs for the LiteBus.Commands.Storage.Marten p… |
| 2026-10-28 00:32:29 | [LiteBus.Commands.Storage.PostgreSql](https://www.nuget.org/packages/LiteBus.Commands.Storage.PostgreSql) | 7.0.0 | A. Shafie | Storage adapter and registration APIs for the LiteBus.Commands.Storage.PostgreS… |
| 2026-10-28 00:33:00 | [LiteBus.Messaging.Extensions.OpenTelemetry](https://www.nuget.org/packages/LiteBus.Messaging.Extensions.OpenTelemetry) | 7.0.0 | A. Shafie | Host-framework composition APIs for the LiteBus.Messaging.Extensions.OpenTeleme… |
| 2026-10-28 00:33:11 | [LiteBus.Outbox.Storage.Marten](https://www.nuget.org/packages/LiteBus.Outbox.Storage.Marten) | 7.0.0 | A. Shafie | Storage adapter and registration APIs for the LiteBus.Outbox.Storage.Marten pac… |
| 2026-10-28 00:33:29 | [StdUnit.Tags.JobsTable](https://www.nuget.org/packages/StdUnit.Tags.JobsTable) | 0.1.0 | StdUnit.Tags.JobsTable | Package Description |
| 2026-10-28 00:40:48 | [Byd.CoreExtensions.Domain.Shared](https://www.nuget.org/packages/Byd.CoreExtensions.Domain.Shared) | 0.3.11 | mertbyd | Byd.CoreExtensions core modul katmani. |
| 2026-10-28 00:40:50 | [Byd.AntiDuplicate.Middleware](https://www.nuget.org/packages/Byd.AntiDuplicate.Middleware) | 0.3.11 | mertbyd | Byd.CoreExtensions core modul katmani. |
| 2026-10-28 00:40:51 | [Byd.CoreExtensions.Domain](https://www.nuget.org/packages/Byd.CoreExtensions.Domain) | 0.3.11 | mertbyd | Byd.CoreExtensions core modul katmani. |
| 2026-10-28 00:40:53 | [Byd.CoreExtensions.Application.Contracts](https://www.nuget.org/packages/Byd.CoreExtensions.Application.Contracts) | 0.3.11 | mertbyd | Byd.CoreExtensions core modul katmani. |
| 2026-10-28 00:40:55 | [Byd.CoreExtensions.EntityFrameworkCore](https://www.nuget.org/packages/Byd.CoreExtensions.EntityFrameworkCore) | 0.3.11 | mertbyd | Byd.CoreExtensions core modul katmani. |
| 2026-10-28 00:40:57 | [Byd.CoreExtensions.Application](https://www.nuget.org/packages/Byd.CoreExtensions.Application) | 0.3.11 | mertbyd | Byd.CoreExtensions core modul katmani. |
| 2026-10-28 00:40:59 | [Byd.CoreExtensions.HttpApi](https://www.nuget.org/packages/Byd.CoreExtensions.HttpApi) | 0.3.11 | mertbyd | Byd.CoreExtensions core modul katmani. |
| 2026-10-28 00:47:11 | [BusinessHarness](https://www.nuget.org/packages/BusinessHarness) | 0.1.0 | Jihad Khawaja | AI repository review, dynamic references, scoped MAGICore memory and optional P… |
| 2026-10-28 00:49:21 | [Nite.Diagnostics](https://www.nuget.org/packages/Nite.Diagnostics) | 0.8.2 | Tim McQueen | Write log messages as Markdown files: a source generator turns each into a fast… |
| 2026-10-28 01:04:13 | [YounMapper](https://www.nuget.org/packages/YounMapper) | 1.0.0 | YounMapper contributors | A small, fast, convention-based object-to-object mapping library for .NET. Mapp… |
| 2026-10-28 01:08:07 | [Webority.Retention](https://www.nuget.org/packages/Webority.Retention) | 0.1.0 | Webority Technologies | Deletes finished work rows from a product's SQL tables once they pass their ret… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
