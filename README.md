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

## Latest list — 2026-11-09 08:21 UTC

New packages created between 2026-11-09 07:20 UTC and 2026-11-09 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T08-21-06-327565Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 07:25:37 | [ZaloBot.Sdk](https://www.nuget.org/packages/ZaloBot.Sdk) | 1.0.0 | TanNhatCMS | Zalo Bot API client for .NET — 11 API methods, official error-code taxonomy, re… |
| 2026-11-09 07:37:48 | [Tabler.Avalonia](https://www.nuget.org/packages/Tabler.Avalonia) | 0.1.0 | Compunet | Tabler Icons (6,000+ outline and filled icons) for AvaloniaUI: a lightweight co… |
| 2026-11-09 07:38:07 | [Niubility.Statistics](https://www.nuget.org/packages/Niubility.Statistics) | 0.1.0 | Niubility | Statistics definitions, validation, collection, query and publication contracts. |
| 2026-11-09 07:38:39 | [Niubility.Statistics.Database](https://www.nuget.org/packages/Niubility.Statistics.Database) | 0.1.0 | Niubility | Statistics collection, queries and aggregate generation for MySQL and SQL Serve… |
| 2026-11-09 07:40:05 | [Zalo.Bot](https://www.nuget.org/packages/Zalo.Bot) | 1.0.1 | TanNhatCMS | Zalo Bot API client for .NET — 11 API methods, official error-code taxonomy, re… |
| 2026-11-09 07:45:52 | [Beesum.Core](https://www.nuget.org/packages/Beesum.Core) | 0.2.0 | air-catfish and Beesum contri… | Transcript-first YouTube summarizer core: WebVTT parsing, yt-dlp integration, p… |
| 2026-11-09 07:45:53 | [Beesum.Testing](https://www.nuget.org/packages/Beesum.Testing) | 0.2.0 | air-catfish and Beesum contri… | In-memory test doubles and AddBeesumTesting() for Beesum.Core. |
| 2026-11-09 07:45:54 | [beesum-mcp](https://www.nuget.org/packages/beesum-mcp) | 0.2.0 | air-catfish and Beesum contri… | MCP stdio server for beesum-min: summarize YouTube URLs or supplied transcripts… |
| 2026-11-09 07:45:55 | [beesum-min](https://www.nuget.org/packages/beesum-min) | 0.2.0 | air-catfish and Beesum contri… | Transcript-first YouTube summarizer CLI. Keeps the transcript on your machine;… |
| 2026-11-09 07:51:00 | [MicroserviceMonolith](https://www.nuget.org/packages/MicroserviceMonolith) | 1.0.0 | Mykola Kusch | MicroserviceMonolith is a comprehensive, production-ready modular monolith fram… |
| 2026-11-09 07:52:46 | [Dignite.Abp.OpenIddict.ClientIdMetadataDocuments](https://www.nuget.org/packages/Dignite.Abp.OpenIddict.ClientIdMetadataDocuments) | 10.7.6 | Dignite | Lets an ABP Framework authorization server built on OpenIddict accept OAuth Cli… |
| 2026-11-09 07:56:34 | [Gosf.Input.Automation](https://www.nuget.org/packages/Gosf.Input.Automation) | 0.1.0 | Gosf.Input.Automation contrib… | Windows foreground and background mouse and keyboard automation. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
