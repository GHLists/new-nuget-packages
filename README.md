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

## Latest list — 2026-10-18 17:19 UTC

New packages created between 2026-10-18 16:21 UTC and 2026-10-18 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T17-19-27-892766Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 16:37:07 | [Zongsoft.Tools.Containerizer](https://www.nuget.org/packages/Zongsoft.Tools.Containerizer) | 1.0.0 | Popeye Zhong(zongsoft@qq.com) | The Zongsoft Containerization .NET Tool. |
| 2026-10-18 16:43:11 | [Ezacloud.Sdk](https://www.nuget.org/packages/Ezacloud.Sdk) | 0.2.0 | Eza Cloud | Official .NET client library for Eza Cloud (PayEdge M-Pesa STK push, Transactio… |
| 2026-10-18 17:07:58 | [Calysto.Huawei.Push](https://www.nuget.org/packages/Calysto.Huawei.Push) | 1.0.4 | Calysto | Provided as-is, no warranty of any kind. |
| 2026-10-18 17:07:58 | [SMSPool](https://www.nuget.org/packages/SMSPool) | 0.1.0 | SMSPool | Official .NET client for the SMSPool API (https://api.smspool.net/docs). |
| 2026-10-18 17:08:54 | [Suncaomei.AdminNetBasic.FullStack.Templates](https://www.nuget.org/packages/Suncaomei.AdminNetBasic.FullStack.Templates) | 1.0.0 | suncaomei | Admin.NET.Pro 精简后的 .NET 10 后端与 Naive UI 前端全栈模板。 |
| 2026-10-18 17:08:55 | [Suncaomei.AdminNetBasic.Templates](https://www.nuget.org/packages/Suncaomei.AdminNetBasic.Templates) | 1.0.0 | suncaomei | Admin.NET.Pro 精简后的 .NET 10 基础管理后端模板。 |
| 2026-10-18 17:15:58 | [Tai.Account.Extension.OAuth.Cli](https://www.nuget.org/packages/Tai.Account.Extension.OAuth.Cli) | 1.1.0 | Tai | Reusable ABP module for WeChat/SMS user login, opt-in tenant-bound OAuth client… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
