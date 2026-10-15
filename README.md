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

## Latest list — 2026-10-15 23:21 UTC

New packages created between 2026-10-15 22:20 UTC and 2026-10-15 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T23-21-01-283417Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 22:23:45 | [ReportHub.Client](https://www.nuget.org/packages/ReportHub.Client) | 0.1.0 | David Santos | Cliente oficial da API do Report Hub: gera PDF, CSV e Excel a partir de templat… |
| 2026-10-15 22:33:27 | [DynamicDisorder.CliUtils](https://www.nuget.org/packages/DynamicDisorder.CliUtils) | 0.1.0 | dynamic-disorder | Shared console output utilities for CLI applications: colored output helpers, S… |
| 2026-10-15 22:58:55 | [PulseTrade.Comm.Spa.Host.ProcControl.Client](https://www.nuget.org/packages/PulseTrade.Comm.Spa.Host.ProcControl.Client) | 0.1.0-alpha3 | PulseTrade.Comm.Spa.Host.Proc… | Package Description |
| 2026-10-15 22:59:24 | [WolverineFx.Pubsub.Http](https://www.nuget.org/packages/WolverineFx.Pubsub.Http) | 6.51.0 | Jeremy D. Miller,Babu Annamal… | Receive Google Cloud Platform Pub/Sub push subscriptions through Wolverine.HTTP… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
