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

## Latest list — 2026-09-30 07:22 UTC

New packages created between 2026-09-30 06:21 UTC and 2026-09-30 07:22 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T07-22-13-245164Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 06:33:05 | [ResponsiveWebPSourceSet](https://www.nuget.org/packages/ResponsiveWebPSourceSet) | 1.0.1 | DraganS | ResponsiveWebPSourceSet is an ASP.NET Core TagHelper that automatically convert… |
| 2026-09-30 06:57:26 | [JamesTryand.DotnetCqrs.Telemetry.Nats](https://www.nuget.org/packages/JamesTryand.DotnetCqrs.Telemetry.Nats) | 0.17.0 | James Tryand | NATS transport for dotnetcqrs's optional telemetry push (health/telemetry contr… |
| 2026-09-30 07:02:00 | [Amanhecer.Compression.Zstd](https://www.nuget.org/packages/Amanhecer.Compression.Zstd) | 2.0.0 | Rafael Andrade | Zstandard compression transformers for Amanhecer: compress and decompress messa… |
| 2026-09-30 07:02:01 | [Amanhecer.Compression.LZ4](https://www.nuget.org/packages/Amanhecer.Compression.LZ4) | 2.0.0 | Rafael Andrade | LZ4 compression transformers for Amanhecer: compress and decompress message pay… |
| 2026-09-30 07:02:02 | [Amanhecer.Extensions.Hosting](https://www.nuget.org/packages/Amanhecer.Extensions.Hosting) | 2.0.0 | Rafael Andrade | Generic-host integration for Amanhecer: runs the messaging gateway consumers as… |
| 2026-09-30 07:02:03 | [Amanhecer.InMemory](https://www.nuget.org/packages/Amanhecer.InMemory) | 2.0.0 | Rafael Andrade | In-memory transport for Amanhecer: publish messages to channel-backed queues an… |
| 2026-09-30 07:02:04 | [Amanhecer.Compression.Snappier](https://www.nuget.org/packages/Amanhecer.Compression.Snappier) | 2.0.0 | Rafael Andrade | Snappy compression transformers for Amanhecer: compress and decompress message… |
| 2026-09-30 07:02:04 | [Amanhecer.Dekaf](https://www.nuget.org/packages/Amanhecer.Dekaf) | 2.0.0 | Rafael Andrade | Kafka transport for Amanhecer (Dekaf): publish messages to topics and consume t… |
| 2026-09-30 07:02:06 | [Amanhecer.ConfluentKafka](https://www.nuget.org/packages/Amanhecer.ConfluentKafka) | 2.0.0 | Rafael Andrade | Kafka transport for Amanhecer (Confluent.Kafka): publish messages to topics and… |
| 2026-09-30 07:02:07 | [Amanhecer.RabbitMq](https://www.nuget.org/packages/Amanhecer.RabbitMq) | 2.0.0 | Rafael Andrade | RabbitMQ transport for Amanhecer: publish messages to exchanges and consume the… |
| 2026-09-30 07:02:08 | [Amanhecer.OpenTelemetry](https://www.nuget.org/packages/Amanhecer.OpenTelemetry) | 2.0.0 | Rafael Andrade | OpenTelemetry integration for Amanhecer: trace and metric instrumentation for t… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
