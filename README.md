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

## Latest list — 2026-10-05 10:20 UTC

New packages created between 2026-10-05 09:20 UTC and 2026-10-05 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T10-20-17-482757Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 09:58:23 | [A2v10.CheckUpdates](https://www.nuget.org/packages/A2v10.CheckUpdates) | 10.1.8668 | Oleksandr Kukhtin | A2v10: build-time warning when a newer platform generation is published |
| 2026-10-05 10:01:37 | [A2v10.Mcp](https://www.nuget.org/packages/A2v10.Mcp) | 10.1.8668 | Oleksandr Kukhtin | A2v10 MCP server with its OAuth authorization server |
| 2026-10-05 10:03:09 | [AgentMemory.Gate](https://www.nuget.org/packages/AgentMemory.Gate) | 1.9.0 | Jose Luis Latorre Millas | Experimental gate for AgentMemory for .NET: a judge at the fan-in that decides,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
