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

## Latest list — 2026-10-03 05:20 UTC

New packages created between 2026-10-03 04:21 UTC and 2026-10-03 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T05-20-13-296439Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 05:11:44 | [AvroSharp.Aws.Glue](https://www.nuget.org/packages/AvroSharp.Aws.Glue) | 1.0.0 | zcsizmadia | A managed AWS Glue Schema Registry serializer on AvroSharp, for every platform:… |
| 2026-10-03 05:11:45 | [AvroSharp.Aws.Glue.Kafka](https://www.nuget.org/packages/AvroSharp.Aws.Glue.Kafka) | 1.0.0 | zcsizmadia | Confluent.Kafka serializers and deserializers for AWS Glue Schema Registry on A… |
| 2026-10-03 05:11:46 | [AvroSharp.Azure.SchemaRegistry](https://www.nuget.org/packages/AvroSharp.Azure.SchemaRegistry) | 1.0.0 | zcsizmadia | An Azure Schema Registry serializer on AvroSharp for Event Hubs and Service Bus… |
| 2026-10-03 05:11:49 | [AvroSharp.Confluent](https://www.nuget.org/packages/AvroSharp.Confluent) | 1.0.0 | zcsizmadia | Confluent Schema Registry serializers and deserializers for Confluent.Kafka on… |
| 2026-10-03 05:11:51 | [AvroSharp.KafkaFlow](https://www.nuget.org/packages/AvroSharp.KafkaFlow) | 1.0.0 | zcsizmadia | KafkaFlow serializers and deserializers for Confluent Schema Registry on AvroSh… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
