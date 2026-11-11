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

## Latest list — 2026-11-11 23:21 UTC

New packages created between 2026-11-11 22:21 UTC and 2026-11-11 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T23-21-02-76413Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 22:22:37 | [Mafesoft.RestClient](https://www.nuget.org/packages/Mafesoft.RestClient) | 3.0.0 | Federico Mazzanti | RestClient is a fluent library for .NET that helps you to consume REST services. |
| 2026-11-11 22:22:38 | [Mafesoft.RestClient.Extensions.DependencyInjection](https://www.nuget.org/packages/Mafesoft.RestClient.Extensions.DependencyInjection) | 3.0.0 | Federico Mazzanti | Registers Mafesoft.RestClient builders in the dependency injection container, o… |
| 2026-11-11 22:24:35 | [TenantGuard.Analyzers](https://www.nuget.org/packages/TenantGuard.Analyzers) | 0.1.0 | Jimmy Kurian | Roslyn analyzers that flag IgnoreQueryFilters() and raw SQL without a tenant pr… |
| 2026-11-11 22:24:35 | [TenantGuard.Testing.XunitV3](https://www.nuget.org/packages/TenantGuard.Testing.XunitV3) | 0.1.0 | Jimmy Kurian | xUnit v3 adapter for the TenantGuard isolation probe: each entity type and chec… |
| 2026-11-11 22:24:35 | [TenantGuard.Testing](https://www.nuget.org/packages/TenantGuard.Testing) | 0.1.0 | Jimmy Kurian | Test kit for TenantGuard: a per-entity tenant isolation probe that seeds every… |
| 2026-11-11 22:24:36 | [TenantGuard.EntityFrameworkCore](https://www.nuget.org/packages/TenantGuard.EntityFrameworkCore) | 0.1.0 | Jimmy Kurian | Proves an EF Core multi-tenant model leaks nothing: startup model validation, a… |
| 2026-11-11 22:24:36 | [TenantGuard.Testing.TUnit](https://www.nuget.org/packages/TenantGuard.Testing.TUnit) | 0.1.0 | Jimmy Kurian | TUnit adapter for the TenantGuard isolation probe: each entity type and check i… |
| 2026-11-11 22:24:37 | [TenantGuard.Tool](https://www.nuget.org/packages/TenantGuard.Tool) | 0.1.0 | Jimmy Kurian | dotnet tenantguard validate: runs TenantGuard's model rules on a compiled app's… |
| 2026-11-11 22:27:01 | [Mafesoft.Localization.Extensions](https://www.nuget.org/packages/Mafesoft.Localization.Extensions) | 4.1.0 | Federico Mazzanti | Microsoft.Extensions integration for Mafesoft.Localization: registers the Local… |
| 2026-11-11 22:30:37 | [Stateflows.Extensions.UnionTypes](https://www.nuget.org/packages/Stateflows.Extensions.UnionTypes) | 0.23.0-beta | Stateflows | Package Description |
| 2026-11-11 22:41:57 | [Cratis.Stage.Extensions](https://www.nuget.org/packages/Cratis.Stage.Extensions) | 5.15.0 | Cratis | The C# SDK for Cratis Stage extension backends: implement abilities, inbound HT… |
| 2026-11-11 22:54:20 | [SharpSTUN](https://www.nuget.org/packages/SharpSTUN) | 0.0.1 | Lukas Volf | A STUN client and server written in C#. |
| 2026-11-11 22:54:29 | [SharpTURN](https://www.nuget.org/packages/SharpTURN) | 0.0.1 | Lukas Volf | A TURN client and server written in C#. |
| 2026-11-11 22:54:38 | [SharpICE](https://www.nuget.org/packages/SharpICE) | 0.0.1 | Lukas Volf | ICE (Interactive Connectivity Establishment) written in C#. |
| 2026-11-11 22:56:41 | [Slugger.Core](https://www.nuget.org/packages/Slugger.Core) | 1.0.0 | Reefact | Human-readable random names, Docker- and Heroku-style (humming_dirac, silvery-m… |
| 2026-11-11 23:00:02 | [essentialMix.Data.Entity.Mapster](https://www.nuget.org/packages/essentialMix.Data.Entity.Mapster) | 17.0.16 | asm | Common extensions methods, helper classes, components, nano systems, and common… |
| 2026-11-11 23:09:17 | [ca.whittaker.Diagnostics.HttpRequestLogging](https://www.nuget.org/packages/ca.whittaker.Diagnostics.HttpRequestLogging) | 1.0.0 | Brett Whittaker | Explicit, bounded ASP.NET Core request diagnostics with opt-in JSON body captur… |
| 2026-11-11 23:09:53 | [MsGraphMcpProvider](https://www.nuget.org/packages/MsGraphMcpProvider) | 0.1.3 | gitdonohue | Embeddable, loopback-only Model Context Protocol (MCP) server that exposes Micr… |
| 2026-11-11 23:09:58 | [TwKit.net](https://www.nuget.org/packages/TwKit.net) | 0.1.1 | TwKit | Downloads and runs the Tailwind CSS CLI before Blazor WebAssembly compilation. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
