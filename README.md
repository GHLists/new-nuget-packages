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

## Latest list — 2026-11-27 00:19 UTC

New packages created between 2026-11-26 23:21 UTC and 2026-11-27 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T00-19-32-916886Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 23:35:48 | [ShambleLog](https://www.nuget.org/packages/ShambleLog) | 0.9.1-alpha | Adam O'Neil | An EF Core-based logger targeting Postgres, ILogger<T> compatible |
| 2026-11-26 23:42:58 | [OmniCore.Mcp](https://www.nuget.org/packages/OmniCore.Mcp) | 1.1.0 | OmniCore | omnicore-mcp, a Model Context Protocol server for the OmniCore database: schema… |
| 2026-11-26 23:49:54 | [SadeemSystems.ChampUI.Templates](https://www.nuget.org/packages/SadeemSystems.ChampUI.Templates) | 0.1.3 | Sadeem Systems | A Blazor Interactive Server dashboard project template built with ChampUI. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
