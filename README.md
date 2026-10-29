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

## Latest list — 2026-10-29 08:22 UTC

New packages created between 2026-10-29 07:20 UTC and 2026-10-29 08:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T08-22-09-316176Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 07:32:07 | [Didit](https://www.nuget.org/packages/Didit) | 1.0.0 | Didit | The official Didit .NET library: identity verification (KYC), business verifica… |
| 2026-10-29 07:32:09 | [Didit.Extensions.DependencyInjection](https://www.nuget.org/packages/Didit.Extensions.DependencyInjection) | 1.0.0 | Didit | Registers the official Didit .NET client with Microsoft.Extensions.DependencyIn… |
| 2026-10-29 07:33:35 | [MonixOne.OidcProxy.Yarp](https://www.nuget.org/packages/MonixOne.OidcProxy.Yarp) | 7.0.0 | Albert Starreveld,Shulyakovsk… | A .NET 10 Backend-for-Frontend for single-page applications using YARP and stan… |
| 2026-10-29 07:33:52 | [SldFile](https://www.nuget.org/packages/SldFile) | 0.1.0-alpha | weianweigan | A pure C# standalone reader and parser for SolidWorks files (SLDPRT, SLDASM, SL… |
| 2026-10-29 07:56:22 | [NCache.OSS.Dapper](https://www.nuget.org/packages/NCache.OSS.Dapper) | 5.3.603 | Alachisoft | NCache Opensource extension for Dapper providing distributed caching of databas… |
| 2026-10-29 08:14:34 | [Nao.DeveloperTools](https://www.nuget.org/packages/Nao.DeveloperTools) | 1.0.0-alpha1 | jichang | Machine-readable scaffolding, validation, diagnostics, evaluation, and migratio… |
| 2026-10-29 08:14:37 | [Nao.Extensions](https://www.nuget.org/packages/Nao.Extensions) | 1.0.0-alpha1 | jichang | Compiled adapter registration, lifecycle, compatibility, conformance, and isola… |
| 2026-10-29 08:14:40 | [Nao.Knowledge.Documents](https://www.nuget.org/packages/Nao.Knowledge.Documents) | 1.0.0-alpha1 | jichang | Nao.Documents parsing adapters for Nao knowledge ingestion. |
| 2026-10-29 08:14:45 | [Nao.Persistence.Infrastructure](https://www.nuget.org/packages/Nao.Persistence.Infrastructure) | 1.0.0-alpha1 | jichang | Nao AI Agent Framework |
| 2026-10-29 08:14:46 | [Nao.Persistence.Memory](https://www.nuget.org/packages/Nao.Persistence.Memory) | 1.0.0-alpha1 | jichang | Nao AI Agent Framework |
| 2026-10-29 08:14:48 | [Nao.Persistence.Observability](https://www.nuget.org/packages/Nao.Persistence.Observability) | 1.0.0-alpha1 | jichang | Nao AI Agent Framework |
| 2026-10-29 08:14:54 | [Nao.Providers.Ollama](https://www.nuget.org/packages/Nao.Providers.Ollama) | 1.0.0-alpha1 | jichang | Nao AI Agent Framework |
| 2026-10-29 08:14:56 | [Nao.Reasoning](https://www.nuget.org/packages/Nao.Reasoning) | 1.0.0-alpha1 | jichang | Nao AI Agent Framework |
| 2026-10-29 08:14:59 | [Nao.Reasoning.Constraints](https://www.nuget.org/packages/Nao.Reasoning.Constraints) | 1.0.0-alpha1 | jichang | Nao AI Agent Framework |
| 2026-10-29 08:15:00 | [Nao.Reasoning.Datalog](https://www.nuget.org/packages/Nao.Reasoning.Datalog) | 1.0.0-alpha1 | jichang | Nao AI Agent Framework |
| 2026-10-29 08:15:02 | [Nao.Semantics](https://www.nuget.org/packages/Nao.Semantics) | 1.0.0-alpha1 | jichang | Nao AI Agent Framework |
| 2026-10-29 08:15:03 | [Nao.Semantics.Rdf](https://www.nuget.org/packages/Nao.Semantics.Rdf) | 1.0.0-alpha1 | jichang | Nao AI Agent Framework |
| 2026-10-29 08:15:04 | [Nao.Telemetry.OpenTelemetry](https://www.nuget.org/packages/Nao.Telemetry.OpenTelemetry) | 1.0.0-alpha1 | jichang | Nao AI Agent Framework |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
