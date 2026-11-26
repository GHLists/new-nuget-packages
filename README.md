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

## Latest list — 2026-11-26 08:21 UTC

New packages created between 2026-11-26 07:21 UTC and 2026-11-26 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T08-21-36-652113Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 07:26:02 | [Mermaider.Animate](https://www.nuget.org/packages/Mermaider.Animate) | 0.19.0 | Nullean and contributors | Animate Mermaid diagrams with a small score language: the author says what happ… |
| 2026-11-26 07:28:49 | [KupaKuper_Language](https://www.nuget.org/packages/KupaKuper_Language) | 1.0.0 | KupaKpuer | 一个使用本地语言包为基准的极简国际化文本支持包,适合小型项目的多语言切换支持 |
| 2026-11-26 07:32:11 | [Mediana.Codecs.Ffv1](https://www.nuget.org/packages/Mediana.Codecs.Ffv1) | 0.1.45 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-26 07:32:23 | [Mediana.Containers.Asf](https://www.nuget.org/packages/Mediana.Containers.Asf) | 0.1.45 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-26 07:34:10 | [Alder.Avalonia](https://www.nuget.org/packages/Alder.Avalonia) | 1.0.0-preview | Alder.Avalonia contributors | Native Avalonia controls for forms, colors, navigation, data display, and AI co… |
| 2026-11-26 07:44:47 | [DbLive.Testcontainers.PostgreSQL](https://www.nuget.org/packages/DbLive.Testcontainers.PostgreSQL) | 2.0.0 | ZACoders | Runs DbLive SQL tests against PostgreSQL in Docker (Testcontainers): a fixture… |
| 2026-11-26 07:44:47 | [DbLive.Testcontainers.MSSQL](https://www.nuget.org/packages/DbLive.Testcontainers.MSSQL) | 2.0.0 | ZACoders | Runs DbLive SQL tests against SQL Server in Docker (Testcontainers): a fixture… |
| 2026-11-26 07:44:49 | [DbLive.Templates](https://www.nuget.org/packages/DbLive.Templates) | 2.0.0 | ZACoders | dotnet new template for DbLive: "dotnet new dblive" creates a SQL Server or Pos… |
| 2026-11-26 07:57:42 | [Admin.NET.Plugin.Pro](https://www.nuget.org/packages/Admin.NET.Plugin.Pro) | 2.0.1 | cf | cf 通用开发平台 1.0.2 去除打包时配置文件，避免覆盖问题。 1.0.4 调试问题 1.0.5 修改基类字段名称，与老系统保持一致 1.0.7 swag… |
| 2026-11-26 08:00:44 | [OpenRobot.Edge.DcFrame](https://www.nuget.org/packages/OpenRobot.Edge.DcFrame) | 0.1.0 | OpenRobot | DC 原始帧本地接入契约：帧结构、二进制编解码、同机点对点服务端与客户端（NamedPipe / Unix Domain Socket）。 |
| 2026-11-26 08:03:21 | [OpenIGI.Releases](https://www.nuget.org/packages/OpenIGI.Releases) | 0.6.9 | OpenIGI Contributors | Package Description |
| 2026-11-26 08:05:31 | [Taskus.Core](https://www.nuget.org/packages/Taskus.Core) | 0.8.0 | vdasus | Task model, validation, mapping, sources and sinks of Taskus, a command-line to… |
| 2026-11-26 08:10:54 | [Hexalith.Folders.EventStoreExtensions](https://www.nuget.org/packages/Hexalith.Folders.EventStoreExtensions) | 2.1.0 | Hexalith Contributors | Folders' idempotency intent policies for the Hexalith EventStore extension API. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
