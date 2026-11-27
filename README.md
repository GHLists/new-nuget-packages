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

## Latest list — 2026-11-27 09:22 UTC

New packages created between 2026-11-27 08:21 UTC and 2026-11-27 09:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T09-22-31-607305Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 08:29:30 | [HaloDot.Core.Maui](https://www.nuget.org/packages/HaloDot.Core.Maui) | 0.1.0 | Halo Dot | Halo Dot tap-on-phone payments for .NET MAUI: the Halo.Core SDK bound to .NET,… |
| 2026-11-27 08:34:19 | [Stil.Mcp](https://www.nuget.org/packages/Stil.Mcp) | 1.3.0 | Ludvig Andersson | An MCP server for Stil: it gives AI assistants (Claude Code, GitHub Copilot, Cu… |
| 2026-11-27 08:41:35 | [Idora.NET.AspNetCore](https://www.nuget.org/packages/Idora.NET.AspNetCore) | 1.1.0 | Jake Seracino | ASP.NET Core support for Idora.NET's prefixed, time-ordered identifiers such as… |
| 2026-11-27 08:41:35 | [Idora.NET.EntityFrameworkCore](https://www.nuget.org/packages/Idora.NET.EntityFrameworkCore) | 1.1.0 | Jake Seracino | Entity Framework Core support for Idora.NET's prefixed, time-ordered identifier… |
| 2026-11-27 08:49:49 | [Lyrascale](https://www.nuget.org/packages/Lyrascale) | 1.104.7 | orlys | Unofficial .NET bindings that embed a Tailscale node (tsnet) in-process. Not af… |
| 2026-11-27 08:51:46 | [DotStat.SdmxStructureRegistry](https://www.nuget.org/packages/DotStat.SdmxStructureRegistry) | 31.1.0 | OECD | Client of the SDMX structure registry (NSI web service, FMR) shared by the .Sta… |
| 2026-11-27 08:56:08 | [Ark.Watch.Storage.MySql](https://www.nuget.org/packages/Ark.Watch.Storage.MySql) | 0.1.5 | Immanuel R | ARK-RAPID Watch on MySQL and MariaDB: a full query store (search, aggregations,… |
| 2026-11-27 08:56:09 | [Ark.Watch.Storage.Postgres](https://www.nuget.org/packages/Ark.Watch.Storage.Postgres) | 0.1.5 | Immanuel R | ARK-RAPID Watch on PostgreSQL: a full query store (search, aggregations, correl… |
| 2026-11-27 08:56:58 | [MessageQueueNET.Cmd](https://www.nuget.org/packages/MessageQueueNET.Cmd) | 4.26.4805 | Jürgen Gstaltmaier | Command line tool for the MessageQueueNET REST API. |
| 2026-11-27 08:59:28 | [OutWit.Controller.AI.Smt.Model](https://www.nuget.org/packages/OutWit.Controller.AI.Smt.Model) | 1.0.0 | Dmitry Ratner | The language layer and data types of the OutWit Smt controller: a strict SMT-LI… |
| 2026-11-27 09:05:02 | [AventusSharp.CSharpExport](https://www.nuget.org/packages/AventusSharp.CSharpExport) | 0.0.25 | Cobwebsite | Convert AventusSharp code to C# |
| 2026-11-27 09:05:17 | [OutWit.Controller.AI.Smt](https://www.nuget.org/packages/OutWit.Controller.AI.Smt) | 1.0.0 | Dmitry Ratner | SMT problems solved on anonymous nodes by a pinned Z3 that runs as a WebAssembl… |
| 2026-11-27 09:06:46 | [RenderApi.Client](https://www.nuget.org/packages/RenderApi.Client) | 1.0.0 | RenderApi | .NET client for the Render API (renderapi.com): render PDF, text/email and bool… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
