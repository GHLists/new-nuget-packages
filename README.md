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

## Latest list — 2026-10-08 15:20 UTC

New packages created between 2026-10-08 14:24 UTC and 2026-10-08 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T15-20-25-584785Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 14:27:02 | [EvaluatedApplications.Blazier](https://www.nuget.org/packages/EvaluatedApplications.Blazier) | 1.0.0 | Evaluated Applications | Lazy, scaffold-first Blazor WebAssembly for static hosts. Generates static HTML… |
| 2026-10-08 14:31:42 | [Umbraco.Community.LogExplorer](https://www.nuget.org/packages/Umbraco.Community.LogExplorer) | 18.0.0 | Jack Stunell | A rich log explorer for the Umbraco backoffice and a drop-in replacement for th… |
| 2026-10-08 14:31:43 | [Umbraco.Community.LogExplorer.Core](https://www.nuget.org/packages/Umbraco.Community.LogExplorer.Core) | 18.0.0 | Jack Stunell | Provider contracts and shared logic for Umbraco Log Explorer. Reference this to… |
| 2026-10-08 14:31:55 | [tsr-StackedFlow](https://www.nuget.org/packages/tsr-StackedFlow) | 0.5.0 | tesuri | RPN like Stacked pipeline for F# |
| 2026-10-08 14:36:29 | [VersionControlService.TextDiff](https://www.nuget.org/packages/VersionControlService.TextDiff) | 0.2.0 | Caroline Ott | Pure incremental text decoding and scanning primitives for VersionControlServic… |
| 2026-10-08 14:39:29 | [TechStrap.Client](https://www.nuget.org/packages/TechStrap.Client) | 0.1.0 | Syntax Circus LLC | Client SDK for TechStrap: submit support tickets to a TechStrap API from any .N… |
| 2026-10-08 14:39:30 | [TechStrap.Contracts](https://www.nuget.org/packages/TechStrap.Contracts) | 0.1.0 | Syntax Circus LLC | Wire contracts for TechStrap: request and response types, header names, routes… |
| 2026-10-08 14:39:30 | [TechStrap.Client.Maui](https://www.nuget.org/packages/TechStrap.Client.Maui) | 0.1.0 | Syntax Circus LLC | Device and app metadata capture and a submit-ticket helper for MAUI apps, on to… |
| 2026-10-08 14:47:01 | [ariankordi.OpenCvSharp4.runtime.ios](https://www.nuget.org/packages/ariankordi.OpenCvSharp4.runtime.ios) | 4.13.0.20261007 | ariankordi | Internal implementation package for OpenCvSharp to work on ios-arm64 and iossim… |
| 2026-10-08 14:49:17 | [uSync.AI.Complete](https://www.nuget.org/packages/uSync.AI.Complete) | 17.0.0 | Kevin Jump | Push and pull Umbraco.AI settings, prompts and agents between servers with uSyn… |
| 2026-10-08 14:49:17 | [uSync.AI.Prompt](https://www.nuget.org/packages/uSync.AI.Prompt) | 17.0.0 | Kevin Jump | uSync handlers and serializers for Umbraco.AI.Prompt prompts. |
| 2026-10-08 14:55:44 | [uSync.Complete.AI](https://www.nuget.org/packages/uSync.Complete.AI) | 17.0.0 | Kevin Jump | uSync.Complete for Umbraco.AI. Installs uSync.AI plus publisher push/pull and a… |
| 2026-10-08 14:55:45 | [uSync.AI.Agent](https://www.nuget.org/packages/uSync.AI.Agent) | 17.0.0 | Kevin Jump | uSync handlers and serializers for Umbraco.AI.Agent agents. |
| 2026-10-08 14:55:46 | [uSync.AI.Sync](https://www.nuget.org/packages/uSync.AI.Sync) | 17.0.0 | Kevin Jump | uSync handlers and serializers for Umbraco.AI connections, profiles, contexts,… |
| 2026-10-08 14:55:47 | [uSync.AI](https://www.nuget.org/packages/uSync.AI) | 17.0.0 | Kevin Jump | uSync for Umbraco.AI. Installs settings, prompt and agent sync plus the uSync a… |
| 2026-10-08 14:55:47 | [uSync.AI.Tools](https://www.nuget.org/packages/uSync.AI.Tools) | 17.0.0 | Kevin Jump | Umbraco.AI agent tools that run uSync reports, exports and imports, gated by th… |
| 2026-10-08 14:59:40 | [Shylonamylo.Tui](https://www.nuget.org/packages/Shylonamylo.Tui) | 0.1.0 | Shylonamylo | Simple TUI framework |
| 2026-10-08 15:00:27 | [Corner49.Infra.Hangfire](https://www.nuget.org/packages/Corner49.Infra.Hangfire) | 10.0.150 | Corner49.Infra.Hangfire | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
