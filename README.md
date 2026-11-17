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

## Latest list — 2026-11-17 05:19 UTC

New packages created between 2026-11-17 04:18 UTC and 2026-11-17 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T05-19-09-994413Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 04:24:35 | [MattEland.HopeLab.Git](https://www.nuget.org/packages/MattEland.HopeLab.Git) | 0.1.10 | Matt Eland | A wrapper over the git CLI for the HopeLab apps: porcelain v2 status, worktree… |
| 2026-11-17 04:24:36 | [MattEland.HopeLab.Updates.ReactiveUI](https://www.nuget.org/packages/MattEland.HopeLab.Updates.ReactiveUI) | 0.1.10 | Matt Eland | The update view model the HopeLab desktop apps share (ReactiveUI, no UI framewo… |
| 2026-11-17 04:24:37 | [MattEland.HopeLab.Updates](https://www.nuget.org/packages/MattEland.HopeLab.Updates) | 0.1.10 | Matt Eland | Updates for apps released on GitHub: latest.json manifests, version checks, pri… |
| 2026-11-17 04:24:38 | [MattEland.HopeLab.Common](https://www.nuget.org/packages/MattEland.HopeLab.Common) | 0.1.10 | Matt Eland | Small building blocks shared by the HopeLab apps: Result<T> and Unit, a clock a… |
| 2026-11-17 04:55:39 | [Manifest.Client.Core](https://www.nuget.org/packages/Manifest.Client.Core) | 1.0.0 | Analytics Consulting | Contracts for the Manifest client: the IManifestClient abstraction, request and… |
| 2026-11-17 04:55:40 | [Manifest.Client.Http](https://www.nuget.org/packages/Manifest.Client.Http) | 1.0.0 | Analytics Consulting | The System.Net implementation of the Manifest client (Manifest.Client.Core): Ht… |
| 2026-11-17 05:09:56 | [IntelligenceBank.OptimizelyCMS13](https://www.nuget.org/packages/IntelligenceBank.OptimizelyCMS13) | 3.0.0 | IntelligenceBank | The IntelligenceBank connector for Optimizely CMS 13. On CMS 12, use Intelligen… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
