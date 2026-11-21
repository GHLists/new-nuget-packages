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

## Latest list — 2026-11-21 05:21 UTC

New packages created between 2026-11-21 04:19 UTC and 2026-11-21 05:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T05-21-18-962635Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 04:57:01 | [Meziantou.Framework.Graphviz](https://www.nuget.org/packages/Meziantou.Framework.Graphviz) | 1.0.0 | meziantou | Reads the DOT language of Graphviz into the flowcharts of Meziantou.Framework.D… |
| 2026-11-21 04:58:28 | [RetroAchievementsSharp.Cli](https://www.nuget.org/packages/RetroAchievementsSharp.Cli) | 1.1.0 | Peterson Fernandes,Pure Logic… | A cross-platform .NET tool for RetroAchievements hashing. Native C# port of the… |
| 2026-11-21 05:03:32 | [Kiji.Runtime.linux-x64](https://www.nuget.org/packages/Kiji.Runtime.linux-x64) | 0.8.0 | zzzkan | Precompiled code of Kiji for linux-x64. Restored with Kiji for a site that buil… |
| 2026-11-21 05:03:33 | [Kiji.Runtime.osx-arm64](https://www.nuget.org/packages/Kiji.Runtime.osx-arm64) | 0.8.0 | zzzkan | Precompiled code of Kiji for osx-arm64. Restored with Kiji for a site that buil… |
| 2026-11-21 05:03:34 | [Kiji.Runtime.linux-arm64](https://www.nuget.org/packages/Kiji.Runtime.linux-arm64) | 0.8.0 | zzzkan | Precompiled code of Kiji for linux-arm64. Restored with Kiji for a site that bu… |
| 2026-11-21 05:03:35 | [Kiji.Runtime.win-arm64](https://www.nuget.org/packages/Kiji.Runtime.win-arm64) | 0.8.0 | zzzkan | Precompiled code of Kiji for win-arm64. Restored with Kiji for a site that buil… |
| 2026-11-21 05:03:35 | [Kiji.Runtime.win-x64](https://www.nuget.org/packages/Kiji.Runtime.win-x64) | 0.8.0 | zzzkan | Precompiled code of Kiji for win-x64. Restored with Kiji for a site that builds… |
| 2026-11-21 05:03:36 | [Kiji.Runtime.osx-x64](https://www.nuget.org/packages/Kiji.Runtime.osx-x64) | 0.8.0 | zzzkan | Precompiled code of Kiji for osx-x64. Restored with Kiji for a site that builds… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
