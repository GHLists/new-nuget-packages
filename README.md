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

## Latest list — 2026-11-13 08:18 UTC

New packages created between 2026-11-13 07:19 UTC and 2026-11-13 08:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T08-18-49-092995Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 07:27:20 | [MediaPipeTasksDecision.Android](https://www.nuget.org/packages/MediaPipeTasksDecision.Android) | 1.2.0 | Howard Good | Android .NET bindings for MediaPipe Tasks Decision Library. |
| 2026-11-13 07:28:22 | [MediaPipeTasksRetrieval.Android](https://www.nuget.org/packages/MediaPipeTasksRetrieval.Android) | 1.2.0 | Howard Good | Android .NET bindings for MediaPipe Tasks Retrieval Library. |
| 2026-11-13 07:46:50 | [Enhanced.Testing.Component.WireMock](https://www.nuget.org/packages/Enhanced.Testing.Component.WireMock) | 1.4.0 | duskembayev | Enhanced.Testing.Component is a NuGet package that provides a set of tools for… |
| 2026-11-13 07:46:53 | [Enhanced.Testing.Component.Time](https://www.nuget.org/packages/Enhanced.Testing.Component.Time) | 1.4.0 | duskembayev | Enhanced.Testing.Component is a NuGet package that provides a set of tools for… |
| 2026-11-13 07:49:46 | [AbpAgent.Graphiti](https://www.nuget.org/packages/AbpAgent.Graphiti) | 0.4.0 | AbpAgent contributors | AbpAgent.Graphiti: agents' memory as a temporal knowledge graph, with graphiti-… |
| 2026-11-13 07:55:05 | [Flowbyte.Secrets](https://www.nuget.org/packages/Flowbyte.Secrets) | 1.0.1 | Flowbyte | Client and Microsoft.Extensions.Configuration provider for the Flowbyte Secrets… |
| 2026-11-13 07:55:07 | [Flowbyte.Secrets.Cli](https://www.nuget.org/packages/Flowbyte.Secrets.Cli) | 1.0.1 | Flowbyte | fbs — command-line client for Flowbyte Secrets (list/get/set/delete/export secr… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
