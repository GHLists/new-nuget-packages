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

## Latest list — 2026-11-13 22:19 UTC

New packages created between 2026-11-13 21:21 UTC and 2026-11-13 22:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T22-19-00-589775Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 21:25:26 | [AzureArtifacts.UniversalPackages.Unofficial](https://www.nuget.org/packages/AzureArtifacts.UniversalPackages.Unofficial) | 0.2.0 | Jeremy Morren | A client for downloading Azure Artifacts Universal Packages over plain HTTP. Un… |
| 2026-11-13 21:33:37 | [PlutoniumBuild](https://www.nuget.org/packages/PlutoniumBuild) | 0.1.0 | Kiryuumaru | Build automation for any repository: declarative test, build, and publish entri… |
| 2026-11-13 21:33:50 | [SB.OpenSearch.Net.Auth.AwsSigV4](https://www.nuget.org/packages/SB.OpenSearch.Net.Auth.AwsSigV4) | 3.0.0 | Stefano Branco | AWS SigV4 authentication handler for the OpenSearch .NET client transport. AI-w… |
| 2026-11-13 21:33:51 | [SB.OpenSearch.Client](https://www.nuget.org/packages/SB.OpenSearch.Client) | 3.0.0 | Stefano Branco | High-level OpenSearch .NET client with fluent query DSL and code-generated type… |
| 2026-11-13 21:33:51 | [SB.OpenSearch.Net](https://www.nuget.org/packages/SB.OpenSearch.Net) | 3.0.0 | Stefano Branco | Low-level transport for OpenSearch .NET clients. AI-written rebuild — not the o… |
| 2026-11-13 21:41:26 | [Fdw.Data.Options](https://www.nuget.org/packages/Fdw.Data.Options) | 1.5.7 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-13 21:41:32 | [Fdw.Data.Options.Abstractions](https://www.nuget.org/packages/Fdw.Data.Options.Abstractions) | 1.5.7 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-13 21:42:53 | [Fdw.Services.Data.Graphs](https://www.nuget.org/packages/Fdw.Services.Data.Graphs) | 1.5.7 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-13 22:01:40 | [BlazorKinetix.Core](https://www.nuget.org/packages/BlazorKinetix.Core) | 1.0.0 | Ivan Kljuce | Shared types and text catalog for BlazorKinetix components. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
