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

## Latest list — 2026-10-16 02:19 UTC

New packages created between 2026-10-16 01:20 UTC and 2026-10-16 02:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T02-19-46-671156Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 01:26:34 | [RevitTestHost.Sdk](https://www.nuget.org/packages/RevitTestHost.Sdk) | 0.1.0 | mahach666 | SDK with attributes and contracts for writing tests that run inside live Revit… |
| 2026-10-16 01:26:36 | [RevitUITesting](https://www.nuget.org/packages/RevitUITesting) | 0.1.0 | mahach666 | Library for end-to-end UI tests of Revit plugins: UI Automation waits and actio… |
| 2026-10-16 01:31:09 | [SyntaxCircus.Seo.Analysis.Yoast](https://www.nuget.org/packages/SyntaxCircus.Seo.Analysis.Yoast) | 0.1.0 | Syntax Circus LLC | Server-side Yoast companion client for SyntaxCircus SEO analysis. |
| 2026-10-16 01:43:52 | [Afic.Minimal](https://www.nuget.org/packages/Afic.Minimal) | 2026.10.32 | nuoyi.cc | Minimal components for Afic.Net |
| 2026-10-16 01:43:55 | [Afic.Minimal.Generator](https://www.nuget.org/packages/Afic.Minimal.Generator) | 2026.10.32 | nuoyi.cc | Minimal components for Afic.Net |
| 2026-10-16 01:43:58 | [Afic.MinimalHost](https://www.nuget.org/packages/Afic.MinimalHost) | 2026.10.32 | nuoyi.cc | Minimal components for Afic.Net |
| 2026-10-16 01:54:24 | [OSK.Petra.Acquisitions](https://www.nuget.org/packages/OSK.Petra.Acquisitions) | 0.1.0 | BlankDev117 | Provides a system that handles acquiring things in an application or game - tha… |
| 2026-10-16 01:54:36 | [VenEl.MCP.Decompiler](https://www.nuget.org/packages/VenEl.MCP.Decompiler) | 1.0.0 | VenEl | Decompilation and binary code analysis module for VenEl MCP Assistant. |
| 2026-10-16 01:56:30 | [Mud.AI.Abstractions](https://www.nuget.org/packages/Mud.AI.Abstractions) | 1.0.0 | Mud Studio | Mud.AI 平台无关端口与工具面契约：会话端口 / 授权链骨架端口 / 通道抽象 / 审批状态机接口；声明契约族（[AgentTool]/[ToolPara… |
| 2026-10-16 01:56:31 | [Mud.AI.Generator](https://www.nuget.org/packages/Mud.AI.Generator) | 1.0.0 | Mud Studio | Mud.AI 工具面源生成引擎（ToolSurface 竖井）：把 [SdkToolProfile] 剖面驱动的工具特性接口编译为「模型可调用工具」的全部编译… |
| 2026-10-16 01:56:32 | [Mud.AI.Agent](https://www.nuget.org/packages/Mud.AI.Agent) | 1.0.0 | Mud Studio | Mud.AI 运行期：工具执行骨架区（ToolExecutor / ToolPagination / ToolDryRun / ToolResult / To… |
| 2026-10-16 01:59:02 | [Sacloud.Sdk.Shared](https://www.nuget.org/packages/Sacloud.Sdk.Shared) | 0.1.8 | SAKURA internet Inc. | .NET Client for SAKURA Cloud Shared Routines |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
