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

## Latest list — 2026-11-19 14:19 UTC

New packages created between 2026-11-19 13:22 UTC and 2026-11-19 14:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T14-19-07-951908Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 13:30:02 | [Msfp.Protocol](https://www.nuget.org/packages/Msfp.Protocol) | 0.1.0-preview | The MSFP contributors | MSFP, the Media Server Federation Protocol, version 1: the protocol's pieces (k… |
| 2026-11-19 13:30:03 | [Msfp.Engine](https://www.nuget.org/packages/Msfp.Engine) | 0.1.0-preview | The MSFP contributors | The MSFP engine: runs the Media Server Federation Protocol inside a media serve… |
| 2026-11-19 13:32:56 | [Sounding.Aspire.Hosting](https://www.nuget.org/packages/Sounding.Aspire.Hosting) | 1.0.0 | famda | An Aspire integration for Sounding: runs the Sounding dashboard and adds the So… |
| 2026-11-19 13:47:47 | [JonasRq.DatabaseMCP](https://www.nuget.org/packages/JonasRq.DatabaseMCP) | 0.1.0-beta | Jonas Requena | MCP server for database metadata and read-only queries. Current engine: SQL Ser… |
| 2026-11-19 13:49:16 | [ForEach.UI.Html.Abstractions](https://www.nuget.org/packages/ForEach.UI.Html.Abstractions) | 0.1.0 | For-Each Smederevo | IHtmlRenderer: the contract for turning untrusted HTML and markdown into safe H… |
| 2026-11-19 13:49:17 | [ForEach.UI.Html](https://www.nuget.org/packages/ForEach.UI.Html) | 0.1.0 | For-Each Smederevo | SafeHtmlRenderer: Markdig and an allow-list HtmlSanitizer behind IHtmlRenderer.… |
| 2026-11-19 13:50:33 | [HeartbeatStatus.FjzClient](https://www.nuget.org/packages/HeartbeatStatus.FjzClient) | 1.0.0 | guinanbei | 面向 .NET Framework 4.8 桌面应用的心跳状态写入库（无第三方依赖，单 DLL）。 |
| 2026-11-19 14:05:53 | [Vane.Logging](https://www.nuget.org/packages/Vane.Logging) | 1.0.0 | netcasewqs | A lightweight, high-performance logging library for .NET with zero external dep… |
| 2026-11-19 14:08:44 | [JamesTryand.DotnetCqrs.Edges.Nats](https://www.nuget.org/packages/JamesTryand.DotnetCqrs.Edges.Nats) | 0.46.0 | James Tryand | Carries a system's internal edges (eventmodelschema's coordinating document, ed… |
| 2026-11-19 14:09:02 | [Vane.Logging.Mel](https://www.nuget.org/packages/Vane.Logging.Mel) | 1.0.0 | netcasewqs | Microsoft.Extensions.Logging adapter for Vane.Logging, enabling Vane.Logging as… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
