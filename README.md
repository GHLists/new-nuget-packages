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

## Latest list — 2026-11-14 10:19 UTC

New packages created between 2026-11-14 09:19 UTC and 2026-11-14 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T10-19-04-720711Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 09:20:37 | [Ranvier.FSharp.Agent](https://www.nuget.org/packages/Ranvier.FSharp.Agent) | 0.1.0 | shayanhabibi | Semantic F# code analysis CLI and Model Context Protocol (MCP) server (`rfs`) b… |
| 2026-11-14 09:29:46 | [PgOutput2Json.ClickHouse](https://www.nuget.org/packages/PgOutput2Json.ClickHouse) | 2.0.0 | PgOutput2Json | PgOutput2Json.ClickHouse library uses logical replication to copy rows from Pos… |
| 2026-11-14 09:32:05 | [Ranvier.Css.View.Traced](https://www.nuget.org/packages/Ranvier.Css.View.Traced) | 0.1.1 | shayanhabibi | Typed CSS utility attributes and reactive style bindings for Ranvier.View. |
| 2026-11-14 09:32:05 | [Ranvier.Css.View](https://www.nuget.org/packages/Ranvier.Css.View) | 0.1.1 | shayanhabibi | Typed CSS utility attributes and reactive style bindings for Ranvier.View. |
| 2026-11-14 09:37:58 | [Ranvier.D5](https://www.nuget.org/packages/Ranvier.D5) | 0.1.0 | Ranvier contributors | Functional visualization foundations for F#: data, scales, geometry, layouts an… |
| 2026-11-14 09:37:59 | [Ranvier.D5.Charts](https://www.nuget.org/packages/Ranvier.D5.Charts) | 0.1.0 | Ranvier contributors | Pure functional chart compositions for Ranvier.D5. |
| 2026-11-14 09:38:00 | [Ranvier.D5.Charts.Traced](https://www.nuget.org/packages/Ranvier.D5.Charts.Traced) | 0.1.0 | Ranvier contributors | Pure functional chart compositions for Ranvier.D5. |
| 2026-11-14 09:38:01 | [Ranvier.D5.Geo](https://www.nuget.org/packages/Ranvier.D5.Geo) | 0.1.0 | Ranvier contributors | Functional geographic geometry and map projections for Ranvier.D5. |
| 2026-11-14 09:38:01 | [Ranvier.D5.Geo.Traced](https://www.nuget.org/packages/Ranvier.D5.Geo.Traced) | 0.1.0 | Ranvier contributors | Functional geographic geometry and map projections for Ranvier.D5. |
| 2026-11-14 09:38:02 | [Ranvier.D5.Traced](https://www.nuget.org/packages/Ranvier.D5.Traced) | 0.1.0 | Ranvier contributors | Functional visualization foundations for F#: data, scales, geometry, layouts an… |
| 2026-11-14 09:38:03 | [Ranvier.D5.View](https://www.nuget.org/packages/Ranvier.D5.View) | 0.1.0 | Ranvier contributors | Keyed native SVG rendering for Ranvier.D5 scenes using Ranvier.View. |
| 2026-11-14 09:38:03 | [Ranvier.D5.View.Traced](https://www.nuget.org/packages/Ranvier.D5.View.Traced) | 0.1.0 | Ranvier contributors | Keyed native SVG rendering for Ranvier.D5 scenes using Ranvier.View. |
| 2026-11-14 09:39:32 | [assembly-differ.skills](https://www.nuget.org/packages/assembly-differ.skills) | 1.0.0 | Nullean and contributors | The agent skill for the assembly-differ dotnet tool: how a coding agent finds o… |
| 2026-11-14 09:55:02 | [CmdWarden](https://www.nuget.org/packages/CmdWarden) | 0.12.0 | CmdWarden | CmdWarden CLI + Session Agent + Approval Gate helper (per-user). State under Lo… |
| 2026-11-14 09:55:25 | [ConstExpr](https://www.nuget.org/packages/ConstExpr) | 0.1.0 | James Hughes | C# compile-time expressions with Roslyn analysers and source generation. |
| 2026-11-14 09:57:46 | [GitSnapshotter](https://www.nuget.org/packages/GitSnapshotter) | 0.1.0 | BusHero | Take a snapshot of a git repository's branches, tags, remotes, HEAD and (option… |
| 2026-11-14 09:57:47 | [GitSnapshotter.Tool](https://www.nuget.org/packages/GitSnapshotter.Tool) | 0.1.0 | BusHero | Command-line tool that takes a snapshot of a git repository's branches, tags, r… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
