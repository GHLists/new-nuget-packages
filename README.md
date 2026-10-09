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

## Latest list — 2026-10-09 23:19 UTC

New packages created between 2026-10-09 22:22 UTC and 2026-10-09 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T23-19-15-126469Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 22:23:55 | [Packata-cli.linux-arm64](https://www.nuget.org/packages/Packata-cli.linux-arm64) | 0.45.0 | Cédric L. Charlier | Cross-platform command-line interface for Packata. |
| 2026-10-09 22:23:57 | [Packata-cli.linux-musl-arm64](https://www.nuget.org/packages/Packata-cli.linux-musl-arm64) | 0.45.0 | Cédric L. Charlier | Cross-platform command-line interface for Packata. |
| 2026-10-09 22:23:58 | [Packata-cli.linux-musl-x64](https://www.nuget.org/packages/Packata-cli.linux-musl-x64) | 0.45.0 | Cédric L. Charlier | Cross-platform command-line interface for Packata. |
| 2026-10-09 22:23:59 | [Packata-cli.linux-x64](https://www.nuget.org/packages/Packata-cli.linux-x64) | 0.45.0 | Cédric L. Charlier | Cross-platform command-line interface for Packata. |
| 2026-10-09 22:24:00 | [Packata-cli.osx-arm64](https://www.nuget.org/packages/Packata-cli.osx-arm64) | 0.45.0 | Cédric L. Charlier | Cross-platform command-line interface for Packata. |
| 2026-10-09 22:24:01 | [Packata-cli.osx-x64](https://www.nuget.org/packages/Packata-cli.osx-x64) | 0.45.0 | Cédric L. Charlier | Cross-platform command-line interface for Packata. |
| 2026-10-09 22:24:03 | [Packata-cli.win-arm64](https://www.nuget.org/packages/Packata-cli.win-arm64) | 0.45.0 | Cédric L. Charlier | Cross-platform command-line interface for Packata. |
| 2026-10-09 22:24:04 | [Packata-cli.win-x64](https://www.nuget.org/packages/Packata-cli.win-x64) | 0.45.0 | Cédric L. Charlier | Cross-platform command-line interface for Packata. |
| 2026-10-09 22:32:22 | [ElBruno.AI.Decisions](https://www.nuget.org/packages/ElBruno.AI.Decisions) | 0.6.1 | Bruno Capuano (ElBruno) | Provider-neutral .NET 10 abstractions for AI decision models: Choice, Score, an… |
| 2026-10-09 22:32:23 | [ElBruno.AI.Decisions.Jev](https://www.nuget.org/packages/ElBruno.AI.Decisions.Jev) | 0.6.1 | Bruno Capuano (ElBruno) | Tentative early-access .NET 10 client for TypeSafe AI Jev and local Laya typed… |
| 2026-10-09 22:32:24 | [ElBruno.AI.Decisions.Foundry](https://www.nuget.org/packages/ElBruno.AI.Decisions.Foundry) | 0.6.1 | Bruno Capuano (ElBruno) | Microsoft-Decision-1 on Microsoft Foundry for ElBruno.AI.Decisions: Choice, Sco… |
| 2026-10-09 22:32:26 | [ElBruno.AI.Decisions.Ollama](https://www.nuget.org/packages/ElBruno.AI.Decisions.Ollama) | 0.6.1 | Bruno Capuano (ElBruno) | Local System One decision models for ElBruno.AI.Decisions through Ollama v0.35.… |
| 2026-10-09 22:54:14 | [AdminForge.EntityFrameworkCore](https://www.nuget.org/packages/AdminForge.EntityFrameworkCore) | 0.7.0 | Adam Verner | Serves AdminForge tables from an EF Core DbContext. |
| 2026-10-09 22:54:15 | [AdminForge.Mcp](https://www.nuget.org/packages/AdminForge.Mcp) | 0.7.0 | Adam Verner | Serves an AdminForge panel as MCP tools behind the panel's own OAuth. |
| 2026-10-09 23:03:46 | [AbpMcp](https://www.nuget.org/packages/AbpMcp) | 0.2.1-alpha | tekthar and abp-mcp contribut… | Auto-generates a Model Context Protocol (MCP) server from an ABP Framework appl… |
| 2026-10-09 23:10:09 | [Cendia.CMS](https://www.nuget.org/packages/Cendia.CMS) | 0.0.1 | Cendia | Placeholder. Cendia packages are not distributed on nuget.org. Add the Cendia f… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
