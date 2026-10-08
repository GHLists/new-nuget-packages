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

## Latest list — 2026-10-08 21:19 UTC

New packages created between 2026-10-08 20:21 UTC and 2026-10-08 21:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T21-19-46-927662Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 20:21:20 | [Albatross.Collections](https://www.nuget.org/packages/Albatross.Collections) | 8.0.2 | Rushui Guan | Extension classes and data structures related to collections |
| 2026-10-08 20:21:21 | [Albatross.Collections.Intervals](https://www.nuget.org/packages/Albatross.Collections.Intervals) | 8.0.2 | Rushui Guan | An utility library for management of Continuous and non overlapping intervals. |
| 2026-10-08 20:21:24 | [MiniLibrary](https://www.nuget.org/packages/MiniLibrary) | 1.0.4 | dziezak | Mini library example |
| 2026-10-08 20:22:18 | [Narula.AI.SystemOne.SDK.Clef](https://www.nuget.org/packages/Narula.AI.SystemOne.SDK.Clef) | 1.0.0 | Narula | Provider-neutral .NET SDK for decision models (Cloudflare Clef via OpenRouter o… |
| 2026-10-08 20:44:02 | [RaiGuard.Analyzer](https://www.nuget.org/packages/RaiGuard.Analyzer) | 4.5.5 | Rainer Burkhardt | Opinionated Roslyn analyzer and code-fix provider enforcing framework physics a… |
| 2026-10-08 20:44:03 | [RaiGuard](https://www.nuget.org/packages/RaiGuard) | 4.5.5 | Rainer Burkhardt | Official .NET Global Tool CLI for RaiGuard opinionated Roslyn guardrails. Audit… |
| 2026-10-08 20:47:35 | [CodeSugar.System.SourceGenerator](https://www.nuget.org/packages/CodeSugar.System.SourceGenerator) | 1.0.0-Prv-20261008-… | Vicente Penades | Source generator that emits useful extension methods for: - System - System.Text |
| 2026-10-08 20:52:04 | [Csla.Testing](https://www.nuget.org/packages/Csla.Testing) | 10.2.0 | Marimer LLC | Supporting types for unit testing CSLA .NET business classes, business rules, a… |
| 2026-10-08 20:52:06 | [Csla.Avalonia](https://www.nuget.org/packages/Csla.Avalonia) | 10.2.0 | Marimer LLC | UI helpers for using CSLA .NET business types with Avalonia. |
| 2026-10-08 20:54:57 | [VenEl.MCP.FileManager](https://www.nuget.org/packages/VenEl.MCP.FileManager) | 1.0.1 | VenEl | An interactive, AI-powered file management MCP plugin. Bring your local file sy… |
| 2026-10-08 21:04:13 | [Icod.Pty](https://www.nuget.org/packages/Icod.Pty) | 1.0.0 | Timothy J. Bruce | Cross-platform pseudoterminal process hosting for .NET. |
| 2026-10-08 21:09:59 | [DevOp.DK.Plus](https://www.nuget.org/packages/DevOp.DK.Plus) | 0.2.0 | Þorvaldur Hafdal (DevOp) | Modern typed .NET client for the DK Plus v1 and v2 APIs. |
| 2026-10-08 21:13:57 | [ZBRA.MessageTrace.Client.Soap](https://www.nuget.org/packages/ZBRA.MessageTrace.Client.Soap) | 1.6.3 | ZBRA | SOAP (WCF) instrumentation for ZBRA MessageTrace. Install alongside ZBRA.Messag… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
