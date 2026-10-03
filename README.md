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

## Latest list — 2026-10-03 16:21 UTC

New packages created between 2026-10-03 15:19 UTC and 2026-10-03 16:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T16-21-16-694935Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 15:20:21 | [Crossmool.Crypto](https://www.nuget.org/packages/Crossmool.Crypto) | 1.3.1 | crossmool | SM2/SM3/SM4 Chinese national cryptographic algorithm library for .NET |
| 2026-10-03 15:45:48 | [PolyhydraGames.AI.Interfaces](https://www.nuget.org/packages/PolyhydraGames.AI.Interfaces) | 2.0.2 | Polyhydra Games | Shared AI abstraction interfaces for Polyhydra Games. |
| 2026-10-03 15:45:49 | [PolyhydraGames.Ollama](https://www.nuget.org/packages/PolyhydraGames.Ollama) | 2.0.2 | PolyhydraGames.Ollama | Ollama client helpers for Polyhydra Games. |
| 2026-10-03 15:47:06 | [Itminus.FSharpExtensions](https://www.nuget.org/packages/Itminus.FSharpExtensions) | 0.2.3 | Itminus.FSharpExtensions | Package Description |
| 2026-10-03 15:56:59 | [Novolis.Storage.AzureBlob](https://www.nuget.org/packages/Novolis.Storage.AzureBlob) | 2026.1.1.50 | Novolis | Typed JSON blob containers backed by Azure Blob Storage. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
