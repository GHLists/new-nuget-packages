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

## Latest list — 2026-11-20 03:20 UTC

New packages created between 2026-11-20 02:19 UTC and 2026-11-20 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T03-20-20-962418Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 02:43:20 | [LiteDriver.Orchestration](https://www.nuget.org/packages/LiteDriver.Orchestration) | 0.2.0 | cnefan31 | LiteDriver 的可视化功能编排库：基于 NanoServer 提供拖拽式编排页面，在线增删改客户端/服务端/协议节点，保存后热应用，无需重启后端服务。 |
| 2026-11-20 02:48:48 | [Seedream.ImagePairPlanner](https://www.nuget.org/packages/Seedream.ImagePairPlanner) | 0.1.0 | js-upup | Plan subject and background image pairs from a labeled manifest. Report missing… |
| 2026-11-20 03:02:30 | [NetApiFlow.Testing](https://www.nuget.org/packages/NetApiFlow.Testing) | 0.5.0 | Douglas Lima | Assertions over the flow a request actually took, for integration tests, such a… |
| 2026-11-20 03:12:09 | [EntityFramework5.Kdbndp](https://www.nuget.org/packages/EntityFramework5.Kdbndp) | 4.5.2.1120 | KingbaseES | 中电科金仓EF5驱动，sqlserver模式专用 |
| 2026-11-20 03:12:56 | [Seawave.DataBaseHelper](https://www.nuget.org/packages/Seawave.DataBaseHelper) | 1.0.0 | Seawave | Database helper library for .NET 8 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
