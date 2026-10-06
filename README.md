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

## Latest list — 2026-10-06 03:21 UTC

New packages created between 2026-10-06 02:20 UTC and 2026-10-06 03:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T03-21-56-785574Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 02:23:31 | [TaskDaemon.Handler](https://www.nuget.org/packages/TaskDaemon.Handler) | 0.1.2 | Jonathan James | TaskDaemon handler SDK for C# |
| 2026-10-06 02:23:33 | [Kommander.RocksDB](https://www.nuget.org/packages/Kommander.RocksDB) | 11.8.1.9001 | Curiosity GmbH, Warren Falk | .NET bindings for RocksDB, including the matching native libraries for Linux, W… |
| 2026-10-06 02:28:30 | [Digger.Debugger.any](https://www.nuget.org/packages/Digger.Debugger.any) | 0.1.0 | Digger contributors | Debug Adapter Protocol server for .NET (CoreCLR) applications. |
| 2026-10-06 02:28:31 | [Digger.Debugger.linux-arm64](https://www.nuget.org/packages/Digger.Debugger.linux-arm64) | 0.1.0 | Digger contributors | Debug Adapter Protocol server for .NET (CoreCLR) applications. |
| 2026-10-06 02:28:33 | [Digger.Debugger.linux-x64](https://www.nuget.org/packages/Digger.Debugger.linux-x64) | 0.1.0 | Digger contributors | Debug Adapter Protocol server for .NET (CoreCLR) applications. |
| 2026-10-06 02:28:34 | [Digger.Debugger.osx-arm64](https://www.nuget.org/packages/Digger.Debugger.osx-arm64) | 0.1.0 | Digger contributors | Debug Adapter Protocol server for .NET (CoreCLR) applications. |
| 2026-10-06 02:28:35 | [Digger.Debugger.osx-x64](https://www.nuget.org/packages/Digger.Debugger.osx-x64) | 0.1.0 | Digger contributors | Debug Adapter Protocol server for .NET (CoreCLR) applications. |
| 2026-10-06 02:28:36 | [Digger.Debugger](https://www.nuget.org/packages/Digger.Debugger) | 0.1.0 | Digger contributors | Debug Adapter Protocol server for .NET (CoreCLR) applications. |
| 2026-10-06 02:28:39 | [StdUnit.Tags.WinUsbKeyboardCodeScanners](https://www.nuget.org/packages/StdUnit.Tags.WinUsbKeyboardCodeScanners) | 0.16.0 | StdUnit.Tags.WinUsbKeyboardCo… | Package Description |
| 2026-10-06 02:40:09 | [UnitSystem](https://www.nuget.org/packages/UnitSystem) | 1.0.0 | LateefKareem | A lightweight .NET library for converting units across length, mass, temperatur… |
| 2026-10-06 02:42:07 | [OSK.Extensions.Petra.Math.Provisions](https://www.nuget.org/packages/OSK.Extensions.Petra.Math.Provisions) | 0.1.0 | BlankDev117 | An extension that combines the math formulas with provisions to accomodate econ… |
| 2026-10-06 02:42:07 | [OSK.Petra.Math.Formulas](https://www.nuget.org/packages/OSK.Petra.Math.Formulas) | 0.1.0 | BlankDev117 | A set of math functions, formulas, and the like to help with math calculations… |
| 2026-10-06 02:44:27 | [dotnetreport.frontend](https://www.nuget.org/packages/dotnetreport.frontend) | 6.3.5 | Dotnet Report Builder | Front end only for Dotnet Report, the embedded analytics and ad-hoc reporting s… |
| 2026-10-06 02:44:28 | [dotnetreport.backend](https://www.nuget.org/packages/dotnetreport.backend) | 6.3.5 | Dotnet Report Builder | Back end only for Dotnet Report, the embedded analytics and ad-hoc reporting so… |
| 2026-10-06 02:51:50 | [Asteroid.Statuses.CompilerTools](https://www.nuget.org/packages/Asteroid.Statuses.CompilerTools) | 0.1.0 | Asteroid.Statuses.CompilerToo… | Source generator paired with Asteroid.Statuses variable declarations ([StatusDe… |
| 2026-10-06 03:01:01 | [Hs.LangSense](https://www.nuget.org/packages/Hs.LangSense) | 1.0.0 | Hs.LangSense Contributors | Practical multilingual text and value intelligence for .NET: conversion, normal… |
| 2026-10-06 03:10:54 | [SCScheduledPublish](https://www.nuget.org/packages/SCScheduledPublish) | 10.5.0 | Nehemiah Jeyakumar | Schedule publish and unpublish of Sitecore items. Items ship as Items as Resour… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
