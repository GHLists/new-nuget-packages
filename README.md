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

## Latest list — 2026-11-15 04:19 UTC

New packages created between 2026-11-15 03:19 UTC and 2026-11-15 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T04-19-32-599127Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 03:29:37 | [Mateu.Dtos](https://www.nuget.org/packages/Mateu.Dtos) | 3.0.0 | Miguel Pérez Colom | Mateu wire model for .NET: the UIIncrement/component DTOs exchanged with every… |
| 2026-11-15 03:29:38 | [Mateu.Core](https://www.nuget.org/packages/Mateu.Core) | 3.0.0 | Miguel Pérez Colom | Mateu engine for .NET: route registry, reflection mapper (view model to compone… |
| 2026-11-15 03:29:38 | [Mateu.Uidl](https://www.nuget.org/packages/Mateu.Uidl) | 3.0.0 | Miguel Pérez Colom | Mateu public API for .NET: the attributes ([UI], [Section], [Button]…), fluent… |
| 2026-11-15 03:29:38 | [Mateu.Bundle](https://www.nuget.org/packages/Mateu.Bundle) | 3.0.0 | Miguel Pérez Colom | dotnet mateu-bundle: exports a Mateu.NET app (code and/or YAML specs) to a stat… |
| 2026-11-15 03:29:39 | [Mateu.AspNetCore](https://www.nuget.org/packages/Mateu.AspNetCore) | 3.0.0 | Miguel Pérez Colom | Mateu for ASP.NET Core: AddMateu()/MapMateu() — DI, identity and the POST /mate… |
| 2026-11-15 03:44:37 | [Pantheon.Common](https://www.nuget.org/packages/Pantheon.Common) | 1.0.2 | itzmerobby | Shared exception types for Pantheon packages, independent of application runtim… |
| 2026-11-15 03:44:48 | [Mekhane.Discovery](https://www.nuget.org/packages/Mekhane.Discovery) | 1.0.2 | itzmerobby | Assembly discovery and dependency ordering for Mekhane modules. |
| 2026-11-15 03:47:33 | [dotnet-http-file](https://www.nuget.org/packages/dotnet-http-file) | 0.1.0 | Jaliya Udagedara | Run Visual Studio .http files from the command line. |
| 2026-11-15 03:50:42 | [Relayer.AspNetCore](https://www.nuget.org/packages/Relayer.AspNetCore) | 0.1.1 | Tom Longhurst | Optional ASP.NET Core dead-letter management endpoints for Relayer. |
| 2026-11-15 03:50:42 | [Relayer.Serialization.MessagePack](https://www.nuget.org/packages/Relayer.Serialization.MessagePack) | 0.1.1 | Tom Longhurst | Buffer-based MessagePack serialization for Relayer using explicit native option… |
| 2026-11-15 03:50:43 | [Relayer.Testing](https://www.nuget.org/packages/Relayer.Testing) | 0.1.1 | Tom Longhurst | Host-local message harness, handler test contexts and reusable transport confor… |
| 2026-11-15 03:50:44 | [Relayer.Outbox.PostgreSql](https://www.nuget.org/packages/Relayer.Outbox.PostgreSql) | 0.1.1 | Tom Longhurst | PostgreSQL (ADO.NET) outbox and inbox for Relayer. |
| 2026-11-15 03:50:45 | [Relayer.Outbox.SqlServer](https://www.nuget.org/packages/Relayer.Outbox.SqlServer) | 0.1.1 | Tom Longhurst | SQL Server transactional outbox enlistment, durable reads and fenced claims for… |
| 2026-11-15 03:50:45 | [Relayer.AmazonSqs.HealthChecks](https://www.nuget.org/packages/Relayer.AmazonSqs.HealthChecks) | 0.1.1 | Tom Longhurst | Optional native connectivity and receiver liveness health adapters for Relayer.… |
| 2026-11-15 03:50:46 | [Relayer.AzureServiceBus](https://www.nuget.org/packages/Relayer.AzureServiceBus) | 0.1.1 | Tom Longhurst | Azure Service Bus transport for Relayer, wrapping Azure.Messaging.ServiceBus. |
| 2026-11-15 03:50:47 | [Relayer.Serialization.Protobuf](https://www.nuget.org/packages/Relayer.Serialization.Protobuf) | 0.1.1 | Tom Longhurst | Buffer-based Protobuf serialization for Relayer using explicitly registered gen… |
| 2026-11-15 03:50:48 | [Relayer.Outbox.PostgreSql.EntityFrameworkCore](https://www.nuget.org/packages/Relayer.Outbox.PostgreSql.EntityFrameworkCore) | 0.1.1 | Tom Longhurst | PostgreSQL provider for Relayer's EF Core outbox and inbox. |
| 2026-11-15 03:50:49 | [Relayer.Kafka.Serialization.Avro](https://www.nuget.org/packages/Relayer.Kafka.Serialization.Avro) | 0.1.1 | Tom Longhurst | Startup-prepared, source-generated Avro serialization for Relayer using the Dek… |
| 2026-11-15 03:50:50 | [Relayer.AzureServiceBus.HealthChecks](https://www.nuget.org/packages/Relayer.AzureServiceBus.HealthChecks) | 0.1.1 | Tom Longhurst | Optional native connectivity and receiver liveness health adapters for Relayer.… |
| 2026-11-15 03:50:51 | [Relayer.RabbitMQ.HealthChecks](https://www.nuget.org/packages/Relayer.RabbitMQ.HealthChecks) | 0.1.1 | Tom Longhurst | Optional native RabbitMQ connectivity and receiver liveness adapters for Relaye… |
| 2026-11-15 03:50:54 | [Relayer.Outbox.MySql](https://www.nuget.org/packages/Relayer.Outbox.MySql) | 0.1.1 | Tom Longhurst | MySQL transactional outbox enqueue, durable reads and fenced claims for Relayer. |
| 2026-11-15 03:50:55 | [Relayer.Nats](https://www.nuget.org/packages/Relayer.Nats) | 0.1.1 | Tom Longhurst | Native NATS JetStream transport for Relayer. |
| 2026-11-15 03:50:55 | [Relayer.Cli](https://www.nuget.org/packages/Relayer.Cli) | 0.1.1 | Tom Longhurst | Relayer topology export, database schema scripts and message lookup. |
| 2026-11-15 03:50:56 | [Relayer.Kafka](https://www.nuget.org/packages/Relayer.Kafka) | 0.1.1 | Tom Longhurst | Kafka transport for Relayer, wrapping Dekaf, a pure C# Kafka client. |
| 2026-11-15 03:50:57 | [Relayer.Sagas.EntityFrameworkCore](https://www.nuget.org/packages/Relayer.Sagas.EntityFrameworkCore) | 0.1.1 | Tom Longhurst | Transactional PostgreSQL saga persistence on Relayer's EF Core inbox and outbox. |
| 2026-11-15 03:50:57 | [Relayer.RabbitMQ](https://www.nuget.org/packages/Relayer.RabbitMQ) | 0.1.1 | Tom Longhurst | RabbitMQ transport for Relayer, wrapping RabbitMQ.Client. |
| 2026-11-15 03:50:58 | [Relayer.Sagas](https://www.nuget.org/packages/Relayer.Sagas) | 0.1.1 | Tom Longhurst | Explicit process diagrams, state and typed saga execution for Relayer. |
| 2026-11-15 04:01:15 | [HyperCache](https://www.nuget.org/packages/HyperCache) | 0.9.0 | HyperCache | A fast in-memory IDistributedCache for .NET that keeps every app instance in sy… |
| 2026-11-15 04:13:28 | [Boutquin.Abstractions](https://www.nuget.org/packages/Boutquin.Abstractions) | 1.0.0 | Pierre G. Boutquin | Current-user and authorization abstractions (ICurrentUserService, IAuthorizatio… |
| 2026-11-15 04:13:29 | [Boutquin.Mediator](https://www.nuget.org/packages/Boutquin.Mediator) | 1.0.0 | Pierre G. Boutquin | Mediator implementation for .NET — request dispatch, notification fan-out, stre… |
| 2026-11-15 04:13:30 | [Boutquin.Mediator.Abstractions](https://www.nuget.org/packages/Boutquin.Mediator.Abstractions) | 1.0.0 | Pierre G. Boutquin | Contracts for the Boutquin mediator — commands, queries, notifications, stream… |
| 2026-11-15 04:13:32 | [Boutquin.Mediator.Reliability](https://www.nuget.org/packages/Boutquin.Mediator.Reliability) | 1.0.0 | Pierre G. Boutquin | Retry pipeline behavior for Boutquin.Mediator — retries failed requests with pe… |
| 2026-11-15 04:13:32 | [Boutquin.Mediator.Caching](https://www.nuget.org/packages/Boutquin.Mediator.Caching) | 1.0.0 | Pierre G. Boutquin | Distributed-cache pipeline behavior for Boutquin.Mediator — caches successful R… |
| 2026-11-15 04:14:07 | [FrontEndCSharp.Overrides.Interop.JS.Browser.fecs](https://www.nuget.org/packages/FrontEndCSharp.Overrides.Interop.JS.Browser.fecs) | 1.0.0 | drewdelano | Compiler and runtime override resources for Interop.JS.Browser in FrontEndCShar… |
| 2026-11-15 04:14:14 | [FrontEndCSharp.Overrides.Interop.JS.MobX.fecs](https://www.nuget.org/packages/FrontEndCSharp.Overrides.Interop.JS.MobX.fecs) | 7.0.6 | drewdelano | Compiler and runtime override resources for Interop.JS.MobX in FrontEndCSharp b… |
| 2026-11-15 04:14:40 | [FrontEndCSharp.Overrides.System.ComponentModel.Annotations.fecs](https://www.nuget.org/packages/FrontEndCSharp.Overrides.System.ComponentModel.Annotations.fecs) | 1.0.0 | drewdelano | Compiler and runtime override resources for System.ComponentModel.Annotations i… |
| 2026-11-15 04:14:41 | [FrontEndCSharp.Overrides.System.Console.fecs](https://www.nuget.org/packages/FrontEndCSharp.Overrides.System.Console.fecs) | 1.0.0 | drewdelano | Compiler and runtime override resources for System.Console in FrontEndCSharp br… |
| 2026-11-15 04:14:42 | [FrontEndCSharp.Overrides.System.Linq.Expressions.fecs](https://www.nuget.org/packages/FrontEndCSharp.Overrides.System.Linq.Expressions.fecs) | 1.0.0 | drewdelano | Compiler and runtime override resources for System.Linq.Expressions in FrontEnd… |
| 2026-11-15 04:14:46 | [FrontEndCSharp.Overrides.System.Net.Http.Json.fecs](https://www.nuget.org/packages/FrontEndCSharp.Overrides.System.Net.Http.Json.fecs) | 1.0.0 | drewdelano | Compiler and runtime override resources for System.Net.Http.Json in FrontEndCSh… |
| 2026-11-15 04:14:50 | [FrontEndCSharp.Overrides.System.Security.Cryptography.fecs](https://www.nuget.org/packages/FrontEndCSharp.Overrides.System.Security.Cryptography.fecs) | 1.0.0 | drewdelano | Compiler and runtime override resources for System.Security.Cryptography in Fro… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
