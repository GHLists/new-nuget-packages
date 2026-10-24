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

## Latest list — 2026-10-24 14:20 UTC

New packages created between 2026-10-24 13:20 UTC and 2026-10-24 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T14-20-41-001697Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 13:37:02 | [Bitzsoft.Integrations.MobilePush](https://www.nuget.org/packages/Bitzsoft.Integrations.MobilePush) | 1.0.0 | Bitzsoft | 移动推送抽象层 — 统一通知、透传消息、设备查询与消息撤回契约（阿里云 EMAS） |
| 2026-10-24 13:41:28 | [Bitzsoft.Integrations.MobilePush.Aliyun](https://www.nuget.org/packages/Bitzsoft.Integrations.MobilePush.Aliyun) | 1.0.0 | Bitzsoft | 阿里云移动推送（EMAS Push）实现 — 通知、透传消息、设备查询与消息撤回 |
| 2026-10-24 13:45:53 | [HKW.FastMember.Generater](https://www.nuget.org/packages/HKW.FastMember.Generater) | 1.3.1 | HKW | Source-generated member access with an independent runtime. |
| 2026-10-24 13:45:54 | [HKW.FastMember.Abstractions](https://www.nuget.org/packages/HKW.FastMember.Abstractions) | 1.3.1 | HKW | Backend-independent member access contracts and immutable metadata. |
| 2026-10-24 13:46:28 | [Bitzsoft.Integrations.MobilePush.All](https://www.nuget.org/packages/Bitzsoft.Integrations.MobilePush.All) | 1.0.0 | Bitzsoft | 移动推送聚合包 — 按配置注册阿里云移动推送实现 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
