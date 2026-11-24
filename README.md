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

## Latest list — 2026-11-24 11:22 UTC

New packages created between 2026-11-24 10:21 UTC and 2026-11-24 11:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T11-22-35-677059Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 10:21:45 | [Grimoire.Cli](https://www.nuget.org/packages/Grimoire.Cli) | 2.21.1 | Guilherme Branco Stracini | Command-line client for Grimoire, the self-hosted Vault & Configuration Manager… |
| 2026-11-24 10:30:55 | [Sphere10.Framework.Generators](https://www.nuget.org/packages/Sphere10.Framework.Generators) | 3.2.0 | Herman Schoenfeld | C# source generators for Sphere10 Framework that generate boilerplate at compil… |
| 2026-11-24 10:30:56 | [Sphere10.Framework.NUnit](https://www.nuget.org/packages/Sphere10.Framework.NUnit) | 3.2.0 | Herman Schoenfeld | NUnit extensions and test helpers for Sphere10 Framework projects. Provides reu… |
| 2026-11-24 10:30:57 | [Sphere10.Framework.NUnit.DB](https://www.nuget.org/packages/Sphere10.Framework.NUnit.DB) | 3.2.0 | Herman Schoenfeld | Database testing helpers for Sphere10.Framework.Data and provider packages usin… |
| 2026-11-24 10:30:57 | [Sphere10.Framework.Web](https://www.nuget.org/packages/Sphere10.Framework.Web) | 3.2.0 | Herman Schoenfeld | Web models and utilities independent of ASP.NET Core: HTML formatting, animatio… |
| 2026-11-24 10:30:59 | [Sphere10.Framework.Web.AspNetCore.Blazor](https://www.nuget.org/packages/Sphere10.Framework.Web.AspNetCore.Blazor) | 3.2.0 | Herman Schoenfeld | Sphere10 Framework Blazor components, application shells, dialogs, wizards and… |
| 2026-11-24 10:31:00 | [Sphere10.Framework.Web.AspNetCore.MVC](https://www.nuget.org/packages/Sphere10.Framework.Web.AspNetCore.MVC) | 3.2.0 | Herman Schoenfeld | ASP.NET Core MVC extensions for Sphere10 Framework: controllers, Razor HTML hel… |
| 2026-11-24 10:31:01 | [Sphere10.Framework.Web.VisualRenderer](https://www.nuget.org/packages/Sphere10.Framework.Web.VisualRenderer) | 3.2.0 | Herman Schoenfeld | Render an independent visual object model to HTML and plain text, using embedde… |
| 2026-11-24 10:31:04 | [Sphere10.Framework.Windows.Forms.DataVisualization](https://www.nuget.org/packages/Sphere10.Framework.Windows.Forms.DataVisualization) | 3.2.0 | Microsoft,.NET Foundation,Kir… | Windows Forms charting controls imported from the legacy Microsoft DataVisualiz… |
| 2026-11-24 10:31:11 | [Sphere10.Framework.Windows.Store](https://www.nuget.org/packages/Sphere10.Framework.Windows.Store) | 3.2.0 | Herman Schoenfeld | Windows Store distribution support for Sphere10 Framework applications. Provide… |
| 2026-11-24 10:42:33 | [Levelmaster.Client](https://www.nuget.org/packages/Levelmaster.Client) | 1.0.0 | J.W. Volschenk | .NET client for the Levelmaster realtime tank-telemetry stream. Authenticates w… |
| 2026-11-24 10:43:58 | [Zharp.Godot](https://www.nuget.org/packages/Zharp.Godot) | 0.2.0 | Zharp | Zharp for Godot .NET (C#) games, with the Zharp Godot addon: ZharpGodot.Start(t… |
| 2026-11-24 10:44:00 | [Zharp.Maui](https://www.nuget.org/packages/Zharp.Maui) | 0.2.0 | Zharp | Zharp for .NET MAUI: builder.UseZharp() reports crashes (saved to disk and sent… |
| 2026-11-24 10:44:01 | [Zharp.Windows](https://www.nuget.org/packages/Zharp.Windows) | 0.2.0 | Zharp | Zharp for WPF and Windows Forms apps: ZharpApp.Start() reports crashes (saved t… |
| 2026-11-24 10:46:33 | [Reglet.Mcp](https://www.nuget.org/packages/Reglet.Mcp) | 1.7.0 | Maik Rehder | MCP server for Reglet: lets AI agents create, convert, read, fill and validate… |
| 2026-11-24 10:48:17 | [LegacyMigrationScanner](https://www.nuget.org/packages/LegacyMigrationScanner) | 0.5.0 | Alex | dotnet tool that scans .NET Framework 4.x solutions and reports migration block… |
| 2026-11-24 10:48:18 | [LegacyMigrationScanner.Core](https://www.nuget.org/packages/LegacyMigrationScanner.Core) | 0.5.0 | Alex | Analysis engine of Legacy Migration Scanner: detects .NET Framework to modern .… |
| 2026-11-24 10:48:19 | [LegacyMigrationScanner.Mcp](https://www.nuget.org/packages/LegacyMigrationScanner.Mcp) | 0.5.0 | Alex | Model Context Protocol tools and prompts for Legacy Migration Scanner (hosted b… |
| 2026-11-24 10:59:45 | [Soenneker.Redis.Tunnels.WebSockets](https://www.nuget.org/packages/Soenneker.Redis.Tunnels.WebSockets) | 11.0.2 | Jake Soenneker | A WebSocket tunnel for StackExchange.Redis connections. |
| 2026-11-24 11:09:15 | [RaiCore.Pdf.Xfa](https://www.nuget.org/packages/RaiCore.Pdf.Xfa) | 1.2.0 | Mikkel Raicevic-Larsen | Render dynamic XFA forms (XML Forms Architecture, from Adobe LiveCycle Designer… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
