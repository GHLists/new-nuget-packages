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

## Latest list — 2026-11-16 22:20 UTC

New packages created between 2026-11-16 21:19 UTC and 2026-11-16 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T22-20-58-606017Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 21:25:02 | [Meziantou.Framework.FileConversion.Tool](https://www.nuget.org/packages/Meziantou.Framework.FileConversion.Tool) | 1.0.0 | meziantou | CLI to convert files from one format to another: images, PDF, EPUB, Markdown, H… |
| 2026-11-16 21:26:52 | [LilyDesignSystem.Blazor.ColorPicker](https://www.nuget.org/packages/LilyDesignSystem.Blazor.ColorPicker) | 0.1.0 | Joel Parker Henderson | Lily Design System Blazor colour picker: recent colours, a palette of swatches… |
| 2026-11-16 21:30:44 | [CacheAside](https://www.nuget.org/packages/CacheAside) | 1.0.0 | Emmanuel Ajibodu | Attribute-driven cache-aside for .NET. Put [Cacheable] and [CacheEvict] on inte… |
| 2026-11-16 21:34:16 | [Scotec.WindowPlacement](https://www.nuget.org/packages/Scotec.WindowPlacement) | 1.0.0 | scotec Software Solutions AB | Package Description |
| 2026-11-16 21:34:16 | [Scotec.WindowPlacement.Avalonia](https://www.nuget.org/packages/Scotec.WindowPlacement.Avalonia) | 1.0.0 | scotec Software Solutions AB | Package Description |
| 2026-11-16 21:34:16 | [Scotec.WindowPlacement.Wpf](https://www.nuget.org/packages/Scotec.WindowPlacement.Wpf) | 1.0.0 | scotec Software Solutions AB | Package Description |
| 2026-11-16 21:52:23 | [Akka.Reminders](https://www.nuget.org/packages/Akka.Reminders) | 1.5.75 | Akka.NET Team | Durable, re-entrant reminders system for Akka.Cluster.Sharding. |
| 2026-11-16 21:52:24 | [Akka.Reminders.PostgreSql](https://www.nuget.org/packages/Akka.Reminders.PostgreSql) | 1.5.75 | Akka.NET Team | PostgreSQL storage implementation for Akka.Reminders. |
| 2026-11-16 21:52:25 | [Akka.Reminders.Sql](https://www.nuget.org/packages/Akka.Reminders.Sql) | 1.5.75 | Akka.NET Team | Compatibility package for SQL Server, PostgreSQL, and SQLite storage in Akka.Re… |
| 2026-11-16 21:52:25 | [Akka.Reminders.Sqlite](https://www.nuget.org/packages/Akka.Reminders.Sqlite) | 1.5.75 | Akka.NET Team | SQLite storage implementation for Akka.Reminders. |
| 2026-11-16 21:52:26 | [Akka.Reminders.SqlServer](https://www.nuget.org/packages/Akka.Reminders.SqlServer) | 1.5.75 | Akka.NET Team | SQL Server storage implementation for Akka.Reminders. |
| 2026-11-16 22:04:37 | [D3sk.AgentCli](https://www.nuget.org/packages/D3sk.AgentCli) | 0.5.0 | neijix | Runs the AI coding CLIs (Claude Code, Cursor, Gemini, Copilot, Grok, OpenCode)… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
