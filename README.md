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

## Latest list — 2026-11-10 20:20 UTC

New packages created between 2026-11-10 19:20 UTC and 2026-11-10 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T20-20-35-193205Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 19:21:38 | [Reverb.Runtime](https://www.nuget.org/packages/Reverb.Runtime) | 0.1.0 | Muneeb Mughal | Display helpers and UI widgets for Reverb notebooks. |
| 2026-11-10 19:21:40 | [Reverb.Notebooks](https://www.nuget.org/packages/Reverb.Notebooks) | 0.1.0 | Muneeb Mughal | Reactive C# notebooks that are plain .cs files. |
| 2026-11-10 19:25:45 | [NetStoneCN](https://www.nuget.org/packages/NetStoneCN) | 1.0.1 | NetStoneCN Contributors | Cookie-based api for Final Fantasy XIV Rising Stones character data. |
| 2026-11-10 19:31:32 | [Beskar.Jobs.Client](https://www.nuget.org/packages/Beskar.Jobs.Client) | 11.0.0 | Marvin Drude | High-performance MQTT job producer, controller, and real-time status streaming… |
| 2026-11-10 19:31:32 | [Beskar.Jobs.Common](https://www.nuget.org/packages/Beskar.Jobs.Common) | 11.0.0 | Marvin Drude | Core models, zero-allocation Cron scheduler, storage abstractions, and telemetr… |
| 2026-11-10 19:31:33 | [Beskar.Jobs.Generator](https://www.nuget.org/packages/Beskar.Jobs.Generator) | 11.0.0 | Marvin Drude | Package Description |
| 2026-11-10 19:31:33 | [Beskar.Jobs.Worker](https://www.nuget.org/packages/Beskar.Jobs.Worker) | 11.0.0 | Marvin Drude | Distributed MQTT job execution worker with Last-Will crash detection, concurren… |
| 2026-11-10 19:31:45 | [Beskar.Jobs.Scheduler](https://www.nuget.org/packages/Beskar.Jobs.Scheduler) | 11.0.0 | Marvin Drude | High-precision Cron and delayed job scheduler, dispatcher, and LWT crash recove… |
| 2026-11-10 19:42:03 | [SI.IdProvider.Client](https://www.nuget.org/packages/SI.IdProvider.Client) | 1.1.0 | Mladen Ristić | Client for SI.IdProvider, the service that hands out Snowflake ids (64-bit, tim… |
| 2026-11-10 19:42:49 | [PANiXiDA.Core.ApiDocumentation](https://www.nuget.org/packages/PANiXiDA.Core.ApiDocumentation) | 1.0.2 | PANiXiDA | Renderer-independent API document contracts and AOT-compatible AsyncAPI generat… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
