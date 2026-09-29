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

## Latest list — 2026-09-29 21:21 UTC

New packages created between 2026-09-29 20:20 UTC and 2026-09-29 21:21 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T21-21-26-46842Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 20:31:57 | [UnitTestEx.Aspire](https://www.nuget.org/packages/UnitTestEx.Aspire) | 5.12.0 | Avanade | UnitTestEx .NET Aspire distributed-application (multi-host) Test Extensions. |
| 2026-09-29 20:37:12 | [Preagonal.Scripting.Corpus](https://www.nuget.org/packages/Preagonal.Scripting.Corpus) | 1.4.91 | Preagonal | Shared GS2 language corpus fixtures (source plus captured C# and official toolc… |
| 2026-09-29 20:38:20 | [Kuestenlogik.Bowire.SchemaDesigner](https://www.nuget.org/packages/Kuestenlogik.Bowire.SchemaDesigner) | 2.8.0 | Kuestenlogik | Bowire Schema Designer rail — a graph view of a discovered schema's type relati… |
| 2026-09-29 20:38:23 | [Kuestenlogik.Bowire.Scaffold](https://www.nuget.org/packages/Kuestenlogik.Bowire.Scaffold) | 2.8.0 | Kuestenlogik | Bowire service scaffolding — turns an entity spec into a schema (OpenAPI 3 or p… |
| 2026-09-29 21:03:51 | [Budoom.MessagingQueues.Abstractions](https://www.nuget.org/packages/Budoom.MessagingQueues.Abstractions) | 0.1.0-beta | bayazidahmed | Broker-neutral messaging contracts: IMessagePublisher, IMessageConsumer and Rec… |
| 2026-09-29 21:03:52 | [Budoom.MessagingQueues.RabbitMq](https://www.nuget.org/packages/Budoom.MessagingQueues.RabbitMq) | 0.1.0-beta | bayazidahmed | RabbitMQ implementation of Budoom.MessagingQueues on the official RabbitMQ.Clie… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
