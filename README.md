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

## Latest list — 2026-11-09 10:19 UTC

New packages created between 2026-11-09 09:19 UTC and 2026-11-09 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T10-19-11-829491Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 09:37:53 | [PavelZaitsau.PhoneFormatter](https://www.nuget.org/packages/PavelZaitsau.PhoneFormatter) | 2.3.2 | Pavel Zaitsau | Parses, validates, and formats phone numbers from many regions as E.164, E.123,… |
| 2026-11-09 09:40:52 | [Semisoft.ExpressionParser](https://www.nuget.org/packages/Semisoft.ExpressionParser) | 1.0.2 | samwizardry | String filter parser that compiles text expressions into strongly-typed LINQ Ex… |
| 2026-11-09 09:49:07 | [L1CacheSystem](https://www.nuget.org/packages/L1CacheSystem) | 10.0.0 | Brevnov Vyacheslav Sergeevich | L1-level cache system for organizing a cache within an application. |
| 2026-11-09 09:49:42 | [L1CacheSystem.Attributes](https://www.nuget.org/packages/L1CacheSystem.Attributes) | 10.0.0 | Brevnov Vyacheslav Sergeevich | Attributes for L1-level cache system for organizing a cache within an applicati… |
| 2026-11-09 09:50:10 | [L1CacheSystem.Generator](https://www.nuget.org/packages/L1CacheSystem.Generator) | 10.0.0 | Brevnov Vyacheslav Sergeevich | Generator L1-level cache system for organizing a cache within an application. |
| 2026-11-09 09:52:33 | [OpenDCP.Framework.Exceptions](https://www.nuget.org/packages/OpenDCP.Framework.Exceptions) | 0.1.0 | OpenDCP.Framework.Exceptions | Package Description |
| 2026-11-09 09:53:13 | [Bridgewiz.AppUpdate](https://www.nuget.org/packages/Bridgewiz.AppUpdate) | 1.0.0 | Mustafa Can Yücel | Client for app-update-server (github.com/mcanyucel/app-update-server): checks f… |
| 2026-11-09 09:53:14 | [Bridgewiz.AppUpdate.Avalonia](https://www.nuget.org/packages/Bridgewiz.AppUpdate.Avalonia) | 1.0.0 | Mustafa Can Yücel | Update dialog and check flows for Avalonia desktop apps using Bridgewiz.AppUpda… |
| 2026-11-09 09:55:11 | [Olax.Messaging.Aws](https://www.nuget.org/packages/Olax.Messaging.Aws) | 1.0.0 | OLAX Innovative Lab | AWS transport for Olax.Messaging: one SNS topic fanned out to one SQS queue per… |
| 2026-11-09 09:55:12 | [Olax.Messaging.Azure.EventHubs](https://www.nuget.org/packages/Olax.Messaging.Azure.EventHubs) | 1.0.0 | OLAX Innovative Lab | Azure Event Hubs transport for Olax.Messaging. Runs the Kafka transport against… |
| 2026-11-09 09:55:14 | [Olax.Messaging.Azure.ServiceBus](https://www.nuget.org/packages/Olax.Messaging.Azure.ServiceBus) | 1.0.0 | OLAX Innovative Lab | Azure Service Bus transport for Olax.Messaging: one topic, one subscription per… |
| 2026-11-09 09:55:15 | [Olax.Messaging.EntityFrameworkCore](https://www.nuget.org/packages/Olax.Messaging.EntityFrameworkCore) | 1.0.0 | OLAX Innovative Lab | Transactional outbox and inbox for OLAX messaging on the service's EF Core DbCo… |
| 2026-11-09 09:55:16 | [Olax.Messaging.Google.PubSub](https://www.nuget.org/packages/Olax.Messaging.Google.PubSub) | 1.0.0 | OLAX Innovative Lab | Google Cloud Pub/Sub transport for Olax.Messaging: a topic per event, a subscri… |
| 2026-11-09 09:55:17 | [Olax.Messaging.Kafka](https://www.nuget.org/packages/Olax.Messaging.Kafka) | 1.0.0 | OLAX Innovative Lab | Kafka transport for Olax.Messaging (also the engine of Olax.Messaging.Azure.Eve… |
| 2026-11-09 09:55:18 | [Olax.Messaging.RabbitMQ](https://www.nuget.org/packages/Olax.Messaging.RabbitMQ) | 1.0.0 | OLAX Innovative Lab | RabbitMQ transport for Olax.Messaging: a topic exchange, one quorum queue per s… |
| 2026-11-09 09:55:20 | [Olax.Messaging](https://www.nuget.org/packages/Olax.Messaging) | 1.0.0 | OLAX Innovative Lab | Broker-neutral core of OLAX messaging: the message envelope, delivery rules, th… |
| 2026-11-09 09:55:21 | [Olax.Messaging.Abstractions](https://www.nuget.org/packages/Olax.Messaging.Abstractions) | 1.0.0 | OLAX Innovative Lab | Integration event contracts for OLAX services: IntegrationEvent, IEventPublishe… |
| 2026-11-09 09:56:33 | [Fdw.Services.Etl.Projects.Nodes.Registration](https://www.nuget.org/packages/Fdw.Services.Etl.Projects.Nodes.Registration) | 1.5.1 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-09 10:03:27 | [Semisoft.LdapHelper](https://www.nuget.org/packages/Semisoft.LdapHelper) | 1.0.3 | samwizardry | .NET library for Active Directory and LDAP operations built on System.Directory… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
