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

## Latest list — 2026-11-22 11:20 UTC

New packages created between 2026-11-22 10:21 UTC and 2026-11-22 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T11-20-31-49902Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 10:22:25 | [Monstertacle.Hosting.Tool](https://www.nuget.org/packages/Monstertacle.Hosting.Tool) | 0.1.0 | Alexander Bleissem | Submit and recover Hosting MCP sessions from GitHub Actions. |
| 2026-11-22 10:29:45 | [OdinIranianIpg](https://www.nuget.org/packages/OdinIranianIpg) | 1.0.0 | Amindada021 | Extensible asynchronous Iranian payment gateway SDK for .NET 10. |
| 2026-11-22 10:34:01 | [Fostry.Branding](https://www.nuget.org/packages/Fostry.Branding) | 0.2.0 | Foste IT | The Fostry brand: its colours, light and dark palettes, the logo recoloured to… |
| 2026-11-22 10:34:02 | [Fostry.Client](https://www.nuget.org/packages/Fostry.Client) | 0.2.0 | Foste IT | A client for Fostry's API: scripts and their runs, agents, alerts and monitors,… |
| 2026-11-22 10:34:03 | [Fostry.SDK.Entra](https://www.nuget.org/packages/Fostry.SDK.Entra) | 0.2.0 | Foste IT | An app's own access to Microsoft Entra ID: its registration made from the app (… |
| 2026-11-22 10:34:04 | [Fostry.SDK.AspNetCore](https://www.nuget.org/packages/Fostry.SDK.AspNetCore) | 0.2.0 | Foste IT | An app Fostry hosts, in ASP.NET Core or Blazor Server: registering with Fostry,… |
| 2026-11-22 10:34:05 | [Fostry.Ui](https://www.nuget.org/packages/Fostry.Ui) | 0.2.0 | Foste IT | How a Fostry app looks, in Blazor and MudBlazor: the shell (rail and panel), se… |
| 2026-11-22 10:58:06 | [FCQRS.Analyzers](https://www.nuget.org/packages/FCQRS.Analyzers) | 1.0.0 | Onur Gumus | Warns when an FCQRS workflow body or aggregate fold reads the clock, a GUID gen… |
| 2026-11-22 11:09:06 | [Iyu.Notifications](https://www.nuget.org/packages/Iyu.Notifications) | 0.1.0 | iyulab | Host-neutral notification routing - events declared in code, recipients resolve… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
