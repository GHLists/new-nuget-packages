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

## Latest list — 2026-10-15 11:20 UTC

New packages created between 2026-10-15 10:20 UTC and 2026-10-15 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T11-20-05-586938Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 10:40:53 | [Arc56.Generated.joe-p.algokit-monorepo-ts](https://www.nuget.org/packages/Arc56.Generated.joe-p.algokit-monorepo-ts) | 1.0.1.2026101510 | joe-p | Generated ARC-56 Algorand smart-contract clients for joe-p/algokit-monorepo-ts. |
| 2026-10-15 10:40:54 | [NSail.Exporting](https://www.nuget.org/packages/NSail.Exporting) | 0.1.118 | Leonardo Porro,Emmanuel Arias | NSail.Exporting, part of NSail Stack: a .NET modular-monolith framework (messag… |
| 2026-10-15 10:40:56 | [NSail.Exporting.Excel](https://www.nuget.org/packages/NSail.Exporting.Excel) | 0.1.118 | Leonardo Porro,Emmanuel Arias | NSail.Exporting.Excel, part of NSail Stack: a .NET modular-monolith framework (… |
| 2026-10-15 10:41:08 | [Arc56.Generated.Marshal-AM.x500-algorand](https://www.nuget.org/packages/Arc56.Generated.Marshal-AM.x500-algorand) | 1.0.1.2026101510 | Marshal-AM | Generated ARC-56 Algorand smart-contract clients for Marshal-AM/x500-algorand. |
| 2026-10-15 10:52:17 | [AStarDev.VelopackPublishingAvalonia](https://www.nuget.org/packages/AStarDev.VelopackPublishingAvalonia) | 0.1.0 | Jason Barden | Shared Avalonia update-available dialog, view model, and notification services… |
| 2026-10-15 10:59:47 | [Mud.HttpUtils.Redis](https://www.nuget.org/packages/Mud.HttpUtils.Redis) | 3.0.7 | Mud Studio | Mud.HttpUtils 官方分布式令牌存储（F-3）：基于 StackExchange.Redis 的 ITokenStore 实现，键前缀 mud:ht… |
| 2026-10-15 10:59:50 | [Mud.HttpUtils.Testing](https://www.nuget.org/packages/Mud.HttpUtils.Testing) | 3.0.7 | Mud Studio | Mud HttpUtils 测试辅助包，提供 StubHttp mock 服务器、路由匹配、网络行为模拟。 |
| 2026-10-15 11:04:33 | [SMSGate](https://www.nuget.org/packages/SMSGate) | 1.0.0 | Armen Kirakosyan | A lightweight SMPP 3.4 client and server library for .NET. Send and receive SMS… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
