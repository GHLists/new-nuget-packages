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

## Latest list — 2026-10-12 01:19 UTC

New packages created between 2026-10-12 00:20 UTC and 2026-10-12 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T01-19-52-279837Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 00:21:54 | [Ourogen](https://www.nuget.org/packages/Ourogen) | 0.0.1-alpha | Scott Sanderson | Package Description |
| 2026-10-12 00:30:10 | [StaxiChat.Maui](https://www.nuget.org/packages/StaxiChat.Maui) | 1.0.0 | NhatNL | SDK chat Staxi cho MAUI: một WebView engine gắn cố định vào Grid của ứng dụng c… |
| 2026-10-12 01:02:24 | [VsMcpBridge](https://www.nuget.org/packages/VsMcpBridge) | 1.0.0 | ric-ros | MCP server that lets AI coding agents drive a running Visual Studio on Windows:… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
