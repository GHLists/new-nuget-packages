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

## Latest list — 2026-11-15 02:20 UTC

New packages created between 2026-11-15 01:19 UTC and 2026-11-15 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T02-20-53-420653Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 01:42:02 | [StellarStriderLib](https://www.nuget.org/packages/StellarStriderLib) | 1.5.1 | StriderDev | A MelonLoader content-registration library for StellarDrive, providing parts, i… |
| 2026-11-15 01:45:01 | [PrintSharp.Preview.AspNetCore](https://www.nuget.org/packages/PrintSharp.Preview.AspNetCore) | 0.3.0 | ogisyouryuu | PrintSharp preview sessions and endpoints. |
| 2026-11-15 01:45:02 | [PrintSharp.Preview.Blazor](https://www.nuget.org/packages/PrintSharp.Preview.Blazor) | 0.3.0 | ogisyouryuu | PrintSharp Canvas preview component for Blazor. |
| 2026-11-15 01:57:46 | [Hydris.Build](https://www.nuget.org/packages/Hydris.Build) | 0.9.6 | neuralfog | View build tool for Hydris and elemix SSR. |
| 2026-11-15 02:09:44 | [Relayer.HealthChecks](https://www.nuget.org/packages/Relayer.HealthChecks) | 0.1.0 | Tom Longhurst | Transport connectivity, consumer liveness and outbox backlog health checks for… |
| 2026-11-15 02:09:45 | [Relayer.AmazonSqs](https://www.nuget.org/packages/Relayer.AmazonSqs) | 0.1.0 | Tom Longhurst | Amazon SQS and SNS transport for Relayer, wrapping the AWS SDK. |
| 2026-11-15 02:09:46 | [Relayer.Kafka.HealthChecks](https://www.nuget.org/packages/Relayer.Kafka.HealthChecks) | 0.1.0 | Tom Longhurst | Optional native Kafka connectivity and receiver liveness adapters for Relayer h… |
| 2026-11-15 02:09:47 | [Relayer.Outbox.EntityFrameworkCore](https://www.nuget.org/packages/Relayer.Outbox.EntityFrameworkCore) | 0.1.0 | Tom Longhurst | Provider-neutral Entity Framework Core transaction coordination for Relayer out… |
| 2026-11-15 02:09:48 | [Relayer](https://www.nuget.org/packages/Relayer) | 0.1.0 | Tom Longhurst | Modern .NET messaging: wraps native broker clients and adds outbox, resiliency,… |
| 2026-11-15 02:09:49 | [Relayer.Aspire](https://www.nuget.org/packages/Relayer.Aspire) | 0.1.0 | Tom Longhurst | OpenTelemetry integration for Relayer. |
| 2026-11-15 02:09:50 | [Relayer.Kafka.SchemaRegistry](https://www.nuget.org/packages/Relayer.Kafka.SchemaRegistry) | 0.1.0 | Tom Longhurst | Explicit, startup-prepared JSON Schema Registry serialization for named Relayer… |
| 2026-11-15 02:09:51 | [Relayer.GooglePubSub](https://www.nuget.org/packages/Relayer.GooglePubSub) | 0.1.0 | Tom Longhurst | Google Cloud Pub/Sub transport using the native .NET client. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
