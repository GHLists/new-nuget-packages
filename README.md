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

## Latest list — 2026-10-14 04:19 UTC

New packages created between 2026-10-14 03:19 UTC and 2026-10-14 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T04-19-56-003738Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 03:29:26 | [SiliconTwin.Abstractions](https://www.nuget.org/packages/SiliconTwin.Abstractions) | 0.1.0 | Iván Montiel Cardona | Shared, dependency-free contracts for microcontroller emulators: cycle-budgeted… |
| 2026-10-14 03:38:12 | [Namsiz.WPF.Window.Ribbon](https://www.nuget.org/packages/Namsiz.WPF.Window.Ribbon) | 1.0.0 | Namsiz.T | 带 Ribbon 菜单的通用 WPF 工具窗口库：内置日志 Tab、数据表格 Tab（筛选/行号/虚拟化/校验着色）、状态栏与忙碌遮罩，引用后只需声明菜单按钮… |
| 2026-10-14 03:46:07 | [CompanyHQ.Services.Shipping.Contracts](https://www.nuget.org/packages/CompanyHQ.Services.Shipping.Contracts) | 2.1.0 | CompanyHQ | Package Description |
| 2026-10-14 03:48:09 | [BarakoCMS.Secrets.Aws](https://www.nuget.org/packages/BarakoCMS.Secrets.Aws) | 5.0.0 | Arnel Robles | Loads barakoCMS configuration values, such as JWT:Key, Secrets:Key and module c… |
| 2026-10-14 03:48:11 | [CompanyHQ.Services.Sales](https://www.nuget.org/packages/CompanyHQ.Services.Sales) | 2.1.0 | CompanyHQ | Package Description |
| 2026-10-14 03:48:14 | [BarakoCMS.Secrets.Gcp](https://www.nuget.org/packages/BarakoCMS.Secrets.Gcp) | 5.0.0 | Arnel Robles | Loads barakoCMS configuration values, such as JWT:Key, Secrets:Key and module c… |
| 2026-10-14 03:48:15 | [CompanyHQ.Services.Shipping](https://www.nuget.org/packages/CompanyHQ.Services.Shipping) | 2.1.0 | CompanyHQ | Package Description |
| 2026-10-14 03:57:14 | [iTool.MyScriptRuntimes.AgentSurface](https://www.nuget.org/packages/iTool.MyScriptRuntimes.AgentSurface) | 4.0.0 | iTool.MyScriptRuntimes.AgentS… | Agent-facing surface of the neutral iTool Runtime: the standard development-too… |
| 2026-10-14 03:58:16 | [iTool.MyAuthentication](https://www.nuget.org/packages/iTool.MyAuthentication) | 4.0.0 | iTool.MyAuthentication | Package Description |
| 2026-10-14 03:59:15 | [iTool.KnowledgeHub](https://www.nuget.org/packages/iTool.KnowledgeHub) | 4.0.0 | iTool.KnowledgeHub | Business-neutral world knowledge protocol, evolution runtime and AgentKernel to… |
| 2026-10-14 03:59:44 | [PerformanceStudio.Cli](https://www.nuget.org/packages/PerformanceStudio.Cli) | 1.30.0 | Erik Darling | Command-line SQL Server execution plan analyzer from Performance Studio. Reads… |
| 2026-10-14 03:59:54 | [iTool.AgentKernel.Persistence](https://www.nuget.org/packages/iTool.AgentKernel.Persistence) | 4.0.0 | iTool.AgentKernel.Persistence | Package Description |
| 2026-10-14 04:00:32 | [iTool.AgentKernel.Orleans](https://www.nuget.org/packages/iTool.AgentKernel.Orleans) | 4.0.0 | iTool.AgentKernel.Orleans | Distributed Orleans host for the business-neutral iTool AgentKernel runtime. |
| 2026-10-14 04:10:48 | [iTool.AgentKernel](https://www.nuget.org/packages/iTool.AgentKernel) | 4.0.0 | iTool.AgentKernel | Business-neutral agent runtime built on Microsoft Agent Framework with ChatClie… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
