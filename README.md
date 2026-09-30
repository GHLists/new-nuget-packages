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

## Latest list — 2026-09-30 23:19 UTC

New packages created between 2026-09-30 22:20 UTC and 2026-09-30 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T23-19-42-863776Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 22:22:29 | [redb.Route.As4](https://www.nuget.org/packages/redb.Route.As4) | 4.2.0 | redbase | AS4 (OASIS ebMS 3.0 AS4 profile, eDelivery AS4 1.16 common profile) B2B transpo… |
| 2026-09-30 22:29:55 | [TKWF.Ext.UserCenter](https://www.nuget.org/packages/TKWF.Ext.UserCenter) | 0.1.0 | LoongBa.cn 龙爸出品 | TKWF 用户中心扩展（档案面内核）——公共 Profile API + 兑换历史/我的应用经扩展间契约协作；领域逻辑（脱敏/降级/聚合）进扩展，数据源由认证… |
| 2026-09-30 22:29:55 | [TKWF.Ext.UserCenter.Abstractions](https://www.nuget.org/packages/TKWF.Ext.UserCenter.Abstractions) | 0.1.0 | LoongBa.cn 龙爸出品 | TKWF 用户中心契约抽象（IUserProfileSource / IRedemptionHistorySource / IUserAppsSource /… |
| 2026-09-30 22:42:03 | [HappyHakunaMatata.Messaging](https://www.nuget.org/packages/HappyHakunaMatata.Messaging) | 1.0.0 | Messaging | Package Description |
| 2026-09-30 22:45:26 | [OpenApiFeatureFlags.AspNetCore](https://www.nuget.org/packages/OpenApiFeatureFlags.AspNetCore) | 0.2.0 | Dogukan Demir | Adapter for OpenApiFeatureFlags for the built-in Microsoft.AspNetCore.OpenApi d… |
| 2026-09-30 23:07:32 | [Smartstore.TinyImage.Jpg.Native.linux-arm64](https://www.nuget.org/packages/Smartstore.TinyImage.Jpg.Native.linux-arm64) | 3.3.1 | Mozilla; libjpeg-turbo Projec… | Native cjpeg executable for linux-arm64 platform. |
| 2026-09-30 23:13:19 | [Namh.Configuration.Template](https://www.nuget.org/packages/Namh.Configuration.Template) | 1.0.0 | Nam Hoang | Resolves references between values in Microsoft.Extensions.Configuration. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
