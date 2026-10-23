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

## Latest list — 2026-10-23 00:18 UTC

New packages created between 2026-10-22 23:21 UTC and 2026-10-23 00:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T00-18-46-87838Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 23:23:54 | [Musictopia2.BasicDependencyInjectionLibrary](https://www.nuget.org/packages/Musictopia2.BasicDependencyInjectionLibrary) | 10.0.1 | BasicDependencyInjectionLibra… | Package Description |
| 2026-10-22 23:24:20 | [Musictopia2.BasicTesseractOcrLibrary](https://www.nuget.org/packages/Musictopia2.BasicTesseractOcrLibrary) | 10.0.1 | BasicTesseractOcrLibrary | Package Description |
| 2026-10-22 23:26:44 | [Musictopia2.WindowsImageAbstractionsLibrary](https://www.nuget.org/packages/Musictopia2.WindowsImageAbstractionsLibrary) | 10.0.1 | WindowsImageAbstractionsLibra… | Package Description |
| 2026-10-22 23:27:09 | [Musictopia2.WindowsScreenCaptureLibrary](https://www.nuget.org/packages/Musictopia2.WindowsScreenCaptureLibrary) | 10.0.1 | WindowsScreenCaptureLibrary | Package Description |
| 2026-10-22 23:28:32 | [ThomasFazzari.RoslynBridge.linux-arm64](https://www.nuget.org/packages/ThomasFazzari.RoslynBridge.linux-arm64) | 1.2.1 | Thomas Fazzari | Lightweight MCP for C# diagnostics, navigation and refactoring, backed by the o… |
| 2026-10-22 23:28:34 | [ThomasFazzari.RoslynBridge.linux-x64](https://www.nuget.org/packages/ThomasFazzari.RoslynBridge.linux-x64) | 1.2.1 | Thomas Fazzari | Lightweight MCP for C# diagnostics, navigation and refactoring, backed by the o… |
| 2026-10-22 23:28:36 | [ThomasFazzari.RoslynBridge.osx-arm64](https://www.nuget.org/packages/ThomasFazzari.RoslynBridge.osx-arm64) | 1.2.1 | Thomas Fazzari | Lightweight MCP for C# diagnostics, navigation and refactoring, backed by the o… |
| 2026-10-22 23:28:38 | [ThomasFazzari.RoslynBridge.osx-x64](https://www.nuget.org/packages/ThomasFazzari.RoslynBridge.osx-x64) | 1.2.1 | Thomas Fazzari | Lightweight MCP for C# diagnostics, navigation and refactoring, backed by the o… |
| 2026-10-22 23:28:39 | [ThomasFazzari.RoslynBridge.win-x64](https://www.nuget.org/packages/ThomasFazzari.RoslynBridge.win-x64) | 1.2.1 | Thomas Fazzari | Lightweight MCP for C# diagnostics, navigation and refactoring, backed by the o… |
| 2026-10-22 23:28:40 | [ThomasFazzari.RoslynBridge](https://www.nuget.org/packages/ThomasFazzari.RoslynBridge) | 1.2.1 | Thomas Fazzari | Lightweight MCP for C# diagnostics, navigation and refactoring, backed by the o… |
| 2026-10-22 23:35:57 | [Bitzsoft.Integrations.SyntheticData.All](https://www.nuget.org/packages/Bitzsoft.Integrations.SyntheticData.All) | 1.0.4 | Bitzsoft | Bitzsoft 智能合成数据全量聚合包 — 一键装配核心引擎与司法（Legal）、企业（Enterprise）、门户（Web）全量垂直语料 |
| 2026-10-22 23:42:43 | [OnionArchitecture.Templates](https://www.nuget.org/packages/OnionArchitecture.Templates) | 1.0.1 | Gökhan Ertoğan | Production-ready .NET 10 microservice template: Onion/Clean architecture, DDD,… |
| 2026-10-23 00:04:07 | [Swiftsoft.Shield](https://www.nuget.org/packages/Swiftsoft.Shield) | 1.0.6 | Swiftsoft (Jospin Chimi) | Encrypts and signs the data exchanged by an ASP.NET Core API, so that it stays… |
| 2026-10-23 00:06:14 | [NAPS2.Windows.Printing](https://www.nuget.org/packages/NAPS2.Windows.Printing) | 0.9.0 | Ben Olden-Cooligan | Print images with the Windows print dialog, including its print preview. Works… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
