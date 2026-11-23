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

## Latest list — 2026-11-23 03:21 UTC

New packages created between 2026-11-23 02:21 UTC and 2026-11-23 03:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T03-21-18-511414Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 02:27:58 | [Gt.IoTelemetry.CNC.Model](https://www.nuget.org/packages/Gt.IoTelemetry.CNC.Model) | 1.0.0 | Gt.IoTelemetry.CNC.Model | Package Description |
| 2026-11-23 02:30:59 | [Kun.Audit.Abstractions](https://www.nuget.org/packages/Kun.Audit.Abstractions) | 2026.11.21 | Kun Framework Contributors | 审计记录、链校验与错误契约。 |
| 2026-11-23 02:31:01 | [Kun.Audit.Postgres](https://www.nuget.org/packages/Kun.Audit.Postgres) | 2026.11.21 | Kun Framework Contributors | 原生 PostgreSQL 审计 Provider：共享 v1 协议、受限追加函数与 NativeData 事务。 |
| 2026-11-23 02:31:08 | [Kun.Configuration.Abstractions](https://www.nuget.org/packages/Kun.Configuration.Abstractions) | 2026.11.21 | Kun Framework Contributors | 配置 seam 的只读端口与错误词汇。 |
| 2026-11-23 02:31:10 | [Kun.Configuration.Secrets](https://www.nuget.org/packages/Kun.Configuration.Secrets) | 2026.11.21 | Kun Framework Contributors | 挂载式密钥文件解析与权限边界。 |
| 2026-11-23 02:31:13 | [Kun.Data.Native.Abstractions](https://www.nuget.org/packages/Kun.Data.Native.Abstractions) | 2026.11.21 | Kun Framework Contributors | 原生数据库连接与事务的 NativeData Definition，不依赖 EF。 |
| 2026-11-23 02:31:14 | [Kun.Data.Native.Postgres](https://www.nuget.org/packages/Kun.Data.Native.Postgres) | 2026.11.21 | Kun Framework Contributors | NativeData 的 PostgreSQL 受限连接、租户隔离与事务 Provider。 |
| 2026-11-23 02:31:17 | [Kun.EntityFrameworkCore.PostgreSQL](https://www.nuget.org/packages/Kun.EntityFrameworkCore.PostgreSQL) | 2026.11.21 | Kun Framework Contributors | Kun 的 PostgreSQL 迁移 SQL 生成器：建租户表时紧接着打开行级安全并建租户策略。 |
| 2026-11-23 02:31:18 | [Kun.Errors](https://www.nuget.org/packages/Kun.Errors) | 2026.11.21 | Kun Framework Contributors | Kun 结构化错误：错误码目录、Error 与 ErrorException、RFC 9457 problem+json 的 ErrorDetail 配置文件… |
| 2026-11-23 02:31:20 | [Kun.Errors.AspNetCore](https://www.nuget.org/packages/Kun.Errors.AspNetCore) | 2026.11.21 | Kun Framework Contributors | Kun 结构化错误的 ASP.NET Core 映射：problem+json（ErrorDetail）输出、异常与状态码兜底、ProblemDetails… |
| 2026-11-23 02:31:24 | [Kun.EventBus.EntityFrameworkCore](https://www.nuget.org/packages/Kun.EventBus.EntityFrameworkCore) | 2026.11.21 | Kun Framework Contributors | EF Core event outbox relay and event component configuration. |
| 2026-11-23 02:31:27 | [Kun.Gateway.Abstractions](https://www.nuget.org/packages/Kun.Gateway.Abstractions) | 2026.11.21 | Kun Framework Contributors | 业务网关的服务键、声明式路由与固定安全配置契约。 |
| 2026-11-23 02:31:36 | [Kun.Plugin.Sdk](https://www.nuget.org/packages/Kun.Plugin.Sdk) | 2026.11.21 | Kun Framework Contributors | Kun 插件开发包：组件的代码声明、生成契约与命令策略协议（内核档）；命令管道在 Kun.Plugin.Sdk.Commands。 |
| 2026-11-23 02:31:37 | [Kun.Plugin.Sdk.Generators](https://www.nuget.org/packages/Kun.Plugin.Sdk.Generators) | 2026.11.21 | Kun Framework Contributors | Kun 插件开发包的增量源生成器：从组件代码派生元数据、能力与作业契约，只以分析器引用。 |
| 2026-11-23 02:31:39 | [Kun.Runtime](https://www.nuget.org/packages/Kun.Runtime) | 2026.11.21 | Kun Framework Contributors | Kun 组件运行时：插件装载、服务键、事件与可逆副作用；不带产品语义（scope 种类与表面目录键由平台档定）。 |
| 2026-11-23 02:31:41 | [Kun.Security.Abstractions](https://www.nuget.org/packages/Kun.Security.Abstractions) | 2026.11.21 | Kun Framework Contributors | Kun 服务间令牌的主体模型与声明词汇表：Principal、DelegationActor、PrincipalKind 与 IdentityClaimNam… |
| 2026-11-23 02:31:48 | [Kun.Testing.Containers](https://www.nuget.org/packages/Kun.Testing.Containers) | 2026.11.21 | Kun Framework Contributors | 使用 xUnit v3 的 .NET 集成测试容器夹具。支持 PostgreSQL、Redis、RabbitMQ、PgBouncer、S3 兼容存储、配置与身… |
| 2026-11-23 02:38:11 | [Alphard.ProbablyStolen.Templates](https://www.nuget.org/packages/Alphard.ProbablyStolen.Templates) | 0.1.0 | Alphard | 最小模板，通过NuGet分发项目模板 适用于Rider |
| 2026-11-23 02:47:53 | [GCCN.ActiveReports.AI.Web](https://www.nuget.org/packages/GCCN.ActiveReports.AI.Web) | 20.2.1 | GrapeCity China, Inc. | ActiveReports AI Web 提供 ASP.NET Core 中间件，将 AI 报表智能辅助功能集成到 Web 报表设计器中，支持智能报表创建和数… |
| 2026-11-23 02:50:16 | [RadiantWorks.Imaging](https://www.nuget.org/packages/RadiantWorks.Imaging) | 1.1.2 | RadiantWorks | 工业图像处理、胶片查重和应用授权校验组件。 |
| 2026-11-23 02:50:18 | [GCCN.ActiveReports.Design.AI.Reporting](https://www.nuget.org/packages/GCCN.ActiveReports.Design.AI.Reporting) | 20.2.1 | GrapeCity China, Inc. | ActiveReports is a set of assemblies that enable you to create, render, print,… |
| 2026-11-23 02:53:06 | [NonceSense.FileGuard](https://www.nuget.org/packages/NonceSense.FileGuard) | 1.0.0 | NonceSense | NonceSense.FileGuard is a lightweight .NET 10 utility library for inspecting fi… |
| 2026-11-23 03:01:57 | [ActualLab.Core.Legacy](https://www.nuget.org/packages/ActualLab.Core.Legacy) | 16.0.4 | Actual Chat, Inc. | ActualLab.Core.Legacy - obsolete ActualLab.Core types kept for compatibility (O… |
| 2026-11-23 03:02:06 | [ActualLab.Fusion.Ext.Backend.Contracts](https://www.nuget.org/packages/ActualLab.Fusion.Ext.Backend.Contracts) | 16.0.4 | Actual Chat, Inc. | Backend service contracts of ActualLab.Fusion extensions (IAuthBackend, IKeyVal… |
| 2026-11-23 03:02:24 | [ActualLab.Serialization.MemoryPack](https://www.nuget.org/packages/ActualLab.Serialization.MemoryPack) | 16.0.4 | Actual Chat, Inc. | ActualLab.Serialization.MemoryPack - MemoryPack support for ActualLab.Fusion: a… |
| 2026-11-23 03:02:26 | [ActualLab.Serialization.NewtonsoftJson](https://www.nuget.org/packages/ActualLab.Serialization.NewtonsoftJson) | 16.0.4 | Actual Chat, Inc. | ActualLab.Serialization.NewtonsoftJson - Newtonsoft.Json support for ActualLab.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
