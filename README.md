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

## Latest list — 2026-10-17 10:20 UTC

New packages created between 2026-10-17 09:20 UTC and 2026-10-17 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T10-20-58-277084Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 09:20:55 | [MisarPost](https://www.nuget.org/packages/MisarPost) | 1.0.0 | Misar.AI | .NET client for MisarPost's social publishing API: schedule and publish posts a… |
| 2026-10-17 09:36:01 | [Micser.Audio](https://www.nuget.org/packages/Micser.Audio) | 0.19.0 | Lucas Loreggia | The plugin SDK of Micser, an audio router for Windows and Linux: audio modules,… |
| 2026-10-17 09:50:06 | [TraceX.AspNetCore](https://www.nuget.org/packages/TraceX.AspNetCore) | 1.0.1 | TraceX | Official TraceX ASP.NET Core middleware and exception boundary SDK for real-tim… |
| 2026-10-17 09:50:07 | [TraceX.Core](https://www.nuget.org/packages/TraceX.Core) | 1.0.1 | TraceX | Core client and protocol engine for TraceX telemetry, exception tracking, and c… |
| 2026-10-17 09:55:53 | [monosmith.osx-x64](https://www.nuget.org/packages/monosmith.osx-x64) | 1.3.1 | monosmith-app | Runs a monorepo in Node, Go and Python: tasks from a cache, CI and releases |
| 2026-10-17 09:55:54 | [monosmith.osx-arm64](https://www.nuget.org/packages/monosmith.osx-arm64) | 1.3.1 | monosmith-app | Runs a monorepo in Node, Go and Python: tasks from a cache, CI and releases |
| 2026-10-17 09:55:54 | [monosmith.linux-x64](https://www.nuget.org/packages/monosmith.linux-x64) | 1.3.1 | monosmith-app | Runs a monorepo in Node, Go and Python: tasks from a cache, CI and releases |
| 2026-10-17 09:55:55 | [monosmith.linux-arm64](https://www.nuget.org/packages/monosmith.linux-arm64) | 1.3.1 | monosmith-app | Runs a monorepo in Node, Go and Python: tasks from a cache, CI and releases |
| 2026-10-17 09:55:56 | [monosmith.win-x64](https://www.nuget.org/packages/monosmith.win-x64) | 1.3.1 | monosmith-app | Runs a monorepo in Node, Go and Python: tasks from a cache, CI and releases |
| 2026-10-17 09:55:56 | [monosmith.win-arm64](https://www.nuget.org/packages/monosmith.win-arm64) | 1.3.1 | monosmith-app | Runs a monorepo in Node, Go and Python: tasks from a cache, CI and releases |
| 2026-10-17 09:55:57 | [monosmith](https://www.nuget.org/packages/monosmith) | 1.3.1 | monosmith-app | Runs a monorepo in Node, Go and Python: tasks from a cache, CI and releases |
| 2026-10-17 10:00:47 | [Arc56.Generated.algorandfoundation.algosdk-future-ts](https://www.nuget.org/packages/Arc56.Generated.algorandfoundation.algosdk-future-ts) | 1.0.1.2026101709 | algorandfoundation | Generated ARC-56 Algorand smart-contract clients for algorandfoundation/algosdk… |
| 2026-10-17 10:01:56 | [Hua.Sort](https://www.nuget.org/packages/Hua.Sort) | 1.0.0 | isHuaMouRen | C# implementation of various sorting algorithms |
| 2026-10-17 10:15:48 | [MadeIt.PixelArt](https://www.nuget.org/packages/MadeIt.PixelArt) | 0.1.0 | TamKungZ_ <dev@tamkungz.me> | Managed .NET binding for the madeitpx pixel-art image conversion library. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
