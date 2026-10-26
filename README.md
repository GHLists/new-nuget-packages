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

## Latest list — 2026-10-26 14:22 UTC

New packages created between 2026-10-26 13:22 UTC and 2026-10-26 14:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T14-22-21-17468Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 13:33:18 | [Xrm.DataManager.Framework.ApplicationInsights](https://www.nuget.org/packages/Xrm.DataManager.Framework.ApplicationInsights) | 2026.0.2 | Aymeric Mouillé | Application Insights logger for Xrm.DataManager.Framework |
| 2026-10-26 13:33:19 | [Xrm.DataManager.Framework.Tds](https://www.nuget.org/packages/Xrm.DataManager.Framework.Tds) | 2026.0.2 | Aymeric Mouillé | Retrieve Dataverse records with SQL (TDS endpoint) for Xrm.DataManager.Framework |
| 2026-10-26 13:39:11 | [CvSharp.PSD](https://www.nuget.org/packages/CvSharp.PSD) | 1.0.0 | GreatBear | Standalone 8/16-bit PSD reader/writer for .NET built on CvSharp. |
| 2026-10-26 13:41:03 | [FoundWell.Umbraco](https://www.nuget.org/packages/FoundWell.Umbraco) | 1.0.0 | Datapad | Connects an Umbraco site to FoundWell (redirects, llms.txt and JSON-LD written… |
| 2026-10-26 13:41:26 | [ParakeetSharp](https://www.nuget.org/packages/ParakeetSharp) | 26.10.7330 | Parakeet contributors | Pure C# (.NET 10) inference for NVIDIA Parakeet TDT speech recognition (FastCon… |
| 2026-10-26 13:50:08 | [Acplite](https://www.nuget.org/packages/Acplite) | 0.1.0 | Cristi Pufu | CLI and stdio ACP bridge server for Claude Code, OpenAI Codex, Grok, and Google… |
| 2026-10-26 13:50:09 | [Acplite.Sdk](https://www.nuget.org/packages/Acplite.Sdk) | 0.1.0 | Cristi Pufu | Native C# / NativeAOT Agent Client Protocol (ACP) SDK and provider bridges for… |
| 2026-10-26 13:52:17 | [JsonRepairNet](https://www.nuget.org/packages/JsonRepairNet) | 0.1.0 | composehk | Unofficial .NET port of json_repair: Repair malformed JSON from LLMs, APIs, and… |
| 2026-10-26 13:52:19 | [JsonRepairNet.Cli](https://www.nuget.org/packages/JsonRepairNet.Cli) | 0.1.0 | composehk | Unofficial .NET port of json_repair: Dotnet tool that repairs malformed JSON. C… |
| 2026-10-26 13:56:56 | [EBitSaaS.DynamicCrud](https://www.nuget.org/packages/EBitSaaS.DynamicCrud) | 0.0.1 | System Administrator | Core services and infrastructure for EBit SaaS platform for dynamic CRUD operat… |
| 2026-10-26 14:12:44 | [Dynatrace.OpenFeature](https://www.nuget.org/packages/Dynatrace.OpenFeature) | 0.0.2-alpha | Dynatrace | The official Dynatrace OpenFeature provider for .NET. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
