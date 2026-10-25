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

## Latest list — 2026-10-25 06:22 UTC

New packages created between 2026-10-25 05:18 UTC and 2026-10-25 06:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T06-22-13-241461Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 05:27:40 | [LilyDesignSystem.Blazor.TimeZonePicker](https://www.nuget.org/packages/LilyDesignSystem.Blazor.TimeZonePicker) | 0.1.0 | Joel Parker Henderson | Lily Design System Blazor time zone picker: an icon button opening an APG listb… |
| 2026-10-25 05:28:52 | [Meziantou.Framework.WebPlatform.Playwright](https://www.nuget.org/packages/Meziantou.Framework.WebPlatform.Playwright) | 1.0.0 | meziantou | A Playwright server for Meziantou.Framework.WebPlatform: the Playwright clients… |
| 2026-10-25 05:28:54 | [Meziantou.Framework.WebPlatform.Playwright.Tool](https://www.nuget.org/packages/Meziantou.Framework.WebPlatform.Playwright.Tool) | 1.0.0 | meziantou | CLI that runs a Playwright server whose browser is Meziantou.Framework.WebPlatf… |
| 2026-10-25 05:32:16 | [Sharphy.Cli](https://www.nuget.org/packages/Sharphy.Cli) | 1.0.2 | Bahar Maulidi | Global CLI and MCP server executable bridge for Sharphy CLR Intelligence. |
| 2026-10-25 05:32:18 | [Sharphy.Core](https://www.nuget.org/packages/Sharphy.Core) | 1.0.2 | Bahar Maulidi | Core diagnostics, decompiler, ECMA-335 metadata, and CIL mutation engines for S… |
| 2026-10-25 05:32:19 | [Sharphy.Server](https://www.nuget.org/packages/Sharphy.Server) | 1.0.2 | Bahar Maulidi | Model Context Protocol (MCP) server dispatcher and protocol handlers for Sharph… |
| 2026-10-25 05:53:40 | [Egami.Video](https://www.nuget.org/packages/Egami.Video) | 1.0.0 | Lars Dytterud | A fully managed, MIT-licensed video and audio library for .NET built on Egami:… |
| 2026-10-25 06:14:12 | [Egami.Video.Cli](https://www.nuget.org/packages/Egami.Video.Cli) | 1.0.0 | Lars Dytterud | The egami-video command: inspect, remux, cut, join, export frames, make clips a… |
| 2026-10-25 06:15:52 | [Egami.Video.H264](https://www.nuget.org/packages/Egami.Video.H264) | 1.0.0 | Lars Dytterud | H.264 (AVC) decoding for Egami.Video, in managed code: progressive Constrained… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
