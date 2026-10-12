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

## Latest list — 2026-10-12 12:19 UTC

New packages created between 2026-10-12 11:20 UTC and 2026-10-12 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T12-19-56-586913Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 11:34:09 | [Payriff](https://www.nuget.org/packages/Payriff) | 0.1.2 | Payriff | .NET client for the Payriff merchant API: orders, direct card payments, saved c… |
| 2026-10-12 11:40:19 | [Synvro.Modulus.Authorization.Management](https://www.nuget.org/packages/Synvro.Modulus.Authorization.Management) | 1.4.0 | synvro | Administration API extensions for Modulus authorization built on the EF Core pe… |
| 2026-10-12 11:40:34 | [Synvro.Modulus.BackgroundJobs.Quartz](https://www.nuget.org/packages/Synvro.Modulus.BackgroundJobs.Quartz) | 1.4.0 | synvro | Quartz.NET adapter for durable background job scheduling with clustering suppor… |
| 2026-10-12 11:40:53 | [Synvro.Modulus.Bff](https://www.nuget.org/packages/Synvro.Modulus.Bff) | 1.4.0 | synvro | Backends for Frontends for Modulus: one edge per client type (web SPA, mobile a… |
| 2026-10-12 11:41:17 | [Synvro.Modulus.Caching.Redis](https://www.nuget.org/packages/Synvro.Modulus.Caching.Redis) | 1.4.0 | synvro | Redis for Modulus caching: FusionCache L2 + backplane, the legacy Redis cache s… |
| 2026-10-12 11:41:31 | [Synvro.Modulus.Core](https://www.nuget.org/packages/Synvro.Modulus.Core) | 1.4.0 | synvro | Core abstractions and utilities for the Modulus framework: module system, domai… |
| 2026-10-12 11:41:48 | [Synvro.Modulus.Data.Abstractions](https://www.nuget.org/packages/Synvro.Modulus.Data.Abstractions) | 1.4.0 | synvro | Data access abstractions for Modulus: generic repository and unit-of-work patte… |
| 2026-10-12 11:42:04 | [Synvro.Modulus.Data.MongoDB](https://www.nuget.org/packages/Synvro.Modulus.Data.MongoDB) | 1.4.0 | synvro | MongoDB data access provider for Modulus with tenant-aware collection filtering. |
| 2026-10-12 11:42:21 | [Synvro.Modulus.Data.MySQL](https://www.nuget.org/packages/Synvro.Modulus.Data.MySQL) | 1.4.0 | synvro | MySQL database provider for Modulus Entity Framework Core modules. |
| 2026-10-12 11:42:42 | [Synvro.Modulus.Data.PostgreSQL](https://www.nuget.org/packages/Synvro.Modulus.Data.PostgreSQL) | 1.4.0 | synvro | PostgreSQL database provider for Modulus Entity Framework Core modules. |
| 2026-10-12 11:42:56 | [Synvro.Modulus.Data.SQLite](https://www.nuget.org/packages/Synvro.Modulus.Data.SQLite) | 1.4.0 | synvro | SQLite database provider for Modulus Entity Framework Core modules. |
| 2026-10-12 11:55:29 | [Synvro.Modulus.Data.SqlServer](https://www.nuget.org/packages/Synvro.Modulus.Data.SqlServer) | 1.4.0 | synvro | SQL Server database provider for Modulus Entity Framework Core modules. |
| 2026-10-12 11:56:23 | [Synvro.Modulus.EntityFrameworkCore](https://www.nuget.org/packages/Synvro.Modulus.EntityFrameworkCore) | 1.4.0 | synvro | Entity Framework Core integration for Modulus: module DbContext base, generic r… |
| 2026-10-12 11:56:58 | [Synvro.Modulus.EventBus.Kafka](https://www.nuget.org/packages/Synvro.Modulus.EventBus.Kafka) | 1.4.0 | synvro | Kafka transport for Modulus integration events with bounded redelivery, poison-… |
| 2026-10-12 11:57:15 | [Synvro.Modulus.EventBus.RabbitMQ](https://www.nuget.org/packages/Synvro.Modulus.EventBus.RabbitMQ) | 1.4.0 | synvro | RabbitMQ transport for Modulus integration events with ambient tenant/correlati… |
| 2026-10-12 11:57:35 | [Synvro.Modulus.Events](https://www.nuget.org/packages/Synvro.Modulus.Events) | 1.4.0 | synvro | In-process eventing for Modulus: domain event dispatcher, integration event reg… |
| 2026-10-12 11:57:50 | [Synvro.Modulus.GraphQL](https://www.nuget.org/packages/Synvro.Modulus.GraphQL) | 1.4.0 | synvro | GraphQL for Modulus (GraphQL.NET, MIT): one schema that every module contribute… |
| 2026-10-12 11:58:04 | [Synvro.Modulus.Grpc](https://www.nuget.org/packages/Synvro.Modulus.Grpc) | 1.4.0 | synvro | gRPC for Modulus: module gRPC services discovered from Presentation assemblies,… |
| 2026-10-12 11:58:51 | [Synvro.Modulus.Identity](https://www.nuget.org/packages/Synvro.Modulus.Identity) | 1.4.0 | synvro | OpenIddict-based identity and authorization server for Modulus with external Id… |
| 2026-10-12 11:59:27 | [Synvro.Modulus.Inbox](https://www.nuget.org/packages/Synvro.Modulus.Inbox) | 1.4.0 | synvro | Idempotent integration-event consumption for Modulus over EF Core: atomic claim… |
| 2026-10-12 11:59:39 | [Kralizek.Lambda.Template.TenantRouting](https://www.nuget.org/packages/Kralizek.Lambda.Template.TenantRouting) | 6.1.0 | Renato Golia | Tenant-aware AWS Lambda invocation routing for Kralizek.Lambda.Template applica… |
| 2026-10-12 11:59:59 | [Synvro.Modulus.Inbox.MongoDB](https://www.nuget.org/packages/Synvro.Modulus.Inbox.MongoDB) | 1.4.0 | synvro | MongoDB inbox store for Modulus idempotent integration-event consumption, shari… |
| 2026-10-12 12:00:28 | [Synvro.Modulus.Mediator](https://www.nuget.org/packages/Synvro.Modulus.Mediator) | 1.4.0 | synvro | In-process mediator for Modulus: commands, queries, and pipeline behaviours (va… |
| 2026-10-12 12:01:03 | [Synvro.Modulus.MultiTenancy.EntityFrameworkCore](https://www.nuget.org/packages/Synvro.Modulus.MultiTenancy.EntityFrameworkCore) | 1.4.0 | synvro | EF Core tenant store for Modulus multi-tenancy: an ITenantStore implementation… |
| 2026-10-12 12:01:22 | [Synvro.Modulus.Observability](https://www.nuget.org/packages/Synvro.Modulus.Observability) | 1.4.0 | synvro | Observability for Modulus: OpenTelemetry wiring, activity sources, tracing beha… |
| 2026-10-12 12:01:38 | [Synvro.Modulus.Outbox](https://www.nuget.org/packages/Synvro.Modulus.Outbox) | 1.4.0 | synvro | Transactional outbox for Modulus over EF Core: atomic claiming, retry back-off,… |
| 2026-10-12 12:01:56 | [Synvro.Modulus.Outbox.Abstractions](https://www.nuget.org/packages/Synvro.Modulus.Outbox.Abstractions) | 1.4.0 | synvro | Shared contracts for the Modulus transactional outbox (message shape, row facto… |
| 2026-10-12 12:02:44 | [Synvro.Modulus.Outbox.Management](https://www.nuget.org/packages/Synvro.Modulus.Outbox.Management) | 1.4.0 | synvro | Operational management API for the transactional outbox: list, inspect, and rep… |
| 2026-10-12 12:03:05 | [Synvro.Modulus.Outbox.MongoDB](https://www.nuget.org/packages/Synvro.Modulus.Outbox.MongoDB) | 1.4.0 | synvro | MongoDB adapter for the Modulus transactional outbox: writer, processor, dispat… |
| 2026-10-12 12:03:24 | [Synvro.Modulus.Platform](https://www.nuget.org/packages/Synvro.Modulus.Platform) | 1.4.0 | synvro | Platform services for Modulus: multi-tenancy, authorization, background jobs, i… |
| 2026-10-12 12:03:40 | [Synvro.Modulus.Realtime](https://www.nuget.org/packages/Synvro.Modulus.Realtime) | 1.4.0 | synvro | Realtime push for Modulus: integration events and app messages delivered to cli… |
| 2026-10-12 12:03:58 | [Synvro.Modulus.Sagas](https://www.nuget.org/packages/Synvro.Modulus.Sagas) | 1.4.0 | synvro | Rebus-based saga/process-manager orchestration for Modulus: Polly resilience, a… |
| 2026-10-12 12:04:17 | [Synvro.Modulus.Realtime.Redis](https://www.nuget.org/packages/Synvro.Modulus.Realtime.Redis) | 1.4.0 | synvro | Redis backplane for Modulus.Realtime: every node receives every realtime messag… |
| 2026-10-12 12:04:36 | [Synvro.Modulus.SignalR.Backplane](https://www.nuget.org/packages/Synvro.Modulus.SignalR.Backplane) | 1.4.0 | synvro | Scale-out backplane options for Modulus SignalR hubs (Redis or Azure SignalR Se… |
| 2026-10-12 12:04:50 | [Synvro.Modulus.Storage.AzureBlobs](https://www.nuget.org/packages/Synvro.Modulus.Storage.AzureBlobs) | 1.4.0 | synvro | Azure Blob Storage file storage provider for Modulus. |
| 2026-10-12 12:05:02 | [Synvro.Modulus.Storage.S3](https://www.nuget.org/packages/Synvro.Modulus.Storage.S3) | 1.4.0 | synvro | Amazon S3 file storage provider for Modulus. |
| 2026-10-12 12:05:16 | [Synvro.Modulus.Testing](https://www.nuget.org/packages/Synvro.Modulus.Testing) | 1.4.0 | synvro | Integration-test harness for Modulus applications: a WebApplicationFactory that… |
| 2026-10-12 12:05:28 | [Synvro.Modulus.Testing.Architecture](https://www.nuget.org/packages/Synvro.Modulus.Testing.Architecture) | 1.4.0 | synvro | Architecture rules for Modulus modular monoliths: enforce module boundaries, la… |
| 2026-10-12 12:05:45 | [Synvro.Modulus.Webhooks](https://www.nuget.org/packages/Synvro.Modulus.Webhooks) | 1.4.0 | synvro | Outgoing webhooks for Modulus: integration events fanned out to tenant-scoped s… |
| 2026-10-12 12:05:48 | [Stellaegis.Caching](https://www.nuget.org/packages/Stellaegis.Caching) | 1.0.0 | FRi | A size-bounded in-memory cache with a long backstop TTL, segment invalidation,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
