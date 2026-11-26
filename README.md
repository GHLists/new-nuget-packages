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

## Latest list — 2026-11-26 05:20 UTC

New packages created between 2026-11-26 04:19 UTC and 2026-11-26 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T05-20-09-284013Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 04:19:16 | [AI.Sentinel.Codex.Cli.any](https://www.nuget.org/packages/AI.Sentinel.Codex.Cli.any) | 6.1.0 | Marcel Roozekrans | Codex CLI hook command for AI.Sentinel — wire into hooks.json or config.toml to… |
| 2026-11-26 04:19:21 | [AI.Sentinel.Codex.Cli.linux-x64](https://www.nuget.org/packages/AI.Sentinel.Codex.Cli.linux-x64) | 6.1.0 | Marcel Roozekrans | Codex CLI hook command for AI.Sentinel — wire into hooks.json or config.toml to… |
| 2026-11-26 04:19:33 | [AI.Sentinel.Codex.Cli.win-x64](https://www.nuget.org/packages/AI.Sentinel.Codex.Cli.win-x64) | 6.1.0 | Marcel Roozekrans | Codex CLI hook command for AI.Sentinel — wire into hooks.json or config.toml to… |
| 2026-11-26 04:19:43 | [AI.Sentinel.Codex.Cli.linux-arm64](https://www.nuget.org/packages/AI.Sentinel.Codex.Cli.linux-arm64) | 6.1.0 | Marcel Roozekrans | Codex CLI hook command for AI.Sentinel — wire into hooks.json or config.toml to… |
| 2026-11-26 04:19:45 | [AI.Sentinel.Codex.Cli.linux-musl-arm64](https://www.nuget.org/packages/AI.Sentinel.Codex.Cli.linux-musl-arm64) | 6.1.0 | Marcel Roozekrans | Codex CLI hook command for AI.Sentinel — wire into hooks.json or config.toml to… |
| 2026-11-26 04:23:12 | [Zifika](https://www.nuget.org/packages/Zifika) | 1.0.0 | Eriq VanBibber | Experimental keyed path-walking cipher with symmetric encryption and offline Mi… |
| 2026-11-26 04:33:15 | [Pernix.OutboxRelay.Core](https://www.nuget.org/packages/Pernix.OutboxRelay.Core) | 1.0.0 | Pernix | Package Description |
| 2026-11-26 04:33:16 | [Pernix.OutboxRelay.Destination.Kafka](https://www.nuget.org/packages/Pernix.OutboxRelay.Destination.Kafka) | 1.0.0 | Pernix | Package Description |
| 2026-11-26 04:33:17 | [Pernix.OutboxRelay.Hosting](https://www.nuget.org/packages/Pernix.OutboxRelay.Hosting) | 1.0.0 | Pernix | Package Description |
| 2026-11-26 04:33:18 | [Pernix.OutboxRelay.Outbox.PostgreSql](https://www.nuget.org/packages/Pernix.OutboxRelay.Outbox.PostgreSql) | 1.0.0 | Pernix | Package Description |
| 2026-11-26 04:35:38 | [AI.Sentinel.Codex.Cli](https://www.nuget.org/packages/AI.Sentinel.Codex.Cli) | 6.1.0 | Marcel Roozekrans | Codex CLI hook command for AI.Sentinel — wire into hooks.json or config.toml to… |
| 2026-11-26 04:38:21 | [Pernix.OutboxRelay.Client](https://www.nuget.org/packages/Pernix.OutboxRelay.Client) | 1.0.0 | Pernix | Engine-neutral producer types for the Pernix Outbox Relay: outbox message, head… |
| 2026-11-26 04:38:22 | [Pernix.OutboxRelay.Client.EntityFrameworkCore](https://www.nuget.org/packages/Pernix.OutboxRelay.Client.EntityFrameworkCore) | 1.0.0 | Pernix | Entity Framework Core add-on for the Pernix Outbox Relay client: enqueues outbo… |
| 2026-11-26 04:38:23 | [Pernix.OutboxRelay.Client.PostgreSql](https://www.nuget.org/packages/Pernix.OutboxRelay.Client.PostgreSql) | 1.0.0 | Pernix | PostgreSQL producer for the Pernix Outbox Relay: publishes outbox rows inside t… |
| 2026-11-26 04:42:15 | [JQLite](https://www.nuget.org/packages/JQLite) | 1.0.0-beta | Daniel Cazzulino | A .NET implementation of the jq filter language for querying and transforming J… |
| 2026-11-26 04:46:32 | [Kanject.Core.Realtime.Annotations](https://www.nuget.org/packages/Kanject.Core.Realtime.Annotations) | 1.0.0 | Akinsanya Omogbolahan | Roslyn analyzers for Kanject Core realtime (proposal 0067): a constant passed a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
