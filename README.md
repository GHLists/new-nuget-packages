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

## Latest list — 2026-10-12 07:21 UTC

New packages created between 2026-10-12 06:20 UTC and 2026-10-12 07:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T07-21-15-525087Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 06:48:26 | [Plex.MassTransit](https://www.nuget.org/packages/Plex.MassTransit) | 8.0.3 | Tom Lee | A lightweight .NET 8 message bus library with pluggable transports (InMemory an… |
| 2026-10-12 07:06:20 | [PalindromeLibraryVisalini](https://www.nuget.org/packages/PalindromeLibraryVisalini) | 1.0.0 | Visalini | Package Description |
| 2026-10-12 07:08:00 | [LogCarverGuard.Local](https://www.nuget.org/packages/LogCarverGuard.Local) | 0.1.0 | Derek | Local MCP server that puts a statement guard, an optional read-only mode and an… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
