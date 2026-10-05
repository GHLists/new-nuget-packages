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

## Latest list — 2026-10-05 11:20 UTC

New packages created between 2026-10-05 10:20 UTC and 2026-10-05 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T11-20-08-880653Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 10:38:34 | [ShotDetector](https://www.nuget.org/packages/ShotDetector) | 0.1.0 | Jakob Boman | Shot/cut detection for video, a faithful C# port of PySceneDetect's ContentDete… |
| 2026-10-05 10:38:35 | [ShotDetector.FastYuv](https://www.nuget.org/packages/ShotDetector.FastYuv) | 0.1.0 | Jakob Boman | Optional fast path for ShotDetector: a bit-exact port of FFmpeg's yuv420p to BG… |
| 2026-10-05 10:43:13 | [ASTrio.ScanBridge](https://www.nuget.org/packages/ASTrio.ScanBridge) | 1.0.0 | ASTrio | A .NET library for integrating USB-COM/Serial and USB HID Keyboard barcode scan… |
| 2026-10-05 10:47:47 | [DCS.WebDav.AspNetCore.Server](https://www.nuget.org/packages/DCS.WebDav.AspNetCore.Server) | 1.0.0 | Daniel Calin Stanus | Fork of Dav.AspNetCore.Server (MIT) providing a WebDav implementation for ASP.N… |
| 2026-10-05 10:47:47 | [DCS.WebDav.AspNetCore.Server.Extensions.SqlServer](https://www.nuget.org/packages/DCS.WebDav.AspNetCore.Server.Extensions.SqlServer) | 1.0.0 | Daniel Calin Stanus | SQL Server lock manager and property store for DCS.WebDav.AspNetCore.Server. Ba… |
| 2026-10-05 10:47:48 | [DCS.WebDav.AspNetCore.Server.Extensions.Sqlite](https://www.nuget.org/packages/DCS.WebDav.AspNetCore.Server.Extensions.Sqlite) | 1.0.0 | Daniel Calin Stanus | SQLite lock manager and property store for DCS.WebDav.AspNetCore.Server. Based… |
| 2026-10-05 10:47:49 | [DCS.WebDav.AspNetCore.Server.Extensions.Npgsql](https://www.nuget.org/packages/DCS.WebDav.AspNetCore.Server.Extensions.Npgsql) | 1.0.0 | Daniel Calin Stanus | PostgreSQL (Npgsql) lock manager and property store for DCS.WebDav.AspNetCore.S… |
| 2026-10-05 10:55:53 | [Rewloy](https://www.nuget.org/packages/Rewloy) | 0.2.3 | Rewloy | The official .NET library for the Rewloy API (digital loyalty cards in Apple Wa… |
| 2026-10-05 10:57:41 | [PowerCLI](https://www.nuget.org/packages/PowerCLI) | 1.0.1 | Raffaele Rialdi (@raffaeler) | A console-independent interactive terminal library with fluent commands, quote-… |
| 2026-10-05 10:58:05 | [PowerCLI.AspNetCore](https://www.nuget.org/packages/PowerCLI.AspNetCore) | 1.0.1 | Raffaele Rialdi (@raffaeler) | Dependency injection registrations and a terminal background service for integr… |
| 2026-10-05 11:00:09 | [RS.DeLucru](https://www.nuget.org/packages/RS.DeLucru) | 1.2.0 | Romanian Software | RS.DeLucru |
| 2026-10-05 11:09:34 | [MiSeal.Core](https://www.nuget.org/packages/MiSeal.Core) | 2.2.1 | ck_yeun9 | 涉密信息加密工具（常用于证件号码、联系方式、住址等隐私信息），基于咖啡与网络(Java&Net) 的 EncryptTools 2.0.1.1（MIT）评估与… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
