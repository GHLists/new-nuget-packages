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

## Latest list — 2026-10-26 04:21 UTC

New packages created between 2026-10-26 03:19 UTC and 2026-10-26 04:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T04-21-26-595062Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 03:37:39 | [Shiny.Maui.Controls.Foldables](https://www.nuget.org/packages/Shiny.Maui.Controls.Foldables) | 2.1.0-beta-0008 | Allan Ritchie | Fold and hinge posture for Shiny.Maui.Controls: built-in providers for Android… |
| 2026-10-26 03:53:08 | [EnvParse.Kit](https://www.nuget.org/packages/EnvParse.Kit) | 1.0.0 | Nick | Lightweight environment file loader for .NET |
| 2026-10-26 04:02:26 | [DotEnv.Lite](https://www.nuget.org/packages/DotEnv.Lite) | 1.0.0 | Nick | Lightweight environment file loader for .NET |
| 2026-10-26 04:02:29 | [Hardhat.Env](https://www.nuget.org/packages/Hardhat.Env) | 1.0.0 | Nick | Lightweight environment file loader for .NET |
| 2026-10-26 04:02:32 | [Mcp.EnvTools](https://www.nuget.org/packages/Mcp.EnvTools) | 1.0.0 | Nick | Layered configuration helper for .NET applications |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
