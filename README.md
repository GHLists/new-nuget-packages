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

## Latest list — 2026-10-04 09:22 UTC

New packages created between 2026-10-04 08:20 UTC and 2026-10-04 09:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T09-22-33-158443Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 08:32:09 | [Vorticity.Zstd](https://www.nuget.org/packages/Vorticity.Zstd) | 0.4.0 | Evariops | A Zstandard (RFC 8878) decompressor and compressor in fully managed C#: no nati… |
| 2026-10-04 08:41:54 | [MentalDesk.Tui](https://www.nuget.org/packages/MentalDesk.Tui) | 0.1.0 | James Crosswell | Shared Terminal.Gui building blocks for MentalDesk TUI apps: themes, commands a… |
| 2026-10-04 08:46:17 | [Gua.Testing.Snapshots](https://www.nuget.org/packages/Gua.Testing.Snapshots) | 1.1.0 | Gua contributors | Deterministic semantic UI and optional World snapshot baselines for Gua tests. |
| 2026-10-04 08:53:01 | [MintOsuAPI](https://www.nuget.org/packages/MintOsuAPI) | 0.1.0 | Tsurumaki-kokoro | osu! API client for .NET — v2 (OAuth2) and legacy v1 (API key), with on-disk to… |
| 2026-10-04 08:57:36 | [Webority.Ai.Actions](https://www.nuget.org/packages/Webority.Ai.Actions) | 0.9.0 | Webority Technologies | Deferred agent actions for Webority products on Webority.Ai: a tool records a p… |
| 2026-10-04 08:57:39 | [Drenalol.Enrichment](https://www.nuget.org/packages/Drenalol.Enrichment) | 0.1.0 | Enrichment contributors | Data enrichers load is reused by FluentValidation contextual validators and Med… |
| 2026-10-04 08:57:40 | [Webority.Ai.Knowledge](https://www.nuget.org/packages/Webority.Ai.Knowledge) | 0.9.0 | Webority Technologies | Retrieval over a product's own content for Webority.Ai: corpora a product regis… |
| 2026-10-04 08:57:41 | [Webority.Ai.Knowledge.Sql](https://www.nuget.org/packages/Webority.Ai.Knowledge.Sql) | 0.9.0 | Webority Technologies | The SQL Server store for Webority.Ai.Knowledge: the AiKnowledgeChunk table in t… |
| 2026-10-04 08:57:42 | [Webority.Ai.Knowledge.AzureSearch](https://www.nuget.org/packages/Webority.Ai.Knowledge.AzureSearch) | 0.9.0 | Webority Technologies | The Azure AI Search store for Webority.Ai.Knowledge: one index of chunks, searc… |
| 2026-10-04 08:57:44 | [Webority.Ai.Actions.AspNetCore](https://www.nuget.org/packages/Webority.Ai.Actions.AspNetCore) | 0.9.0 | Webority Technologies | Agent action decisions over HTTP for Webority.Ai.Actions: one handler a product… |
| 2026-10-04 09:05:50 | [Webority.CsCheck](https://www.nuget.org/packages/Webority.CsCheck) | 0.1.0 | Webority Technologies | Fast, small C# compile checker for coding agents: one shared background process… |
| 2026-10-04 09:06:42 | [Orbyss.Foundation.Build](https://www.nuget.org/packages/Orbyss.Foundation.Build) | 0.1.0 | Orbyss | Publisher-owned feature descriptor production for Foundation-compatible package… |
| 2026-10-04 09:09:37 | [Sunsetless.Ews.NETStandard](https://www.nuget.org/packages/Sunsetless.Ews.NETStandard) | 1.1.0 | Sunsetless | Keep your async EWS Managed API code (Microsoft.Exchange.WebServices.NETStandar… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
