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

## Latest list — 2026-10-27 11:20 UTC

New packages created between 2026-10-27 10:20 UTC and 2026-10-27 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T11-20-36-876684Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 10:35:04 | [Slotlock.Client](https://www.nuget.org/packages/Slotlock.Client) | 0.3.0 | Slotlock | A client for Slotlock's REST API: calendars AI agents cannot double-book. |
| 2026-10-27 10:40:52 | [DependencyInjection.Lifetime.Analyzers.Scan](https://www.nuget.org/packages/DependencyInjection.Lifetime.Analyzers.Scan) | 3.9.0 | George Wall | Scan any .NET solution for Microsoft.Extensions.DependencyInjection lifetime pr… |
| 2026-10-27 10:55:22 | [AuraORM](https://www.nuget.org/packages/AuraORM) | 0.1.0 | YUKIKEDA | A type-safe SQL query builder for .NET with predictable SQL, compatible with Na… |
| 2026-10-27 10:56:12 | [ZplCore](https://www.nuget.org/packages/ZplCore) | 1.0.0 | zplCore.com | zplCore.com – High Performance .NET Labelprint Engine. Cross-platform ZPL II /… |
| 2026-10-27 10:56:13 | [ZplCore.VectorLift](https://www.nuget.org/packages/ZplCore.VectorLift) | 1.0.0 | zplCore.com | zplCore.com Vector-Lift: converts PDF and SVG labels (e.g. carrier label PDFs)… |
| 2026-10-27 10:56:15 | [ZplCore.Testing](https://www.nuget.org/packages/ZplCore.Testing) | 1.0.0 | zplCore.com | zplCore.com Testing+: semantic label assertions for .NET tests (xUnit, NUnit, M… |
| 2026-10-27 10:56:17 | [ZplCore.Import.Print](https://www.nuget.org/packages/ZplCore.Import.Print) | 1.0.0 | zplCore.com | zplCore.com print import: turns what a Windows label program prints (the EMF pr… |
| 2026-10-27 10:56:19 | [ZplCore.Designer](https://www.nuget.org/packages/ZplCore.Designer) | 1.0.0 | zplCore.com | zplCore Designer – embeddable WYSIWYG label editor for ASP.NET Core: AddZplCore… |
| 2026-10-27 10:56:21 | [ZplCore.Designer.Blazor](https://www.nuget.org/packages/ZplCore.Designer.Blazor) | 1.0.0 | zplCore.com | zplCore Designer for Blazor – <ZplCoreDesigner @bind-Design="doc" Data="rows" B… |
| 2026-10-27 10:56:30 | [ZplCore.Cli](https://www.nuget.org/packages/ZplCore.Cli) | 1.0.0 | zplCore.com | Command line tool for zplCore.com (High Performance .NET Labelprint Engine): re… |
| 2026-10-27 10:56:36 | [ZplCore.Mcp](https://www.nuget.org/packages/ZplCore.Mcp) | 1.0.0 | zplCore.com | MCP server (Model Context Protocol, stdio only) for zplCore.com: lets coding ag… |
| 2026-10-27 11:00:10 | [WidgetStudio.Contracts](https://www.nuget.org/packages/WidgetStudio.Contracts) | 0.1.0 | Liesel Thuriot | System.Text.Json contracts for widgets rendered by widget-renderer. |
| 2026-10-27 11:00:32 | [FSharp.Windows.Dsl.Codegen](https://www.nuget.org/packages/FSharp.Windows.Dsl.Codegen) | 0.5.0 | contributors | Code generation tool for FSharp.Windows.Dsl — generates F# DSL wrappers from WP… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
