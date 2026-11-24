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

## Latest list — 2026-11-24 10:21 UTC

New packages created between 2026-11-24 09:19 UTC and 2026-11-24 10:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T10-21-00-511257Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 09:21:04 | [Fungusware.WinFormsThemes](https://www.nuget.org/packages/Fungusware.WinFormsThemes) | 2026.11.24.920 | Fungusware | Themes for WinForms apps: colour tokens, ready-made light and dark themes, in-p… |
| 2026-11-24 09:21:06 | [Fungusware.WinFormsThemes.Krypton](https://www.nuget.org/packages/Fungusware.WinFormsThemes.Krypton) | 2026.11.24.920 | Fungusware | Fungusware.WinFormsThemes for Krypton Toolkit: builds the Krypton palette (form… |
| 2026-11-24 09:21:09 | [Fungusware.WinFormsThemes.ObjectListView](https://www.nuget.org/packages/Fungusware.WinFormsThemes.ObjectListView) | 2026.11.24.920 | Fungusware | Fungusware.WinFormsThemes for ObjectListView: themed headers, selection colours… |
| 2026-11-24 09:21:11 | [Fungusware.WinFormsThemes.Editor](https://www.nuget.org/packages/Fungusware.WinFormsThemes.Editor) | 2026.11.24.920 | Fungusware | A fast, themeable WinForms code editor control with syntax highlighting, minima… |
| 2026-11-24 09:26:08 | [PinguApps.Playbook.win-x64](https://www.nuget.org/packages/PinguApps.Playbook.win-x64) | 1.1.0 | PinguApps | Original, offline .NET implementation recipes for coding agents over stdio MCP. |
| 2026-11-24 09:26:17 | [PinguApps.Playbook.win-arm64](https://www.nuget.org/packages/PinguApps.Playbook.win-arm64) | 1.1.0 | PinguApps | Original, offline .NET implementation recipes for coding agents over stdio MCP. |
| 2026-11-24 09:26:26 | [PinguApps.Playbook.osx-x64](https://www.nuget.org/packages/PinguApps.Playbook.osx-x64) | 1.1.0 | PinguApps | Original, offline .NET implementation recipes for coding agents over stdio MCP. |
| 2026-11-24 09:26:35 | [PinguApps.Playbook.osx-arm64](https://www.nuget.org/packages/PinguApps.Playbook.osx-arm64) | 1.1.0 | PinguApps | Original, offline .NET implementation recipes for coding agents over stdio MCP. |
| 2026-11-24 09:26:44 | [PinguApps.Playbook.linux-x64](https://www.nuget.org/packages/PinguApps.Playbook.linux-x64) | 1.1.0 | PinguApps | Original, offline .NET implementation recipes for coding agents over stdio MCP. |
| 2026-11-24 09:26:53 | [PinguApps.Playbook.linux-arm64](https://www.nuget.org/packages/PinguApps.Playbook.linux-arm64) | 1.1.0 | PinguApps | Original, offline .NET implementation recipes for coding agents over stdio MCP. |
| 2026-11-24 09:27:01 | [PinguApps.Playbook.any](https://www.nuget.org/packages/PinguApps.Playbook.any) | 1.1.0 | PinguApps | Original, offline .NET implementation recipes for coding agents over stdio MCP. |
| 2026-11-24 10:06:18 | [Waniwani.Relay](https://www.nuget.org/packages/Waniwani.Relay) | 0.7.1 | Waniwani | Records AI agent visits to your website and serves Waniwani agent pages. The co… |
| 2026-11-24 10:06:18 | [Waniwani.Relay.AspNetCore](https://www.nuget.org/packages/Waniwani.Relay.AspNetCore) | 0.7.1 | Waniwani | The Waniwani relay for ASP.NET Core. Middleware that records AI agent visits an… |
| 2026-11-24 10:06:19 | [Waniwani.Relay.AspNet](https://www.nuget.org/packages/Waniwani.Relay.AspNet) | 0.7.1 | Waniwani | The Waniwani relay for classic ASP.NET (System.Web) on IIS. An IHttpModule that… |
| 2026-11-24 10:08:00 | [InnovateSoftware.Promotions.Client](https://www.nuget.org/packages/InnovateSoftware.Promotions.Client) | 1.0.0 | Innovate Software | Client for the Integration API of Aliya Promotions & Loyalty: price carts, rese… |
| 2026-11-24 10:11:07 | [Credfeto.Git.Mcp](https://www.nuget.org/packages/Credfeto.Git.Mcp) | 0.0.3.71-read-only-… | Mark Ridgwell | Credfeto Git MCP server: a fixed set of git operations with validated inputs ov… |
| 2026-11-24 10:11:07 | [Credfeto.Git.Mcp.any](https://www.nuget.org/packages/Credfeto.Git.Mcp.any) | 0.0.3.71-read-only-… | Mark Ridgwell | Credfeto Git MCP server: a fixed set of git operations with validated inputs ov… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
