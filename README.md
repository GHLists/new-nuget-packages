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

## Latest list — 2026-10-18 16:21 UTC

New packages created between 2026-10-18 15:19 UTC and 2026-10-18 16:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T16-21-43-42192Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 15:21:42 | [Bachs.Sdk](https://www.nuget.org/packages/Bachs.Sdk) | 1.0.0 | Amaechi Ugwu | Developer-first .NET 8+ SDK for the Bachs payments and billing API: hosted chec… |
| 2026-10-18 15:31:47 | [Zaldaryon.Pharos.XUnit.V3](https://www.nuget.org/packages/Zaldaryon.Pharos.XUnit.V3) | 0.7.0-preview | Zaldaryon | xUnit v3 integration preview package for Pharos headless client test harness. |
| 2026-10-18 15:37:36 | [Laching.Web.Images](https://www.nuget.org/packages/Laching.Web.Images) | 0.19.1 | Vlad Mihalachi | Image uploads with SkiaSharp: format detection by magic bytes (PNG, JPEG, WebP;… |
| 2026-10-18 15:37:36 | [Laching.Web.Tailwind](https://www.nuget.org/packages/Laching.Web.Tailwind) | 0.19.1 | Vlad Mihalachi | Tailwind CSS v4 in dotnet build, without Node: downloads the pinned standalone… |
| 2026-10-18 15:37:37 | [Laching.Web.Aspire](https://www.nuget.org/packages/Laching.Web.Aspire) | 0.19.1 | Vlad Mihalachi | Aspire AppHost pieces for Azure Container Apps: ingress that accepts only Cloud… |
| 2026-10-18 15:37:37 | [Laching.Web.Jobs](https://www.nuget.org/packages/Laching.Web.Jobs) | 0.19.1 | Vlad Mihalachi | A PostgreSQL job table for background work with EF Core: jobs enqueued in the s… |
| 2026-10-18 15:37:38 | [Laching.Web.Cloudflare](https://www.nuget.org/packages/Laching.Web.Cloudflare) | 0.19.1 | Vlad Mihalachi | Cloudflare APIs over HttpClient, without ASP.NET Core: Turnstile token verifica… |
| 2026-10-18 15:37:38 | [Laching.Web.AspNetCore](https://www.nuget.org/packages/Laching.Web.AspNetCore) | 0.19.1 | Vlad Mihalachi | ASP.NET Core pieces for a site behind Cloudflare: an origin check with a shared… |
| 2026-10-18 15:38:00 | [IntoSQL](https://www.nuget.org/packages/IntoSQL) | 0.1.0 | IntoSQL | Convert spreadsheets, CSV and JSON into SQL with the IntoSQL API. |
| 2026-10-18 15:43:52 | [opencode-roslyn](https://www.nuget.org/packages/opencode-roslyn) | 1.0.0 | Alexey Shirshov | Roslyn semantic analysis CLI for opencode: structure, symbols, members, refs, c… |
| 2026-10-18 15:47:18 | [LapViz.Client](https://www.nuget.org/packages/LapViz.Client) | 1.0.0 | Mengal SRL | Official .NET client of the LapViz API (https://lapviz.com/developers): search,… |
| 2026-10-18 15:53:49 | [MagnusOpera.FScript.Extensibility](https://www.nuget.org/packages/MagnusOpera.FScript.Extensibility) | 1.0.0 | FScript contributors | Stable, implementation-independent FScript extension contracts and authoring he… |
| 2026-10-18 15:59:50 | [MagicArchive](https://www.nuget.org/packages/MagicArchive) | 0.1.0 | Retro & Chill | High-performance .NET serialization library. |
| 2026-10-18 15:59:51 | [MagicArchive.Core](https://www.nuget.org/packages/MagicArchive.Core) | 0.1.0 | Retro & Chill | High-performance .NET serialization library. |
| 2026-10-18 15:59:52 | [MagicArchive.SourceGenerator](https://www.nuget.org/packages/MagicArchive.SourceGenerator) | 0.1.0 | Retro & Chill | High-performance .NET serialization library. |
| 2026-10-18 16:16:49 | [Caly.Rendering.Scene3D.Prc](https://www.nuget.org/packages/Caly.Rendering.Scene3D.Prc) | 1.0.0 | BobLd | Reader for PRC (ISO 14739-1) files. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
