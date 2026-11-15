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

## Latest list — 2026-11-15 19:20 UTC

New packages created between 2026-11-15 18:21 UTC and 2026-11-15 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T19-20-37-327084Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 18:37:12 | [Pipoburgos.SharedKernel.Api.OpenApi](https://www.nuget.org/packages/Pipoburgos.SharedKernel.Api.OpenApi) | 11.0.0.3 | Roberto Fernández Salinas | C# DDD Distributed Services Layer |
| 2026-11-15 18:38:21 | [Nefarius.Utilities.ETW.Relay.CLI](https://www.nuget.org/packages/Nefarius.Utilities.ETW.Relay.CLI) | 3.0.0 | Benjamin Höglinger-Stelzer | Optional companion tool for etwutils: reads raw ETW relay frames from stdin and… |
| 2026-11-15 18:42:32 | [Fable.Ranvier.Wgpu](https://www.nuget.org/packages/Fable.Ranvier.Wgpu) | 0.1.0 | shayanhabibi | The Ranvier.Wgpu 3D scene API for the browser, compiled to JavaScript with Fick… |
| 2026-11-15 18:56:19 | [Migracle.Cli](https://www.nuget.org/packages/Migracle.Cli) | 1.0.0 | Migracle Contributors | CLI Runner for Migracle PostgreSQL Migration & Integrity Engine |
| 2026-11-15 18:56:20 | [Migracle.Core](https://www.nuget.org/packages/Migracle.Core) | 1.0.0 | Migracle Team | Enterprise Database Migration & Integrity Guard for PostgreSQL |
| 2026-11-15 19:01:34 | [GraphEssentialsX](https://www.nuget.org/packages/GraphEssentialsX) | 1.0.0 | Przemyslaw Klys | Typed, capability-first Graph/O365 engine. |
| 2026-11-15 19:01:35 | [GraphEssentialsX.Monitoring](https://www.nuget.org/packages/GraphEssentialsX.Monitoring) | 1.0.0 | Przemyslaw Klys | Caller-invoked Conditional Access evaluation and DbaClientX record-store adapte… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
