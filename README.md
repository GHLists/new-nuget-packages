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

## Latest list — 2026-10-12 23:19 UTC

New packages created between 2026-10-12 22:20 UTC and 2026-10-12 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T23-19-11-574559Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 22:26:43 | [StoveDotnet.SchemaRegistry](https://www.nuget.org/packages/StoveDotnet.SchemaRegistry) | 0.1.6 | cokceken | Confluent Schema Registry system for StoveDotnet, with setup migrations and exi… |
| 2026-10-12 22:26:47 | [StoveDotnet.Kafka.Avro](https://www.nuget.org/packages/StoveDotnet.Kafka.Avro) | 0.1.6 | cokceken | Typed Avro publishing and observation for StoveDotnet Kafka using Confluent Sch… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
