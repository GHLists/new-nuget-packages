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

## Latest list — 2026-09-30 19:21 UTC

New packages created between 2026-09-30 18:20 UTC and 2026-09-30 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T19-21-11-166022Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 18:33:09 | [Rkd.Scalar.FluentValidation](https://www.nuget.org/packages/Rkd.Scalar.FluentValidation) | 2.8.0 | Rodrigo Kmiecik | FluentValidation integration for Rkd.Scalar: WithFluentValidation() runs the IV… |
| 2026-09-30 18:41:04 | [Basalt.BedrockData](https://www.nuget.org/packages/Basalt.BedrockData) | 0.1.2 | BedrockData | Generated Minecraft Bedrock data for Basalt. |
| 2026-09-30 18:54:25 | [ZeroAlloc.Saga.Outbox.Orm](https://www.nuget.org/packages/ZeroAlloc.Saga.Outbox.Orm) | 4.1.0 | Marcel Roozekrans | Transactional outbox unit of work for ZeroAlloc.Saga.Outbox + ZeroAlloc.Saga.Or… |
| 2026-09-30 19:01:37 | [FluxIndex.Integrations.FluxGuard](https://www.nuget.org/packages/FluxIndex.Integrations.FluxGuard) | 0.66.0 | iyulab | FluxGuard RAG security for FluxIndex — an IRetrievalGuard that runs search resu… |
| 2026-09-30 19:03:21 | [GlmSharpRenewed](https://www.nuget.org/packages/GlmSharpRenewed) | 1.0.4 | GlmSharpRenewed | Package Description |
| 2026-09-30 19:03:25 | [GlmSharpCompatRenewed](https://www.nuget.org/packages/GlmSharpCompatRenewed) | 1.0.4 | GlmSharpCompatRenewed | Package Description |
| 2026-09-30 19:09:05 | [Majorsilence.Crystal.Converter](https://www.nuget.org/packages/Majorsilence.Crystal.Converter) | 0.1.0 | Peter Gill | RDL emitter and Crystal formula transpiler (Irony grammar) that converts a pars… |
| 2026-09-30 19:09:05 | [Majorsilence.Crystal.RptEngine](https://www.nuget.org/packages/Majorsilence.Crystal.RptEngine) | 0.1.0 | Peter Gill | Renders Crystal Reports .rpt files (with runtime data/parameter/formula overrid… |
| 2026-09-30 19:09:06 | [Majorsilence.Crystal.Runtime](https://www.nuget.org/packages/Majorsilence.Crystal.Runtime) | 0.1.0 | Peter Gill | Engine-agnostic runtime-override application and render preparation for a parse… |
| 2026-09-30 19:09:08 | [Majorsilence.Crystal.Cli](https://www.nuget.org/packages/Majorsilence.Crystal.Cli) | 0.1.0 | Peter Gill | Batch CLI for converting Crystal Reports .rpt files to SSRS RDL and verifying t… |
| 2026-09-30 19:09:09 | [Majorsilence.Crystal.Parser](https://www.nuget.org/packages/Majorsilence.Crystal.Parser) | 0.1.0 | Peter Gill | OLE reader, TSLV parser, AES-CFB128 decryptor, and zlib inflate for Crystal Rep… |
| 2026-09-30 19:09:10 | [Majorsilence.Crystal.Model](https://www.nuget.org/packages/Majorsilence.Crystal.Model) | 0.1.0 | Peter Gill | Neutral object model for a parsed Crystal Reports .rpt file — ReportDefinition,… |
| 2026-09-30 19:09:54 | [Majo.LineEditing](https://www.nuget.org/packages/Majo.LineEditing) | 0.0.3 | Sweety Majo | A small, cross-platform interactive line editor for .NET. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
