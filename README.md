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

## Latest list — 2026-10-09 10:19 UTC

New packages created between 2026-10-09 09:19 UTC and 2026-10-09 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T10-19-16-706448Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 09:21:42 | [Retro.NET](https://www.nuget.org/packages/Retro.NET) | 1.0.11 | owen800q | A pixel-faithful retro enterprise (classic SAP GUI / Windows 9x) theme and cont… |
| 2026-10-09 09:24:49 | [SVF.NET](https://www.nuget.org/packages/SVF.NET) | 1.0.0 | SVF-tools, dg1474 | .NET / C# bindings and native runtime wrapper for SVF (Static Value-Flow Analys… |
| 2026-10-09 09:31:41 | [SimplyWorks.Serverless.Tooling](https://www.nuget.org/packages/SimplyWorks.Serverless.Tooling) | 10.1.0 | SW.Serverless.Tooling | Package Description |
| 2026-10-09 09:32:07 | [ApeFree.ApeRpc.BytesIO](https://www.nuget.org/packages/ApeFree.ApeRpc.BytesIO) | 0.0.3-alpha61009 | Guijie Lee | 面向直连场景的高性能轻量级 RPC 类库，基于 STTech.BytesIO 统一网络通信层抽象（TCP、IPC 命名管道、串口 SerialPort 等），… |
| 2026-10-09 09:32:11 | [ApeFree.ApeRpc.Grpc](https://www.nuget.org/packages/ApeFree.ApeRpc.Grpc) | 0.0.3-alpha61009 | Guijie Lee, HuJJJJ | 为 ApeFree.ApeRpc 提供基于 gRPC (HTTP/2) 的高性能底层通道实现，支持方法远程过程调用与流式事件订阅通知。 |
| 2026-10-09 09:38:55 | [WpfFoundation](https://www.nuget.org/packages/WpfFoundation) | 1.0.0 | gbolotin | Reusable WPF infrastructure for .NET 10 built on the native Windows Fluent them… |
| 2026-10-09 09:40:50 | [Thruput.Semgrep.Rules](https://www.nuget.org/packages/Thruput.Semgrep.Rules) | 0.0.9 | Thruput | Curated Semgrep ruleset for .NET codebases with auto-bootstrapped CLI support,… |
| 2026-10-09 09:43:58 | [GORM](https://www.nuget.org/packages/GORM) | 3.2.0 | Pjotr Casteel | Strongly typed SQL Server Graph ORM for .NET with LINQ, graph tracking, mutatio… |
| 2026-10-09 09:44:10 | [CifroArts.SimplifiedCSharp](https://www.nuget.org/packages/CifroArts.SimplifiedCSharp) | 1.0.0 | CifroArts | Adds extensions to existing types and provides the ability to use the most comm… |
| 2026-10-09 09:50:43 | [AudioCpp.NET.Runtime.Vulkan](https://www.nuget.org/packages/AudioCpp.NET.Runtime.Vulkan) | 0.3.0 | dongfangzhizhu | Native audio.cpp shim (Vulkan backend) for AudioCpp.NET. Adds runtimes/win-x64… |
| 2026-10-09 09:55:52 | [Eziriz.IntelliLock.TrimHelper](https://www.nuget.org/packages/Eziriz.IntelliLock.TrimHelper) | 3.7.0 | Eziriz | If you want to protect self-contained trimmed .NET 5.0-11.0 applications with I… |
| 2026-10-09 10:07:37 | [TauriKit.Sidecar.Loopback.AspNetCore](https://www.nuget.org/packages/TauriKit.Sidecar.Loopback.AspNetCore) | 0.14.0 | iyulab | The ASP.NET Core host of a desktop app's loopback backend: listen on 127.0.0.1… |
| 2026-10-09 10:08:51 | [MarkupReporter](https://www.nuget.org/packages/MarkupReporter) | 1.0.0 | Chad Wheeler | Design PDF reports visually and render them from JSON or SQL data in ASP.NET Co… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
