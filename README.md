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

## Latest list — 2026-10-14 01:21 UTC

New packages created between 2026-10-14 00:21 UTC and 2026-10-14 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T01-21-42-65511Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 00:28:51 | [ACM](https://www.nuget.org/packages/ACM) | 1.0.10 | ACM | Package Description |
| 2026-10-14 00:37:28 | [HunterAhlquist.Solo.Templates](https://www.nuget.org/packages/HunterAhlquist.Solo.Templates) | 1.9.0 | Hunter Ahlquist | Project templates for extensions to Solo, the self-hosted project management ap… |
| 2026-10-14 01:05:08 | [ShotDetector.Native](https://www.nuget.org/packages/ShotDetector.Native) | 2.1.0 | Jakob Boman | FFmpeg's shared libraries for ShotDetector and FrameReader on every platform: d… |
| 2026-10-14 01:13:26 | [VigorGlow.Dapr](https://www.nuget.org/packages/VigorGlow.Dapr) | 1.0.0 | VigorGlow | VigorGlow Dapr IoC 聚合模块，包含 Common、ProxyGenerator、Client、Server、Mesh 全部程序集 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
