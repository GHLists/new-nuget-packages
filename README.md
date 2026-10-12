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

## Latest list — 2026-10-12 15:20 UTC

New packages created between 2026-10-12 14:20 UTC and 2026-10-12 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T15-20-14-541133Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 14:29:57 | [Iyu.Conventions.Testing.Snippets](https://www.nuget.org/packages/Iyu.Conventions.Testing.Snippets) | 0.9.0 | iyulab | Compiles the C# examples in a repository's Markdown (README, docs) from its own… |
| 2026-10-12 14:36:59 | [NymBroker.Endpoint.AwsSqs](https://www.nuget.org/packages/NymBroker.Endpoint.AwsSqs) | 0.11.0 | nymankla@gmail.com | Amazon SQS endpoint add-on for NymBroker: standard and FIFO queues, long pollin… |
| 2026-10-12 14:37:00 | [NymBroker.Idempotency.MySql](https://www.nuget.org/packages/NymBroker.Idempotency.MySql) | 0.11.0 | nymankla@gmail.com | Durable MySQL / MariaDB idempotency store (idempotent receiver) for NymBroker. |
| 2026-10-12 14:37:01 | [NymBroker.Endpoint.Http](https://www.nuget.org/packages/NymBroker.Endpoint.Http) | 0.11.0 | nymankla@gmail.com | HTTP / webhook endpoint add-on for NymBroker: delivers messages to a URL with r… |
| 2026-10-12 14:37:03 | [NymBroker.Endpoint.MySql](https://www.nuget.org/packages/NymBroker.Endpoint.MySql) | 0.11.0 | nymankla@gmail.com | MySQL / MariaDB queue-table endpoint add-on for NymBroker. |
| 2026-10-12 14:42:05 | [parsley-tool](https://www.nuget.org/packages/parsley-tool) | 1.0.0 | honey the codewitch | An advanced LL parser synthesizer for C# |
| 2026-10-12 14:42:34 | [parsley-luthor](https://www.nuget.org/packages/parsley-luthor) | 1.0.0 | parsley-luthor | Luthor lexer generator in a Parsley friendly package |
| 2026-10-12 14:50:08 | [TensorSharp.Knowledge](https://www.nuget.org/packages/TensorSharp.Knowledge) | 2026.10.11 | Zhongkai Fu | Durable local knowledge collections, bounded ingestion, hybrid retrieval, and s… |
| 2026-10-12 14:55:10 | [ITBees.Lantic](https://www.nuget.org/packages/ITBees.Lantic) | 8.0.1 | ITBees | Client library for Inveo LanTick Ethernet I/O modules (PE-8-0, PE-0-4, PE-4-4,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
