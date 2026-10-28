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

## Latest list — 2026-10-28 10:20 UTC

New packages created between 2026-10-28 09:20 UTC and 2026-10-28 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T10-20-38-627773Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 09:29:40 | [EvolvitLabs.HaloNetCore](https://www.nuget.org/packages/EvolvitLabs.HaloNetCore) | 1.1.21 | Evolvit Solutions AB | Package Description |
| 2026-10-28 09:29:52 | [Cangming.Logs](https://www.nuget.org/packages/Cangming.Logs) | 0.1.1.1028 | Fangyu | 仅组织内部使用。日志领域的基础实现。 |
| 2026-10-28 09:29:54 | [Cangming.Logs.Contracts](https://www.nuget.org/packages/Cangming.Logs.Contracts) | 0.1.1.1028 | Fangyu | 仅组织内部使用。日志领域的对外契约：分区掩码、日志事件与日志服务契约。 |
| 2026-10-28 09:29:57 | [Cangming.Logs.NLog](https://www.nuget.org/packages/Cangming.Logs.NLog) | 0.1.1.1028 | Fangyu | 仅组织内部使用。当使用 NLog 作为日志基础时，提供对日志相关契约的落地实现。 |
| 2026-10-28 09:29:58 | [Cangming.Logs.xUnit](https://www.nuget.org/packages/Cangming.Logs.xUnit) | 0.1.1.1028 | Fangyu | 仅组织内部使用。为 xUnit 测试提供把 Microsoft.Extensions.Logging 日志路由到 ITestOutputHelper 的适配器。 |
| 2026-10-28 09:30:01 | [Cangming.PicoPlugins](https://www.nuget.org/packages/Cangming.PicoPlugins) | 0.1.1.1028 | Fangyu | 仅组织内部使用。为软件实现插件管理机制的基础库。 |
| 2026-10-28 09:30:03 | [Cangming.PicoPlugins.Avalonias](https://www.nuget.org/packages/Cangming.PicoPlugins.Avalonias) | 0.1.1.1028 | Fangyu | 仅组织内部使用。为桌面软件(Avalonia)实现 Avalonia 界面插件管理机制的基础库。 |
| 2026-10-28 09:30:08 | [Cangming.PicoPlugins.HttpApi](https://www.nuget.org/packages/Cangming.PicoPlugins.HttpApi) | 0.1.1.1028 | Fangyu | 仅组织内部使用。为服务端宿主(HTTP)把已装载插件与 Module 能力暴露成只读端点。 |
| 2026-10-28 09:30:10 | [Cangming.PicoPlugins.WPF](https://www.nuget.org/packages/Cangming.PicoPlugins.WPF) | 0.1.1.1028 | Fangyu | 仅组织内部使用。为桌面软件(WPF)实现界面插件管理机制的基础库。 |
| 2026-10-28 09:30:14 | [Cangming.Platform](https://www.nuget.org/packages/Cangming.Platform) | 0.1.1.1028 | Fangyu | Cangming 客户端通用基座框架库（插件化宿主）。 |
| 2026-10-28 09:30:17 | [Cangming.Platform.Contracts](https://www.nuget.org/packages/Cangming.Platform.Contracts) | 0.1.1.1028 | Fangyu | Cangming 客户端通用基座框架库（插件化宿主）。 |
| 2026-10-28 09:30:19 | [Cangming.Primitive](https://www.nuget.org/packages/Cangming.Primitive) | 0.1.1.1028 | Fangyu | Cangming 客户端通用基座框架库（插件化宿主）。 |
| 2026-10-28 09:30:22 | [Cangming.Shell](https://www.nuget.org/packages/Cangming.Shell) | 0.1.1.1028 | Fangyu | Cangming 客户端通用基座框架库（插件化宿主）。 |
| 2026-10-28 09:30:30 | [Cangming.Shell.Contracts](https://www.nuget.org/packages/Cangming.Shell.Contracts) | 0.1.1.1028 | Fangyu | Cangming 客户端通用基座框架库（插件化宿主）。 |
| 2026-10-28 09:30:33 | [Cangming.Toolkit](https://www.nuget.org/packages/Cangming.Toolkit) | 0.1.1.1028 | Fangyu | Cangming 客户端通用基座框架库（插件化宿主）。 |
| 2026-10-28 09:30:36 | [Cangming.Toolkit.Avalonias](https://www.nuget.org/packages/Cangming.Toolkit.Avalonias) | 0.1.1.1028 | Fangyu | 仅组织内部使用。Avalonia 对话框与向导基础类型。 |
| 2026-10-28 09:30:39 | [Cangming.Toolkit.Avalonias.Sukis](https://www.nuget.org/packages/Cangming.Toolkit.Avalonias.Sukis) | 0.1.1.1028 | Fangyu | 仅组织内部使用。基于 SukiUI 的对话框实现。 |
| 2026-10-28 09:30:41 | [Cangming.Workspace](https://www.nuget.org/packages/Cangming.Workspace) | 0.1.1.1028 | Fangyu | Cangming 客户端通用基座框架库（插件化宿主）。 |
| 2026-10-28 09:30:43 | [Cangming.Workspace.Contracts](https://www.nuget.org/packages/Cangming.Workspace.Contracts) | 0.1.1.1028 | Fangyu | Cangming 客户端通用基座框架库（插件化宿主）。 |
| 2026-10-28 09:43:20 | [XStatic.CloudflarePages](https://www.nuget.org/packages/XStatic.CloudflarePages) | 1.0.0-alpha | Sam Mullins | Cloudflare Pages deployer for xStatic for Umbraco. Deploy your static sites dir… |
| 2026-10-28 09:51:05 | [Analogy.LogViewer.Interfaces.Drawing](https://www.nuget.org/packages/Analogy.LogViewer.Interfaces.Drawing) | 9.0.6 | Lior Banai | Interfaces assembly for creating custom data providers for Analogy Log Viewer |
| 2026-10-28 09:57:43 | [ZeroAlloc.Rest.Anthropic](https://www.nuget.org/packages/ZeroAlloc.Rest.Anthropic) | 3.5.0 | Marcel Roozekrans | A typed, AOT-compatible Anthropic Messages API client for .NET, built on ZeroAl… |
| 2026-10-28 09:57:44 | [ZeroAlloc.Rest.Ollama](https://www.nuget.org/packages/ZeroAlloc.Rest.Ollama) | 3.5.0 | Marcel Roozekrans | A typed, AOT-compatible Ollama embed client for .NET, built on ZeroAlloc.Rest:… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
