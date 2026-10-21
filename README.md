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

## Latest list — 2026-10-21 10:21 UTC

New packages created between 2026-10-21 09:21 UTC and 2026-10-21 10:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T10-21-51-098402Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 09:22:40 | [Zooper.Ant](https://www.nuget.org/packages/Zooper.Ant) | 1.0.0 | Daniel Martin | Caller-selected paging for .NET: continuable, counted and capped pages over any… |
| 2026-10-21 09:22:43 | [Zooper.Ant.AspNetCore](https://www.nuget.org/packages/Zooper.Ant.AspNetCore) | 1.0.0 | Daniel Martin | ASP.NET Core companion of Zooper.Ant: query binding for the five paging paramet… |
| 2026-10-21 09:24:53 | [Escorp.Atom.Web.Services](https://www.nuget.org/packages/Escorp.Atom.Web.Services) | 0.0.1 | Yuriy Yesin, Escorp Labs | Package Description |
| 2026-10-21 09:44:46 | [Frontmatec.Net.SqlServer](https://www.nuget.org/packages/Frontmatec.Net.SqlServer) | 2.0.6 | Frontmatec | A SQL Server endpoint for your application: return data from simple methods and… |
| 2026-10-21 09:45:12 | [AgentFrameworkToolkit.Codex](https://www.nuget.org/packages/AgentFrameworkToolkit.Codex) | 1.25.2 | Rasmus Wulff Jensen | Codex app-server coding agents for Microsoft Agent Framework. |
| 2026-10-21 09:49:51 | [Escorp.Atom.Web.Services.Proxies](https://www.nuget.org/packages/Escorp.Atom.Web.Services.Proxies) | 0.0.1 | Yuriy Yesin, Escorp Labs | Package Description |
| 2026-10-21 09:50:34 | [PictureSharp.Tiff](https://www.nuget.org/packages/PictureSharp.Tiff) | 0.3.0 | Artur Pelzak | TIFF format plugin for PictureSharp, written entirely in C#. No native dependen… |
| 2026-10-21 10:00:07 | [DiNet.CliToolkit](https://www.nuget.org/packages/DiNet.CliToolkit) | 0.0.1 | DifolderyXXL | Cli toolkit for One-command-call. Supports native DI. |
| 2026-10-21 10:06:10 | [ICOT.Core](https://www.nuget.org/packages/ICOT.Core) | 1.0.1 | ICOT.Core | Package Description |
| 2026-10-21 10:10:43 | [Vespertan.Ssms.AgentProxy.Contracts](https://www.nuget.org/packages/Vespertan.Ssms.AgentProxy.Contracts) | 1.0.0 | Vespertan | Shared SSMS Agent Proxy contracts, independent of SSMS and VS SDK. |
| 2026-10-21 10:11:06 | [Vespertan.Ssms.AgentProxy.Client](https://www.nuget.org/packages/Vespertan.Ssms.AgentProxy.Client) | 0.10.5 | Vespertan | Command-line client for SSMS results, Messages, timing, XML plans, SQL buffers,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
