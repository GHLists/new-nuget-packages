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

## Latest list — 2026-10-10 22:20 UTC

New packages created between 2026-10-10 21:20 UTC and 2026-10-10 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T22-20-50-124593Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 21:47:37 | [ParallelGpu](https://www.nuget.org/packages/ParallelGpu) | 0.1.0 | Valery Asiryan | Typed GPU parallel loops with automatic lambda compilation and collection trans… |
| 2026-10-10 21:50:31 | [CShells.Nuplane](https://www.nuget.org/packages/CShells.Nuplane) | 0.0.30 | Sipke Schoorstra | Optional integration that discovers loaded Nuplane package features and refresh… |
| 2026-10-10 21:52:24 | [Cogito.MassTransit.Scheduler.Hangfire](https://www.nuget.org/packages/Cogito.MassTransit.Scheduler.Hangfire) | 3.0.0 | Alethic Solutions | Publishes MassTransit periodic messages on a schedule kept by Hangfire. |
| 2026-10-10 21:52:24 | [Cogito.MassTransit.Scheduler.Quartz](https://www.nuget.org/packages/Cogito.MassTransit.Scheduler.Quartz) | 3.0.0 | Alethic Solutions | Publishes MassTransit periodic messages on a schedule kept by Quartz. |
| 2026-10-10 22:03:19 | [FormEventExplorer](https://www.nuget.org/packages/FormEventExplorer) | 1.0.0 | Sushant-Salunkhe | Inspect main form events, field OnChange handlers and business rules. |
| 2026-10-10 22:04:37 | [RoguelikeToolkit.StateMachine](https://www.nuget.org/packages/RoguelikeToolkit.StateMachine) | 0.4.0 | RoguelikeToolkit Contributors | Finite state machine with shared context, guards, entry/exit actions, and trans… |
| 2026-10-10 22:06:06 | [Lustral.Api](https://www.nuget.org/packages/Lustral.Api) | 0.1.0 | Lustral Team | The public API for Lustral mods. |
| 2026-10-10 22:06:07 | [Lustral.Sdk](https://www.nuget.org/packages/Lustral.Sdk) | 0.1.0 | Lustral Team | MSBuild SDK for Lustral mods. Locates the game, references its assemblies, gene… |
| 2026-10-10 22:06:08 | [Lustral.Templates](https://www.nuget.org/packages/Lustral.Templates) | 0.1.0 | Lustral Team | Project templates for Lustral mods. Usage: dotnet new lustral-mod --game "Game… |
| 2026-10-10 22:14:30 | [RoguelikeToolkit.EventAggregator](https://www.nuget.org/packages/RoguelikeToolkit.EventAggregator) | 0.3.0 | RoguelikeToolkit Contributors | Lightweight synchronous in-process event aggregator (publish/subscribe messagin… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
