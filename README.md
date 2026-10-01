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

## Latest list — 2026-10-01 18:22 UTC

New packages created between 2026-10-01 17:19 UTC and 2026-10-01 18:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T18-22-13-510655Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 17:20:15 | [LilyDesignSystem.Blazor.GanttChart](https://www.nuget.org/packages/LilyDesignSystem.Blazor.GanttChart) | 0.1.0 | Joel Parker Henderson | Lily Design System Blazor Gantt chart: a keyboard-accessible Gantt chart compos… |
| 2026-10-01 17:20:17 | [LilyDesignSystem.Blazor.KanbanBoard](https://www.nuget.org/packages/LilyDesignSystem.Blazor.KanbanBoard) | 0.1.0 | Joel Parker Henderson | Lily Design System Blazor kanban board: a keyboard-accessible kanban board comp… |
| 2026-10-01 17:24:04 | [ascii-video-player](https://www.nuget.org/packages/ascii-video-player) | 2.0.0 | Gustavo Victor | Toca vídeos no terminal em arte ASCII colorida, com o áudio sincronizado. Preci… |
| 2026-10-01 17:31:21 | [ShortifyKit](https://www.nuget.org/packages/ShortifyKit) | 100.42.1 | Absoluit | Typed .NET client for the Shortify URL-shortening API: API-key auth, short link… |
| 2026-10-01 17:34:12 | [Writeback](https://www.nuget.org/packages/Writeback) | 0.1.0 | Murat Ay | Persistence commands for Dapper: insert, update, delete and get with database-g… |
| 2026-10-01 17:34:12 | [Vex.Controls](https://www.nuget.org/packages/Vex.Controls) | 1.1.2.7 | 沙漠尽头的狼 | Vex product controls for Avalonia applications. |
| 2026-10-01 17:34:13 | [Writeback.PostgreSql](https://www.nuget.org/packages/Writeback.PostgreSql) | 0.1.0 | Murat Ay | Binary COPY bulk loading for Writeback entities on PostgreSQL. |
| 2026-10-01 17:34:14 | [Writeback.SqlServer](https://www.nuget.org/packages/Writeback.SqlServer) | 0.1.0 | Murat Ay | SqlBulkCopy-based bulk loading for Writeback entities. |
| 2026-10-01 17:34:14 | [Vex.Controls.Themes](https://www.nuget.org/packages/Vex.Controls.Themes) | 1.1.2.7 | 沙漠尽头的狼 | Theme resources for Vex.Controls. |
| 2026-10-01 17:45:48 | [Bennewitz.Ninja.AppServices.EntryPoint](https://www.nuget.org/packages/Bennewitz.Ninja.AppServices.EntryPoint) | 2026.4.1001 | Brian Bennewitz | One entry point for console, web and desktop apps: an unhandled exception is re… |
| 2026-10-01 18:02:21 | [ModelingEvolution.WeldingMachine.Seeed.Plugin](https://www.nuget.org/packages/ModelingEvolution.WeldingMachine.Seeed.Plugin) | 1.0.1 | ModelingEvolution | RocketWelder device plugin for a welding machine (e.g. a plasma cutter) whose o… |
| 2026-10-01 18:05:40 | [Sms.Mcp](https://www.nuget.org/packages/Sms.Mcp) | 0.0.2 | SuperJMN | Fully managed, cross-platform MCP server for debugging Sega Master System and G… |
| 2026-10-01 18:07:06 | [AppRights](https://www.nuget.org/packages/AppRights) | 1.1.0 | go | 基于 ASP.NET Core 的应用程序授权管理客户端 SDK，支持本地缓存、AES 加密、AOT 兼容 |
| 2026-10-01 18:11:32 | [ShieldLabs](https://www.nuget.org/packages/ShieldLabs) | 1.0.0 | ShieldLabs Inc. | Server SDK for ShieldLabs device intelligence and fraud detection: read identif… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
