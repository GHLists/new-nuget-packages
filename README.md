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

## Latest list — 2026-11-27 03:20 UTC

New packages created between 2026-11-27 02:20 UTC and 2026-11-27 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T03-20-52-707772Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 02:24:08 | [Karl.AIExtension.Abstractions](https://www.nuget.org/packages/Karl.AIExtension.Abstractions) | 0.6.1 | Karl | AI Extension 契约层：AI 契约标注特性、桥接基类、UI 上下文追踪与 DI 基础设施。 |
| 2026-11-27 02:24:09 | [Karl.AIExtension.Blazor](https://www.nuget.org/packages/Karl.AIExtension.Blazor) | 0.6.1 | Karl | AI Extension 的 Blazor 外壳：与 WPF 共享会话核心的聊天组件。 |
| 2026-11-27 02:24:10 | [Karl.AIExtension.Core](https://www.nuget.org/packages/Karl.AIExtension.Core) | 0.6.1 | Karl | AI Extension 运行时核心：会话、流式输出、MCP 进程内宿主、UI 上下文环形日志、MVVM 基础设施。 |
| 2026-11-27 02:24:11 | [Karl.AIExtension.WPF](https://www.nuget.org/packages/Karl.AIExtension.WPF) | 0.6.1 | Karl | AI Extension 的 WPF 外壳：聊天面板、工具调用可视化、UI 线程调度实现、MCP 对外暴露（HTTP / stdio）。 |
| 2026-11-27 02:55:37 | [PolyhydraGames.Core.NAS](https://www.nuget.org/packages/PolyhydraGames.Core.NAS) | 0.1.0 | Polyhydra Games | Reusable NAS and media-platform services for the NasDb family. |
| 2026-11-27 02:57:09 | [CSoft.Protocol.IOBoard1629](https://www.nuget.org/packages/CSoft.Protocol.IOBoard1629) | 11.0.0 | CSoft | IOBoard-1629 接口板 QL 寄存器客户端，封装电池、数字量、模拟量及电子门锁 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
