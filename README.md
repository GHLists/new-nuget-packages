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

## Latest list — 2026-10-29 20:19 UTC

New packages created between 2026-10-29 19:20 UTC and 2026-10-29 20:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T20-19-49-334921Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 19:22:42 | [Whoopi](https://www.nuget.org/packages/Whoopi) | 12.3.0 | William Farokhzad and Whoopi… | Whoopi (https://whoopi.dev) is a next-generation cross-platform UI framework an… |
| 2026-10-29 19:39:36 | [VirtualADGV.Core](https://www.nuget.org/packages/VirtualADGV.Core) | 2.0.0 | HibrahimBoz | UI-independent virtual table sources, minimap model, row search and ordinal sel… |
| 2026-10-29 19:44:59 | [Soenneker.Incident.HttpClients](https://www.nuget.org/packages/Soenneker.Incident.HttpClients) | 11.0.1 | Jake Soenneker | A thread-safe singleton HttpClient for Incident's OpenAPI integration. |
| 2026-10-29 19:45:12 | [Soenneker.Incident.OpenApiClient](https://www.nuget.org/packages/Soenneker.Incident.OpenApiClient) | 11.0.1 | Jake Soenneker | A generated OpenAPI client for incident.io. |
| 2026-10-29 19:56:05 | [LlamaLogic.TuningArchive](https://www.nuget.org/packages/LlamaLogic.TuningArchive) | 1.0.3 | LlamaLogic | Capture The Sims 4 tuning into a versioned archive, compare versions, and follo… |
| 2026-10-29 20:03:10 | [ArcadeShare](https://www.nuget.org/packages/ArcadeShare) | 3.0.0 | La_TNT | Bibliothèque .NET pour créer des salles de partage et de synchronisation audio… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
