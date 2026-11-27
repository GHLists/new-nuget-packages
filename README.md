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

## Latest list — 2026-11-27 13:21 UTC

New packages created between 2026-11-27 12:20 UTC and 2026-11-27 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T13-21-08-342112Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 12:26:34 | [PowerCraft.Secrets.Core](https://www.nuget.org/packages/PowerCraft.Secrets.Core) | 2.0.0 | The Code Kitchen | Kernel of PowerCraft.Secrets: an encrypted secret store on disk. A secret is a… |
| 2026-11-27 12:43:14 | [DotHarness.Acp](https://www.nuget.org/packages/DotHarness.Acp) | 0.1.0 | DotHarness | Typed .NET Client and Agent SDK for the Agent Client Protocol v1. |
| 2026-11-27 12:43:17 | [DotHarness.Acp.Registry](https://www.nuget.org/packages/DotHarness.Acp.Registry) | 0.1.0 | DotHarness | Read-only .NET client and models for the Agent Client Protocol Registry. |
| 2026-11-27 12:46:06 | [RedCrab.OperationContract](https://www.nuget.org/packages/RedCrab.OperationContract) | 1.0.0 | Nicola Boffoli | RedCrab.OperationContract – the governed operation contract of the Request–Repl… |
| 2026-11-27 12:46:06 | [Relay.Authorization](https://www.nuget.org/packages/Relay.Authorization) | 1.1.0 | mohamadrezant | A modular .NET library providing Dispatcher, Mapper, Validation, and Authorizat… |
| 2026-11-27 12:46:06 | [RedCrab.Runtime.Requestor](https://www.nuget.org/packages/RedCrab.Runtime.Requestor) | 1.0.0 | Nicola Boffoli | RedCrab.Requestor – client-side runtime to send typed RedCrab requests and awai… |
| 2026-11-27 12:46:07 | [RedCrab.Transport.Pulsar](https://www.nuget.org/packages/RedCrab.Transport.Pulsar) | 1.0.0 | Nicola Boffoli | RedCrab.Transport.Pulsar – the Apache Pulsar adapter of the RedCrab transport a… |
| 2026-11-27 12:46:07 | [RedCrab.Surfaces](https://www.nuget.org/packages/RedCrab.Surfaces) | 1.0.0 | Nicola Boffoli | RedCrab public contracts used by generated stubs and surface integrations (requ… |
| 2026-11-27 12:46:08 | [RedCrab.Transport.Abstractions](https://www.nuget.org/packages/RedCrab.Transport.Abstractions) | 1.0.0 | Nicola Boffoli | RedCrab.Transport.Abstractions – the threshold of the broker: what the runtimes… |
| 2026-11-27 12:46:08 | [RedCrab](https://www.nuget.org/packages/RedCrab) | 1.0.0 | Nicola Boffoli | RedCrab – request–reply middleware for event-driven, broker-based architectures… |
| 2026-11-27 12:46:09 | [RedCrab.Runtime.Replier](https://www.nuget.org/packages/RedCrab.Runtime.Replier) | 1.0.0 | Nicola Boffoli | RedCrab.Replier – server-side runtime to host typed handlers and publish typed… |
| 2026-11-27 12:46:10 | [RedCrab.LocalPolicies](https://www.nuget.org/packages/RedCrab.LocalPolicies) | 1.0.0 | Nicola Boffoli | RedCrab.LocalPolicies – the local policies and the handler dispatcher of the Re… |
| 2026-11-27 12:46:10 | [RedCrab.ProtocolBinding](https://www.nuget.org/packages/RedCrab.ProtocolBinding) | 1.0.0 | Nicola Boffoli | RedCrab.ProtocolBinding – the bound operation protocol of the Request–Reply bou… |
| 2026-11-27 12:46:10 | [Relay.Authorization.Adapters.InMemory](https://www.nuget.org/packages/Relay.Authorization.Adapters.InMemory) | 1.1.0 | mohamadrezant | A modular .NET library providing Dispatcher, Mapper, Validation, and Authorizat… |
| 2026-11-27 12:46:11 | [RedCrab.Transport.Kafka](https://www.nuget.org/packages/RedCrab.Transport.Kafka) | 1.0.0 | Nicola Boffoli | RedCrab.Transport.Kafka – Kafka/Redpanda transport implementation for RedCrab,… |
| 2026-11-27 13:08:10 | [Nxa.Avalonia.Provider](https://www.nuget.org/packages/Nxa.Avalonia.Provider) | 0.1.0 | Nxa Lab | Dependency injection and state management utilities for Avalonia UI, including… |
| 2026-11-27 13:10:39 | [Mizanpage](https://www.nuget.org/packages/Mizanpage) | 1.0.0 | Laudelout Studio | Client officiel de l'API Mizanpage : générer des PDF depuis vos modèles, en dir… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
