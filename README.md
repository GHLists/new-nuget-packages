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

## Latest list — 2026-11-24 19:20 UTC

New packages created between 2026-11-24 18:20 UTC and 2026-11-24 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T19-20-44-097802Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 18:26:16 | [Databento.CSharpApiClient.Caching](https://www.nuget.org/packages/Databento.CSharpApiClient.Caching) | 1.0.0 | Vardan Tovmasyan | A disk cache and Parquet archive for Databento.CSharpApiClient, so each day of… |
| 2026-11-24 18:43:47 | [BitBindle.ClosedXML.Parser](https://www.nuget.org/packages/BitBindle.ClosedXML.Parser) | 3.0.0 | Jan Havlíček, BitBindle | A lexer and parser of Excel formulas with focus on performance. Its goal is to… |
| 2026-11-24 18:54:09 | [Credfeto.Build.Python.Server](https://www.nuget.org/packages/Credfeto.Build.Python.Server) | 0.0.11.217-python-s… | Mark Ridgwell | Credfeto Build MCP Python server: restore, lint, test and coverage for Python r… |
| 2026-11-24 18:54:10 | [Credfeto.Build.Python.Server.linux-x64](https://www.nuget.org/packages/Credfeto.Build.Python.Server.linux-x64) | 0.0.11.217-python-s… | Mark Ridgwell | Credfeto Build MCP Python server: restore, lint, test and coverage for Python r… |
| 2026-11-24 18:58:03 | [StratumKit.Cli](https://www.nuget.org/packages/StratumKit.Cli) | 0.36.2 | Stratum | Stratum: a .NET 10 microservice generator with your team's conventions (CLI, vi… |
| 2026-11-24 18:58:04 | [StratumKit.Messaging](https://www.nuget.org/packages/StratumKit.Messaging) | 0.36.2 | Stratum | Stratum messaging between services: integration events through an outbox (no ev… |
| 2026-11-24 18:58:05 | [StratumKit.Messaging.AzureServiceBus](https://www.nuget.org/packages/StratumKit.Messaging.AzureServiceBus) | 0.36.2 | Stratum | Azure Service Bus broker for Stratum.Messaging: one topic per integration event… |
| 2026-11-24 18:58:06 | [StratumKit.ServiceDefaults](https://www.nuget.org/packages/StratumKit.ServiceDefaults) | 0.36.2 | Stratum | Stratum service defaults: health checks, ProblemDetails, correlation id, valida… |
| 2026-11-24 18:58:07 | [StratumKit.Messaging.Kafka](https://www.nuget.org/packages/StratumKit.Messaging.Kafka) | 0.36.2 | Stratum | Kafka broker for Stratum.Messaging (Confluent.Kafka): one topic per integration… |
| 2026-11-24 18:58:08 | [StratumKit.ServiceDefaults.Resilience](https://www.nuget.org/packages/StratumKit.ServiceDefaults.Resilience) | 0.36.2 | Stratum | Stratum service defaults for HTTP clients: standard resilience pipeline (retry,… |
| 2026-11-24 18:58:09 | [StratumKit.Ddd](https://www.nuget.org/packages/StratumKit.Ddd) | 0.36.2 | Stratum | Stratum DDD building blocks: aggregates, domain events, domain exceptions, comm… |
| 2026-11-24 18:58:09 | [StratumKit.ServiceDefaults.OpenTelemetry](https://www.nuget.org/packages/StratumKit.ServiceDefaults.OpenTelemetry) | 0.36.2 | Stratum | Stratum service defaults: OpenTelemetry traces, metrics and logs with OTLP expo… |
| 2026-11-24 18:58:10 | [StratumKit.ServiceDefaults.Authentication](https://www.nuget.org/packages/StratumKit.ServiceDefaults.Authentication) | 0.36.2 | Stratum | Stratum service defaults: JWT bearer authentication, secure by default (authent… |
| 2026-11-24 18:58:11 | [StratumKit.Messaging.EntityFrameworkCore](https://www.nuget.org/packages/StratumKit.Messaging.EntityFrameworkCore) | 0.36.2 | Stratum | Transactional outbox and inbox for Stratum.Messaging with EF Core: integration… |
| 2026-11-24 19:05:51 | [Themis.Inference.Remote.SystemOne](https://www.nuget.org/packages/Themis.Inference.Remote.SystemOne) | 4.7.0 | Themis contributors | System One decision protocol mapping over Themis' shared HTTP transport. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
