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

## Latest list — 2026-10-03 18:20 UTC

New packages created between 2026-10-03 17:19 UTC and 2026-10-03 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T18-20-21-885895Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 17:22:55 | [McpSpan](https://www.nuget.org/packages/McpSpan) | 0.1.0 | Kacper Zatoń | Self-hosted analytics for MCP servers: which tools, resources and prompts get u… |
| 2026-10-03 17:30:30 | [DaffyDuo](https://www.nuget.org/packages/DaffyDuo) | 0.1.0 | TroBeeOne LLC | A SQL Server gateway that gives one client connection up to three SQL Server co… |
| 2026-10-03 17:33:28 | [SourceGenMediator.Abstractions](https://www.nuget.org/packages/SourceGenMediator.Abstractions) | 1.0.0 | Ramesh Kumar | Public contracts for SourceGenMediator: requests, commands, queries, notificati… |
| 2026-10-03 17:33:29 | [SourceGenMediator](https://www.nuget.org/packages/SourceGenMediator) | 1.0.0 | Ramesh Kumar | Compile-time, reflection-free, NativeAOT-safe mediator. Install this package to… |
| 2026-10-03 17:33:29 | [SourceGenMediator.Generator](https://www.nuget.org/packages/SourceGenMediator.Generator) | 1.0.0 | Ramesh Kumar | Roslyn source generator for SourceGenMediator: discovers handlers and emits the… |
| 2026-10-03 17:33:29 | [SourceGenMediator.DependencyInjection](https://www.nuget.org/packages/SourceGenMediator.DependencyInjection) | 1.0.0 | Ramesh Kumar | Dependency-injection integration for SourceGenMediator (Microsoft.Extensions.De… |
| 2026-10-03 17:33:30 | [SourceGenMediator.Runtime](https://www.nuget.org/packages/SourceGenMediator.Runtime) | 1.0.0 | Ramesh Kumar | AOT-safe runtime for SourceGenMediator: generated-dispatch mediator and notific… |
| 2026-10-03 17:55:05 | [ManagedCode.Storage.Cartograph](https://www.nuget.org/packages/ManagedCode.Storage.Cartograph) | 10.0.15 | ManagedCode | Read-only Storage provider for files inside Cartograph artifacts. |
| 2026-10-03 18:03:29 | [Benten.PassCode](https://www.nuget.org/packages/Benten.PassCode) | 1.0.0 | Huzefa Karachiwala | Benten's native passcode engine for .NET, part of the Benten Authentication and… |
| 2026-10-03 18:13:46 | [Humanizexternity](https://www.nuget.org/packages/Humanizexternity) | 0.1.0 | Eduardo Zitinho | Humanize any measure. 1024 MB to 1 GB. 1500 g to 1.5 kg. 3661 s to 1 h 1 min 1… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
