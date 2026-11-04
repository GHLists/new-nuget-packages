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

## Latest list — 2026-11-04 16:20 UTC

New packages created between 2026-11-04 15:18 UTC and 2026-11-04 16:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T16-20-34-673638Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 15:19:12 | [Neph.GenericLibs.Net.LLMLib](https://www.nuget.org/packages/Neph.GenericLibs.Net.LLMLib) | 0.1.0 | Neph | Generic LLM chat abstractions (service interface, DTOs and a reusable ASP.NET C… |
| 2026-11-04 15:25:32 | [SimisSharp](https://www.nuget.org/packages/SimisSharp) | 0.1.0 | Miroslav Rábek | Reads, edits and writes the text files of Microsoft Train Simulator (MSTS) and… |
| 2026-11-04 15:25:40 | [KeelMatrix.PackageSurface](https://www.nuget.org/packages/KeelMatrix.PackageSurface) | 0.1.0 | KeelMatrix | Baselines the execution-capable surface of resolved NuGet dependencies. Detects… |
| 2026-11-04 15:29:12 | [Bounteous.Data.SQLite](https://www.nuget.org/packages/Bounteous.Data.SQLite) | 0.0.2 | Bounteous | Package Description |
| 2026-11-04 15:31:32 | [Kopis.iSolutions.iFramework.ReportViewer](https://www.nuget.org/packages/Kopis.iSolutions.iFramework.ReportViewer) | 6.3.44-beta | iSolutions.iFramework.ReportV… | Package Description |
| 2026-11-04 15:31:40 | [Kopis.iSolutions.iReports.Admin](https://www.nuget.org/packages/Kopis.iSolutions.iReports.Admin) | 6.3.44-beta | iSolutions.iReports.Admin | Contains functionality needed to add iReport Administration functions to projec… |
| 2026-11-04 15:38:54 | [Hostpanel.Sdk.Packaging](https://www.nuget.org/packages/Hostpanel.Sdk.Packaging) | 3.1.0 | Hostpanel contributors | Shared plugin package validation for hostpanel: the signature format and Ed2551… |
| 2026-11-04 15:44:33 | [Shenora.Chromium.Codecs.win-x64](https://www.nuget.org/packages/Shenora.Chromium.Codecs.win-x64) | 154.0.32 | Jiarong Gu | CEF 154.0.32 (Chromium 154.0.8037.58) for Windows x64, built with Chromium's pr… |
| 2026-11-04 16:01:50 | [KetPsi.MessageBrokers.RabbitMQ](https://www.nuget.org/packages/KetPsi.MessageBrokers.RabbitMQ) | 1.0.0 | KetPsi | Native AOT and trim compatible publish/subscribe on RabbitMQ.Client 7. Subscrib… |
| 2026-11-04 16:02:13 | [DbnFetch.win-x64](https://www.nuget.org/packages/DbnFetch.win-x64) | 0.1.0 | SquidEyes | DbnFetch (dbnf): download raw and processed market data from a DbnSync archive… |
| 2026-11-04 16:02:14 | [DbnFetch.linux-x64](https://www.nuget.org/packages/DbnFetch.linux-x64) | 0.1.0 | SquidEyes | DbnFetch (dbnf): download raw and processed market data from a DbnSync archive… |
| 2026-11-04 16:02:15 | [DbnFetch.win-arm64](https://www.nuget.org/packages/DbnFetch.win-arm64) | 0.1.0 | SquidEyes | DbnFetch (dbnf): download raw and processed market data from a DbnSync archive… |
| 2026-11-04 16:02:16 | [DbnFetch.osx-arm64](https://www.nuget.org/packages/DbnFetch.osx-arm64) | 0.1.0 | SquidEyes | DbnFetch (dbnf): download raw and processed market data from a DbnSync archive… |
| 2026-11-04 16:02:16 | [DbnFetch](https://www.nuget.org/packages/DbnFetch) | 0.1.0 | SquidEyes | DbnFetch (dbnf): download raw and processed market data from a DbnSync archive… |
| 2026-11-04 16:02:17 | [DbnFetch.any](https://www.nuget.org/packages/DbnFetch.any) | 0.1.0 | SquidEyes | DbnFetch (dbnf): download raw and processed market data from a DbnSync archive… |
| 2026-11-04 16:02:17 | [DbnClient](https://www.nuget.org/packages/DbnClient) | 0.1.0 | SquidEyes | DbnClient: reads a DbnSync archive of Databento® files: raw days, continuous se… |
| 2026-11-04 16:04:21 | [Dloizides.Erasure](https://www.nuget.org/packages/Dloizides.Erasure) | 0.1.0 | DLoizides | GDPR erasure participant contract: an idempotent, secret-protected POST endpoin… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
