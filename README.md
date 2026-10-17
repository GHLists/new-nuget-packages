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

## Latest list — 2026-10-17 23:21 UTC

New packages created between 2026-10-17 22:20 UTC and 2026-10-17 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T23-21-40-742165Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 22:23:03 | [DubUrl.Application](https://www.nuget.org/packages/DubUrl.Application) | 0.31.1 | Cédric L. Charlier | Transport-neutral application services for validating, rendering, and deploying… |
| 2026-10-17 22:23:08 | [DubUrl.Schema.Documents](https://www.nuget.org/packages/DubUrl.Schema.Documents) | 0.31.1 | Cédric L. Charlier | Versioned YAML and JSON schema documents for DubUrl. |
| 2026-10-17 22:23:10 | [DubUrl-cli](https://www.nuget.org/packages/DubUrl-cli) | 0.31.1 | Cédric L. Charlier | Package Description |
| 2026-10-17 22:23:12 | [DubUrl-cli.linux-musl-x64](https://www.nuget.org/packages/DubUrl-cli.linux-musl-x64) | 0.31.1 | Cédric L. Charlier | Package Description |
| 2026-10-17 22:23:15 | [DubUrl-cli.linux-x64](https://www.nuget.org/packages/DubUrl-cli.linux-x64) | 0.31.1 | Cédric L. Charlier | Package Description |
| 2026-10-17 22:23:17 | [DubUrl-cli.win-arm64](https://www.nuget.org/packages/DubUrl-cli.win-arm64) | 0.31.1 | Cédric L. Charlier | Package Description |
| 2026-10-17 22:23:19 | [DubUrl-cli.win-x64](https://www.nuget.org/packages/DubUrl-cli.win-x64) | 0.31.1 | Cédric L. Charlier | Package Description |
| 2026-10-17 22:32:56 | [Losol.Spark.Store.PostgreSQL](https://www.nuget.org/packages/Losol.Spark.Store.PostgreSQL) | 0.1.0 | Losol AS | PostgreSQL Storage Implementation for Spark |
| 2026-10-17 23:04:53 | [TKWF.Federation.WeChat.MessageGateway](https://www.nuget.org/packages/TKWF.Federation.WeChat.MessageGateway) | 0.1.1 | LoongBa.cn 龙爸出品 | TKWF 运行库（纯逻辑零实体零持久化——微信公众号消息网关核心判定，对齐 DataPort/Tagging 运行库提炼先例）：路由规则判定 / 幂等键规范化… |
| 2026-10-17 23:07:56 | [KeysetEngine.Core](https://www.nuget.org/packages/KeysetEngine.Core) | 1.0.0 | Paul Abib Camano | High-performance, database-agnostic keyset pagination, expression tree builders… |
| 2026-10-17 23:07:58 | [KeysetEngine.DataProtection](https://www.nuget.org/packages/KeysetEngine.DataProtection) | 1.0.0 | Paul Abib Camano | Cryptographic ASP.NET Core Data Protection cursor tokens with purpose and entit… |
| 2026-10-17 23:07:59 | [KeysetEngine.PostgreSql](https://www.nuget.org/packages/KeysetEngine.PostgreSql) | 1.0.0 | Paul Abib Camano | PostgreSQL dialect search adapters for KeysetEngine using EF.Functions.ILike an… |
| 2026-10-17 23:08:01 | [KeysetEngine.SqlServer](https://www.nuget.org/packages/KeysetEngine.SqlServer) | 1.0.0 | Paul Abib Camano | Microsoft SQL Server dialect search adapters for KeysetEngine using EF.Function… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
