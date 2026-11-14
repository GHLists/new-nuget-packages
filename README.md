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

## Latest list — 2026-11-14 05:18 UTC

New packages created between 2026-11-14 04:21 UTC and 2026-11-14 05:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T05-18-53-047682Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 04:35:09 | [FY.License.AspNetCore](https://www.nuget.org/packages/FY.License.AspNetCore) | 2.0.2 | FY.License.AspNetCore | FY 离线产品与模块授权的 .NET 10 ASP.NET Core 集成 |
| 2026-11-14 04:48:40 | [NativeMarkdown.Wpf](https://www.nuget.org/packages/NativeMarkdown.Wpf) | 1.0.1 | ClipSafe | A fast, native WPF Markdown renderer built on Markdig. Renders into a FlowDocum… |
| 2026-11-14 04:56:03 | [AuroraScienceHub.Integrations.DtuSpaceClient](https://www.nuget.org/packages/AuroraScienceHub.Integrations.DtuSpaceClient) | 1.9.0 | Aleksei Ermilov,Alexander Nik… | Provides HTTP client interfaces for accessing DTU Space (National Space Institu… |
| 2026-11-14 04:56:03 | [AuroraScienceHub.Integrations.FmiClient](https://www.nuget.org/packages/AuroraScienceHub.Integrations.FmiClient) | 1.9.0 | Aleksei Ermilov,Alexander Nik… | HTTP client for FMI real-time IU and IL electrojet indices |
| 2026-11-14 04:56:04 | [AuroraScienceHub.Integrations.WdcClient](https://www.nuget.org/packages/AuroraScienceHub.Integrations.WdcClient) | 1.9.0 | Aleksei Ermilov,Alexander Nik… | HTTP client for World Data Center for Geomagnetism, Kyoto real-time hourly Dst… |
| 2026-11-14 05:07:53 | [Ranvier.Persistence.KurrentDB.Traced](https://www.nuget.org/packages/Ranvier.Persistence.KurrentDB.Traced) | 0.1.1 | shayanhabibi | Small scoped snapshots in KurrentDB for Ranvier, with atomic batches and option… |
| 2026-11-14 05:07:53 | [Ranvier.Persistence.Marten](https://www.nuget.org/packages/Ranvier.Persistence.Marten) | 0.1.1 | shayanhabibi | Marten PostgreSQL state storage for Ranvier, with scoped records and optional o… |
| 2026-11-14 05:07:53 | [Ranvier.Persistence.Marten.Traced](https://www.nuget.org/packages/Ranvier.Persistence.Marten.Traced) | 0.1.1 | shayanhabibi | Marten PostgreSQL state storage for Ranvier, with scoped records and optional o… |
| 2026-11-14 05:07:54 | [Ranvier.Persistence.KurrentDB](https://www.nuget.org/packages/Ranvier.Persistence.KurrentDB) | 0.1.1 | shayanhabibi | Small scoped snapshots in KurrentDB for Ranvier, with atomic batches and option… |
| 2026-11-14 05:07:54 | [Ranvier.Persistence.Traced](https://www.nuget.org/packages/Ranvier.Persistence.Traced) | 0.1.1 | shayanhabibi | Keyed persisted inputs for Ranvier graphs: signals and keyed collections restor… |
| 2026-11-14 05:07:54 | [Ranvier.Persistence](https://www.nuget.org/packages/Ranvier.Persistence) | 0.1.1 | shayanhabibi | Keyed persisted inputs for Ranvier graphs: signals and keyed collections restor… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
