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

## Latest list — 2026-11-25 01:21 UTC

New packages created between 2026-11-25 00:19 UTC and 2026-11-25 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T01-21-08-228676Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 00:34:43 | [OpenCreativeSuite.Components.Files](https://www.nuget.org/packages/OpenCreativeSuite.Components.Files) | 1.0.0 | OpenCreativeSuite.Components.… | File browser components for Donkeh apps. |
| 2026-11-25 00:48:18 | [WASU.SDK.RPC](https://www.nuget.org/packages/WASU.SDK.RPC) | 26.1125.8 | WASU.SDK.RPC | Package Description |
| 2026-11-25 00:57:36 | [NCode.Coordination.Abstractions](https://www.nuget.org/packages/NCode.Coordination.Abstractions) | 0.1.0 | NCode Group | The contracts of NCode.Coordination: structured keys, the guarantee vocabulary,… |
| 2026-11-25 01:10:34 | [PalDDD.Dapper](https://www.nuget.org/packages/PalDDD.Dapper) | 5.0.0 | PalDDD | Pal.DDD Dapper 持久化适配器（调用点级 NativeAOT：`[module:DapperAot]` 已启用，34 调用点拦截器接管，三方言实测… |
| 2026-11-25 01:10:35 | [PalDDD.Dapper.MySql](https://www.nuget.org/packages/PalDDD.Dapper.MySql) | 5.0.0 | PalDDD | Pal.DDD MySQL 增强扩展包（AOT 状态随母包：调用点级 NativeAOT 已启用，详见 PalDDD.Dapper） |
| 2026-11-25 01:10:36 | [PalDDD.Dapper.PostgreSql](https://www.nuget.org/packages/PalDDD.Dapper.PostgreSql) | 5.0.0 | PalDDD | Pal.DDD PostgreSQL 增强扩展包（AOT 状态随母包：调用点级 NativeAOT 已启用，详见 PalDDD.Dapper） |
| 2026-11-25 01:10:37 | [PalDDD.Dapper.Sqlite](https://www.nuget.org/packages/PalDDD.Dapper.Sqlite) | 5.0.0 | PalDDD | Pal.DDD SQLite FTS5/JSON1 与 PRAGMA 增强扩展包（AOT 状态随母包：调用点级 NativeAOT 已启用，详见 PalDDD… |
| 2026-11-25 01:10:38 | [PalDDD.DependencyInjection](https://www.nuget.org/packages/PalDDD.DependencyInjection) | 5.0.0 | PalDDD | Pal.DDD DI 组装 — AddPalCoreStack/AddPalCqrs 等组件级注册入口与 IPalLogger 门面接线。 |
| 2026-11-25 01:10:39 | [PalDDD.EventLog.EFCore](https://www.nuget.org/packages/PalDDD.EventLog.EFCore) | 5.0.0 | PalDDD | Pal.DDD EventLog 的 EF Core 适配器 — EventLogDbContext 与乐观并发追加（非 AOT 栈）。 |
| 2026-11-25 01:10:40 | [PalDDD.Extension](https://www.nuget.org/packages/PalDDD.Extension) | 5.0.0 | PalDDD | Pal.DDD 扩展元包 — 全量 DDD 能力：CQRS + 事件日志 + 幂等 + 投影 + 消息 + 事务 + DI 装配。含非 AOT 的 Trans… |
| 2026-11-25 01:10:41 | [PalDDD.Hosting.AspNetCore.OutboxHealth](https://www.nuget.org/packages/PalDDD.Hosting.AspNetCore.OutboxHealth) | 5.0.0 | PalDDD | Pal.DDD 可选 Outbox 健康检查包：不需要健康检查的 Hosting 消费方不必再传递引用 Transactions。 |
| 2026-11-25 01:10:43 | [PalDDD.Idempotency.EFCore](https://www.nuget.org/packages/PalDDD.Idempotency.EFCore) | 5.0.0 | PalDDD | Pal.DDD 幂等的 EF Core 适配器 — 幂等记录存储（非 AOT 栈）。 |
| 2026-11-25 01:10:49 | [PalDDD.Projections.EFCore](https://www.nuget.org/packages/PalDDD.Projections.EFCore) | 5.0.0 | PalDDD | Pal.DDD 投影的 EF Core 适配器 — 检查点存储（非 AOT 栈）。 |
| 2026-11-25 01:10:51 | [PalDDD.Repository.EFCore](https://www.nuget.org/packages/PalDDD.Repository.EFCore) | 5.0.0 | PalDDD | Pal.DDD 仓储的 EF Core 适配器 — IRepository<T> 实现与领域事件 Outbox 桥（非 AOT 栈）。 |
| 2026-11-25 01:10:55 | [PalDDD.Transactions.EFCore](https://www.nuget.org/packages/PalDDD.Transactions.EFCore) | 5.0.0 | PalDDD | Pal.DDD Outbox/Inbox 的 EF Core 方言基类 — PostgreSql/MySql/Sqlite OutboxDbContext（非… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
