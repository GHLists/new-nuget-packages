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

## Latest list — 2026-11-14 11:19 UTC

New packages created between 2026-11-14 10:19 UTC and 2026-11-14 11:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T11-19-56-459722Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 10:27:52 | [Mossie.Incus.Client](https://www.nuget.org/packages/Mossie.Incus.Client) | 7.6.0-alpha | Mossie | C# client for the Incus REST API, translated from the official Go client and sh… |
| 2026-11-14 10:32:52 | [GCR.Domains.Core.Common](https://www.nuget.org/packages/GCR.Domains.Core.Common) | 0.1.0 | GCR | Core 模块领域层：实体基类与通用抽象 |
| 2026-11-14 10:32:58 | [GCR.Applications.Core.Common](https://www.nuget.org/packages/GCR.Applications.Core.Common) | 0.1.0 | GCR | Core 模块应用层：通用异常与分页结果 |
| 2026-11-14 10:33:01 | [GCR.Applications.Core.Extensions](https://www.nuget.org/packages/GCR.Applications.Core.Extensions) | 0.1.0 | GCR | Core 模块应用层：扩展契约、装配目录与核心模块 |
| 2026-11-14 10:33:03 | [GCR.Applications.Core.Localization](https://www.nuget.org/packages/GCR.Applications.Core.Localization) | 0.1.0 | GCR | Core 模块应用层：多语言基础设施，语言包装载与本地化服务 |
| 2026-11-14 10:33:06 | [GCR.Blazor.Components](https://www.nuget.org/packages/GCR.Blazor.Components) | 0.1.0 | GCR | GCR 通用后台组件库：基于 gcr.css 设计体系的 Blazor 组件集合 |
| 2026-11-14 10:33:08 | [GCR.Domains.Admin.Audit](https://www.nuget.org/packages/GCR.Domains.Admin.Audit) | 0.1.0 | GCR | Admin 模块领域层：审计上下文 |
| 2026-11-14 10:33:10 | [GCR.Domains.Admin.Branding](https://www.nuget.org/packages/GCR.Domains.Admin.Branding) | 0.1.0 | GCR | Admin 内置模块领域层：品牌与站点上下文 |
| 2026-11-14 10:33:12 | [GCR.Domains.Admin.Identity](https://www.nuget.org/packages/GCR.Domains.Admin.Identity) | 0.1.0 | GCR | Admin 模块领域层：身份与访问上下文 |
| 2026-11-14 10:33:14 | [GCR.Domains.Core.Security](https://www.nuget.org/packages/GCR.Domains.Core.Security) | 0.1.0 | GCR | Core 模块领域层：安全抽象与密码哈希基本实现 |
| 2026-11-14 10:33:16 | [GCR.Infrastructures.Core.Persistence](https://www.nuget.org/packages/GCR.Infrastructures.Core.Persistence) | 0.1.0 | GCR | Core 模块基础设施层：EF Core 上下文与种子数据 |
| 2026-11-14 10:33:19 | [GCR.Infrastructures.Core.Security](https://www.nuget.org/packages/GCR.Infrastructures.Core.Security) | 0.1.0 | GCR | Core 模块基础设施层：JWT 签发基本实现 |
| 2026-11-14 10:37:45 | [ExcelFAST](https://www.nuget.org/packages/ExcelFAST) | 6.2611.14-Beta | Smurf-IV | ## 2026-11-13 - V6 - Excel_FAST - Beta - ✅ Add .Net11 TFM support across all fo… |
| 2026-11-14 10:51:19 | [Ished](https://www.nuget.org/packages/Ished) | 0.1.0 | Bridge | IshedDB, written as MongoDB’s official driver of each language (.NET, as MongoD… |
| 2026-11-14 10:56:40 | [PolishOpenData.Eli](https://www.nuget.org/packages/PolishOpenData.Eli) | 1.9.0 | JacekSmi | Typed .NET client for the Polish legal-acts API of the Sejm (ELI, api.sejm.gov.… |
| 2026-11-14 11:02:44 | [AbpPlugin.Web](https://www.nuget.org/packages/AbpPlugin.Web) | 0.2.0 | AbpPlugin contributors | Plugins' web parts for an AbpPlugin host: serves each enabled plugin's browser… |
| 2026-11-14 11:04:24 | [AbpWebhooks](https://www.nuget.org/packages/AbpWebhooks) | 0.5.0 | AbpCluster contributors | AbpWebhooks: signed outgoing webhooks for an ABP app on .NET 10 and EF Core. A… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
