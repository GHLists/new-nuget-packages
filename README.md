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

## Latest list — 2026-11-18 10:23 UTC

New packages created between 2026-11-18 09:21 UTC and 2026-11-18 10:23 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T10-23-16-509522Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 09:25:54 | [AZcaptcha.Sdk](https://www.nuget.org/packages/AZcaptcha.Sdk) | 1.0.0 | AZcaptcha | Official AZcaptcha SDK — reCAPTCHA, hCaptcha, Turnstile and image captchas |
| 2026-11-18 09:47:32 | [Pixata.Blazor.PdfViewer](https://www.nuget.org/packages/Pixata.Blazor.PdfViewer) | 1.1.0 | Avrohom Yisroel Silver | A PDF viewer for Blazor, with page navigation, zoom, rotation, text search, dow… |
| 2026-11-18 09:49:53 | [Pixata.Pdf](https://www.nuget.org/packages/Pixata.Pdf) | 1.1.0 | Avrohom Yisroel Silver | Combines several PDFs into one, keeping each page's size and orientation, such… |
| 2026-11-18 09:57:46 | [AStarDev.SingleInstance](https://www.nuget.org/packages/AStarDev.SingleInstance) | 0.1.1 | Jason Barden | One running instance per user for AStar Development desktop apps, with a hand-o… |
| 2026-11-18 09:57:47 | [AStarDev.InfrastructureFilesDb](https://www.nuget.org/packages/AStarDev.InfrastructureFilesDb) | 0.1.0 | AStar Development, Jason Bard… | EF Core persistence models and configuration for scraper and file metadata. |
| 2026-11-18 09:58:01 | [AStarDev.VelopackPublishing](https://www.nuget.org/packages/AStarDev.VelopackPublishing) | 1.3.1 | Jason Barden | Shared Velopack update check/download/apply service and options binding used by… |
| 2026-11-18 10:03:06 | [tongyong_lei2](https://www.nuget.org/packages/tongyong_lei2) | 1.0.0 | tongyong_lei2 | 通用 MySQL 访问辅助库（IMySqlHelper / 分组连接） |
| 2026-11-18 10:09:02 | [Bielu.AspNetCore.Arazzo.Scalar](https://www.nuget.org/packages/Bielu.AspNetCore.Arazzo.Scalar) | 3.0.0 | Arkadiusz Biel | Arazzo workflows in the Scalar API Reference for ASP.NET Core. Serves a Scalar… |
| 2026-11-18 10:09:43 | [Umbraco.Mcp.HostedAuth](https://www.nuget.org/packages/Umbraco.Mcp.HostedAuth) | 18.0.0 | Umbraco | Wires hosted Umbraco MCP Cloudflare Workers into the backoffice OAuth flow, on… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
