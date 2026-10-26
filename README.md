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

## Latest list — 2026-10-26 10:21 UTC

New packages created between 2026-10-26 09:21 UTC and 2026-10-26 10:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T10-21-42-552433Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 09:23:08 | [Konstera.Sdk.Contexts](https://www.nuget.org/packages/Konstera.Sdk.Contexts) | 1.0.1 | Konstera | Typed constants for the Konstera Standard Context Pack v1 — canonical glossary… |
| 2026-10-26 09:43:29 | [ai-proxy.osx-arm64](https://www.nuget.org/packages/ai-proxy.osx-arm64) | 0.15.2 | Rafał Araszkiewicz | A machine-wide local HTTP(S) forward proxy that inspects canonical LLM provider… |
| 2026-10-26 09:43:31 | [ai-proxy.linux-x64](https://www.nuget.org/packages/ai-proxy.linux-x64) | 0.15.2 | Rafał Araszkiewicz | A machine-wide local HTTP(S) forward proxy that inspects canonical LLM provider… |
| 2026-10-26 09:43:33 | [ai-proxy.win-x64](https://www.nuget.org/packages/ai-proxy.win-x64) | 0.15.2 | Rafał Araszkiewicz | A machine-wide local HTTP(S) forward proxy that inspects canonical LLM provider… |
| 2026-10-26 09:43:36 | [ai-proxy.win-arm64](https://www.nuget.org/packages/ai-proxy.win-arm64) | 0.15.2 | Rafał Araszkiewicz | A machine-wide local HTTP(S) forward proxy that inspects canonical LLM provider… |
| 2026-10-26 09:43:39 | [ai-proxy.linux-arm64](https://www.nuget.org/packages/ai-proxy.linux-arm64) | 0.15.2 | Rafał Araszkiewicz | A machine-wide local HTTP(S) forward proxy that inspects canonical LLM provider… |
| 2026-10-26 09:43:42 | [ai-proxy.linux-musl-x64](https://www.nuget.org/packages/ai-proxy.linux-musl-x64) | 0.15.2 | Rafał Araszkiewicz | A machine-wide local HTTP(S) forward proxy that inspects canonical LLM provider… |
| 2026-10-26 09:43:44 | [ai-proxy](https://www.nuget.org/packages/ai-proxy) | 0.15.2 | Rafał Araszkiewicz | A machine-wide local HTTP(S) forward proxy that inspects canonical LLM provider… |
| 2026-10-26 09:46:10 | [Skyline.DataMiner.QAOps.Admin](https://www.nuget.org/packages/Skyline.DataMiner.QAOps.Admin) | 3.1.0-staging1 | SkylineCommunications | QAOps administrative access client |
| 2026-10-26 10:05:38 | [csharpc.linux-arm64](https://www.nuget.org/packages/csharpc.linux-arm64) | 0.1.0-spike | csharpc contributors | csharpc: a C# compiler front-end for LLVM (Roslyn -> LLVM IR -> native). |
| 2026-10-26 10:05:45 | [csharpc.linux-x64](https://www.nuget.org/packages/csharpc.linux-x64) | 0.1.0-spike | csharpc contributors | csharpc: a C# compiler front-end for LLVM (Roslyn -> LLVM IR -> native). |
| 2026-10-26 10:05:48 | [csharpc.osx-arm64](https://www.nuget.org/packages/csharpc.osx-arm64) | 0.1.0-spike | csharpc contributors | csharpc: a C# compiler front-end for LLVM (Roslyn -> LLVM IR -> native). |
| 2026-10-26 10:05:52 | [csharpc](https://www.nuget.org/packages/csharpc) | 0.1.0-spike | csharpc contributors | csharpc: a C# compiler front-end for LLVM (Roslyn -> LLVM IR -> native). RID-sp… |
| 2026-10-26 10:07:56 | [CodeAlta.Cli](https://www.nuget.org/packages/CodeAlta.Cli) | 2.1.0 | Alexandre Mutel | CodeAlta CLI: the CodeAlta harness without a window, for scripts, CI jobs, cont… |
| 2026-10-26 10:08:09 | [CodeAlta.Cli.linux-arm64](https://www.nuget.org/packages/CodeAlta.Cli.linux-arm64) | 2.1.0 | Alexandre Mutel | CodeAlta CLI: the CodeAlta harness without a window, for scripts, CI jobs, cont… |
| 2026-10-26 10:08:11 | [CodeAlta.Cli.linux-x64](https://www.nuget.org/packages/CodeAlta.Cli.linux-x64) | 2.1.0 | Alexandre Mutel | CodeAlta CLI: the CodeAlta harness without a window, for scripts, CI jobs, cont… |
| 2026-10-26 10:13:33 | [DcsvIo.D2.Pagination.EntityFrameworkCore](https://www.nuget.org/packages/DcsvIo.D2.Pagination.EntityFrameworkCore) | 0.6.8 | DCSV | EF Core multi-mode list-page helpers for D2 - SortCatalog and ToListPageAsync. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
