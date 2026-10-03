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

## Latest list — 2026-10-03 22:19 UTC

New packages created between 2026-10-03 21:18 UTC and 2026-10-03 22:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T22-19-27-512068Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 21:20:41 | [Syntrony.Web](https://www.nuget.org/packages/Syntrony.Web) | 1.0.0 | Syntrony Technologies Inc. | Base template for Syntrony nuget packages |
| 2026-10-03 21:25:19 | [SSRS2.Mcp](https://www.nuget.org/packages/SSRS2.Mcp) | 1.3.0 | SSRS2 | Tools for AI coding agents working on RDLC and RDL reports: validate_report che… |
| 2026-10-03 21:28:39 | [TemplateMaster.Contracts](https://www.nuget.org/packages/TemplateMaster.Contracts) | 1.0.207 | TemplateMaster | TemplateMaster data contracts (DTOs). Dependency of TemplateMaster.AspNetCore. |
| 2026-10-03 21:28:39 | [TemplateMaster.Persistence.SqlServer](https://www.nuget.org/packages/TemplateMaster.Persistence.SqlServer) | 1.0.207 | TemplateMaster | TemplateMaster EF Core model (SQL Server). Dependency of TemplateMaster.AspNetC… |
| 2026-10-03 21:28:40 | [TemplateMaster.Licensing](https://www.nuget.org/packages/TemplateMaster.Licensing) | 1.0.207 | TemplateMaster | TemplateMaster license validation. Dependency of TemplateMaster.AspNetCore. |
| 2026-10-03 21:28:41 | [TemplateMaster.DocumentGeneration](https://www.nuget.org/packages/TemplateMaster.DocumentGeneration) | 1.0.207 | TemplateMaster | TemplateMaster PDF generation (Puppeteer Sharp, WeasyPrint, iText). Dependency… |
| 2026-10-03 21:28:44 | [TemplateMaster.AspNetCore](https://www.nuget.org/packages/TemplateMaster.AspNetCore) | 1.0.207 | TemplateMaster | Embed TemplateMaster (visual document/email template editor, PDF and email gene… |
| 2026-10-03 21:28:45 | [TemplateMaster.Domain](https://www.nuget.org/packages/TemplateMaster.Domain) | 1.0.207 | TemplateMaster | TemplateMaster business layer (CQRS commands/queries, rendering, e-mails, stora… |
| 2026-10-03 21:44:22 | [Alethic.AspNet.Optimization.Rollup](https://www.nuget.org/packages/Alethic.AspNet.Optimization.Rollup) | 1.0.0 | Jerome Haltom | System.Web.Optimization bundles built by Rollup, Sass, SWC, Terser and Lightnin… |
| 2026-10-03 21:47:14 | [TheHive.Api](https://www.nuget.org/packages/TheHive.Api) | 5.8.9 | Panoramic Data Limited | .NET 10 client for the TheHive 5 REST API. |
| 2026-10-03 21:55:58 | [MudShadcn](https://www.nuget.org/packages/MudShadcn) | 1.0.0 | Sardar Qaslany | The shadcn/ui look for every MudBlazor component, charts included: a MudTheme a… |
| 2026-10-03 21:56:04 | [UO.Analyzers](https://www.nuget.org/packages/UO.Analyzers) | 1.0.0 | uozturk | Company Roslyn analyzers, code fixes and refactorings. Includes a CA1848 source… |
| 2026-10-03 21:57:44 | [Patware.Pipeline.Core](https://www.nuget.org/packages/Patware.Pipeline.Core) | 0.1.0 | Patware | Build composable, typed workflow graphs for .NET with dependencies, conditions,… |
| 2026-10-03 22:12:20 | [Patware.Pipeline.Runtime](https://www.nuget.org/packages/Patware.Pipeline.Runtime) | 0.1.0 | Patware | The runtime for the composable pipeline library for .NET. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
