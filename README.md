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

## Latest list — 2026-10-16 20:20 UTC

New packages created between 2026-10-16 19:20 UTC and 2026-10-16 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T20-20-24-753997Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 19:28:06 | [ColumnWeaver.NET](https://www.nuget.org/packages/ColumnWeaver.NET) | 1.0.0-beta | Hitesh Bhanushali | Client-specific object-to-string formatting for .NET Framework 4.8. Reuse one t… |
| 2026-10-16 19:46:49 | [DeployAngel.Hangfire](https://www.nuget.org/packages/DeployAngel.Hangfire) | 0.1.0 | Jordan Owens | DeployAngel for Hangfire: job runs, failures, running jobs, and recurring job s… |
| 2026-10-16 19:46:50 | [DeployAngel](https://www.nuget.org/packages/DeployAngel) | 0.1.0 | Jordan Owens | DeployAngel agent for ASP.NET Core: verifies every deploy from aggregated HTTP,… |
| 2026-10-16 19:46:50 | [DeployAngel.Tool](https://www.nuget.org/packages/DeployAngel.Tool) | 0.1.0 | Jordan Owens | The deployangel command and MCP server: check a deploy's verdict, register depl… |
| 2026-10-16 19:53:14 | [AbraxasDB](https://www.nuget.org/packages/AbraxasDB) | 1.0.0 | alt160 | An embedded, .NET-native object recordbase with durable records, maintained ind… |
| 2026-10-16 19:55:37 | [OSK.Petra.Godot.Acquisitions](https://www.nuget.org/packages/OSK.Petra.Godot.Acquisitions) | 0.1.0 | BlankDev117 | Provides an implementation for configuration and related data structures for Ac… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
