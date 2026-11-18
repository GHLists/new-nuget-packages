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

## Latest list — 2026-11-18 21:20 UTC

New packages created between 2026-11-18 20:21 UTC and 2026-11-18 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T21-20-25-082954Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 20:22:04 | [HtmlToImageRenderer](https://www.nuget.org/packages/HtmlToImageRenderer) | 0.0.1 | Zveruga | Lightweight HTML5 + CSS renderer that rasterizes markup to PNG via SkiaSharp. |
| 2026-11-18 20:34:59 | [PowerShell.linux-arm](https://www.nuget.org/packages/PowerShell.linux-arm) | 7.7.0 | Microsoft | PowerShell global tool |
| 2026-11-18 20:35:02 | [PowerShell.linux-arm64](https://www.nuget.org/packages/PowerShell.linux-arm64) | 7.7.0 | Microsoft | PowerShell global tool |
| 2026-11-18 20:35:06 | [REDcat.Modding.TLD.ModSettings](https://www.nuget.org/packages/REDcat.Modding.TLD.ModSettings) | 2.2.6 | REDcat | Package Description |
| 2026-11-18 20:35:12 | [PowerShell.linux-musl-x64](https://www.nuget.org/packages/PowerShell.linux-musl-x64) | 7.7.0 | Microsoft | PowerShell global tool |
| 2026-11-18 20:35:15 | [PowerShell.linux-x64](https://www.nuget.org/packages/PowerShell.linux-x64) | 7.7.0 | Microsoft | PowerShell global tool |
| 2026-11-18 20:35:17 | [PowerShell.osx-arm64](https://www.nuget.org/packages/PowerShell.osx-arm64) | 7.7.0 | Microsoft | PowerShell global tool |
| 2026-11-18 20:35:20 | [PowerShell.osx-x64](https://www.nuget.org/packages/PowerShell.osx-x64) | 7.7.0 | Microsoft | PowerShell global tool |
| 2026-11-18 20:35:23 | [PowerShell.win-arm64](https://www.nuget.org/packages/PowerShell.win-arm64) | 7.7.0 | Microsoft | PowerShell global tool |
| 2026-11-18 20:35:27 | [PowerShell.win-x64](https://www.nuget.org/packages/PowerShell.win-x64) | 7.7.0 | Microsoft | PowerShell global tool |
| 2026-11-18 20:49:24 | [bitbucket-mcp.linux-x64](https://www.nuget.org/packages/bitbucket-mcp.linux-x64) | 1.4.0 | Marko Lahma | Model Context Protocol server for Bitbucket Cloud pull requests - list, read, d… |
| 2026-11-18 20:49:25 | [bitbucket-mcp.linux-arm64](https://www.nuget.org/packages/bitbucket-mcp.linux-arm64) | 1.4.0 | Marko Lahma | Model Context Protocol server for Bitbucket Cloud pull requests - list, read, d… |
| 2026-11-18 20:49:26 | [bitbucket-mcp.win-x64](https://www.nuget.org/packages/bitbucket-mcp.win-x64) | 1.4.0 | Marko Lahma | Model Context Protocol server for Bitbucket Cloud pull requests - list, read, d… |
| 2026-11-18 20:49:28 | [bitbucket-mcp.win-arm64](https://www.nuget.org/packages/bitbucket-mcp.win-arm64) | 1.4.0 | Marko Lahma | Model Context Protocol server for Bitbucket Cloud pull requests - list, read, d… |
| 2026-11-18 20:49:29 | [bitbucket-mcp.osx-arm64](https://www.nuget.org/packages/bitbucket-mcp.osx-arm64) | 1.4.0 | Marko Lahma | Model Context Protocol server for Bitbucket Cloud pull requests - list, read, d… |
| 2026-11-18 20:49:30 | [bitbucket-mcp.any](https://www.nuget.org/packages/bitbucket-mcp.any) | 1.4.0 | Marko Lahma | Model Context Protocol server for Bitbucket Cloud pull requests - list, read, d… |
| 2026-11-18 20:54:56 | [Jspassgen](https://www.nuget.org/packages/Jspassgen) | 0.0.22 | Sebastien Rousseau | Native .NET port of the jspassgen password generator core, on the platform CSPR… |
| 2026-11-18 21:04:10 | [MVAI.WebDAV.Update](https://www.nuget.org/packages/MVAI.WebDAV.Update) | 1.0.0-alpha | CuPhoenix | 从主源或备源进行 WebDAV 目录检查、校验并打开 Windows MSIX 或 Android APK 更新。 |
| 2026-11-18 21:06:35 | [EcoSQL.Request](https://www.nuget.org/packages/EcoSQL.Request) | 1.0.0 | Sleddie | Package Description |
| 2026-11-18 21:06:55 | [RecDiffy.Extensions](https://www.nuget.org/packages/RecDiffy.Extensions) | 1.2.0 | Michael Vaysman | Reconciliation for .NET: extension methods that return the result of a RecDiffy… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
