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

## Latest list — 2026-10-07 05:19 UTC

New packages created between 2026-10-07 04:21 UTC and 2026-10-07 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T05-19-30-48246Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 04:35:11 | [PropStruct](https://www.nuget.org/packages/PropStruct) | 0.1.0 | Eduard Burachek | Monte Carlo model of the local structure of composite solid propellants (pocket… |
| 2026-10-07 04:35:11 | [PropStruct.Cli](https://www.nuget.org/packages/PropStruct.Cli) | 0.1.0 | Eduard Burachek | The propstruct command line: the pocket model of the local structure of composi… |
| 2026-10-07 04:42:28 | [TheoryNexus.Helm.Abstractions](https://www.nuget.org/packages/TheoryNexus.Helm.Abstractions) | 0.3.0 | Theory Nexus | The IHelm interface and its record types, with no dependencies, plus a recordin… |
| 2026-10-07 04:44:30 | [Meteion.Toolkit.Dialogs.Abstractions](https://www.nuget.org/packages/Meteion.Toolkit.Dialogs.Abstractions) | 1.5.0 | frogcrush | UI-framework-agnostic abstractions (IDialogService and option types) for showin… |
| 2026-10-07 04:44:37 | [Meteion.Toolkit.WPF.Dialogs](https://www.nuget.org/packages/Meteion.Toolkit.WPF.Dialogs) | 1.5.0 | frogcrush | Open, save, and folder dialogs for WPF. Uses the framework's own dialogs on .NE… |
| 2026-10-07 04:47:26 | [StdUnit.Tags.Core](https://www.nuget.org/packages/StdUnit.Tags.Core) | 1.0.0 | itminus | 硬件无关的核心抽象，无外部依赖 |
| 2026-10-07 04:47:29 | [StdUnit.Tags](https://www.nuget.org/packages/StdUnit.Tags) | 1.0.0 | itminus | 依赖于 StdUnit.Tags.Core，补充项目、日志、插件等功能 |
| 2026-10-07 04:47:34 | [StdUnit.Tags.McpServer](https://www.nuget.org/packages/StdUnit.Tags.McpServer) | 1.0.0 | itminus | MCP Server 扩展，把测点项目暴露给 AI 助手（ModelContextProtocol） |
| 2026-10-07 04:47:37 | [StdUnit.Tags.S7](https://www.nuget.org/packages/StdUnit.Tags.S7) | 1.0.0 | itminus | 西门子 S7 通信支持 |
| 2026-10-07 04:47:41 | [StdUnit.Tags.SimpleFiles](https://www.nuget.org/packages/StdUnit.Tags.SimpleFiles) | 1.0.0 | itminus | 简单文件支持，把测点树映射为文件树 |
| 2026-10-07 04:47:45 | [StdUnit.Tags.ModbusTcp](https://www.nuget.org/packages/StdUnit.Tags.ModbusTcp) | 1.0.0 | itminus | ModbusTcp 通信支持 |
| 2026-10-07 04:47:49 | [StdUnit.Tags.ZLan](https://www.nuget.org/packages/StdUnit.Tags.ZLan) | 1.0.0 | itminus | ZLan 远程IO 通信支持（建立在 ModbusTcp 之上） |
| 2026-10-07 04:47:54 | [StdUnit.Tags.Hjzk](https://www.nuget.org/packages/StdUnit.Tags.Hjzk) | 1.0.0 | itminus | Hjzk 远程IO 通信支持（建立在 ModbusTcp 之上） |
| 2026-10-07 04:47:58 | [StdUnit.Tags.OpcUaClient](https://www.nuget.org/packages/StdUnit.Tags.OpcUaClient) | 1.0.0 | itminus | OPC UA 通信支持 |
| 2026-10-07 04:48:02 | [StdUnit.Tags.ComScanner](https://www.nuget.org/packages/StdUnit.Tags.ComScanner) | 1.0.0 | itminus | 串口通信支持 |
| 2026-10-07 04:48:06 | [StdUnit.Tags.RxExtensions](https://www.nuget.org/packages/StdUnit.Tags.RxExtensions) | 1.0.0 | itminus | Rx.NET 扩展 |
| 2026-10-07 04:48:10 | [StdUnit.Tags.R3Extensions](https://www.nuget.org/packages/StdUnit.Tags.R3Extensions) | 1.0.0 | itminus | R3 扩展 |
| 2026-10-07 04:48:15 | [StdUnit.Tags.BlazorLib.Core](https://www.nuget.org/packages/StdUnit.Tags.BlazorLib.Core) | 1.0.0 | itminus | Blazor 组件库（核心）：测点树与通道的查看、编辑组件 |
| 2026-10-07 04:48:20 | [StdUnit.Tags.BlazorLib](https://www.nuget.org/packages/StdUnit.Tags.BlazorLib) | 1.0.0 | itminus | Blazor 组件库：各驱动的通道描述符查看器与编辑器 |
| 2026-10-07 04:50:29 | [WebViewHostBridge](https://www.nuget.org/packages/WebViewHostBridge) | 1.0.0 | Serhii Khrolenko | Zero-dependency contracts between a desktop shell (WinForms/WPF hosting WebView… |
| 2026-10-07 04:55:55 | [codegiveness.postgresql-sharp-mcp](https://www.nuget.org/packages/codegiveness.postgresql-sharp-mcp) | 0.3.2 | codegiveness | Database-agnostic PostgreSQL MCP server with live discovery and bounded per-cal… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
