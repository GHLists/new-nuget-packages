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

## Latest list — 2026-11-18 18:21 UTC

New packages created between 2026-11-18 17:20 UTC and 2026-11-18 18:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T18-21-53-256666Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 17:28:38 | [Synthigy](https://www.nuget.org/packages/Synthigy) | 0.4.0 | Robert Geršak | Client for Synthigy's /data endpoint. |
| 2026-11-18 17:28:39 | [Synthigy.Gen](https://www.nuget.org/packages/Synthigy.Gen) | 0.4.0 | Robert Geršak | Generates typed C# from .xsql files against a Synthigy engine. |
| 2026-11-18 17:29:47 | [FunnySharp](https://www.nuget.org/packages/FunnySharp) | 0.2.0 | FunnySharp contributors | Pragmatic, BCL-first functional programming for modern C#. |
| 2026-11-18 17:29:48 | [FunnySharp.AspNetCore](https://www.nuget.org/packages/FunnySharp.AspNetCore) | 0.2.0 | FunnySharp contributors | Explicit ASP.NET Core result mapping for FunnySharp outcomes and effects. |
| 2026-11-18 17:37:32 | [CxO.Workers](https://www.nuget.org/packages/CxO.Workers) | 0.1.0 | Codaxy | Helpers for ConductorSharp workers that run CxO order stages. Today: the tempor… |
| 2026-11-18 17:56:31 | [Metalama.Framework.Implementation.5.12.0](https://www.nuget.org/packages/Metalama.Framework.Implementation.5.12.0) | 2027.0.7-preview | PostSharp Technologies and co… | The implementation assemblies of Metalama.Framework for Roslyn 5.12.0. This pac… |
| 2026-11-18 17:56:42 | [Metalama.Introspection.Navigation](https://www.nuget.org/packages/Metalama.Introspection.Navigation) | 2027.0.7-preview | PostSharp Technologies and co… | Walks objects of the Metalama code model and introspection API, summarizes them… |
| 2026-11-18 17:56:51 | [Metalama.Mcp](https://www.nuget.org/packages/Metalama.Mcp) | 2027.0.7-preview | PostSharp Technologies and co… | A local Model Context Protocol server that lets coding agents load C# projects… |
| 2026-11-18 18:03:52 | [strand](https://www.nuget.org/packages/strand) | 0.0.1 | strand | Package Description |
| 2026-11-18 18:11:30 | [StrandSystem.Strand.Rules](https://www.nuget.org/packages/StrandSystem.Strand.Rules) | 0.0.1 | StrandSystem.Strand.Rules | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
