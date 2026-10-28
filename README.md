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

## Latest list — 2026-10-28 09:20 UTC

New packages created between 2026-10-28 08:19 UTC and 2026-10-28 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T09-20-07-453874Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 08:22:00 | [AspNetCoreSharedServer.Middleware](https://www.nuget.org/packages/AspNetCoreSharedServer.Middleware) | 4.0.0 | simonegli8 | Middleware for ASP.NET Core applications that run behind AspNetCoreSharedServer… |
| 2026-10-28 08:24:46 | [OpenRobot.Litegraph.Common](https://www.nuget.org/packages/OpenRobot.Litegraph.Common) | 1.0.0 | OpenRobot | Litegraph 流程引擎基础模型：图模型（节点/连线/区域）、值格式化与共享文本工具，零外部依赖。 |
| 2026-10-28 08:25:12 | [OpenRobot.Litegraph.Cloud](https://www.nuget.org/packages/OpenRobot.Litegraph.Cloud) | 1.0.0 | OpenRobot | Litegraph 云端对接：画布拉取与备份、云端工件（画布/元数据）发布、ABP 信封解析；传输层留缝，可走 HTTP 直连或宿主自己的出网通道。 |
| 2026-10-28 08:25:28 | [OpenRobot.Litegraph.Core](https://www.nuget.org/packages/OpenRobot.Litegraph.Core) | 1.0.0 | OpenRobot | Litegraph 流程引擎核心：画布解析与校验、图模型、46 个内置节点处理器、同步/异步通道、触发流程与主流程 tick、执行记录诊断。 |
| 2026-10-28 08:25:45 | [OpenRobot.Litegraph.MmidSyntax](https://www.nuget.org/packages/OpenRobot.Litegraph.MmidSyntax) | 1.0.0 | OpenRobot | MMID 规则选择器的文本 ⇄ AST 解析与序列化（类 CSS 选择器语法）。纯函数、零依赖，不认任何 DC / 业务类型。 |
| 2026-10-28 08:26:11 | [OpenRobot.Litegraph.RuleEngine](https://www.nuget.org/packages/OpenRobot.Litegraph.RuleEngine) | 1.0.0 | OpenRobot | MMID 规则引擎的模型层：规则模型、语义校验、SegmentKey 匹配与 MMID 选择器求值。不含执行器，也不含画布编译器。 |
| 2026-10-28 08:40:48 | [Afic.Wpf](https://www.nuget.org/packages/Afic.Wpf) | 2026.10.38 | nuoyi.cc | Package Description |
| 2026-10-28 08:44:47 | [Evergine.OpenXR.Natives.AndroidXR](https://www.nuget.org/packages/Evergine.OpenXR.Natives.AndroidXR) | 2026.10.28.3 | Evergine.OpenXR.Natives.Andro… | Provides the android native libraries of OpenXR loader for Android XR devices t… |
| 2026-10-28 08:51:54 | [Masterly.BusinessRules.DependencyInjection](https://www.nuget.org/packages/Masterly.BusinessRules.DependencyInjection) | 3.0.0 | Ahmad Omar Al-Freihat | Microsoft.Extensions.DependencyInjection integration for Masterly.BusinessRules… |
| 2026-10-28 08:51:57 | [Masterly.BusinessRules.Diagnostics](https://www.nuget.org/packages/Masterly.BusinessRules.Diagnostics) | 3.0.0 | Ahmad Omar Al-Freihat | Structured ILogger observer plus OpenTelemetry ActivitySource spans and Meter i… |
| 2026-10-28 08:51:58 | [Masterly.BusinessRules.Expressions](https://www.nuget.org/packages/Masterly.BusinessRules.Expressions) | 3.0.0 | Ahmad Omar Al-Freihat | Rule expression DSL for Masterly.BusinessRules: parse a textual condition once,… |
| 2026-10-28 08:52:00 | [Masterly.BusinessRules.FeatureManagement](https://www.nuget.org/packages/Masterly.BusinessRules.FeatureManagement) | 3.0.0 | Ahmad Omar Al-Freihat | Microsoft.FeatureManagement adapter supplying Masterly.BusinessRules feature-ga… |
| 2026-10-28 08:52:01 | [Masterly.BusinessRules.Testing](https://www.nuget.org/packages/Masterly.BusinessRules.Testing) | 3.0.0 | Ahmad Omar Al-Freihat | Testing utilities for Masterly.BusinessRules: outcome coverage, boundary finder… |
| 2026-10-28 08:54:34 | [CanFx.Generator](https://www.nuget.org/packages/CanFx.Generator) | 0.3.0 | Oğuzhan Can | canfxgen: CanFx çözümlerinde entity'den CRUD (CQRS) kodu üreten komut satırı ar… |
| 2026-10-28 09:07:59 | [EntityFrameworkCore.Doris](https://www.nuget.org/packages/EntityFrameworkCore.Doris) | 1.0.0 | ymjake | Apache Doris database provider for Entity Framework Core. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
