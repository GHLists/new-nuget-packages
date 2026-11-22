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

## Latest list — 2026-11-22 01:21 UTC

New packages created between 2026-11-22 00:20 UTC and 2026-11-22 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T01-21-05-589596Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 00:26:01 | [Besapi.MSBuild](https://www.nuget.org/packages/Besapi.MSBuild) | 2026.11.1 | Besapi | Build-time C# and TypeScript client generation from OpenAPI documents. |
| 2026-11-22 00:26:31 | [SparkplugNet.Extensions.Json](https://www.nuget.org/packages/SparkplugNet.Extensions.Json) | 1.5.0 | SeppPenner | JSON converters for Sparkplug B metrics using System.Text.Json or Newtonsoft.Js… |
| 2026-11-22 00:27:09 | [TaintSharp](https://www.nuget.org/packages/TaintSharp) | 1.0.0 | uwx | .NET bindings for taint, a SPIR-V to WGSL translator built on Google's Tint. |
| 2026-11-22 00:34:27 | [Mermaid.Terminal](https://www.nuget.org/packages/Mermaid.Terminal) | 0.5.0 | Mermaid.Terminal | Render Mermaid flowcharts and sequence diagrams to terminal text. A port of the… |
| 2026-11-22 01:05:57 | [Hansho](https://www.nuget.org/packages/Hansho) | 0.1.0 | Recodive | Official .NET client for a Hansho hub: pair users, define channels, templates a… |
| 2026-11-22 01:07:45 | [NoticeForge](https://www.nuget.org/packages/NoticeForge) | 0.1.0 | prota-p | Generates a third-party notices file from a .NET publish folder, using the orig… |
| 2026-11-22 01:08:50 | [No2SQL.win-x64](https://www.nuget.org/packages/No2SQL.win-x64) | 1.1.0 | Preet Talati | No2SQL MCP server that transforms MongoDB schemas into SQL schema scripts and E… |
| 2026-11-22 01:09:23 | [No2SQL.linux-arm64](https://www.nuget.org/packages/No2SQL.linux-arm64) | 1.1.0 | Preet Talati | No2SQL MCP server that transforms MongoDB schemas into SQL schema scripts and E… |
| 2026-11-22 01:09:44 | [No2SQL.osx-arm64](https://www.nuget.org/packages/No2SQL.osx-arm64) | 1.1.0 | Preet Talati | No2SQL MCP server that transforms MongoDB schemas into SQL schema scripts and E… |
| 2026-11-22 01:12:26 | [CSX.CliTool](https://www.nuget.org/packages/CSX.CliTool) | 1.0.0 | CSX.CliTool | Package Description |
| 2026-11-22 01:12:27 | [CSX.LanguageServer](https://www.nuget.org/packages/CSX.LanguageServer) | 1.0.0 | CSX.LanguageServer | Package Description |
| 2026-11-22 01:12:27 | [CSX.Parser](https://www.nuget.org/packages/CSX.Parser) | 1.0.0 | CSX.Parser | Package Description |
| 2026-11-22 01:12:28 | [CSX.Transformer](https://www.nuget.org/packages/CSX.Transformer) | 1.0.0 | CSX.Transformer | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
