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

## Latest list — 2026-10-27 08:20 UTC

New packages created between 2026-10-27 07:18 UTC and 2026-10-27 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T08-20-15-901533Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 07:19:29 | [Render.NET.Jpeg2000](https://www.nuget.org/packages/Render.NET.Jpeg2000) | 0.3.10 | Vadim Belov | Managed JPEG 2000 Part 1 decoding from JP2 containers and raw J2K codestreams w… |
| 2026-10-27 07:27:40 | [Cyan.Design.Core](https://www.nuget.org/packages/Cyan.Design.Core) | 1.0.0 | CyanFlag | Cyan.Design Core — 基于 Avalonia 12.0 的 UI 控件库核心包，包含按钮、输入框、布局、导航、反馈等 60+ 控件 |
| 2026-10-27 07:28:28 | [Cyan.Design.Themes](https://www.nuget.org/packages/Cyan.Design.Themes) | 1.0.0 | CyanFlag | Cyan.Design Themes — 28 套主题样式包（AntDesign/Shadcn/ParkUI/Mantine/Skeleton×23），含 L… |
| 2026-10-27 07:34:55 | [ControlResell.Sdk](https://www.nuget.org/packages/ControlResell.Sdk) | 1.0.0 | ControlResell | .NET client for the ControlResell public API: typed operations generated from i… |
| 2026-10-27 07:52:10 | [Easy.WorkFlow.CoreKit](https://www.nuget.org/packages/Easy.WorkFlow.CoreKit) | 1.0.2 | Easy.WorkFlow contributors | 工作流核心模型：链式编排 DSL、流程中间表示、上下文序列化与定义版本计算。 |
| 2026-10-27 07:53:46 | [Azure.ResourceManager.CloudHealth](https://www.nuget.org/packages/Azure.ResourceManager.CloudHealth) | 1.0.0 | Microsoft | Azure Resource Manager client SDK for Azure resource provider CloudHealth. |
| 2026-10-27 07:54:39 | [Zyga.NetDaemon.Fluent.Entities](https://www.nuget.org/packages/Zyga.NetDaemon.Fluent.Entities) | 0.1.0 | Szymon Zywert | An unofficial, community-maintained fluent device/entity mapping framework for… |
| 2026-10-27 07:57:48 | [VwV.Sms](https://www.nuget.org/packages/VwV.Sms) | 1.0.0 | Vira Web Vorna (VwV) | Independent SMS contracts, explicit tenant routing and guarded Kavenegar facili… |
| 2026-10-27 07:57:49 | [VwV.Sms.Kavenegar](https://www.nuget.org/packages/VwV.Sms.Kavenegar) | 1.0.0 | Vira Web Vorna (VwV) | Independent SMS contracts, explicit tenant routing and guarded Kavenegar facili… |
| 2026-10-27 07:57:50 | [VwV.Sms.DependencyInjection](https://www.nuget.org/packages/VwV.Sms.DependencyInjection) | 1.0.0 | Vira Web Vorna (VwV) | Independent SMS contracts, explicit tenant routing and guarded Kavenegar facili… |
| 2026-10-27 08:03:34 | [Render.NET.Jbig2](https://www.nuget.org/packages/Render.NET.Jbig2) | 0.3.10 | Vadim Belov | Managed JBIG2 decoding for standalone files and embedded PDF image streams, inc… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
