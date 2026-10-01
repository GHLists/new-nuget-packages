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

## Latest list — 2026-10-01 12:19 UTC

New packages created between 2026-10-01 11:20 UTC and 2026-10-01 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T12-19-53-202579Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 12:07:25 | [Lesphere.Framework.Core](https://www.nuget.org/packages/Lesphere.Framework.Core) | 1.0.0 | Lesphere | 乐枢 .NET 10 后端公共基础：异常、身份、查询分页、依赖注入、序列化、校验与通用扩展。 |
| 2026-10-01 12:07:28 | [Lesphere.Framework.DatabaseAccessor](https://www.nuget.org/packages/Lesphere.Framework.DatabaseAccessor) | 1.0.0 | Lesphere | 乐枢 .NET 10 数据访问基础：SqlSugar 仓储、连接选择、单库事务及 SQLite 显式维护能力。 |
| 2026-10-01 12:07:30 | [Lesphere.Framework.AspNetCore](https://www.nuget.org/packages/Lesphere.Framework.AspNetCore) | 1.0.0 | Lesphere | 乐枢 .NET 10 Web 基础：统一响应、全局异常、可信身份上下文和健康探针。 |
| 2026-10-01 12:13:24 | [AnointedAutomation.Serialization](https://www.nuget.org/packages/AnointedAutomation.Serialization) | 1.0.0 | Anointed Automation LLC, Alex… | Shared serialization helpers: naming rules (camel, Pascal, snake and the hybrid… |
| 2026-10-01 12:13:25 | [AnointedAutomation.Shopify](https://www.nuget.org/packages/AnointedAutomation.Shopify) | 1.0.0 | Anointed Automation LLC, Alex… | Plain Newtonsoft.Json POCO models for the Shopify Admin REST API (customers, or… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
