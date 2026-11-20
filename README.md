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

## Latest list — 2026-11-20 07:21 UTC

New packages created between 2026-11-20 06:19 UTC and 2026-11-20 07:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T07-21-23-071769Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 06:20:32 | [TKCode.Arc.StreamMark](https://www.nuget.org/packages/TKCode.Arc.StreamMark) | 1.3.0 | TKCode.Arc contributors | StreamMark: streaming Markdown rendering for Avalonia, built for AI chat. The c… |
| 2026-11-20 06:20:33 | [TKCode.Arc.StreamMark.TextMate](https://www.nuget.org/packages/TKCode.Arc.StreamMark.TextMate) | 1.3.0 | TKCode.Arc contributors | TextMate-based incremental syntax highlighting for StreamMark code blocks (Text… |
| 2026-11-20 06:20:34 | [TKCode.Arc.StreamMark.RaTeX](https://www.nuget.org/packages/TKCode.Arc.StreamMark.RaTeX) | 1.3.0 | TKCode.Arc contributors | LaTeX math for StreamMark through the RaTeX native engine (KaTeX-compatible lay… |
| 2026-11-20 06:20:35 | [TKCode.Arc.StreamMark.Mermaid](https://www.nuget.org/packages/TKCode.Arc.StreamMark.Mermaid) | 1.3.0 | TKCode.Arc contributors | Mermaid diagrams for StreamMark (Mermaider and Svg.Skia), drawn without a brows… |
| 2026-11-20 06:45:48 | [Nikno.ApiResult](https://www.nuget.org/packages/Nikno.ApiResult) | 1.0.0 | Nikno | Unified API response result wrapper tool |
| 2026-11-20 06:53:53 | [VisioForge.CrossPlatform.RealSense.Windows.x64](https://www.nuget.org/packages/VisioForge.CrossPlatform.RealSense.Windows.x64) | 2026.11.17 | VisioForge | Intel RealSense depth camera support package for VisioForge .NET SDKs: colour,… |
| 2026-11-20 06:54:54 | [RazvanApps.McpServer.Blueprint](https://www.nuget.org/packages/RazvanApps.McpServer.Blueprint) | 1.0.0 | Razvan Mares | Production-ready .NET 10 MCP server blueprint with stdio and Streamable HTTP tr… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
