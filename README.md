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

## Latest list — 2026-11-26 14:21 UTC

New packages created between 2026-11-26 13:19 UTC and 2026-11-26 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T14-21-10-660068Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 13:25:42 | [Avig.Ord](https://www.nuget.org/packages/Avig.Ord) | 1.0.0 | Marcus Lindh | Read, write and edit Word .docx files: a streaming reader and writer, a documen… |
| 2026-11-26 13:26:15 | [Avig.Kalkyl](https://www.nuget.org/packages/Avig.Kalkyl) | 1.0.0 | Marcus Lindh | Read, write, edit and calculate Excel .xlsx files: typed lists through a source… |
| 2026-11-26 13:38:16 | [RepoStack.MongoDB](https://www.nuget.org/packages/RepoStack.MongoDB) | 0.0.1-alpha-2 | Dzmitry Pratsko | MongoDB provider and repository implementations for RepoStack. |
| 2026-11-26 13:38:17 | [RepoStack.PostgreSQL](https://www.nuget.org/packages/RepoStack.PostgreSQL) | 0.0.1-alpha-2 | Dzmitry Pratsko | PostgreSQL provider and repository implementations for RepoStack using Npgsql. |
| 2026-11-26 13:38:32 | [RepoStack.SqlServer](https://www.nuget.org/packages/RepoStack.SqlServer) | 0.0.1-alpha-2 | Dzmitry Pratsko | SQL Server provider and repository implementations for RepoStack using Microsof… |
| 2026-11-26 13:48:03 | [Traqio.Maui](https://www.nuget.org/packages/Traqio.Maui) | 0.1.0 | khufu.io | Traqio .NET MAUI SDK — deterministic install attribution (Play Install Referrer… |
| 2026-11-26 13:58:00 | [Tubatools.Crosshair](https://www.nuget.org/packages/Tubatools.Crosshair) | 1.4.0 | HuaTuo | 屏幕准星：在屏幕中央叠加置顶准星，支持十字、圆环、圆点三种形状与可选中心点，大小、粗细、间隙、中心点、不透明度均可滑块或精确数值输入，可存 3 套带备注的配置… |
| 2026-11-26 14:00:37 | [Dora.FastReport.OpenSource](https://www.nuget.org/packages/Dora.FastReport.OpenSource) | 1.0.0 | Hwx | Dora.FastReport.OpenSource |
| 2026-11-26 14:05:37 | [VisioForge.CrossPlatform.RealSense.Windows.arm64](https://www.nuget.org/packages/VisioForge.CrossPlatform.RealSense.Windows.arm64) | 2026.11.26 | VisioForge | Intel RealSense depth camera support package for VisioForge .NET SDKs: colour,… |
| 2026-11-26 14:08:26 | [RonSijm.MediumAPI.Analyser](https://www.nuget.org/packages/RonSijm.MediumAPI.Analyser) | 0.1.0 | RonSijm | Source generator, route analyzers and code fixes for RonSijm.MediumAPI. |
| 2026-11-26 14:08:26 | [RonSijm.MediumAPI](https://www.nuget.org/packages/RonSijm.MediumAPI) | 0.1.0 | RonSijm | A class-based endpoint framework for ASP.NET Core Minimal APIs. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
