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

## Latest list — 2026-11-22 05:19 UTC

New packages created between 2026-11-22 04:20 UTC and 2026-11-22 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T05-19-21-847934Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 04:24:23 | [OmniCore.Database.Connector](https://www.nuget.org/packages/OmniCore.Database.Connector) | 1.2.0 | OmniCore | Client runtime for the OmniCore document database: an HTTP client, change-track… |
| 2026-11-22 04:27:15 | [OmniCore.PlugIn](https://www.nuget.org/packages/OmniCore.PlugIn) | 1.2.0 | OmniCore | Build OmniCore plugins: implement IPlugin, mark the class with [FireOnAdd], [Fi… |
| 2026-11-22 04:30:21 | [OmniCore.Cli](https://www.nuget.org/packages/OmniCore.Cli) | 1.3.0 | OmniCore | occtl, the OmniCore command line: sign in to an OmniCore server, manage plugins… |
| 2026-11-22 04:52:03 | [AbpLanguages](https://www.nuget.org/packages/AbpLanguages) | 0.7.0 | AbpCluster contributors | AbpLanguages: a site's languages and translations for ABP apps on .NET 10. Lang… |
| 2026-11-22 04:52:04 | [AbpLanguages.HttpApi](https://www.nuget.org/packages/AbpLanguages.HttpApi) | 0.7.0 | AbpCluster contributors | AbpLanguages.HttpApi: AbpLanguages' API over HTTP, under a route prefix the hos… |
| 2026-11-22 04:54:42 | [Pdfwright](https://www.nuget.org/packages/Pdfwright) | 0.1.0 | Sinan Oran | A small, MIT-licensed PDF writer for reports: paragraphs and tables with pagina… |
| 2026-11-22 05:01:05 | [Decisions.Codex](https://www.nuget.org/packages/Decisions.Codex) | 1.0.0 | Yue Zhishun | 通过本机 Codex App Server 提供 OpenAI Decisions、Jev System One 和结构化回答。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
