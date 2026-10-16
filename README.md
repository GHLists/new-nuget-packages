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

## Latest list — 2026-10-16 01:20 UTC

New packages created between 2026-10-16 00:19 UTC and 2026-10-16 01:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T01-20-44-859573Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 00:39:07 | [DotCourier.Caching.Redis](https://www.nuget.org/packages/DotCourier.Caching.Redis) | 0.12.0 | Valossa515 | Redis lock for DotCourier's [Idempotent] requests: a duplicate runs once even w… |
| 2026-10-16 00:42:30 | [MFT.LogFile](https://www.nuget.org/packages/MFT.LogFile) | 2026.10.1 | Eric R. Zimmerman | Parses NTFS $LogFile: restart areas, log record pages and NTFS log records (red… |
| 2026-10-16 00:44:03 | [sts2-mcp](https://www.nuget.org/packages/sts2-mcp) | 0.1.0 | PixeliciousLLC | MCP server for testing Slay the Spire 2 mods: launch local co-op test copies, r… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
