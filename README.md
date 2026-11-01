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

## Latest list — 2026-11-01 17:20 UTC

New packages created between 2026-11-01 16:20 UTC and 2026-11-01 17:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T17-20-04-806338Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 16:35:04 | [Terp.Akka](https://www.nuget.org/packages/Terp.Akka) | 0.1.0 | st0o0 | Akka.NET helpers built on Akka.Hosting. |
| 2026-11-01 16:35:05 | [Terp](https://www.nuget.org/packages/Terp) | 0.1.0 | st0o0 | Foundation helpers for .NET apps: host setups, startup gates, diagnostics, resi… |
| 2026-11-01 16:37:51 | [Kappie.Core.Pipelines](https://www.nuget.org/packages/Kappie.Core.Pipelines) | 1.2.16 | Kamil Pietraszko | Provides multi-step pipeline orchestration, short-circuit execution, and cross-… |
| 2026-11-01 16:40:03 | [Infrastructure.Foundation](https://www.nuget.org/packages/Infrastructure.Foundation) | 1.0.0 | Sukhov A.A. | The package providing core MVVM components for WPF applications. Includes reusa… |
| 2026-11-01 16:45:04 | [Serde.FS](https://www.nuget.org/packages/Serde.FS) | 1.0.0 | Jordan Marr | Strict, deterministic serialization core for F#. Provides the [Serde] attribute… |
| 2026-11-01 16:45:05 | [Serde.FS.AspNet](https://www.nuget.org/packages/Serde.FS.AspNet) | 1.0.0 | Jordan Marr | ASP.NET Core integration for Serde.FS RPC. Provides MapRpcApi extension for rou… |
| 2026-11-01 16:45:07 | [Serde.FS.Fable](https://www.nuget.org/packages/Serde.FS.Fable) | 1.0.0 | Jordan Marr | Fable client generator for Serde.FS RPC. Install on a Fable client project to a… |
| 2026-11-01 16:45:08 | [Serde.FS.Json](https://www.nuget.org/packages/Serde.FS.Json) | 1.0.0 | Jordan Marr | High‑performance JSON backend for Serde.FS. Uses generated serializers—no refle… |
| 2026-11-01 16:50:27 | [FIAP.TechChallenge.OS.Application.Messaging](https://www.nuget.org/packages/FIAP.TechChallenge.OS.Application.Messaging) | 0.1.0 | João Victor Maieru Teixeira | Integration message contracts published by the OS service. |
| 2026-11-01 17:11:38 | [TWebApi](https://www.nuget.org/packages/TWebApi) | 2.1.52 | TWebApi | 供独立宿主复用的 TouchSocket Web API 统一结果、参数验证与依赖注入桥接。 |
| 2026-11-01 17:11:40 | [TWebApi.Generator](https://www.nuget.org/packages/TWebApi.Generator) | 2.0.53 | TWebApi.Generator | Package Description |
| 2026-11-01 17:12:16 | [TeklaHelper.DrawingNative](https://www.nuget.org/packages/TeklaHelper.DrawingNative) | 1.0.0 | Nguyen Thang | OOP wrapper for the native drawing Plugin API of Tekla Structures (Drawings.dll… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
