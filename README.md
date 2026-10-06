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

## Latest list — 2026-10-06 01:21 UTC

New packages created between 2026-10-06 00:20 UTC and 2026-10-06 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T01-21-02-999869Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 00:27:47 | [WASU.SDK.FormEngine](https://www.nuget.org/packages/WASU.SDK.FormEngine) | 26.1006.8 | WASU.SDK.FormEngine | Package Description |
| 2026-10-06 00:31:39 | [EasyCheckBoxList](https://www.nuget.org/packages/EasyCheckBoxList) | 1.0.0 | EasyCheckBoxList | EasyCheckBoxList is an ASP.NET Core Tag Helper that transforms standard checkbo… |
| 2026-10-06 00:43:03 | [LsMsgPack.Mcp](https://www.nuget.org/packages/LsMsgPack.Mcp) | 2026.10.6.4 | Louis Somers | MsgPack for AI agents: an MCP server (stdio) and command line tool that decode… |
| 2026-10-06 00:56:40 | [CoreCli.DateTime](https://www.nuget.org/packages/CoreCli.DateTime) | 2.0.1 | Jan Ruhlaender | Format the current date and time from the command line. |
| 2026-10-06 00:56:41 | [CoreCli.IpInfo](https://www.nuget.org/packages/CoreCli.IpInfo) | 2.0.1 | Jan Ruhlaender | Show public and local IP addresses from the command line. |
| 2026-10-06 00:56:42 | [CoreCli.UpInfo](https://www.nuget.org/packages/CoreCli.UpInfo) | 2.0.1 | Jan Ruhlaender | Show system uptime and boot time from the command line. |
| 2026-10-06 01:07:30 | [Hymma.ZeroBounce](https://www.nuget.org/packages/Hymma.ZeroBounce) | 1.0.0 | Hymma | A modern .NET client library for the ZeroBounce email validation API (v2). Asyn… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
