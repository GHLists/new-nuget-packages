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

## Latest list — 2026-11-24 22:22 UTC

New packages created between 2026-11-24 21:22 UTC and 2026-11-24 22:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T22-22-35-830103Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 21:25:27 | [Anarchy.Toolkit.Infrastructure.Messaging.CloudEvents](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Messaging.CloudEvents) | 1.0.0 | Leandro Melão Medeiros | Transport-independent mapping between Anarchy event envelopes and CloudEvents. |
| 2026-11-24 21:25:28 | [Anarchy.Toolkit.Infrastructure.Messaging.Kafka](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Messaging.Kafka) | 1.0.0 | Leandro Melão Medeiros | Apache Kafka publisher and inbound mapping for the message-broker contracts. |
| 2026-11-24 21:25:31 | [Anarchy.Toolkit.Infrastructure.Persistence.Db.Events](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Persistence.Db.Events) | 1.0.0 | Leandro Melão Medeiros | Provider-agnostic relational event-store repository bases and transactional out… |
| 2026-11-24 21:25:35 | [Anarchy.Toolkit.Infrastructure.Telemetry.StatsD](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Telemetry.StatsD) | 1.0.0 | Leandro Melão Medeiros | Optional DogStatsD metrics recorder and dependency injection integration for An… |
| 2026-11-24 21:25:41 | [Anarchy.Toolkit.Testing.Kafka](https://www.nuget.org/packages/Anarchy.Toolkit.Testing.Kafka) | 1.0.0 | Leandro Melão Medeiros | Kafka message fixture and consumer helper for tests against a Kafka-compatible… |
| 2026-11-24 21:31:23 | [fksegundo.Hangfire.Dashboard.JobSearch.Core](https://www.nuget.org/packages/fksegundo.Hangfire.Dashboard.JobSearch.Core) | 1.2.0 | fksegundo | Core library for Hangfire Dashboard JobSearch: metadata extraction, dashboard U… |
| 2026-11-24 21:31:23 | [fksegundo.Hangfire.Dashboard.JobSearch.PostgreSql](https://www.nuget.org/packages/fksegundo.Hangfire.Dashboard.JobSearch.PostgreSql) | 1.2.0 | fksegundo | PostgreSQL storage provider for Hangfire.Dashboard.JobSearch. |
| 2026-11-24 21:31:24 | [fksegundo.Hangfire.Dashboard.JobSearch.Redis](https://www.nuget.org/packages/fksegundo.Hangfire.Dashboard.JobSearch.Redis) | 1.2.0 | fksegundo | Redis storage provider for Hangfire.Dashboard.JobSearch using StackExchange.Red… |
| 2026-11-24 21:31:25 | [fksegundo.Hangfire.Dashboard.JobSearch.SqlServer](https://www.nuget.org/packages/fksegundo.Hangfire.Dashboard.JobSearch.SqlServer) | 1.2.0 | fksegundo | SQL Server storage provider for Hangfire.Dashboard.JobSearch. |
| 2026-11-24 21:34:43 | [BitBindle.ProseMirror](https://www.nuget.org/packages/BitBindle.ProseMirror) | 2.0.0 | ProTip, BitBindle | A direct translation of the core ProseMirror packages from TypeScript to C# |
| 2026-11-24 21:51:53 | [nugetscope](https://www.nuget.org/packages/nugetscope) | 0.1.0 | Eren | Interactive terminal dashboard for the NuGet packages of a whole .NET solution… |
| 2026-11-24 22:02:43 | [MHX](https://www.nuget.org/packages/MHX) | 0.2.3 | Moaid Hathot | A small configurable process launcher with NuGet v2 .NET tool execution. |
| 2026-11-24 22:02:59 | [Printsluis.Contracts](https://www.nuget.org/packages/Printsluis.Contracts) | 2.0.0 | Isatis Projects | Request and response contracts shared by Printsluis, its agent and the client S… |
| 2026-11-24 22:03:00 | [Printsluis.Client](https://www.nuget.org/packages/Printsluis.Client) | 2.0.0 | Isatis Projects | .NET client for the Printsluis API. |
| 2026-11-24 22:11:02 | [XDevPlatform.Xdk](https://www.nuget.org/packages/XDevPlatform.Xdk) | 0.1.1 | X Corp. | Official C# / .NET SDK for the X API v2 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
