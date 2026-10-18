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

## Latest list — 2026-10-18 13:19 UTC

New packages created between 2026-10-18 12:19 UTC and 2026-10-18 13:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T13-19-44-680221Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 12:32:43 | [KeelMatrix.ResilienceSpec](https://www.nuget.org/packages/KeelMatrix.ResilienceSpec) | 0.1.0 | KeelMatrix | Verify how your real .NET HttpClient resilience chain retries, delays, times ou… |
| 2026-10-18 13:00:03 | [ErinnArrayQueue](https://www.nuget.org/packages/ErinnArrayQueue) | 1.0.0 | Molth Nevin | Bounded multi-producer, multi-consumer array queue with fixed capacity. |
| 2026-10-18 13:03:02 | [Novolis.IO.SystemMetrics](https://www.nuget.org/packages/Novolis.IO.SystemMetrics) | 2026.1.1.56 | Novolis | Cross-platform system resource inventory and time-series metrics capture. |
| 2026-10-18 13:11:57 | [Xingqiao.SDK.Tools](https://www.nuget.org/packages/Xingqiao.SDK.Tools) | 1.0.0-alpha | CuPhoenix | 提供智能体工具封装、工具集合管理、自动发现及 OpenAI Responses 工具定义导出。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
