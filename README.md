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

## Latest list — 2026-10-23 18:20 UTC

New packages created between 2026-10-23 17:20 UTC and 2026-10-23 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T18-20-04-07491Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 17:23:51 | [PgProj.Engine](https://www.nuget.org/packages/PgProj.Engine) | 0.1.0 | Cory Maass | pgproj as a library: build a PostgreSQL schema project from SQL files, compare… |
| 2026-10-23 17:30:26 | [pgproj](https://www.nuget.org/packages/pgproj) | 0.1.0 | Cory Maass | PostgreSQL database project compiler: builds a schema from SQL files, compares… |
| 2026-10-23 17:39:45 | [Gil.Review](https://www.nuget.org/packages/Gil.Review) | 0.1.0 | iyulab | Review statistics for checking automated decisions by hand: seeded stratified s… |
| 2026-10-23 17:47:20 | [ZeroCdp](https://www.nuget.org/packages/ZeroCdp) | 0.1.0-alpha | ZeroCDP contributors | Zero-allocation, NativeAOT-friendly Chrome DevTools Protocol client for .NET. |
| 2026-10-23 17:48:25 | [Daml.Codegen.CSharp.MSBuild](https://www.nuget.org/packages/Daml.Codegen.CSharp.MSBuild) | 0.7.1 | Peaceful Studio OÜ | MSBuild integration for the Daml C# code generator. A <DamlArchive> item (or a… |
| 2026-10-23 18:01:15 | [SystemOne](https://www.nuget.org/packages/SystemOne) | 0.1.0 | orlys | Typed .NET client for System One decision models (noul / choice / score / box):… |
| 2026-10-23 18:01:16 | [SystemOne.Abstractions](https://www.nuget.org/packages/SystemOne.Abstractions) | 0.1.0 | orlys | Contracts for System One decision-model providers: ISystemOne, the SystemOnePro… |
| 2026-10-23 18:01:16 | [SystemOne.ModelSources.HuggingFace](https://www.nuget.org/packages/SystemOne.ModelSources.HuggingFace) | 0.1.0 | orlys | SystemOne.ModelSources.FromHuggingFace: zero-dependency, cached download of mod… |
| 2026-10-23 18:01:17 | [SystemOne.Providers.Clef](https://www.nuget.org/packages/SystemOne.Providers.Clef) | 0.1.0 | orlys | Shortcut for a self-hosted clef server (e.g. clef-mlx) for SystemOne: SystemOne… |
| 2026-10-23 18:01:18 | [SystemOne.Providers.Cloudflare](https://www.nuget.org/packages/SystemOne.Providers.Cloudflare) | 0.1.0 | orlys | Cloudflare Workers AI clef for SystemOne: account-scoped URL and the success/re… |
| 2026-10-23 18:01:18 | [SystemOne.Providers.OpenRouter](https://www.nuget.org/packages/SystemOne.Providers.OpenRouter) | 0.1.0 | orlys | OpenRouter gateway for SystemOne decision models (Jev, clef). SystemOne.Provide… |
| 2026-10-23 18:01:19 | [SystemOne.Providers.TypeSafe](https://www.nuget.org/packages/SystemOne.Providers.TypeSafe) | 0.1.0 | orlys | TypeSafe-hosted Jev for SystemOne: assets-style images and the danger-zone head… |
| 2026-10-23 18:01:20 | [SystemOne.Providers.Vercel](https://www.nuget.org/packages/SystemOne.Providers.Vercel) | 0.1.0 | orlys | Vercel AI Gateway (TypeSafe-compatible endpoint) for SystemOne decision models.… |
| 2026-10-23 18:01:20 | [SystemOne.Testing](https://www.nuget.org/packages/SystemOne.Testing) | 0.1.0 | orlys | MockSystemOneProvider, a configurable and recording test double for System One… |
| 2026-10-23 18:03:17 | [Octeka.UI.Wpf.TreeGrid](https://www.nuget.org/packages/Octeka.UI.Wpf.TreeGrid) | 1.0.0 | Patrick Robichaud | High-performance, virtualized multi-column tree data grid control for modern WP… |
| 2026-10-23 18:13:00 | [Mkx.Templates.React](https://www.nuget.org/packages/Mkx.Templates.React) | 0.2.0 | Mkx | Agent-first .NET 10 and React TypeScript ASP.NET Core hosted solution template. |
| 2026-10-23 18:13:40 | [MJCZone.DapperMatic.GraphQL](https://www.nuget.org/packages/MJCZone.DapperMatic.GraphQL) | 0.2.0 | MJCZone Inc. | Adds a GraphQL endpoint to DapperMatic's ASP.NET Core integration, built with G… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
