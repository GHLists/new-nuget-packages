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

## Latest list — 2026-10-20 02:21 UTC

New packages created between 2026-10-20 01:21 UTC and 2026-10-20 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T02-21-55-701423Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 02:00:59 | [RockBot.Llm.Anthropic](https://www.nuget.org/packages/RockBot.Llm.Anthropic) | 0.16.14 | Marimer LLC | Native Anthropic (Claude API) LLM provider for RockBot, with prompt caching, ex… |
| 2026-10-20 02:07:41 | [Cosmos.OpenTelemetry.Functions](https://www.nuget.org/packages/Cosmos.OpenTelemetry.Functions) | 0.1.0 | Cosmos | Configuración OpenTelemetry del worker aislado de Azure Functions para los boun… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
