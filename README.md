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

## Latest list — 2026-10-10 01:22 UTC

New packages created between 2026-10-10 00:19 UTC and 2026-10-10 01:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T01-22-02-242313Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 00:31:12 | [Widgentic.Mcp](https://www.nuget.org/packages/Widgentic.Mcp) | 0.9.0 | Diego Hoyos | BETA, render-only. widgentic widgets for .NET MCP servers: runs the published @… |
| 2026-10-10 00:48:21 | [PiSharp.Codemode](https://www.nuget.org/packages/PiSharp.Codemode) | 1.1.0.2 | PiSharp contributors | Codemode for PiSharp: model-written JavaScript in a Jint sandbox that calls the… |
| 2026-10-10 00:48:29 | [PiSharp.Tools.Skia](https://www.nuget.org/packages/PiSharp.Tools.Skia) | 1.1.0.2 | PiSharp contributors | SkiaSharp image codec for the PiSharp read tool: decoding, resizing and re-enco… |
| 2026-10-10 00:48:45 | [Tracepoint](https://www.nuget.org/packages/Tracepoint) | 0.1.0 | konnta0 | Declarative System.Diagnostics.Activity tracing for C# methods. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
