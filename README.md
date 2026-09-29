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

## Latest list — 2026-09-29 23:21 UTC

New packages created between 2026-09-29 22:21 UTC and 2026-09-29 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T23-21-48-773282Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 22:54:27 | [FractalKVS](https://www.nuget.org/packages/FractalKVS) | 1.0.0 | alt160 | A .NET-native, file-backed durable dictionary for ulong keys and binary values,… |
| 2026-09-29 22:59:43 | [TKWF.Ext.SecurityLog.Abstractions](https://www.nuget.org/packages/TKWF.Ext.SecurityLog.Abstractions) | 0.1.0 | LoongBa.cn 龙爸出品 | TKWF 扩展抽象：安全日志契约（ISecurityLogStore/ISecurityLogQueryService/ISecurityLogAnalyti… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
