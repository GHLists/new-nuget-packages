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

## Latest list — 2026-11-01 10:18 UTC

New packages created between 2026-11-01 09:21 UTC and 2026-11-01 10:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T10-18-29-870124Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 09:24:10 | [Roslynaut](https://www.nuget.org/packages/Roslynaut) | 0.1.1 | Wesley Baartman | An MCP server that exposes Roslyn and MSBuild to agents: navigation, analysis,… |
| 2026-11-01 09:41:49 | [GroupDocs.Editor.Mcp](https://www.nuget.org/packages/GroupDocs.Editor.Mcp) | 26.10.0 | GroupDocs Contributors | MCP server for GroupDocs.Editor — edit Word, Excel, PowerPoint and PDF via HTML… |
| 2026-11-01 10:09:46 | [PocketCsvReader.SecurityLogs](https://www.nuget.org/packages/PocketCsvReader.SecurityLogs) | 2.60.0 | Cédric L. Charlier | Streaming CEF and LEEF security event readers for PocketCsvReader. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
