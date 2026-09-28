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

## Latest list — 2026-09-28 14:25 UTC

New packages created between 2026-09-28 13:23 UTC and 2026-09-28 14:25 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T14-25-22-557129Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 13:25:38 | [Meringue.AvaDock](https://www.nuget.org/packages/Meringue.AvaDock) | 0.1.0 | Scott Kupec | A docking system for Avalonia. |
| 2026-09-28 13:34:57 | [Soenneker.Extensions.Objects.Reflection](https://www.nuget.org/packages/Soenneker.Extensions.Objects.Reflection) | 4.0.5 | Jake Soenneker | Reflection-based object extensions for dictionaries, query strings, logging, an… |
| 2026-09-28 13:43:40 | [JLVisionLib](https://www.nuget.org/packages/JLVisionLib) | 1.0.0 | JLVision | Headless .NET vision library (HALCON-style operators, single managed assembly)… |
| 2026-09-28 13:47:15 | [Bozzis.Observability](https://www.nuget.org/packages/Bozzis.Observability) | 1.0.0 | Dennis Bozzi | Sends an ASP.NET Core API's request logs to Bozzis (bozzis.com) in the backgrou… |
| 2026-09-28 13:52:46 | [Formbase.Sqlite](https://www.nuget.org/packages/Formbase.Sqlite) | 0.13.0 | iyulab | SQLite adapter for formbase — a single-file projection store, projection state… |
| 2026-09-28 13:53:02 | [MDD4All.DME.AssemblyLoading](https://www.nuget.org/packages/MDD4All.DME.AssemblyLoading) | 2.0.0.1 | Dr. Oliver Alt, mDuckLab | Loads an assembly into a context of its own, so it can be dropped again when an… |
| 2026-09-28 13:53:15 | [Synorvia.FileAccess.WPF](https://www.nuget.org/packages/Synorvia.FileAccess.WPF) | 2.0.0.1 | Dr. Oliver Alt | WPF implementation of FileAccess contracts using IoC design pattern. |
| 2026-09-28 13:53:25 | [Synorvia.UI.BlazorComponents](https://www.nuget.org/packages/Synorvia.UI.BlazorComponents) | 2.0.0.1 | Dr. Oliver Alt, mDuckLab | A collection of Blazor user interface components |
| 2026-09-28 14:04:45 | [HyperDev.Remoting](https://www.nuget.org/packages/HyperDev.Remoting) | 1.0.0 | Ivan Senatore, Wemake Informa… | HyperDev Fatum Framework |
| 2026-09-28 14:06:25 | [Universal.Operative.Sdk.Discrete.Microsoft.Foundry](https://www.nuget.org/packages/Universal.Operative.Sdk.Discrete.Microsoft.Foundry) | 1.0.0 | Andrew Ong | Microsoft Foundry OpenAI, Anthropic, and MAI model adapters for Universal.Opera… |
| 2026-09-28 14:08:13 | [AuthEndpoints.Templates](https://www.nuget.org/packages/AuthEndpoints.Templates) | 1.0.0 | madeyoga | ASP.NET Core Web API template with AuthEndpoints cookie auth, EF Core + Postgre… |
| 2026-09-28 14:10:21 | [MDD4All.DME.AssemblyTree](https://www.nuget.org/packages/MDD4All.DME.AssemblyTree) | 2.0.0.1 | Dr. Oliver Alt, mDuckLab | Shows the types of a .NET assembly as a tree - assembly, namespaces, types - to… |
| 2026-09-28 14:19:14 | [Curiosus.Migrations](https://www.nuget.org/packages/Curiosus.Migrations) | 5.0.0 | Maxim Markelow (@markeli), Ki… | Without migrations you need to create a lots of sql scripts that have to be run… |
| 2026-09-28 14:19:15 | [Curiosus.Migrations.Utils](https://www.nuget.org/packages/Curiosus.Migrations.Utils) | 5.0.0 | Maxim Markelow (@markeli), An… | Without migrations you need to create a lots of sql scripts that have to be run… |
| 2026-09-28 14:19:17 | [Curiosus.Migrations.PostgreSQL](https://www.nuget.org/packages/Curiosus.Migrations.PostgreSQL) | 5.0.0 | Maxim Markelow (@markeli), Ki… | Curiosus.Migrations is a migration framework that uses SQL scripts and code mig… |
| 2026-09-28 14:19:18 | [Curiosus.Migrations.SqlServer](https://www.nuget.org/packages/Curiosus.Migrations.SqlServer) | 5.0.0 | Maxim Markelow (@markeli), An… | Curiosus.Migrations is a migration framework that uses SQL scripts and code mig… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
