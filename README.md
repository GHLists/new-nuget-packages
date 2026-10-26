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

## Latest list — 2026-10-26 09:21 UTC

New packages created between 2026-10-26 08:19 UTC and 2026-10-26 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T09-21-32-985809Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 08:24:08 | [McpFramework](https://www.nuget.org/packages/McpFramework) | 1.0.0 | McpFramework | 通用 MCP 框架：引用后把方法标成 [McpServerTool]，一行 McpServer.StartAsync 即可把任意 .NET 程序（Consol… |
| 2026-10-26 08:55:50 | [Juice.Storage.Azure](https://www.nuget.org/packages/Juice.Storage.Azure) | 10.3.0 | Creatorflow.io | Azure Blob Storage provider on backend |
| 2026-10-26 08:55:52 | [Juice.Storage.S3](https://www.nuget.org/packages/Juice.Storage.S3) | 10.3.0 | Creatorflow.io | Amazon S3 and S3 compatible (MinIO, Ceph...) storage provider on backend |
| 2026-10-26 08:58:04 | [Sortition](https://www.nuget.org/packages/Sortition) | 0.1.0 | Small Gear Lab,Marie | Fair, repeatable and verifiable random lotteries (draws without replacement). A… |
| 2026-10-26 09:01:18 | [Photino.Cerberus](https://www.nuget.org/packages/Photino.Cerberus) | 0.1.0 | txrbo | Custom window chrome for Photino.Blazor: title bar, resize borders, rounded cor… |
| 2026-10-26 09:02:16 | [Cerberus.UI](https://www.nuget.org/packages/Cerberus.UI) | 0.1.0 | txrbo | Blazor component library with light/dark theming: buttons, cards, forms, dialog… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
