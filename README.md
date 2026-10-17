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

## Latest list — 2026-10-17 08:19 UTC

New packages created between 2026-10-17 07:21 UTC and 2026-10-17 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T08-19-30-240294Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 07:24:10 | [Drenalol.Telegram.Bot.Forms](https://www.nuget.org/packages/Drenalol.Telegram.Bot.Forms) | 1.0.0 | Bogdan Yanysh | Chat-first Telegram bot framework for Telegram.Bot: DI-scoped forms, per-chat n… |
| 2026-10-17 07:27:43 | [SLVZ.CoreDb](https://www.nuget.org/packages/SLVZ.CoreDb) | 1.0.0 | SLVZ | Embedded local database for .NET (net8.0+, Windows / Android / anything). No de… |
| 2026-10-17 07:39:29 | [mGO.Log.Abstractions](https://www.nuget.org/packages/mGO.Log.Abstractions) | 1.0.0 | MarioGO | Public contracts and immutable events for mGO.Log. |
| 2026-10-17 07:40:17 | [mGO.Log](https://www.nuget.org/packages/mGO.Log) | 1.0.0 | MarioGO | Bounded asynchronous structured logging engine and rotating file sink for .NET… |
| 2026-10-17 07:40:29 | [mGO.Log.Extensions.Hosting](https://www.nuget.org/packages/mGO.Log.Extensions.Hosting) | 1.0.0 | MarioGO | Dependency injection, configuration and host lifecycle integration for mGO.Log. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
