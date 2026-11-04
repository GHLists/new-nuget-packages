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

## Latest list — 2026-11-04 14:21 UTC

New packages created between 2026-11-04 13:19 UTC and 2026-11-04 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T14-21-39-418356Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 13:24:00 | [TaipanLang.Sdk](https://www.nuget.org/packages/TaipanLang.Sdk) | 0.4.0 | Discover Edge, LLC | The MSBuild project SDK that builds Taipan (.tpnproj) projects with dotnet buil… |
| 2026-11-04 13:24:01 | [TaipanLang](https://www.nuget.org/packages/TaipanLang) | 0.4.0 | Discover Edge, LLC | The Taipan compiler: a statically typed language with Python's syntax, compiled… |
| 2026-11-04 13:24:01 | [TaipanLang.Runtime](https://www.nuget.org/packages/TaipanLang.Runtime) | 0.4.0 | Discover Edge, LLC | The runtime library that programs compiled by Taipan reference. |
| 2026-11-04 13:31:32 | [Cilica.Core](https://www.nuget.org/packages/Cilica.Core) | 0.14.0-preview | hez2010,dubiousconst282 | Optimizer and intermediate representation for .NET IL. |
| 2026-11-04 13:31:32 | [Cilica.OptimizerTask](https://www.nuget.org/packages/Cilica.OptimizerTask) | 0.14.0-preview | hez2010,dubiousconst282 | MSBuild tasks for post-build IL optimization. |
| 2026-11-04 13:32:10 | [Kuestenlogik.Bowire.Interop](https://www.nuget.org/packages/Kuestenlogik.Bowire.Interop) | 2.10.0 | Kuestenlogik | Bowire interop — import Insomnia exports, Bruno collections and .http files int… |
| 2026-11-04 13:32:17 | [Kuestenlogik.Bowire.DataSets](https://www.nuget.org/packages/Kuestenlogik.Bowire.DataSets) | 2.10.0 | Kuestenlogik | Bowire data sets — parse CSV and JSON data files into rows for data-driven runs… |
| 2026-11-04 13:33:18 | [AppWeaver.Auditing](https://www.nuget.org/packages/AppWeaver.Auditing) | 1.0.0 | Team AppWeaver | Provider-agnostic auditing abstractions for the AppWeaver framework. Defines ma… |
| 2026-11-04 13:34:48 | [AppWeaver.Auditing.EfCore](https://www.nuget.org/packages/AppWeaver.Auditing.EfCore) | 1.0.0 | Team AppWeaver | EF Core provider implementation for AppWeaver.Auditing. Includes interceptors,… |
| 2026-11-04 13:35:32 | [Arc56.Generated.Shivanikinagi.Dehug](https://www.nuget.org/packages/Arc56.Generated.Shivanikinagi.Dehug) | 1.0.1.2026110413 | Shivanikinagi | Generated ARC-56 Algorand smart-contract clients for Shivanikinagi/Dehug. |
| 2026-11-04 13:40:27 | [HeartbeatScheduler](https://www.nuget.org/packages/HeartbeatScheduler) | 0.1.0 | Mark Hammond | Heartbeat scheduling for micro-task parallel loops: sequential by default, each… |
| 2026-11-04 13:41:48 | [Biz.Bizadm.MCP.ToolKit](https://www.nuget.org/packages/Biz.Bizadm.MCP.ToolKit) | 1.0.0 | SeongSikChae | ASP.NET Core MCP Server에 WithTools로 등록하는 Tool 모음 |
| 2026-11-04 13:43:39 | [Audis.Authentication.Hmac](https://www.nuget.org/packages/Audis.Authentication.Hmac) | 2.0.0 | softaware gmbh | HMAC mechanism for Audis.Authentication: inbound scheme wrapping softaware.Auth… |
| 2026-11-04 13:43:44 | [MusselSheet](https://www.nuget.org/packages/MusselSheet) | 0.0.1 | machi_pon | Excel-like input sheet for Blazor, made for keyboard and IME entry |
| 2026-11-04 13:43:52 | [Audis.Authentication.Jwt](https://www.nuget.org/packages/Audis.Authentication.Jwt) | 2.0.0 | softaware gmbh | JWT mechanism for Audis.Authentication based on Microsoft.AspNetCore.Authentica… |
| 2026-11-04 13:54:36 | [YngveHestem.Quill.Markdown](https://www.nuget.org/packages/YngveHestem.Quill.Markdown) | 1.0.0 | Yngve J. K. Hestem | This library contains DTO's and other abstractions that is used in YngveHestem.… |
| 2026-11-04 13:55:44 | [Anarchon.SqlServer](https://www.nuget.org/packages/Anarchon.SqlServer) | 0.6.1 | Aristotelis | SQL Server and Azure SQL backend for Anarchon, on Microsoft.Data.SqlClient: one… |
| 2026-11-04 13:57:32 | [alkpli.SkiaSharp.NativeAssets.Linux](https://www.nuget.org/packages/alkpli.SkiaSharp.NativeAssets.Linux) | 4.152.4 | Microsoft | SkiaSharp.NativeAssets.Linux provides native runtime assets for SkiaSharp. |
| 2026-11-04 13:58:46 | [ManoxCZ.Noesis.MonoGame](https://www.nuget.org/packages/ManoxCZ.Noesis.MonoGame) | 4.0.1-preview | ManoxCZ | NoesisUI integration into MonoGame framework using the "native" Noesis renderer… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
