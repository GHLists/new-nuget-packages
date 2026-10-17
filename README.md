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

## Latest list — 2026-10-17 19:18 UTC

New packages created between 2026-10-17 18:20 UTC and 2026-10-17 19:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T19-18-57-955863Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 18:21:26 | [Hexalith.McpCli.Abstractions](https://www.nuget.org/packages/Hexalith.McpCli.Abstractions) | 1.0.0 | Hexalith Contributors | Attributes and naming helpers for declaring Hexalith agent operations. |
| 2026-10-17 18:38:22 | [Zwergenland.CleanMessageBus.Hosting](https://www.nuget.org/packages/Zwergenland.CleanMessageBus.Hosting) | 1.0.0 | Florian Königsmann | Minimal-API-style event handler registration, consume/publish pipelines and bui… |
| 2026-10-17 18:52:01 | [Anybox](https://www.nuget.org/packages/Anybox) | 0.9.0 | ethereal | one API for the most popular passthrough boxes, over the anybox C ABI |
| 2026-10-17 19:04:57 | [DirectUpload.Blazor](https://www.nuget.org/packages/DirectUpload.Blazor) | 0.1.0 | Sjoerd Lemmen | Blazor side of BlazorDirectUpload: uploads large files from the browser straigh… |
| 2026-10-17 19:04:58 | [DirectUpload.Server](https://www.nuget.org/packages/DirectUpload.Server) | 0.1.0 | Sjoerd Lemmen | Server side of BlazorDirectUpload: minimal-API endpoints that orchestrate presi… |
| 2026-10-17 19:05:47 | [Lokad.Svg](https://www.nuget.org/packages/Lokad.Svg) | 0.1.0 | Lokad | A pure managed SVG to PNG renderer for .NET. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
