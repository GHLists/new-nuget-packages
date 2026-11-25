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

## Latest list — 2026-11-25 09:20 UTC

New packages created between 2026-11-25 08:21 UTC and 2026-11-25 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T09-20-21-371571Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 08:29:57 | [MetaEngine.Dart.OpenApi.Dio](https://www.nuget.org/packages/MetaEngine.Dart.OpenApi.Dio) | 0.0.1 | Jose A. Saldana Perez | Convert OpenAPI specifications to Dart Dio HTTP clients with hand-written fromJ… |
| 2026-11-25 08:30:32 | [Nodalir](https://www.nuget.org/packages/Nodalir) | 0.0.1 | Nodalir | Nodalir — MEP & BIM engineering automation library for .NET and Revit (early pr… |
| 2026-11-25 08:39:44 | [Hlibz.UseCases](https://www.nuget.org/packages/Hlibz.UseCases) | 1.0.0 | Hlib Zinchenko | Use cases for .NET apps with several clients (HTTP endpoints, MCP tools, gRPC s… |
| 2026-11-25 08:49:36 | [Hlibz.OpenApi.UseCases](https://www.nuget.org/packages/Hlibz.OpenApi.UseCases) | 1.1.0 | Hlib Zinchenko | Publishes Hlibz.UseCases in OpenAPI documents built with Microsoft.AspNetCore.O… |
| 2026-11-25 08:49:37 | [Hlibz.OpenApi.Paging](https://www.nuget.org/packages/Hlibz.OpenApi.Paging) | 1.1.0 | Hlib Zinchenko | Publishes Hlibz.Paging in OpenAPI documents built with Microsoft.AspNetCore.Ope… |
| 2026-11-25 08:54:39 | [Pengin1011.ModuleSdk](https://www.nuget.org/packages/Pengin1011.ModuleSdk) | 1.0.0 | JSTks24 | Build independent C# modules for the Pengin1011 Discord bot host. |
| 2026-11-25 08:57:21 | [SysML2.NET.Validation](https://www.nuget.org/packages/SysML2.NET.Validation) | 0.27.0 | Sam Gerené | A .NET implementation of the OMG SysML v2 REST/HTTP PSM request validators |
| 2026-11-25 09:04:03 | [Eagle.Mes.Core](https://www.nuget.org/packages/Eagle.Mes.Core) | 1.0.0 | Eagle MES | MES 通用基础库：MD5 与密码加密、Hex/MAC 处理、JSON 包装、日期时间工具、安全数学、集合扩展、Hangfire Cron 表达式、Licen… |
| 2026-11-25 09:04:32 | [RedBot.Tool](https://www.nuget.org/packages/RedBot.Tool) | 1.0.0 | RedBot Innovations | Reusable Windows Forms ROI and Measurement Toolbox with drawing, measurement, e… |
| 2026-11-25 09:05:22 | [JedPlotUtils.LiveCharts](https://www.nuget.org/packages/JedPlotUtils.LiveCharts) | 1.1.0 | Demortier Jeremy | Package Description |
| 2026-11-25 09:10:13 | [DCS.Translator](https://www.nuget.org/packages/DCS.Translator) | 1.1.0 | DCS | Lightweight multi-provider text translation library. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
