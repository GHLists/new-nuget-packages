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

## Latest list — 2026-09-30 06:21 UTC

New packages created between 2026-09-30 05:20 UTC and 2026-09-30 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T06-21-05-731288Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 05:34:33 | [ScreenKeyboard.Core](https://www.nuget.org/packages/ScreenKeyboard.Core) | 1.0.0 | Wiesław Šoltés | Platform-agnostic engine for professional on-screen keyboards: FlorisBoard-comp… |
| 2026-09-30 05:34:35 | [ScreenKeyboard.Uno](https://www.nuget.org/packages/ScreenKeyboard.Uno) | 1.0.0 | Wiesław Šoltés | A professional, themable on-screen keyboard control for Uno Platform (WinUI): F… |
| 2026-09-30 06:06:51 | [Afrowave.Toolbox.WhenItFails](https://www.nuget.org/packages/Afrowave.Toolbox.WhenItFails) | 0.1.0 | Afrowave | Structured error catalogs, runtime resolution, recovery, profiles, mapping, and… |
| 2026-09-30 06:06:55 | [Twinbox.Nats](https://www.nuget.org/packages/Twinbox.Nats) | 1.0.0 | Twinbox contributors | NATS JetStream transport for Twinbox: deduplicated, acknowledged publishes and… |
| 2026-09-30 06:06:55 | [Twinbox.SqlServer](https://www.nuget.org/packages/Twinbox.SqlServer) | 1.0.0 | Twinbox contributors | SQL Server storage for Twinbox with plain ADO.NET or Dapper: save outbox messag… |
| 2026-09-30 06:06:56 | [Twinbox.Oracle](https://www.nuget.org/packages/Twinbox.Oracle) | 1.0.0 | Twinbox contributors | Oracle Database storage for Twinbox with plain ADO.NET or Dapper: save outbox m… |
| 2026-09-30 06:06:56 | [Twinbox](https://www.nuget.org/packages/Twinbox) | 1.0.0 | Twinbox contributors | Transactional outbox and inbox for .NET: reliable delivery to any message broke… |
| 2026-09-30 06:06:57 | [Twinbox.AzureServiceBus](https://www.nuget.org/packages/Twinbox.AzureServiceBus) | 1.0.0 | Twinbox contributors | Azure Service Bus transport for Twinbox: sends outbox messages to queues and to… |
| 2026-09-30 06:06:57 | [Twinbox.Http](https://www.nuget.org/packages/Twinbox.Http) | 1.0.0 | Twinbox contributors | HTTP transport for Twinbox: calls vendor APIs and delivers webhooks from the ou… |
| 2026-09-30 06:06:57 | [Twinbox.RabbitMQ](https://www.nuget.org/packages/Twinbox.RabbitMQ) | 1.0.0 | Twinbox contributors | RabbitMQ transport for Twinbox: publisher-confirmed sends and quorum-queue cons… |
| 2026-09-30 06:06:58 | [Twinbox.Aspire](https://www.nuget.org/packages/Twinbox.Aspire) | 1.0.0 | Twinbox contributors | .NET Aspire service defaults for Twinbox: OpenTelemetry tracing and metrics plu… |
| 2026-09-30 06:06:58 | [Twinbox.InMemory](https://www.nuget.org/packages/Twinbox.InMemory) | 1.0.0 | Twinbox contributors | In-memory store and transport for Twinbox, for tests and local development. |
| 2026-09-30 06:06:58 | [Twinbox.EventHubs](https://www.nuget.org/packages/Twinbox.EventHubs) | 1.0.0 | Twinbox contributors | Azure Event Hubs transport for Twinbox: keyed sends and partition processors th… |
| 2026-09-30 06:06:59 | [Twinbox.RedisStreams](https://www.nuget.org/packages/Twinbox.RedisStreams) | 1.0.0 | Twinbox contributors | Redis Streams transport for Twinbox: consumer groups that acknowledge only afte… |
| 2026-09-30 06:06:59 | [Twinbox.EntityFrameworkCore](https://www.nuget.org/packages/Twinbox.EntityFrameworkCore) | 1.0.0 | Twinbox contributors | EF Core storage for Twinbox: outbox messages are saved in the same SaveChanges… |
| 2026-09-30 06:06:59 | [Twinbox.GooglePubSub](https://www.nuget.org/packages/Twinbox.GooglePubSub) | 1.0.0 | Twinbox contributors | Google Cloud Pub/Sub transport for Twinbox: publishes to topics with optional o… |
| 2026-09-30 06:07:00 | [Twinbox.AzureFunctions](https://www.nuget.org/packages/Twinbox.AzureFunctions) | 1.0.0 | Twinbox contributors | Azure Functions (isolated worker) support for Twinbox: dispatch the outbox from… |
| 2026-09-30 06:07:00 | [Twinbox.PostgreSql](https://www.nuget.org/packages/Twinbox.PostgreSql) | 1.0.0 | Twinbox contributors | PostgreSQL storage for Twinbox with plain ADO.NET or Dapper: save outbox messag… |
| 2026-09-30 06:07:00 | [Twinbox.Abstractions](https://www.nuget.org/packages/Twinbox.Abstractions) | 1.0.0 | Twinbox contributors | Contracts for Twinbox, the transactional outbox and inbox for .NET. Zero depend… |
| 2026-09-30 06:07:01 | [Twinbox.Webhooks](https://www.nuget.org/packages/Twinbox.Webhooks) | 1.0.0 | Twinbox contributors | Signed webhook ingress for Twinbox: verify, store durably and acknowledge fast,… |
| 2026-09-30 06:07:01 | [Twinbox.Testing](https://www.nuget.org/packages/Twinbox.Testing) | 1.0.0 | Twinbox contributors | Test harness and provider conformance suite for Twinbox. Works with any test fr… |
| 2026-09-30 06:07:01 | [Twinbox.MongoDB](https://www.nuget.org/packages/Twinbox.MongoDB) | 1.0.0 | Twinbox contributors | MongoDB storage for Twinbox: save outbox messages in your own MongoDB transacti… |
| 2026-09-30 06:07:02 | [Twinbox.Kafka](https://www.nuget.org/packages/Twinbox.Kafka) | 1.0.0 | Twinbox contributors | Kafka transport for Twinbox: idempotent, keyed sends and consumer groups that c… |
| 2026-09-30 06:07:02 | [Twinbox.MySql](https://www.nuget.org/packages/Twinbox.MySql) | 1.0.0 | Twinbox contributors | MySQL storage for Twinbox with plain ADO.NET or Dapper: save outbox messages in… |
| 2026-09-30 06:07:02 | [Twinbox.Dashboard](https://www.nuget.org/packages/Twinbox.Dashboard) | 1.0.0 | Twinbox contributors | Operations dashboard for Twinbox: outbox statistics, message browsing, and repl… |
| 2026-09-30 06:07:03 | [Twinbox.Aspire.Hosting](https://www.nuget.org/packages/Twinbox.Aspire.Hosting) | 1.0.0 | Twinbox contributors | .NET Aspire AppHost integration for Twinbox: links a resource's Twinbox dashboa… |
| 2026-09-30 06:07:03 | [Twinbox.AmazonSqs](https://www.nuget.org/packages/Twinbox.AmazonSqs) | 1.0.0 | Twinbox contributors | Amazon SQS and SNS transport for Twinbox: sends to queues or fans out through t… |
| 2026-09-30 06:07:03 | [Twinbox.Pulsar](https://www.nuget.org/packages/Twinbox.Pulsar) | 1.0.0 | Twinbox contributors | Apache Pulsar transport for Twinbox: keyed sends and subscriptions that acknowl… |
| 2026-09-30 06:09:12 | [OptiCli](https://www.nuget.org/packages/OptiCli) | 0.3.0 | opticli contributors | Read and write local Optimizely CMS 12 sites from the command line. |
| 2026-09-30 06:13:39 | [Beans.Requestable](https://www.nuget.org/packages/Beans.Requestable) | 1.0.0 | Craig Duggan (craigduggan90) | Stuff I keep rewriting for lightweight CQRS. |
| 2026-09-30 06:14:03 | [Beans.Pageable](https://www.nuget.org/packages/Beans.Pageable) | 1.0.0 | Craig Duggan (craigduggan90) | Stuff I keep rewriting for date filtering. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
