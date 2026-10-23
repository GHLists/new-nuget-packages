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

## Latest list — 2026-10-23 23:19 UTC

New packages created between 2026-10-23 22:21 UTC and 2026-10-23 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T23-19-18-02048Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 22:50:02 | [Goo.Audio](https://www.nuget.org/packages/Goo.Audio) | 0.12.0 | Xaz | Optional UI cues and bounded audio primitives for Goo. |
| 2026-10-23 23:05:16 | [Snail.MCP.CleanUp.any](https://www.nuget.org/packages/Snail.MCP.CleanUp.any) | 0.1.0 | orldev | Local MCP server that keeps account of what AI agents leave behind on a Mac — p… |
| 2026-10-23 23:05:17 | [Snail.MCP.CleanUp.linux-arm64](https://www.nuget.org/packages/Snail.MCP.CleanUp.linux-arm64) | 0.1.0 | orldev | Local MCP server that keeps account of what AI agents leave behind on a Mac — p… |
| 2026-10-23 23:05:19 | [Snail.MCP.CleanUp.linux-x64](https://www.nuget.org/packages/Snail.MCP.CleanUp.linux-x64) | 0.1.0 | orldev | Local MCP server that keeps account of what AI agents leave behind on a Mac — p… |
| 2026-10-23 23:05:20 | [Snail.MCP.CleanUp.osx-arm64](https://www.nuget.org/packages/Snail.MCP.CleanUp.osx-arm64) | 0.1.0 | orldev | Local MCP server that keeps account of what AI agents leave behind on a Mac — p… |
| 2026-10-23 23:05:21 | [Snail.MCP.CleanUp.osx-x64](https://www.nuget.org/packages/Snail.MCP.CleanUp.osx-x64) | 0.1.0 | orldev | Local MCP server that keeps account of what AI agents leave behind on a Mac — p… |
| 2026-10-23 23:05:22 | [Snail.MCP.CleanUp](https://www.nuget.org/packages/Snail.MCP.CleanUp) | 0.1.0 | orldev | Local MCP server that keeps account of what AI agents leave behind on a Mac — p… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
