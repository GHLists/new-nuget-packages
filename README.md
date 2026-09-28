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

## Latest list — 2026-09-28 07:22 UTC

New packages created between 2026-09-28 06:19 UTC and 2026-09-28 07:22 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T07-22-47-833229Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 06:42:28 | [RainPointClient](https://www.nuget.org/packages/RainPointClient) | 1.0.0 | Neil Colvin | A typed RainPoint Home / Smart+ cloud client. |
| 2026-09-28 06:50:09 | [Universal.Typesense.Client](https://www.nuget.org/packages/Universal.Typesense.Client) | 1.0.0 | Andrew Ong | Client for the Typesense v30 HTTP API. |
| 2026-09-28 07:00:19 | [LggNet.Common](https://www.nuget.org/packages/LggNet.Common) | 1.0.1 | lggnet | Common utilities library (renamed from A3Common). Namespaces remain A3Common fo… |
| 2026-09-28 07:15:57 | [Universal.Search](https://www.nuget.org/packages/Universal.Search) | 1.0.0 | Andrew Ong | Provider-neutral query abstractions for search services. |
| 2026-09-28 07:16:08 | [Universal.Search.AzureAISearch](https://www.nuget.org/packages/Universal.Search.AzureAISearch) | 1.0.0 | Andrew Ong | Azure AI Search provider for Universal.Search. |
| 2026-09-28 07:16:20 | [Universal.Search.InMemory](https://www.nuget.org/packages/Universal.Search.InMemory) | 1.0.0 | Andrew Ong | In-memory search provider for Universal.Search. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
