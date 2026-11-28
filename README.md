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

## Latest list — 2026-11-28 05:22 UTC

New packages created between 2026-11-28 04:21 UTC and 2026-11-28 05:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-28T05-22-05-710083Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-28 05:15:30 | [ClassPixelPro.Platforms.Abstractions](https://www.nuget.org/packages/ClassPixelPro.Platforms.Abstractions) | 2.0.0 | ClassPixelPro | ClassPixelPro 应用跨平台抽象基类。 |
| 2026-11-28 05:15:34 | [ClassPixelPro.Shared](https://www.nuget.org/packages/ClassPixelPro.Shared) | 2.0.0 | ClassPixelPro | ClassPixelPro 的核心共享库。 |
| 2026-11-28 05:15:35 | [ClassPixelPro.Shared.IPC](https://www.nuget.org/packages/ClassPixelPro.Shared.IPC) | 2.0.0 | ClassPixelPro | 用于的客户端与 ClassPixelPro 应用进行跨进程通信库。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
