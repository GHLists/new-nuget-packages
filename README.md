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

## Latest list — 2026-10-28 00:18 UTC

New packages created between 2026-10-27 23:19 UTC and 2026-10-28 00:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T00-18-39-077823Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 23:26:54 | [Cronlight.Quartz.Dashboard.Mcp](https://www.nuget.org/packages/Cronlight.Quartz.Dashboard.Mcp) | 0.2.0 | Cronlight contributors | An MCP server for Cronlight: lets AI assistants (Claude, Copilot, any MCP clien… |
| 2026-10-27 23:35:20 | [RecursiveAI.OneGame.Pages](https://www.nuget.org/packages/RecursiveAI.OneGame.Pages) | 1.6.0 | Recursive AI, LLC | Draws OneRender pages (builder trees and HTML) through the render graph, with i… |
| 2026-10-27 23:39:52 | [Useful.TinyDB](https://www.nuget.org/packages/Useful.TinyDB) | 1.0.0 | pmpwsk | Cross-platform .NET library written in C# that allows you to persistently store… |
| 2026-10-27 23:46:10 | [Useful.TinyTUI](https://www.nuget.org/packages/Useful.TinyTUI) | 1.0.0 | pmpwsk | Cross-platform .NET library written in C# that allows you to create simple term… |
| 2026-10-28 00:01:17 | [Olve.TypeSpec](https://www.nuget.org/packages/Olve.TypeSpec) | 0.58.0 | Oliver Vea | Runtime for the C# minimal-API surface that @olivervea/typespec-csharp generate… |
| 2026-10-28 00:03:08 | [Stateflows.Extensions.Json](https://www.nuget.org/packages/Stateflows.Extensions.Json) | 0.22.0-beta | Stateflows | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
