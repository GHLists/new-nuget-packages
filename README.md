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

## Latest list — 2026-10-14 22:22 UTC

New packages created between 2026-10-14 21:22 UTC and 2026-10-14 22:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T22-22-37-945463Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 21:25:00 | [Kododo.Reiho.AspNetCore.Mcp](https://www.nuget.org/packages/Kododo.Reiho.AspNetCore.Mcp) | 2.0.0 | Kododo | Offers Reiho requests as tools to AI agents over the Model Context Protocol. |
| 2026-10-14 21:27:04 | [BorrowedTorch.Camera](https://www.nuget.org/packages/BorrowedTorch.Camera) | 1.5.2 | Vladyslav Pysarenko | Camera functionality. |
| 2026-10-14 21:32:00 | [LagomEvent](https://www.nuget.org/packages/LagomEvent) | 1.0.0 | Devseesharp | A lightweight generic event handler with disposable subscriptions for publishin… |
| 2026-10-14 21:34:19 | [Trax.Api.Dashboard](https://www.nuget.org/packages/Trax.Api.Dashboard) | 1.63.1 | Theauxm | The Trax .NET operations dashboard as a single-page app your Trax.Api host serv… |
| 2026-10-14 21:46:17 | [DotCourier.FluentValidation](https://www.nuget.org/packages/DotCourier.FluentValidation) | 0.3.0 | Valossa515 | FluentValidation integration for DotCourier: IValidator<T> runs in the pipeline… |
| 2026-10-14 21:58:24 | [Belin.Which.FSharp](https://www.nuget.org/packages/Belin.Which.FSharp) | 2026.10.0 | CedX | Find the instances of an executable in the system path. Like the `which` Linux… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
