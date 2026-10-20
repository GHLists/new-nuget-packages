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

## Latest list — 2026-10-20 11:22 UTC

New packages created between 2026-10-20 10:19 UTC and 2026-10-20 11:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T11-22-23-535985Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 10:30:56 | [FaceSign.SDK](https://www.nuget.org/packages/FaceSign.SDK) | 0.0.3 | FaceSign | Official FaceSign client SDK for .NET. |
| 2026-10-20 10:31:59 | [tryAGI.Inception](https://www.nuget.org/packages/tryAGI.Inception) | 0.1.0-dev | tryAGI and contributors | C# SDK for Inception Mercury chat, typed decisions, code autocomplete, and code… |
| 2026-10-20 10:34:52 | [GoPromotional.EventPlanner](https://www.nuget.org/packages/GoPromotional.EventPlanner) | 1.0.1 | GoPromotional | Event countdown, planning timeline, giveaway quantities and print order-by date… |
| 2026-10-20 10:35:19 | [GoPromotional.SipLog](https://www.nuget.org/packages/GoPromotional.SipLog) | 1.0.1 | GoPromotional | Daily water goal estimate and a simple hydration log with streaks. |
| 2026-10-20 10:35:42 | [GoPromotional.PackList](https://www.nuget.org/packages/GoPromotional.PackList) | 1.0.1 | GoPromotional | Packing checklists with templates, per-night quantities and a Markdown format. |
| 2026-10-20 10:36:06 | [GoPromotional.MugDay](https://www.nuget.org/packages/GoPromotional.MugDay) | 1.0.1 | GoPromotional | Caffeine tracker with half-life estimate, sleep-ready time and reusable-cup sta… |
| 2026-10-20 10:43:23 | [Corvus.Regex.Ecma262](https://www.nuget.org/packages/Corvus.Regex.Ecma262) | 1.0.0 | Endjin Limited | A drop-in replacement for System.Text.RegularExpressions that answers as ECMASc… |
| 2026-10-20 10:44:03 | [FuzzyRegex](https://www.nuget.org/packages/FuzzyRegex) | 1.0.0 | Gerard Howell | A .NET port of mrab-regex: a full-featured regex engine with fuzzy (approximate… |
| 2026-10-20 10:51:47 | [Setalabs.Sdk](https://www.nuget.org/packages/Setalabs.Sdk) | 1.0.0 | Setalabs | C# client for the Setalabs API gateway. |
| 2026-10-20 10:56:41 | [EasyChatz.Core](https://www.nuget.org/packages/EasyChatz.Core) | 1.0.0 | Matt Gordon | Models, service contracts and chat rules shared by the EasyChatz server and the… |
| 2026-10-20 10:56:59 | [EasyChatz.Data](https://www.nuget.org/packages/EasyChatz.Data) | 1.0.0 | Matt Gordon | Provider-agnostic data model for EasyChatz. Tables live in the chatz schema. |
| 2026-10-20 10:57:12 | [EasyChatz.Data.MySql](https://www.nuget.org/packages/EasyChatz.Data.MySql) | 1.0.0 | Matt Gordon | MySQL storage for EasyChatz. |
| 2026-10-20 10:57:28 | [EasyChatz.Data.Npgsql](https://www.nuget.org/packages/EasyChatz.Data.Npgsql) | 1.0.0 | Matt Gordon | PostgreSQL storage for EasyChatz. |
| 2026-10-20 10:57:42 | [EasyChatz.Data.Sql](https://www.nuget.org/packages/EasyChatz.Data.Sql) | 1.0.0 | Matt Gordon | SQL Server storage for EasyChatz. |
| 2026-10-20 10:57:55 | [EasyChatz.Data.Sqlite](https://www.nuget.org/packages/EasyChatz.Data.Sqlite) | 1.0.0 | Matt Gordon | SQLite storage for EasyChatz. |
| 2026-10-20 10:58:13 | [EasyChatz.Services](https://www.nuget.org/packages/EasyChatz.Services) | 1.0.0 | Matt Gordon | Services behind EasyChatz: rooms, direct messages and unread notifications. |
| 2026-10-20 10:58:32 | [EasyChatz.Components](https://www.nuget.org/packages/EasyChatz.Components) | 1.0.0 | Matt Gordon | Blazor chat UI. Drop it into a Blazor or MVC app, or publish EasyChatz.CustomEl… |
| 2026-10-20 10:58:44 | [EasyChatz.AspNetCore](https://www.nuget.org/packages/EasyChatz.AspNetCore) | 1.0.0 | Matt Gordon | Registers EasyChatz in an ASP.NET Core app and maps its HTTP API and SignalR hu… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
