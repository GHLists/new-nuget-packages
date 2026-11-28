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

## Latest list — 2026-11-28 06:21 UTC

New packages created between 2026-11-28 05:22 UTC and 2026-11-28 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-28T06-21-11-483245Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-28 05:22:06 | [SXM.NetFramework.Attributes](https://www.nuget.org/packages/SXM.NetFramework.Attributes) | 1.0.0 | SXM.NetFramework.Attributes | Marker attributes used by SXM.NetFramework source generators and framework conv… |
| 2026-11-28 05:22:08 | [SXM.NetFramework.Auth.WSO2](https://www.nuget.org/packages/SXM.NetFramework.Auth.WSO2) | 1.0.0 | SXM.NetFramework.Auth.WSO2 | WSO2 authentication integration for SXM backend framework consumers. |
| 2026-11-28 05:22:10 | [SXM.NetFramework.Booking](https://www.nuget.org/packages/SXM.NetFramework.Booking) | 1.0.0 | SXM.NetFramework.Booking | Core abstractions, models, and options for the SXM appointment booking framewor… |
| 2026-11-28 05:22:12 | [SXM.NetFramework.Booking.Application](https://www.nuget.org/packages/SXM.NetFramework.Booking.Application) | 1.0.0 | SXM.NetFramework.Booking.Appl… | Availability engine, holiday rules, and booking orchestration for the SXM appoi… |
| 2026-11-28 05:22:14 | [SXM.NetFramework.Booking.Driver](https://www.nuget.org/packages/SXM.NetFramework.Booking.Driver) | 1.0.0 | SXM.NetFramework.Booking.Driv… | Single-package appointment booking driver for SXM services: one-call registrati… |
| 2026-11-28 05:22:17 | [SXM.NetFramework.Booking.Infrastructure](https://www.nuget.org/packages/SXM.NetFramework.Booking.Infrastructure) | 1.0.0 | SXM.NetFramework.Booking.Infr… | Vendor adapters (Microsoft Bookings via Graph), token acquisition, persistence,… |
| 2026-11-28 05:22:19 | [SXM.NetFramework.CacheClient](https://www.nuget.org/packages/SXM.NetFramework.CacheClient) | 1.0.0 | SXM.NetFramework.CacheClient | Redis-backed and no-op cache abstractions for SXM backend framework consumers. |
| 2026-11-28 05:22:21 | [SXM.NetFramework.CanonicalSync.Abstractions](https://www.nuget.org/packages/SXM.NetFramework.CanonicalSync.Abstractions) | 1.0.0 | SXM.NetFramework.CanonicalSyn… | Canonical Sync abstractions: envelope, mapper/handler/pipeline interfaces, inbo… |
| 2026-11-28 05:22:22 | [SXM.NetFramework.CanonicalSync.Contracts](https://www.nuget.org/packages/SXM.NetFramework.CanonicalSync.Contracts) | 1.0.0 | SXM.NetFramework.CanonicalSyn… | Canonical Sync wire contracts: registry integration event, source lineage and c… |
| 2026-11-28 05:22:25 | [SXM.NetFramework.CanonicalSync.Hosting](https://www.nuget.org/packages/SXM.NetFramework.CanonicalSync.Hosting) | 1.0.0 | SXM.NetFramework.CanonicalSyn… | Canonical Sync hosting: MassTransit Azure Service Bus consumer, subscription en… |
| 2026-11-28 05:22:27 | [SXM.NetFramework.CanonicalSync.Infrastructure](https://www.nuget.org/packages/SXM.NetFramework.CanonicalSync.Infrastructure) | 1.0.0 | SXM.NetFramework.CanonicalSyn… | Canonical Sync transport-agnostic core: pipeline, resolvers, validation, retry… |
| 2026-11-28 05:22:29 | [SXM.NetFramework.CanonicalSync.Redis](https://www.nuget.org/packages/SXM.NetFramework.CanonicalSync.Redis) | 1.0.0 | SXM.NetFramework.CanonicalSyn… | Canonical Sync Redis storage: distributed-cache inbox and source-link stores wi… |
| 2026-11-28 05:22:31 | [SXM.NetFramework.CanonicalSync.SqlServer](https://www.nuget.org/packages/SXM.NetFramework.CanonicalSync.SqlServer) | 1.0.0 | SXM.NetFramework.CanonicalSyn… | Canonical Sync SQL Server storage: durable inbox, source-link writer, transacti… |
| 2026-11-28 05:22:33 | [SXM.NetFramework.Communication](https://www.nuget.org/packages/SXM.NetFramework.Communication) | 1.0.0 | SXM.NetFramework.Communication | Platform package for unified Email, SMS, and File Storage integration across SX… |
| 2026-11-28 05:22:35 | [SXM.NetFramework.Communication.Application](https://www.nuget.org/packages/SXM.NetFramework.Communication.Application) | 1.0.0 | SXM.NetFramework.Communicatio… | CQRS commands and queries for the SXM communication framework — email queue, SM… |
| 2026-11-28 05:22:37 | [SXM.NetFramework.Communication.Driver](https://www.nuget.org/packages/SXM.NetFramework.Communication.Driver) | 1.0.0 | SXM.NetFramework.Communicatio… | Single-package communication driver that unifies Email, SMS, and File Storage a… |
| 2026-11-28 05:22:39 | [SXM.NetFramework.Email](https://www.nuget.org/packages/SXM.NetFramework.Email) | 1.0.0 | SXM.NetFramework.Email | Reusable email contracts, templates, and delivery abstractions for SXM modular… |
| 2026-11-28 05:22:41 | [SXM.NetFramework.Email.Azure](https://www.nuget.org/packages/SXM.NetFramework.Email.Azure) | 1.0.0 | SXM.NetFramework.Email.Azure | Azure Communication Services email provider for the reusable SXM email module. |
| 2026-11-28 05:22:43 | [SXM.NetFramework.Email.Driver](https://www.nuget.org/packages/SXM.NetFramework.Email.Driver) | 1.0.0 | SXM.NetFramework.Email.Driver | Single-package email driver for SXM services with one-call API and background d… |
| 2026-11-28 05:22:46 | [SXM.NetFramework.Entity](https://www.nuget.org/packages/SXM.NetFramework.Entity) | 26.11.3 | SXM.NetFramework.Entity | Shared entity models, GraphQL partial update helpers, and legacy framework enti… |
| 2026-11-28 05:22:48 | [SXM.NetFramework.FileStorage](https://www.nuget.org/packages/SXM.NetFramework.FileStorage) | 1.0.0 | SXM.NetFramework.FileStorage | Reusable file storage abstractions and provider implementations for Azure Blob,… |
| 2026-11-28 05:22:49 | [SXM.NetFramework.GraphQL](https://www.nuget.org/packages/SXM.NetFramework.GraphQL) | 1.0.0 | SXM.NetFramework.GraphQL | GraphQL host extensions for SXM backend services based on Hot Chocolate. |
| 2026-11-28 05:22:52 | [SXM.NetFramework.GraphQLGenerator](https://www.nuget.org/packages/SXM.NetFramework.GraphQLGenerator) | 1.0.0 | SXM.NetFramework.GraphQLGener… | Source generator that emits Hot Chocolate queries and repository-based CRUD mut… |
| 2026-11-28 05:22:53 | [SXM.NetFramework.Identity.BackOffice](https://www.nuget.org/packages/SXM.NetFramework.Identity.BackOffice) | 1.0.0 | SXM.NetFramework.Identity.Bac… | Reusable backoffice identity domain models, contracts, and configuration for SX… |
| 2026-11-28 05:22:56 | [SXM.NetFramework.Identity.BackOffice.Application](https://www.nuget.org/packages/SXM.NetFramework.Identity.BackOffice.Application) | 1.0.0 | SXM.NetFramework.Identity.Bac… | CQRS handlers and application services for SXM.NetFramework.Identity.BackOffice. |
| 2026-11-28 05:22:58 | [SXM.NetFramework.Identity.BackOffice.Infrastructure](https://www.nuget.org/packages/SXM.NetFramework.Identity.BackOffice.Infrastructure) | 1.0.0 | SXM.NetFramework.Identity.Bac… | linq2db and Dapper persistence, JWT authentication, and default infrastructure… |
| 2026-11-28 05:23:00 | [SXM.NetFramework.Identity.BackOffice.OpenId](https://www.nuget.org/packages/SXM.NetFramework.Identity.BackOffice.OpenId) | 1.0.0 | SXM.NetFramework.Identity.Bac… | OpenID Connect and OAuth2 resource-server integration for SXM backoffice identi… |
| 2026-11-28 05:23:02 | [SXM.NetFramework.Identity.WSO2](https://www.nuget.org/packages/SXM.NetFramework.Identity.WSO2) | 1.0.0 | SXM.NetFramework.Identity.WSO2 | Citizen-login WSO2 orchestration module that composes the SXM framework, TwoFac… |
| 2026-11-28 05:23:04 | [SXM.NetFramework.Infrastructure](https://www.nuget.org/packages/SXM.NetFramework.Infrastructure) | 1.0.0 | SXM.NetFramework.Infrastructu… | Database, outbox, and persistence building blocks for SXM backend framework con… |
| 2026-11-28 05:23:06 | [SXM.NetFramework.Localization](https://www.nuget.org/packages/SXM.NetFramework.Localization) | 1.0.0 | SXM.NetFramework.Localization | Localization services, loaders, sources, and embedded framework translations fo… |
| 2026-11-28 05:23:08 | [SXM.NetFramework.Logging](https://www.nuget.org/packages/SXM.NetFramework.Logging) | 1.0.0 | SXM.NetFramework.Logging | Reusable production-grade Serilog configuration for SXM backend services. |
| 2026-11-28 05:23:10 | [SXM.NetFramework.MessageBroker](https://www.nuget.org/packages/SXM.NetFramework.MessageBroker) | 1.0.0 | SXM.NetFramework.MessageBroker | Message broker abstractions and provider support for RabbitMQ, Azure Service Bu… |
| 2026-11-28 05:23:13 | [SXM.NetFramework.Notification.Driver](https://www.nuget.org/packages/SXM.NetFramework.Notification.Driver) | 1.0.0 | SXM.NetFramework.Notification… | Single-package notification driver for SXM services: SignalR web push and Fireb… |
| 2026-11-28 05:23:14 | [SXM.NetFramework.Observability](https://www.nuget.org/packages/SXM.NetFramework.Observability) | 1.0.0 | SXM.NetFramework.Observability | OpenTelemetry tracing and metrics bootstrap for SXM backend services. |
| 2026-11-28 05:23:16 | [SXM.NetFramework.Push](https://www.nuget.org/packages/SXM.NetFramework.Push) | 1.0.0 | SXM.NetFramework.Push | Reusable mobile push notification abstractions and models for SXM backend servi… |
| 2026-11-28 05:23:18 | [SXM.NetFramework.QrCode](https://www.nuget.org/packages/SXM.NetFramework.QrCode) | 1.0.0 | SXM.NetFramework.QrCode | Core abstractions, models, and options for the SXM QR code and barcode generati… |
| 2026-11-28 05:23:20 | [SXM.NetFramework.QrCode.Application](https://www.nuget.org/packages/SXM.NetFramework.QrCode.Application) | 1.0.0 | SXM.NetFramework.QrCode.Appli… | Generation orchestrator and request validation for the SXM QR code framework. |
| 2026-11-28 05:23:23 | [SXM.NetFramework.QrCode.Driver](https://www.nuget.org/packages/SXM.NetFramework.QrCode.Driver) | 1.0.0 | SXM.NetFramework.QrCode.Driver | Single-package QR code and barcode driver for SXM services: one-call registrati… |
| 2026-11-28 05:23:25 | [SXM.NetFramework.QrCode.Infrastructure](https://www.nuget.org/packages/SXM.NetFramework.QrCode.Infrastructure) | 1.0.0 | SXM.NetFramework.QrCode.Infra… | Renderers (QRCoder, ZXing.Net), logo compositors, and the FileUpload-backed sto… |
| 2026-11-28 05:23:27 | [SXM.NetFramework.Realtime](https://www.nuget.org/packages/SXM.NetFramework.Realtime) | 1.0.0 | SXM.NetFramework.Realtime | SignalR-based real-time publishing support for SXM backend services. |
| 2026-11-28 05:23:29 | [SXM.NetFramework.Repositories](https://www.nuget.org/packages/SXM.NetFramework.Repositories) | 1.0.0 | SXM.NetFramework.Repositories | Generic repository and repository factory implementation for SXM services built… |
| 2026-11-28 05:23:31 | [SXM.NetFramework.Scheduling](https://www.nuget.org/packages/SXM.NetFramework.Scheduling) | 1.0.0 | SXM.NetFramework.Scheduling | Scheduling core: database-driven schedule reconciler, generic job dispatcher, h… |
| 2026-11-28 05:23:33 | [SXM.NetFramework.Scheduling.Abstractions](https://www.nuget.org/packages/SXM.NetFramework.Scheduling.Abstractions) | 1.0.0 | SXM.NetFramework.Scheduling.A… | Scheduling contracts: handler interface, execution context, schedule descriptor… |
| 2026-11-28 05:23:35 | [SXM.NetFramework.Scheduling.Infrastructure](https://www.nuget.org/packages/SXM.NetFramework.Scheduling.Infrastructure) | 1.0.0 | SXM.NetFramework.Scheduling.I… | Hangfire-backed scheduling infrastructure: server bootstrap, recurring-job adap… |
| 2026-11-28 05:23:37 | [SXM.NetFramework.Security](https://www.nuget.org/packages/SXM.NetFramework.Security) | 1.0.0 | SXM.NetFramework.Security | Inbound access control middleware for domain and IP allow/deny policies. |
| 2026-11-28 05:23:39 | [SXM.NetFramework.ServiceClient](https://www.nuget.org/packages/SXM.NetFramework.ServiceClient) | 1.0.0 | SXM.NetFramework.ServiceClient | Package Description |
| 2026-11-28 05:23:41 | [SXM.NetFramework.Sms.Driver](https://www.nuget.org/packages/SXM.NetFramework.Sms.Driver) | 1.0.0 | SXM.NetFramework.Sms.Driver | Single-package SMS driver for SXM services built on the TwoFactor SMS delivery… |
| 2026-11-28 05:23:43 | [SXM.NetFramework.TwoFactor](https://www.nuget.org/packages/SXM.NetFramework.TwoFactor) | 1.0.0 | SXM.NetFramework.TwoFactor | Reusable two-factor authentication domain contracts and challenge lifecycle for… |
| 2026-11-28 05:23:45 | [SXM.NetFramework.TwoFactor.Application](https://www.nuget.org/packages/SXM.NetFramework.TwoFactor.Application) | 1.0.0 | SXM.NetFramework.TwoFactor.Ap… | CQRS command handlers and validation pipeline for reusable two-factor flows. |
| 2026-11-28 05:23:47 | [SXM.NetFramework.TwoFactor.Azure](https://www.nuget.org/packages/SXM.NetFramework.TwoFactor.Azure) | 1.0.0 | SXM.NetFramework.TwoFactor.Az… | Azure Communication Services delivery providers for SXM.NetFramework.TwoFactor. |
| 2026-11-28 05:23:49 | [SXM.NetFramework.TwoFactor.Infrastructure](https://www.nuget.org/packages/SXM.NetFramework.TwoFactor.Infrastructure) | 1.0.0 | SXM.NetFramework.TwoFactor.In… | linq2db persistence and default infrastructure services for SXM.NetFramework.Tw… |
| 2026-11-28 05:23:51 | [SXM.NetFramework.Web](https://www.nuget.org/packages/SXM.NetFramework.Web) | 1.0.0 | SXM.NetFramework.Web | Web host bootstrap, middleware, rate limiting, problem-details handling, and Op… |
| 2026-11-28 05:47:28 | [FineVoice](https://www.nuget.org/packages/FineVoice) | 0.1.3 | FineVoice | C# SDK for the FineVoice API: text to speech, voice conversion, music generatio… |
| 2026-11-28 05:50:26 | [Pumpkin.DotNet.Runtime](https://www.nuget.org/packages/Pumpkin.DotNet.Runtime) | 0.2.0-alpha | Glesity | Pumpkin.NET runtime. |
| 2026-11-28 05:50:26 | [Pumpkin.DotNet.Sdk](https://www.nuget.org/packages/Pumpkin.DotNet.Sdk) | 0.2.0-alpha | Pumpkin.DotNet.Sdk | Package Description |
| 2026-11-28 06:02:52 | [BoltMySql](https://www.nuget.org/packages/BoltMySql) | 0.1.1 | Logan (Ezgaminglogan) | Fast, zero-ceremony, anti-SQL-injection MySQL & MariaDB micro-ORM for .NET Fram… |
| 2026-11-28 06:14:29 | [Cloudsimpl.Identity.Api.BasicAuth.Utils](https://www.nuget.org/packages/Cloudsimpl.Identity.Api.BasicAuth.Utils) | 7.0.0 | Cloudsimpl.Identity.Api.Basic… | Package Description |
| 2026-11-28 06:15:46 | [StalSend](https://www.nuget.org/packages/StalSend) | 0.1.0 | StalSend | Official .NET client for the StalSend email API |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
