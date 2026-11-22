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

## Latest list — 2026-11-22 18:19 UTC

New packages created between 2026-11-22 17:21 UTC and 2026-11-22 18:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T18-19-04-307252Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 17:27:01 | [grdev.tasks-ui](https://www.nuget.org/packages/grdev.tasks-ui) | 0.1.5 | Thomas Sarmis (thomas.sarmis@… | A local web board for plain-text tasks: capture, ingest, refine, schedule and a… |
| 2026-11-22 17:27:02 | [Nextorm.Extensions.OpenCode](https://www.nuget.org/packages/Nextorm.Extensions.OpenCode) | 1.0.0 | Nextorm.Extensions.OpenCode | Nextorm repository context for the OpenCode SQLite database schema. |
| 2026-11-22 17:35:25 | [Chris82111.GitManager.GitWrapper.Core](https://www.nuget.org/packages/Chris82111.GitManager.GitWrapper.Core) | 1.0.0 | Chris82111 | Core solution for using Git in a portable form. Supports: Locally installed Git… |
| 2026-11-22 17:37:36 | [Beskar.Networking.Datagram](https://www.nuget.org/packages/Beskar.Networking.Datagram) | 11.2.0 | Marvin Drude | Specialized, low-allocation UDP datagram and multi-channel reliability protocol… |
| 2026-11-22 17:48:01 | [Loopia.Console](https://www.nuget.org/packages/Loopia.Console) | 0.1.0 | nielsbosma | CLI tool for the Loopia API - manage domains, subdomains, and DNS zone records |
| 2026-11-22 17:51:40 | [AgentKit.Mail](https://www.nuget.org/packages/AgentKit.Mail) | 0.1.11 | Lenka Scherfel | Send email through Resend's REST API without its SDK: one send contract (from,… |
| 2026-11-22 17:53:38 | [z3l.FastHtmlParser.Readability](https://www.nuget.org/packages/z3l.FastHtmlParser.Readability) | 1.8.0 | z3l | Fast main-content extraction for .NET 9/10/11 by the method of Mozilla Readabil… |
| 2026-11-22 17:53:39 | [z3l.FastHtmlParser.HtmlSanitizer](https://www.nuget.org/packages/z3l.FastHtmlParser.HtmlSanitizer) | 1.8.0 | z3l | Fast HTML sanitizer for .NET 9/10/11 against XSS, built on z3l.FastHtmlParser:… |
| 2026-11-22 18:01:02 | [Dbsp.Hosting](https://www.nuget.org/packages/Dbsp.Hosting) | 0.2.0 | James Lanng | Generic Host and dependency-injection integration for Dbsp: register a circuit… |
| 2026-11-22 18:01:03 | [Dbsp](https://www.nuget.org/packages/Dbsp) | 0.2.0 | James Lanng | DBSP-style incremental stream processing for .NET: collections are Z-sets, stre… |
| 2026-11-22 18:01:04 | [Dbsp.Kafka](https://www.nuget.org/packages/Dbsp.Kafka) | 0.2.0 | James Lanng | Kafka-backed durability for Dbsp: the state changelog and shared-table logs on… |
| 2026-11-22 18:01:04 | [Dbsp.Storage.Redis](https://www.nuget.org/packages/Dbsp.Storage.Redis) | 0.2.0 | James Lanng | Redis-backed storage provider for Dbsp: operator state in Redis hashes with ato… |
| 2026-11-22 18:04:46 | [Iciclecreek.Lucene.Net.Temporal](https://www.nuget.org/packages/Iciclecreek.Lucene.Net.Temporal) | 1.0.0 | Tom Laird-McConnell | TIMEX-based temporal indexing and filtering for Lucene.NET 4.8: store whole, pa… |
| 2026-11-22 18:05:51 | [TcfOss.DatabaseManager.App](https://www.nuget.org/packages/TcfOss.DatabaseManager.App) | 0.9.0 | Thomas C. Flanagan | Package Description |
| 2026-11-22 18:11:34 | [NanoByte.StructureEditor.EtoForms](https://www.nuget.org/packages/NanoByte.StructureEditor.EtoForms) | 4.0.0 | Bastian Eicher | Cross-platform Eto.Forms controls for building split-screen editors for data st… |
| 2026-11-22 18:11:35 | [NanoByte.StructureEditor.Json](https://www.nuget.org/packages/NanoByte.StructureEditor.Json) | 4.0.0 | Bastian Eicher | System.Text.Json serialization support for split-screen editors for data struct… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
