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

## Latest list — 2026-10-16 00:19 UTC

New packages created between 2026-10-15 23:21 UTC and 2026-10-16 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T00-19-16-834481Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 23:30:30 | [Couchbase.OperationalInsightsClient](https://www.nuget.org/packages/Couchbase.OperationalInsightsClient) | 1.0.0 | Couchbase, Inc. | The Official Couchbase OperationalInsights .NET SDK |
| 2026-10-15 23:35:00 | [OpenDebug.Net.linux-arm64](https://www.nuget.org/packages/OpenDebug.Net.linux-arm64) | 0.0.11 | OpenDebug.Net contributors | A fast Native AOT Debug Adapter Protocol server for live managed .NET processes. |
| 2026-10-15 23:35:01 | [OpenDebug.Net.osx-arm64](https://www.nuget.org/packages/OpenDebug.Net.osx-arm64) | 0.0.11 | OpenDebug.Net contributors | A fast Native AOT Debug Adapter Protocol server for live managed .NET processes. |
| 2026-10-15 23:35:02 | [OpenDebug.Net.osx-x64](https://www.nuget.org/packages/OpenDebug.Net.osx-x64) | 0.0.11 | OpenDebug.Net contributors | A fast Native AOT Debug Adapter Protocol server for live managed .NET processes. |
| 2026-10-15 23:35:03 | [OpenDebug.Net.win-arm64](https://www.nuget.org/packages/OpenDebug.Net.win-arm64) | 0.0.11 | OpenDebug.Net contributors | A fast Native AOT Debug Adapter Protocol server for live managed .NET processes. |
| 2026-10-15 23:35:04 | [OpenDebug.Net.win-x64](https://www.nuget.org/packages/OpenDebug.Net.win-x64) | 0.0.11 | OpenDebug.Net contributors | A fast Native AOT Debug Adapter Protocol server for live managed .NET processes. |
| 2026-10-15 23:42:53 | [DinaCSharp](https://www.nuget.org/packages/DinaCSharp) | 3.0.0 | LACOMBE Dominique | DinaCSharp est un framework développé par LACOMBE Dominique et réalisé à partir… |
| 2026-10-15 23:46:16 | [Soenneker.HuggingFace.HttpClients](https://www.nuget.org/packages/Soenneker.HuggingFace.HttpClients) | 4.0.1 | Jake Soenneker | A thread-safe singleton HttpClient for HuggingFace's OpenAPI integration. |
| 2026-10-15 23:48:20 | [Soenneker.HuggingFace.OpenApiClient](https://www.nuget.org/packages/Soenneker.HuggingFace.OpenApiClient) | 4.0.1 | Jake Soenneker | A generated OpenAPI client for the Hugging Face Hub API. |
| 2026-10-16 00:04:36 | [PDFjet](https://www.nuget.org/packages/PDFjet) | 9.0.9 | PDFjet Software | Fast, dependency-free PDF generation: text in many scripts with TrueType and Op… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
