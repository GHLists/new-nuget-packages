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

## Latest list — 2026-10-07 17:22 UTC

New packages created between 2026-10-07 16:20 UTC and 2026-10-07 17:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T17-22-02-999784Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 16:44:51 | [Microsoft.Testing.Extensions.PackagedApp.MSBuild](https://www.nuget.org/packages/Microsoft.Testing.Extensions.PackagedApp.MSBuild) | 2.5.1 | Microsoft | Run packaged Windows test applications through a full-trust Microsoft.Testing.P… |
| 2026-10-07 16:45:03 | [MSTest.Windows.UIAutomation](https://www.nuget.org/packages/MSTest.Windows.UIAutomation) | 4.5.1 | Microsoft | MSTest lifecycle integration for Windows desktop UI Automation tests. MSTest is… |
| 2026-10-07 16:54:10 | [Soenneker.Librarian.AzureBlob](https://www.nuget.org/packages/Soenneker.Librarian.AzureBlob) | 4.0.71 | Jake Soenneker | Librarian document storage backed by Azure Blob Storage snapshots. |
| 2026-10-07 17:03:32 | [NymBroker.Idempotency.Sqlite](https://www.nuget.org/packages/NymBroker.Idempotency.Sqlite) | 0.9.1 | nymankla@gmail.com | Durable SQLite idempotency store (idempotent receiver) for NymBroker. Single ho… |
| 2026-10-07 17:03:33 | [NymBroker.Idempotency.Postgres](https://www.nuget.org/packages/NymBroker.Idempotency.Postgres) | 0.9.1 | nymankla@gmail.com | Durable PostgreSQL idempotency store (idempotent receiver) for NymBroker. |
| 2026-10-07 17:03:34 | [NymBroker.Endpoint.AzureServiceBus](https://www.nuget.org/packages/NymBroker.Endpoint.AzureServiceBus) | 0.9.1 | nymankla@gmail.com | Azure Service Bus endpoint add-on for NymBroker, with native dead-lettering. |
| 2026-10-07 17:03:34 | [NymBroker.Endpoint.SqlServer](https://www.nuget.org/packages/NymBroker.Endpoint.SqlServer) | 0.9.1 | nymankla@gmail.com | SQL Server endpoint add-on for NymBroker. |
| 2026-10-07 17:03:35 | [NymBroker.Endpoint.Postgres](https://www.nuget.org/packages/NymBroker.Endpoint.Postgres) | 0.9.1 | nymankla@gmail.com | PostgreSQL endpoint add-on for NymBroker. |
| 2026-10-07 17:03:36 | [NymBroker.Idempotency.SqlServer](https://www.nuget.org/packages/NymBroker.Idempotency.SqlServer) | 0.9.1 | nymankla@gmail.com | Durable SQL Server idempotency store (idempotent receiver) for NymBroker. |
| 2026-10-07 17:03:37 | [NymBroker](https://www.nuget.org/packages/NymBroker) | 0.9.1 | nymankla@gmail.com | A .NET 10 enterprise message processing framework. |
| 2026-10-07 17:03:37 | [NymBroker.Endpoint.Sqlite](https://www.nuget.org/packages/NymBroker.Endpoint.Sqlite) | 0.9.1 | nymankla@gmail.com | SQLite endpoint add-on for NymBroker. |
| 2026-10-07 17:03:38 | [NymBroker.Endpoint.RabbitMq](https://www.nuget.org/packages/NymBroker.Endpoint.RabbitMq) | 0.9.1 | nymankla@gmail.com | RabbitMQ endpoint add-on for NymBroker. |
| 2026-10-07 17:13:59 | [Brindletap](https://www.nuget.org/packages/Brindletap) | 2.1.0 | Brindletap | Roslyn CompletionProvider для C# и XAML-сниппетов из демо-экзамена. Совместим с… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
