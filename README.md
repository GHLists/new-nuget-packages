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

## Latest list — 2026-11-01 20:20 UTC

New packages created between 2026-11-01 19:21 UTC and 2026-11-01 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T20-20-17-545117Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 19:40:35 | [CoreSystem.OpenApi](https://www.nuget.org/packages/CoreSystem.OpenApi) | 1.0.0 | Federin Pastor Gutierrez Ortiz | Reusable OpenAPI and Swagger infrastructure for ASP.NET Core APIs. |
| 2026-11-01 19:42:49 | [Korzen.BotProtection](https://www.nuget.org/packages/Korzen.BotProtection) | 1.0.0 | Korzen | Korzen Bot Protection for ASP.NET Core: asks Bot Protection about a request bef… |
| 2026-11-01 19:43:34 | [Naravel.Broadcasting](https://www.nuget.org/packages/Naravel.Broadcasting) | 0.1.0 | Naravel contributors | Typed real-time broadcasting over SignalR for Naravel: IBroadcastable events, c… |
| 2026-11-01 19:43:35 | [Naravel.Cache](https://www.nuget.org/packages/Naravel.Cache) | 0.1.0 | Naravel contributors | Named cache stores, tagging, scoping and locks for Naravel, built on Naravel.Fo… |
| 2026-11-01 19:43:36 | [Naravel.Cache.Memcached](https://www.nuget.org/packages/Naravel.Cache.Memcached) | 0.1.0 | Naravel contributors | Memcached cache and lock providers for Naravel.Cache. |
| 2026-11-01 19:43:36 | [Naravel.Cache.Redis](https://www.nuget.org/packages/Naravel.Cache.Redis) | 0.1.0 | Naravel contributors | Redis cache and distributed-lock providers for Naravel.Cache. |
| 2026-11-01 19:43:37 | [Naravel.Database](https://www.nuget.org/packages/Naravel.Database) | 0.1.0 | Naravel contributors | Laravel-style query builder for Naravel on ADO.NET and Dapper: named connection… |
| 2026-11-01 19:43:38 | [Naravel.Database.EntityFrameworkCore](https://www.nuget.org/packages/Naravel.Database.EntityFrameworkCore) | 0.1.0 | Naravel contributors | EF Core interop for Naravel.Database: a DbContext and the query builder share o… |
| 2026-11-01 19:43:38 | [Naravel.Database.MySql](https://www.nuget.org/packages/Naravel.Database.MySql) | 0.1.0 | Naravel contributors | MySQL driver for Naravel.Database, built on MySqlConnector. |
| 2026-11-01 19:43:39 | [Naravel.Database.Postgres](https://www.nuget.org/packages/Naravel.Database.Postgres) | 0.1.0 | Naravel contributors | PostgreSQL driver for Naravel.Database, built on Npgsql. |
| 2026-11-01 19:43:40 | [Naravel.Database.SqlServer](https://www.nuget.org/packages/Naravel.Database.SqlServer) | 0.1.0 | Naravel contributors | SQL Server driver for Naravel.Database, built on Microsoft.Data.SqlClient. |
| 2026-11-01 19:43:41 | [Naravel.Database.Sqlite](https://www.nuget.org/packages/Naravel.Database.Sqlite) | 0.1.0 | Naravel contributors | SQLite driver for Naravel.Database, built on Microsoft.Data.Sqlite. |
| 2026-11-01 19:43:41 | [Naravel.Encryption](https://www.nuget.org/packages/Naravel.Encryption) | 0.1.0 | Naravel contributors | A thin Encrypt/Decrypt facade over ASP.NET Core Data Protection. No custom cryp… |
| 2026-11-01 19:43:42 | [Naravel.Events](https://www.nuget.org/packages/Naravel.Events) | 0.1.0 | Naravel contributors | Typed event dispatcher with listener ordering, stop propagation, and optional q… |
| 2026-11-01 19:43:43 | [Naravel.Events.Queue](https://www.nuget.org/packages/Naravel.Events.Queue) | 0.1.0 | Naravel contributors | Optional Naravel.Events adapter for running selected event listeners through Na… |
| 2026-11-01 19:43:43 | [Naravel.Filesystem](https://www.nuget.org/packages/Naravel.Filesystem) | 0.1.0 | Naravel contributors | Shared Manager -> Driver -> Factory Filesystem for Naravel modules (Laravel Ill… |
| 2026-11-01 19:43:44 | [Naravel.Foundation](https://www.nuget.org/packages/Naravel.Foundation) | 0.1.0 | Naravel contributors | Package Description |
| 2026-11-01 19:43:44 | [Naravel.Mail](https://www.nuget.org/packages/Naravel.Mail) | 0.1.0 | Naravel contributors | Typed mail contract for Naravel: Mailable classes, named transports (log, array… |
| 2026-11-01 19:43:45 | [Naravel.Mail.Queue](https://www.nuget.org/packages/Naravel.Mail.Queue) | 0.1.0 | Naravel contributors | Optional Naravel.Mail adapter that delivers mail through Naravel.Queue: QueueAs… |
| 2026-11-01 19:43:46 | [Naravel.Mail.Smtp](https://www.nuget.org/packages/Naravel.Mail.Smtp) | 0.1.0 | Naravel contributors | Optional SMTP transport for Naravel.Mail, built on MailKit. |
| 2026-11-01 19:43:46 | [Naravel.Notifications](https://www.nuget.org/packages/Naravel.Notifications) | 0.1.0 | Naravel contributors | Typed notification fan-out over explicitly named channels, with a fake for test… |
| 2026-11-01 19:43:47 | [Naravel.Notifications.Mail](https://www.nuget.org/packages/Naravel.Notifications.Mail) | 0.1.0 | Naravel contributors | Optional Naravel.Notifications adapter: a "mail" channel that delivers a notifi… |
| 2026-11-01 19:43:48 | [Naravel.Notifications.Queue](https://www.nuget.org/packages/Naravel.Notifications.Queue) | 0.1.0 | Naravel contributors | Optional Naravel.Notifications adapter that delivers notifications through Nara… |
| 2026-11-01 19:43:48 | [Naravel.Pagination](https://www.nuget.org/packages/Naravel.Pagination) | 0.1.0 | Naravel contributors | Laravel-style pagination results for .NET: length-aware, simple and cursor page… |
| 2026-11-01 19:43:49 | [Naravel.Pagination.EntityFrameworkCore](https://www.nuget.org/packages/Naravel.Pagination.EntityFrameworkCore) | 0.1.0 | Naravel contributors | PaginateAsync, SimplePaginateAsync and CursorPaginateAsync for EF Core queries,… |
| 2026-11-01 19:43:50 | [Naravel.Queue](https://www.nuget.org/packages/Naravel.Queue) | 0.1.0 | Naravel contributors | A Laravel-inspired, driver-based background job queue for .NET. Dispatch, retry… |
| 2026-11-01 19:43:50 | [Naravel.Queue.Coordination](https://www.nuget.org/packages/Naravel.Queue.Coordination) | 0.1.0 | Naravel contributors | Optional Naravel.Queue job middleware that coordinates workers through Naravel.… |
| 2026-11-01 19:43:51 | [Naravel.Queue.Database](https://www.nuget.org/packages/Naravel.Queue.Database) | 0.1.0 | Naravel contributors | EF Core-backed queue driver for Naravel.Queue - works with any EF Core provider… |
| 2026-11-01 19:43:52 | [Naravel.Queue.Encryption](https://www.nuget.org/packages/Naravel.Queue.Encryption) | 0.1.0 | Naravel contributors | Optional Naravel.Queue adapter that encrypts the payload of jobs marked IShould… |
| 2026-11-01 19:43:52 | [Naravel.Queue.File](https://www.nuget.org/packages/Naravel.Queue.File) | 0.1.0 | Naravel contributors | File-based queue driver for Naravel.Queue - durable, zero external services req… |
| 2026-11-01 19:43:53 | [Naravel.Queue.Kafka](https://www.nuget.org/packages/Naravel.Queue.Kafka) | 0.1.0 | Naravel contributors | Kafka queue driver for Naravel.Queue, built on Confluent.Kafka - semantics adap… |
| 2026-11-01 19:43:54 | [Naravel.Queue.Memory](https://www.nuget.org/packages/Naravel.Queue.Memory) | 0.1.0 | Naravel contributors | In-process "memory" queue driver for Naravel.Queue - zero dependencies, ideal f… |
| 2026-11-01 19:43:54 | [Naravel.Queue.RabbitMQ](https://www.nuget.org/packages/Naravel.Queue.RabbitMQ) | 0.1.0 | Naravel contributors | RabbitMQ queue driver for Naravel.Queue - delayed jobs via per-message TTL + de… |
| 2026-11-01 19:43:55 | [Naravel.Queue.Redis](https://www.nuget.org/packages/Naravel.Queue.Redis) | 0.1.0 | Naravel contributors | Redis queue driver for Naravel.Queue, built on StackExchange.Redis - priority b… |
| 2026-11-01 19:43:56 | [Naravel.Redis](https://www.nuget.org/packages/Naravel.Redis) | 0.1.0 | Naravel contributors | Named, shared Redis connections for Naravel modules: one StackExchange.Redis mu… |
| 2026-11-01 19:43:56 | [Naravel.Routing](https://www.nuget.org/packages/Naravel.Routing) | 0.1.0 | Naravel contributors | Laravel-style routing and middleware for ASP.NET Core: fluent route groups, nam… |
| 2026-11-01 19:43:57 | [Naravel.Scheduling](https://www.nuget.org/packages/Naravel.Scheduling) | 0.1.0 | Naravel contributors | Naravel task scheduling: a fluent, named schedule run by a hosted service, with… |
| 2026-11-01 20:02:08 | [OpenPhysical.Biometrics.NBIS.Cli](https://www.nuget.org/packages/OpenPhysical.Biometrics.NBIS.Cli) | 1.0.0 | OpenPhysical Contributors | Package Description |
| 2026-11-01 20:02:08 | [OpenPhysical.Biometrics.NBIS](https://www.nuget.org/packages/OpenPhysical.Biometrics.NBIS) | 1.0.0 | OpenPhysical Contributors | Standalone in-memory NIST NBIS MINDTCT extraction and Bozorth3 matching. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
