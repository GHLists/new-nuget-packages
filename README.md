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

## Latest list — 2026-11-12 12:21 UTC

New packages created between 2026-11-12 11:21 UTC and 2026-11-12 12:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T12-21-37-962235Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 11:29:27 | [AVCoders.SignalR.Audit](https://www.nuget.org/packages/AVCoders.SignalR.Audit) | 2026.11.1 | AV Coders | SignalR hub filter that audits every state-changing hub call with the calling p… |
| 2026-11-12 11:29:27 | [AVCoders.SignalR.Connections](https://www.nuget.org/packages/AVCoders.SignalR.Connections) | 2026.11.1 | AV Coders | Connection tracking and unknown-group reporting shared by the AV Coders SignalR… |
| 2026-11-12 11:39:28 | [Tubatools.NexBoxSkin](https://www.nuget.org/packages/Tubatools.NexBoxSkin) | 1.0.1 | 图吧工具箱 | NexBox 风格主界面皮肤：工具、硬件、优化、显示滤镜与三角洲专区；默认开启 |
| 2026-11-12 11:39:35 | [JT2Any](https://www.nuget.org/packages/JT2Any) | 2.0.0 | TunerDav | Local, managed JT tessellation conversion to GLB (glTF 2.0) and binary STL, wit… |
| 2026-11-12 11:41:27 | [Umbraco.Cms.Search.Extension.FileToText](https://www.nuget.org/packages/Umbraco.Cms.Search.Extension.FileToText) | 19.0.0-rc1 | Umbraco | Extends Umbraco Search with indexing of the text contents of files (such as PDF… |
| 2026-11-12 11:49:00 | [NtvLibs.cuda13.nvrtc-builtins64_135.runtime.json](https://www.nuget.org/packages/NtvLibs.cuda13.nvrtc-builtins64_135.runtime.json) | 13.5.0 | nietras | native library meta package |
| 2026-11-12 11:49:03 | [NtvLibs.cuda13.nvrtc-builtins64_135.runtime.win-x64](https://www.nuget.org/packages/NtvLibs.cuda13.nvrtc-builtins64_135.runtime.win-x64) | 13.5.0 | nietras | native library runtime specific package |
| 2026-11-12 11:49:50 | [CopybookKit](https://www.nuget.org/packages/CopybookKit) | 0.1.0 | muffindonor | Reads mainframe data files in .NET. Parses a COBOL copybook at run time and dec… |
| 2026-11-12 11:49:51 | [CopybookKit.Tool](https://www.nuget.org/packages/CopybookKit.Tool) | 0.1.0 | muffindonor | Command-line tool that converts mainframe data files to JSON Lines or CSV using… |
| 2026-11-12 11:50:05 | [TrendyolClient.Sharp](https://www.nuget.org/packages/TrendyolClient.Sharp) | 2.0.0 | bberka | TrendyolClient.Sharp is a simple Trendyol API Client for C# for .NET 8, .NET 9… |
| 2026-11-12 11:59:49 | [Poshteh.Core.Calendar](https://www.nuget.org/packages/Poshteh.Core.Calendar) | 10.0.3 | Poshteh | Dependency-free Jalali (Persian) calendar display helpers. Storage and logic st… |
| 2026-11-12 12:06:15 | [Co.Revington.Sightline](https://www.nuget.org/packages/Co.Revington.Sightline) | 0.1.0 | Ravindu Wijegunawardhana | A live, editable map of a .NET solution. See projects, packages, types, depende… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
