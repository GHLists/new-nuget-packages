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

## Latest list — 2026-10-19 00:22 UTC

New packages created between 2026-10-18 23:19 UTC and 2026-10-19 00:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T00-22-23-356956Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 23:35:22 | [PulseTrade.Comm.Mcp.Server](https://www.nuget.org/packages/PulseTrade.Comm.Mcp.Server) | 0.1.1 | PulseTrade | Archived PulseTrade.Comm MCP executable retained for migration and backend extr… |
| 2026-10-18 23:39:06 | [RebolParse](https://www.nuget.org/packages/RebolParse) | 0.2.0 | kealist | A REBOL-style parse dialect for C#. Match strings or lists of values with a flu… |
| 2026-10-18 23:54:30 | [SharpView.Export.Mermaid](https://www.nuget.org/packages/SharpView.Export.Mermaid) | 0.0.1 | Stanislav Tadtaev | Formats SharpView project maps and call diagrams as Mermaid flowcharts in Markd… |
| 2026-10-18 23:54:31 | [SharpView](https://www.nuget.org/packages/SharpView) | 0.0.1 | Stanislav Tadtaev | Source-backed analysis of ASP.NET Core Web APIs for people and agents: the MSBu… |
| 2026-10-18 23:54:32 | [SharpView.Core](https://www.nuget.org/packages/SharpView.Core) | 0.0.1 | Stanislav Tadtaev | Fact model and queries behind SharpView: call-graph reachability and paths, exc… |
| 2026-10-18 23:54:32 | [SharpView.Graph](https://www.nuget.org/packages/SharpView.Graph) | 0.0.1 | Stanislav Tadtaev | Small generic immutable directed multigraph for .NET: out/in edges, breadth-fir… |
| 2026-10-18 23:54:33 | [SharpView.Roslyn](https://www.nuget.org/packages/SharpView.Roslyn) | 0.0.1 | Stanislav Tadtaev | Loads .csproj, .sln and .slnx inputs with MSBuild and Roslyn and extracts the S… |
| 2026-10-18 23:55:08 | [Liturgy.Godot](https://www.nuget.org/packages/Liturgy.Godot) | 0.1.0 | Oddness | Attribute-based global hooks for Godot C#. Mark static methods with [Rite.OnRea… |
| 2026-10-18 23:58:12 | [IKVM.Templates](https://www.nuget.org/packages/IKVM.Templates) | 8.16.3 | Jeroen Frijters,Jerome Haltom | Templates for creating Java projects compiled to .NET by IKVM.NET.Sdk. |
| 2026-10-19 00:01:17 | [GetOpts.NET](https://www.nuget.org/packages/GetOpts.NET) | 1.3.0 | Latency McLaughlin | A callback-based program option parser for C#. |
| 2026-10-19 00:03:40 | [ZeroDev.Kora](https://www.nuget.org/packages/ZeroDev.Kora) | 3.1.1 | Zero Development | Official .NET SDK for Kora licensing |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
