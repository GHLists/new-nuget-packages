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

## Latest list — 2026-11-05 20:20 UTC

New packages created between 2026-11-05 19:19 UTC and 2026-11-05 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T20-20-15-530705Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 19:27:04 | [LHFD.CleanArch.Template](https://www.nuget.org/packages/LHFD.CleanArch.Template) | 1.0.1 | Lucas Henrique Faria de Deus | Clean Architecture template with Entity Framework Core CRUD base. |
| 2026-11-05 19:35:16 | [YouBIM.Common.Middlewares.Lib](https://www.nuget.org/packages/YouBIM.Common.Middlewares.Lib) | 1.0.0 | YouBIM developers team | A shared middleware library for YouBIM ASP.NET Core applications. |
| 2026-11-05 19:37:43 | [Webority.Seo.AspNetCore.Testing](https://www.nuget.org/packages/Webority.Seo.AspNetCore.Testing) | 0.18.0 | Webority Technologies | In-process SEO checks for a Razor Pages site: one call requests every declared… |
| 2026-11-05 19:50:47 | [RecursiveAI.OneDiff.Documents](https://www.nuget.org/packages/RecursiveAI.OneDiff.Documents) | 1.0.0 | Recursive AI, LLC | Text diff and document comparison for .NET. The document engine: a compare mode… |
| 2026-11-05 19:50:47 | [RecursiveAI.OneDiff](https://www.nuget.org/packages/RecursiveAI.OneDiff) | 1.0.0 | Recursive AI, LLC | Text diff and document comparison for .NET. The core package: Myers, patience a… |
| 2026-11-05 19:50:48 | [RecursiveAI.OneDiff.Pdf](https://www.nuget.org/packages/RecursiveAI.OneDiff.Pdf) | 1.0.0 | Recursive AI, LLC | Text diff and document comparison for .NET. PDF comparison: a document source t… |
| 2026-11-05 19:50:49 | [RecursiveAI.OneDiff.Ocr](https://www.nuget.org/packages/RecursiveAI.OneDiff.Ocr) | 1.0.0 | Recursive AI, LLC | Text diff and document comparison for .NET. Scan comparison: a document source… |
| 2026-11-05 19:50:50 | [RecursiveAI.OneDiff.Tool](https://www.nuget.org/packages/RecursiveAI.OneDiff.Tool) | 1.0.0 | Recursive AI, LLC | Text diff and document comparison for .NET: the onediff command-line tool, whic… |
| 2026-11-05 19:55:10 | [AbsLang](https://www.nuget.org/packages/AbsLang) | 0.6.0 | Franco Vinciarelli | Agent Behavior Specification (ABS) — describe, run and evaluate AI agent behavi… |
| 2026-11-05 19:55:10 | [AbsLang.Adapters.Aws](https://www.nuget.org/packages/AbsLang.Adapters.Aws) | 0.6.0 | Franco Vinciarelli | AWS Bedrock evaluator adapter for AbsLang (Agent Behavior Specification). |
| 2026-11-05 19:55:11 | [AbsLang.Adapters.Google](https://www.nuget.org/packages/AbsLang.Adapters.Google) | 0.6.0 | Franco Vinciarelli | Google Vertex AI evaluator adapter for AbsLang (Agent Behavior Specification). |
| 2026-11-05 20:00:43 | [AWSSDK.AccountAccessRuntime](https://www.nuget.org/packages/AWSSDK.AccountAccessRuntime) | 4.0.100 | Amazon Web Services | The Amazon Web Services SDK for .NET - Account Access Runtime |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
