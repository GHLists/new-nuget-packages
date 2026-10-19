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

## Latest list — 2026-10-19 22:22 UTC

New packages created between 2026-10-19 21:19 UTC and 2026-10-19 22:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T22-22-41-616681Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 21:22:39 | [CodeBinder.CLang.Sdk](https://www.nuget.org/packages/CodeBinder.CLang.Sdk) | 0.1.0 | CodeBinder.CLang | CodeBinder .NET SDK for native API wrapper generation |
| 2026-10-19 21:24:02 | [PersonalUI.Blazor](https://www.nuget.org/packages/PersonalUI.Blazor) | 1.0.0 | Andreas Liepins Krusager | Custom tactile dark-mode UI library for Blazor: windows, 3D buttons, inputs, mo… |
| 2026-10-19 21:27:43 | [Trellis.AgentDocs.Packaging](https://www.nuget.org/packages/Trellis.AgentDocs.Packaging) | 1.0.2 | Xavier John | Build-only helper for packing versioned coding-agent documentation into NuGet p… |
| 2026-10-19 21:27:44 | [Trellis.AgentDocs](https://www.nuget.org/packages/Trellis.AgentDocs) | 1.0.2 | Xavier John | Opt-in repository installer for versioned NuGet package guidance for coding age… |
| 2026-10-19 21:30:29 | [GameHost.Keys](https://www.nuget.org/packages/GameHost.Keys) | 0.0.109 | Maksim Shimshon | Core Package for Lunatic Panel's PLugin |
| 2026-10-19 21:42:04 | [Programaris.Tenancy.Abstractions](https://www.nuget.org/packages/Programaris.Tenancy.Abstractions) | 0.1.0 | PROGRAMARIS | Public tenant context contracts for PROGRAMARIS integration clients. |
| 2026-10-19 21:48:34 | [JJConsulting.DbUp](https://www.nuget.org/packages/JJConsulting.DbUp) | 1.0.0 | JJConsulting | SQL Server migrations and versionable database objects using DbUp and DbUpX. |
| 2026-10-19 21:51:54 | [Trellis.ServiceLevelIndicators](https://www.nuget.org/packages/Trellis.ServiceLevelIndicators) | 10.0.0 | Xavier John | Core library for emitting Service Level Indicator (SLI) latency metrics in mill… |
| 2026-10-19 21:51:54 | [Trellis.ServiceLevelIndicators.Asp](https://www.nuget.org/packages/Trellis.ServiceLevelIndicators.Asp) | 10.0.0 | Xavier John | ASP.NET Core middleware for emitting Service Level Indicator (SLI) latency metr… |
| 2026-10-19 21:51:54 | [Trellis.ServiceLevelIndicators.Asp.ApiVersioning](https://www.nuget.org/packages/Trellis.ServiceLevelIndicators.Asp.ApiVersioning) | 10.0.0 | Xavier John | Adds the resolved API version as the http.api.version SLI dimension when the AS… |
| 2026-10-19 21:56:54 | [Programaris.Tenancy](https://www.nuget.org/packages/Programaris.Tenancy) | 0.1.0 | PROGRAMARIS | Core tenant identifier validation for PROGRAMARIS integrations. |
| 2026-10-19 21:56:55 | [Programaris.Tenancy.AspNetCore](https://www.nuget.org/packages/Programaris.Tenancy.AspNetCore) | 0.1.0 | PROGRAMARIS | ASP.NET Core tenant header selection helpers for PROGRAMARIS integrations. |
| 2026-10-19 21:57:08 | [RazorPlus.AspNetCore](https://www.nuget.org/packages/RazorPlus.AspNetCore) | 0.3.0 | RazorPlus contributors | Explicit Razor model metadata and a TypeScript client runtime. |
| 2026-10-19 22:05:55 | [VpnHood.AppUi.Hosting.Desktop.Abstractions](https://www.nuget.org/packages/VpnHood.AppUi.Hosting.Desktop.Abstractions) | 9.0.856 | VpnHood.AppUi.Hosting.Desktop… | What a desktop host and a desktop UI agree on - IDesktopUi, what the host hands… |
| 2026-10-19 22:07:21 | [CosmicChimps.Aspire.Hosting.Caravana](https://www.nuget.org/packages/CosmicChimps.Aspire.Hosting.Caravana) | 0.1.0 | Cosmic Chimps | Caravana deployment integration for Aspire: `aspire deploy` publishes the AppHo… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
