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

## Latest list — 2026-11-28 11:19 UTC

New packages created between 2026-11-28 10:20 UTC and 2026-11-28 11:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-28T11-19-10-443561Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-28 10:25:40 | [BitMagic.X16Oscar64](https://www.nuget.org/packages/BitMagic.X16Oscar64) | 0.1.2 | Yazwh0 | Oscar64 debug information (.dbj) for the Commander X16: reader, line and scope… |
| 2026-11-28 10:25:41 | [BitMagic.X16Oscar64.Debugger](https://www.nuget.org/packages/BitMagic.X16Oscar64.Debugger) | 0.1.2 | Yazwh0 | Debugs C programs compiled with Oscar64 for the Commander X16, in X16D. |
| 2026-11-28 10:27:55 | [ToucanHub.EventStore.Outbox.Abstractions](https://www.nuget.org/packages/ToucanHub.EventStore.Outbox.Abstractions) | 0.8.0 | junglistkirss | Outbox store abstractions |
| 2026-11-28 10:27:56 | [ToucanHub.EventStore.Outbox.PgSql](https://www.nuget.org/packages/ToucanHub.EventStore.Outbox.PgSql) | 0.8.0 | junglistkirss | Outbox store for PostgreSQL |
| 2026-11-28 10:28:53 | [Nextorm.Extensions.PostgreSql](https://www.nuget.org/packages/Nextorm.Extensions.PostgreSql) | 1.0.0 | Nextorm.Extensions.PostgreSql | NextORM mappings and query functions for the PostgreSQL system catalog and pgve… |
| 2026-11-28 10:32:22 | [Inertia.Net.Live.Sse](https://www.nuget.org/packages/Inertia.Net.Live.Sse) | 1.9.11 | Inertia.Net contributors | Server-Sent Events transport for Inertia.Net live props: one endpoint, no clien… |
| 2026-11-28 10:33:50 | [VL.Globe](https://www.nuget.org/packages/VL.Globe) | 0.1.0-alpha | red | A globe of map tiles in VL, drawn with Stride from the whole Earth down to stre… |
| 2026-11-28 10:41:38 | [Hexalith.Projects.EventStoreExtensions](https://www.nuget.org/packages/Hexalith.Projects.EventStoreExtensions) | 2.1.0 | Hexalith Contributors | Tenant-scoped project workspace and context-resolution module for .NET built on… |
| 2026-11-28 10:47:52 | [Gantry.Transport.Ssh](https://www.nuget.org/packages/Gantry.Transport.Ssh) | 0.1.1 | Patrick Matthiesen | SSH transport for Gantry automation on Linux and Windows targets. |
| 2026-11-28 10:47:53 | [Gantry.Host](https://www.nuget.org/packages/Gantry.Host) | 0.1.1 | Patrick Matthiesen | Build a Gantry command-line app that runs your own configuration and automation… |
| 2026-11-28 10:47:54 | [Gantry.Secrets](https://www.nuget.org/packages/Gantry.Secrets) | 0.1.1 | Patrick Matthiesen | Environment, file, Azure Key Vault, and in-memory secret providers for Gantry. |
| 2026-11-28 10:47:54 | [Gantry.Engine](https://www.nuget.org/packages/Gantry.Engine) | 0.1.1 | Patrick Matthiesen | Validate, plan, and execute Gantry pipelines. |
| 2026-11-28 10:47:55 | [Gantry.Cli](https://www.nuget.org/packages/Gantry.Cli) | 0.1.1 | Patrick Matthiesen | The Gantry command-line tool for validating, planning, and applying pipelines. |
| 2026-11-28 10:47:56 | [Gantry.Core](https://www.nuget.org/packages/Gantry.Core) | 0.1.1 | Patrick Matthiesen | Gantry's configuration model, pipeline DSL, and execution interfaces. |
| 2026-11-28 10:58:29 | [BricklinkSharp.Extensions.DependencyInjection](https://www.nuget.org/packages/BricklinkSharp.Extensions.DependencyInjection) | 2.0.0 | Jens Eisenbach | Dependency injection support (AddBrickLinkClient) for BricklinkSharp. |
| 2026-11-28 10:59:34 | [Tellurian.Trains.Schedules.Model.Files](https://www.nuget.org/packages/Tellurian.Trains.Schedules.Model.Files) | 5.0.0 | Stefan Fjällemark | The envelope of the Tellurian Trains files and the chain of migrations that bri… |
| 2026-11-28 10:59:35 | [Tellurian.Trains.Schedules.Model.Drawings](https://www.nuget.org/packages/Tellurian.Trains.Schedules.Model.Drawings) | 5.0.0 | Stefan Fjällemark | The drawn model railway layout: modules with their drawings, end profiles, stan… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
