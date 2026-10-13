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

## Latest list — 2026-10-13 05:19 UTC

New packages created between 2026-10-13 04:19 UTC and 2026-10-13 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T05-19-52-261695Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 04:32:32 | [Fleans.Plugins.CamundaExternalTask](https://www.nuget.org/packages/Fleans.Plugins.CamundaExternalTask) | 0.6.0 | nightBaker | Fleans Camunda 7 External Task compatibility plugin — queues <serviceTask type=… |
| 2026-10-13 04:36:11 | [Andras.Result](https://www.nuget.org/packages/Andras.Result) | 1.0.0 | André Melchior | Biblioteca compartilhada para implementação do Result Pattern em aplicações .NE… |
| 2026-10-13 04:55:44 | [Soenneker.TikTok.OpenApiClientUtil](https://www.nuget.org/packages/Soenneker.TikTok.OpenApiClientUtil) | 4.0.9 | Jake Soenneker | A thread-safe utility for obtaining TikTok's OpenApiClient singleton. |
| 2026-10-13 05:07:31 | [ISL.NetFramework.Payment.Driver](https://www.nuget.org/packages/ISL.NetFramework.Payment.Driver) | 1.0.0 | ISL.com | Single-package multi-gateway payment driver for ISL services: one-call registra… |
| 2026-10-13 05:14:06 | [EasyAdminBlazor.CodeGenerator](https://www.nuget.org/packages/EasyAdminBlazor.CodeGenerator) | 2.4.0 | gudufy | EasyAdminBlazor CRUD 代码生成器扩展 |
| 2026-10-13 05:14:08 | [EasyAdminBlazor.Print](https://www.nuget.org/packages/EasyAdminBlazor.Print) | 2.4.0 | gudufy | EasyAdminBlazor 打印模板与报表设计器扩展 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
