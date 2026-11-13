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

## Latest list — 2026-11-13 19:21 UTC

New packages created between 2026-11-13 18:19 UTC and 2026-11-13 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T19-21-19-07259Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 18:22:19 | [Sondor.Options.FluentValidation](https://www.nuget.org/packages/Sondor.Options.FluentValidation) | 0.1.0 | Sondor Dev | FluentValidation for Sondor.Options: validates options with the IValidator of t… |
| 2026-11-13 18:37:05 | [DevelApp.Self-Evolving-Framework](https://www.nuget.org/packages/DevelApp.Self-Evolving-Framework) | 1.8.0 | DevelApp-ai | Framework primitives for secure LLM-driven code evolution in C#. |
| 2026-11-13 18:38:52 | [Webority.Ai.AzureOpenAi](https://www.nuget.org/packages/Webority.Ai.AzureOpenAi) | 0.59.0 | Webority Technologies | The Azure OpenAI v1 transport for Webority.Ai: agents and embeddings run throug… |
| 2026-11-13 18:45:17 | [AbpGateway](https://www.nuget.org/packages/AbpGateway) | 0.4.0 | AbpCluster contributors | AbpGateway: one origin in front of an ABP site's servers and its web app, on YA… |
| 2026-11-13 19:07:34 | [AbpCluster.Storage](https://www.nuget.org/packages/AbpCluster.Storage) | 0.4.0 | AbpCluster contributors | AbpCluster.Storage: where an ABP app on .NET 10 keeps its files, set by configu… |
| 2026-11-13 19:16:04 | [Redis.Iris.ContextRetriever.Modeling](https://www.nuget.org/packages/Redis.Iris.ContextRetriever.Modeling) | 0.1.1-preview | Redis, Inc. | Annotated POCO modeling, serialization, and comparison for Redis Iris Context R… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
