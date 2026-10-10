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

## Latest list — 2026-10-10 07:20 UTC

New packages created between 2026-10-10 06:18 UTC and 2026-10-10 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T07-20-10-317754Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 06:21:31 | [UO.Graphs.Cli](https://www.nuget.org/packages/UO.Graphs.Cli) | 0.9.0 | UO.Graphs contributors | Local C# evidence graph CLI; requires a prepared .NET SDK and explicit MSBuild… |
| 2026-10-10 06:35:11 | [Singleton.Godot](https://www.nuget.org/packages/Singleton.Godot) | 1.0.0 | Gatongone | Build a singleton in Godot without a base type: a partial class, an attribute,… |
| 2026-10-10 07:09:52 | [SinkSharp.Enrichers.Azure](https://www.nuget.org/packages/SinkSharp.Enrichers.Azure) | 1.0.0 | SinkSharp | Azure context enricher for SinkSharp. Stamps region, resource group, deployment… |
| 2026-10-10 07:11:29 | [Bielu.AspNetCore.AsyncApi.Wolverine](https://www.nuget.org/packages/Bielu.AspNetCore.AsyncApi.Wolverine) | 1.1.0 | Arkadiusz Biel | Wolverine integration for Bielu.AspNetCore.AsyncApi. Builds AsyncAPI channels,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
