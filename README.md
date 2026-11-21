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

## Latest list — 2026-11-21 00:19 UTC

New packages created between 2026-11-20 23:21 UTC and 2026-11-21 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T00-19-05-797367Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 23:38:35 | [HsnSoft.Base.Concurrency.EventBus](https://www.nuget.org/packages/HsnSoft.Base.Concurrency.EventBus) | 2026.11.0 | HsnSoft | A place of a concurrency limit travels with an event: an endpoint takes it and… |
| 2026-11-20 23:43:39 | [MTConnect.NET-AgentModule-HaasAdapter](https://www.nuget.org/packages/MTConnect.NET-AgentModule-HaasAdapter) | 7.2.0.103-prerelease | TrakHound | MTConnect.NET-AgentModule-HaasAdapter reads data from Haas CNC machines over Et… |
| 2026-11-20 23:43:40 | [MTConnect.NET-AgentModule-TormachAdapter](https://www.nuget.org/packages/MTConnect.NET-AgentModule-TormachAdapter) | 7.2.0.103-prerelease | TrakHound | MTConnect.NET-AgentModule-TormachAdapter reads data from Tormach PathPilot (Lin… |
| 2026-11-20 23:43:41 | [MTConnect.NET-AgentModule-FanucAdapter](https://www.nuget.org/packages/MTConnect.NET-AgentModule-FanucAdapter) | 7.2.0.103-prerelease | TrakHound | MTConnect.NET-AgentModule-FanucAdapter reads data from Fanuc CNC controls using… |
| 2026-11-20 23:43:47 | [MTConnect.NET-AgentModule-WebUI](https://www.nuget.org/packages/MTConnect.NET-AgentModule-WebUI) | 7.2.0.103-prerelease | TrakHound | MTConnect.NET-AgentModule-WebUI hosts a lightweight browser user interface for… |
| 2026-11-20 23:52:32 | [SOU.Live.Contracts](https://www.nuget.org/packages/SOU.Live.Contracts) | 0.3.0 | sofc | Read-only sOU HUD API v2 and v3 game, managed match and panel contracts. |
| 2026-11-20 23:52:33 | [SOU.Hud.Sdk](https://www.nuget.org/packages/SOU.Hud.Sdk) | 0.3.0 | sofc | Local sOU HUD v2 and v3 browser client for Blazor WebAssembly. |
| 2026-11-20 23:52:34 | [SOU.Hud.Sdk.Blazor](https://www.nuget.org/packages/SOU.Hud.Sdk.Blazor) | 0.3.0 | sofc | Official Blazor adapter for the sOU HUD SDK v3 runtime. |
| 2026-11-20 23:52:35 | [SOU.Hud.Tool](https://www.nuget.org/packages/SOU.Hud.Tool) | 0.3.0 | sofc | Create, preview with synthetic data, validate and package standalone sOU HUDs. |
| 2026-11-20 23:52:36 | [SOU.Hud.Templates](https://www.nuget.org/packages/SOU.Hud.Templates) | 0.3.0 | sofc | Standalone sOU HUD starter projects for HTML/JavaScript and Blazor WebAssembly. |
| 2026-11-20 23:54:10 | [Fuaran.Compute.Elementary](https://www.nuget.org/packages/Fuaran.Compute.Elementary) | 0.45.0 | Andrew J. Willshire | Fuaran.Compute.Elementary — the scalar pinned mathematics at the bottom of Fuar… |
| 2026-11-20 23:54:10 | [Fuaran.Compute.PipelineTree](https://www.nuget.org/packages/Fuaran.Compute.PipelineTree) | 0.45.0 | Andrew J. Willshire | Fuaran.Compute.PipelineTree — a Transform pipeline as a Fuaran.Core tree, edite… |
| 2026-11-20 23:54:11 | [Fuaran.Compute.Solvers](https://www.nuget.org/packages/Fuaran.Compute.Solvers) | 0.45.0 | Andrew J. Willshire | Fuaran.Compute.Solvers — pinned root finding, one-dimensional minimisation and… |
| 2026-11-20 23:54:11 | [Fuaran.Compute.Distributions](https://www.nuget.org/packages/Fuaran.Compute.Distributions) | 0.45.0 | Andrew J. Willshire | Fuaran.Compute.Distributions — pinned probability distributions: the cumulative… |
| 2026-11-20 23:54:12 | [Fuaran.Compute.Regression](https://www.nuget.org/packages/Fuaran.Compute.Regression) | 0.45.0 | Andrew J. Willshire | Fuaran.Compute.Regression — regression modelling over the pinned matrix operati… |
| 2026-11-20 23:58:57 | [ServiceResult.Http](https://www.nuget.org/packages/ServiceResult.Http) | 1.0.0 | Yunus Emre Arıtürk | Lightweight, zero-dependency Result<T> wrapper for .NET, WCF, Web API, and ASP.… |
| 2026-11-21 00:04:48 | [TuyaLan](https://www.nuget.org/packages/TuyaLan) | 2.0.0 | Puneet Swarup | Tuya LAN protocol (3.3 / 3.4 / 3.5) and Tuya Cloud API client for .NET. Discove… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
