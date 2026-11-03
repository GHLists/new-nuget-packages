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

## Latest list — 2026-11-03 13:21 UTC

New packages created between 2026-11-03 12:19 UTC and 2026-11-03 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T13-21-06-463265Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 12:43:43 | [Delih](https://www.nuget.org/packages/Delih) | 0.1.0-alpha | Enrico Kip | Puts AI-generated code through an organization's own architectural rules, allow… |
| 2026-11-03 12:44:16 | [Bondarukini.Mapper](https://www.nuget.org/packages/Bondarukini.Mapper) | 10.0.0 | Yurii Bondaruk | Object mapping for .NET 10 with compiled plans, profiles, nested collections an… |
| 2026-11-03 12:44:45 | [Bondarukini.Mapper.DependencyInjection](https://www.nuget.org/packages/Bondarukini.Mapper.DependencyInjection) | 10.0.0 | Yurii Bondaruk | Microsoft dependency injection and profile scanning for Bondarukini.Mapper. |
| 2026-11-03 12:47:40 | [io7.FreePDF.Gdi](https://www.nuget.org/packages/io7.FreePDF.Gdi) | 7.1.0 | io7 | MIT PDF creation and editing for Windows desktop and .NET Framework apps, drawi… |
| 2026-11-03 12:47:41 | [io7.FreePDF.Layout.Gdi](https://www.nuget.org/packages/io7.FreePDF.Layout.Gdi) | 7.1.0 | io7 | MIT document layout with paragraphs, tables, charts and PDF/RTF output for io7.… |
| 2026-11-03 12:47:42 | [io7.FreePDF.Wpf](https://www.nuget.org/packages/io7.FreePDF.Wpf) | 7.1.0 | io7 | MIT PDF creation and editing for Windows desktop and .NET Framework apps, drawi… |
| 2026-11-03 12:47:43 | [io7.FreePDF.Layout.Wpf](https://www.nuget.org/packages/io7.FreePDF.Layout.Wpf) | 7.1.0 | io7 | MIT document layout with paragraphs, tables, charts and PDF/RTF output for io7.… |
| 2026-11-03 12:53:17 | [AppWeaver.Web.Security](https://www.nuget.org/packages/AppWeaver.Web.Security) | 1.0.0 | Team AppWeaver | Shared web security/cache policy primitives for AppWeaver endpoints. |
| 2026-11-03 12:53:55 | [CryptoExchange.Net.Web3](https://www.nuget.org/packages/CryptoExchange.Net.Web3) | 13.0.0 | JKorf | CryptoExchange.Net.Web3 is a helper library adding Web3 utilities to CryptoExch… |
| 2026-11-03 12:54:20 | [Instana.OpenTelemetry.Exporter](https://www.nuget.org/packages/Instana.OpenTelemetry.Exporter) | 1.329.1 | Instana | Instana .NET Exporter for OpenTelemetry — converts OTel SDK and instrumentation… |
| 2026-11-03 12:56:08 | [Ananke.Embeddings.Onnx](https://www.nuget.org/packages/Ananke.Embeddings.Onnx) | 0.9.1 | sevensamurai | Local embeddings for Ananke — an IEmbeddingModel that runs a BERT-style ONNX mo… |
| 2026-11-03 12:56:22 | [Ananke.Postgres](https://www.nuget.org/packages/Ananke.Postgres) | 0.9.1 | sevensamurai | PostgreSQL provider for Ananke — IKnowledgeStore and IKnowledgeCatalog on Postg… |
| 2026-11-03 12:58:04 | [AppWeaver.Web.Extensions](https://www.nuget.org/packages/AppWeaver.Web.Extensions) | 1.0.0 | Team AppWeaver | AppWeaver Web Extensions Library in AppWeaver framework. |
| 2026-11-03 13:01:22 | [AppWeaver.MinimalEndpoint](https://www.nuget.org/packages/AppWeaver.MinimalEndpoint) | 1.0.0 | Team AppWeaver | Minimal API helpers for AppWeaver: map Result<T>/UnitResult via DI-based Result… |
| 2026-11-03 13:03:03 | [AppWeaver.FastEndpoint](https://www.nuget.org/packages/AppWeaver.FastEndpoint) | 1.0.0 | Team AppWeaver | FastEndpoints helpers for AppWeaver: send Result<T>/UnitResult via DI-based Res… |
| 2026-11-03 13:07:58 | [ForEach.Infrastructure.External.eOtpremnica](https://www.nuget.org/packages/ForEach.Infrastructure.External.eOtpremnica) | 0.1.0 | ForEach | Client and UBL 2.1 Despatch Advice writer for the Serbian central register of e… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
