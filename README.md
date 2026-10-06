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

## Latest list — 2026-10-06 12:20 UTC

New packages created between 2026-10-06 11:19 UTC and 2026-10-06 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T12-20-37-431445Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 11:34:52 | [Pronaos.FX.Templates](https://www.nuget.org/packages/Pronaos.FX.Templates) | 1.0.0 | Pronaos.FX Team | Template de microservico Pronaos.FX — Arquitetura Hexagonal/Clean, autenticacao… |
| 2026-10-06 11:43:30 | [DoNotUseTheGreaterThanSign.Analyzer.Net](https://www.nuget.org/packages/DoNotUseTheGreaterThanSign.Analyzer.Net) | 0.0.1 | Llewellyn Falco | Roslyn analyzer and code fix that replaces '>' and '>=' with '<' and '<=' as a… |
| 2026-10-06 11:47:34 | [ZEventAggregator](https://www.nuget.org/packages/ZEventAggregator) | 1.0.0-rc | Albin Sjöström | EventAggregator using interfaces with support for ref structs |
| 2026-10-06 12:05:00 | [ClickUp.Net](https://www.nuget.org/packages/ClickUp.Net) | 1.0.0 | zahid94 | A strongly typed .NET 6 client library for the ClickUp API v2. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
