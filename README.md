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

## Latest list — 2026-10-12 02:20 UTC

New packages created between 2026-10-12 01:19 UTC and 2026-10-12 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T02-20-53-608594Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 01:25:19 | [YH_SDK_HX_CAMERA](https://www.nuget.org/packages/YH_SDK_HX_CAMERA) | 1.0.2 | YH_SDK_HX_CAMERA | Package Description |
| 2026-10-12 01:33:59 | [LogCarver.Mcp](https://www.nuget.org/packages/LogCarver.Mcp) | 0.1.0 | Derek | Read-only MCP server that recovers deleted SQL Server rows from the active tran… |
| 2026-10-12 02:01:00 | [Zeeq.Biome](https://www.nuget.org/packages/Zeeq.Biome) | 1.0.0 | Zeeq | Terse, readable test scenario setup: recreate your entity graph in miniature wi… |
| 2026-10-12 02:01:03 | [Zeeq.Biome.EntityFrameworkCore](https://www.nuget.org/packages/Zeeq.Biome.EntityFrameworkCore) | 1.0.0 | Zeeq | Entity Framework Core store for Zeeq.Biome: persist a biome's entity graph with… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
