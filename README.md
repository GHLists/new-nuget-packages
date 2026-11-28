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

## Latest list — 2026-11-28 10:20 UTC

New packages created between 2026-11-28 09:19 UTC and 2026-11-28 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-28T10-20-39-75934Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-28 09:21:02 | [Glesity.Wasm.Sqlite](https://www.nuget.org/packages/Glesity.Wasm.Sqlite) | 0.1.0-alpha | Glesity | Zero-reflection, NativeAOT-LLVM static SQLite engine for .NET WASI / WebAssembl… |
| 2026-11-28 10:02:52 | [z3l.Scraper](https://www.nuget.org/packages/z3l.Scraper) | 0.9.0 | z3l | Block-aware web scraping engine for .NET 9/10/11: request queue with priorities… |
| 2026-11-28 10:02:53 | [z3l.Scraper.Playwright](https://www.nuget.org/packages/z3l.Scraper.Playwright) | 0.9.0 | z3l | Headless browser page loader for z3l.Scraper on Microsoft Playwright: Chromium,… |
| 2026-11-28 10:02:54 | [z3l.Scraper.Loaders.ScrapingBee](https://www.nuget.org/packages/z3l.Scraper.Loaders.ScrapingBee) | 0.9.0 | z3l | A page loader for z3l.Scraper through the ScrapingBee web scraping API: its rot… |
| 2026-11-28 10:08:14 | [PatTech.IcoNet.Builder](https://www.nuget.org/packages/PatTech.IcoNet.Builder) | 0.3.0 | Patrick Zahra | Writes and reads Windows icons (.ico), cursors (.cur) and animated cursors (.an… |
| 2026-11-28 10:08:24 | [PatTech.IcoNet.Pipeline](https://www.nuget.org/packages/PatTech.IcoNet.Pipeline) | 0.3.0 | Patrick Zahra | Builds multi-resolution Windows icons (.ico), cursors (.cur) and animated curso… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
