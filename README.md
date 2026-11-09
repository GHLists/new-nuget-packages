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

## Latest list — 2026-11-09 16:21 UTC

New packages created between 2026-11-09 15:21 UTC and 2026-11-09 16:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T16-21-02-228493Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 15:33:41 | [Snail.Sdk.Mcp.Programs](https://www.nuget.org/packages/Snail.Sdk.Mcp.Programs) | 0.5.0 | orldev | run_program for a Snail MCP server: a small JavaScript program, run on Jint bes… |
| 2026-11-09 15:34:49 | [Siteimprove.Umbraco17.Plugin](https://www.nuget.org/packages/Siteimprove.Umbraco17.Plugin) | 1.0.0 | Siteimprove.Umbraco17.Plugin | Siteimprove Content Assistant for Umbraco 17 on Cloud and self-hosted sites. |
| 2026-11-09 15:34:52 | [Esatto.Umbraco.Backoffice.Seo](https://www.nuget.org/packages/Esatto.Umbraco.Backoffice.Seo) | 1.0.0 | Carl Schéle | SEO Health for Umbraco: a Content-section dashboard that scans every published… |
| 2026-11-09 15:35:29 | [VisioForge.CrossPlatform.OpenCV.iOS](https://www.nuget.org/packages/VisioForge.CrossPlatform.OpenCV.iOS) | 2026.11.8 | VisioForge | OpenCV computer vision libraries package for VisioForge .NET SDKs. Enables adva… |
| 2026-11-09 15:54:22 | [Etch.Cms.Umbraco.AI](https://www.nuget.org/packages/Etch.Cms.Umbraco.AI) | 17.0.12 | Etch | AI-assisted editing for the Umbraco backoffice, built on Umbraco.AI: meta title… |
| 2026-11-09 15:59:05 | [Squiggly](https://www.nuget.org/packages/Squiggly) | 1.0.0 | Muneeb Mughal | Play Snake, Tetris and Minesweeper in your compiler errors. Diagnostics are the… |
| 2026-11-09 15:59:49 | [Craticula.SigningProbe](https://www.nuget.org/packages/Craticula.SigningProbe) | 0.0.1 | pluries | Signing probe, not for use |
| 2026-11-09 16:06:16 | [Bob.The.Builder](https://www.nuget.org/packages/Bob.The.Builder) | 0.0.2 | Mogens Heller Grabe | Bob is a build tool that invokes scripts/build and scripts/release in the curre… |
| 2026-11-09 16:14:23 | [ez2lazer.Veldrid](https://www.nuget.org/packages/ez2lazer.Veldrid) | 2026.1109.0 | SK-la, Veldrid contributors | A low-level, hardware-accelerated graphics and compute library for .NET, with b… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
