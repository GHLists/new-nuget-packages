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

## Latest list — 2026-10-27 14:20 UTC

New packages created between 2026-10-27 13:21 UTC and 2026-10-27 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T14-20-35-143222Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 13:42:23 | [Bitwarden.Server.Sdk.RestrictedDependencies](https://www.nuget.org/packages/Bitwarden.Server.Sdk.RestrictedDependencies) | 0.1.0 | Bitwarden Inc. | Roslyn analyzer that budgets the use of types marked [RestrictedDependency]: ev… |
| 2026-10-27 13:50:55 | [Rocket.Surgery.ApiReference](https://www.nuget.org/packages/Rocket.Surgery.ApiReference) | 0.1.13 | David Driscoll,Rocket Surgeon… | Generates the JSON that the docs sites render their C# API reference from, usin… |
| 2026-10-27 13:53:46 | [Primus.AutoMapping](https://www.nuget.org/packages/Primus.AutoMapping) | 1.0.0 | Primus | High-performance object-to-object mapper for .NET with an AutoMapper-style API,… |
| 2026-10-27 13:55:03 | [OptimaJet.Workflow.Api.Forms](https://www.nuget.org/packages/OptimaJet.Workflow.Api.Forms) | 23.0.0 | Optimajet Limited | Workflow Forms integration for Workflow Engine API by Optimajet. Registers Form… |
| 2026-10-27 13:55:06 | [OptimaJet.Workflow.Api.RealTimeTrackingPlugin](https://www.nuget.org/packages/OptimaJet.Workflow.Api.RealTimeTrackingPlugin) | 23.0.0 | Optimajet Limited | Adds tenant-aware SignalR process tracking to the Workflow Engine HTTP API, usi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
