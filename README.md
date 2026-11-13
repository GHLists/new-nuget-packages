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

## Latest list — 2026-11-13 02:20 UTC

New packages created between 2026-11-13 01:20 UTC and 2026-11-13 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T02-20-11-219065Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 01:21:03 | [Meziantou.Framework.WebPlatform.DevTools](https://www.nuget.org/packages/Meziantou.Framework.WebPlatform.DevTools) | 1.0.0 | meziantou | A Chrome DevTools Protocol (CDP) server for Meziantou.Framework.WebPlatform: Pl… |
| 2026-11-13 01:21:04 | [Meziantou.Framework.WebPlatform.DevTools.Tool](https://www.nuget.org/packages/Meziantou.Framework.WebPlatform.DevTools.Tool) | 1.0.0 | meziantou | CLI that runs a Chrome DevTools Protocol server whose browser is Meziantou.Fram… |
| 2026-11-13 01:35:52 | [Euonia.Auditing](https://www.nuget.org/packages/Euonia.Auditing) | 2026.5.0 | damon | Euonia 审计能力内核：作用域/动作模型、记录契约、写入队列、脱敏序列化与 InMemory 存储。 / Auditing kernel for Euon… |
| 2026-11-13 01:35:53 | [Euonia.Auditing.EfCore](https://www.nuget.org/packages/Euonia.Auditing.EfCore) | 2026.5.0 | damon | Euonia 审计的 EF Core 存储适配：独立审计库、幂等落库、动作去重与索引约定。 / EF Core persistence adapter for… |
| 2026-11-13 01:35:54 | [Euonia.Auditing.Mongo](https://www.nuget.org/packages/Euonia.Auditing.Mongo) | 2026.5.0 | damon | Euonia 审计的 MongoDB 存储适配：按作用域幂等、动作键去重与唯一索引。 / MongoDB persistence adapter for Eu… |
| 2026-11-13 01:35:58 | [Euonia.Endpoint](https://www.nuget.org/packages/Euonia.Endpoint) | 2026.5.0 | damon | Euonia Endpoint contracts: attributes and shared data contracts for exposing se… |
| 2026-11-13 01:35:59 | [Euonia.Endpoint.Grpc](https://www.nuget.org/packages/Euonia.Endpoint.Grpc) | 2026.5.0 | damon | Euonia Endpoint gRPC runtime. |
| 2026-11-13 01:35:59 | [Euonia.Endpoint.Http](https://www.nuget.org/packages/Euonia.Endpoint.Http) | 2026.5.0 | damon | Euonia Endpoint HTTP runtime: expose marked service methods as Minimal API endp… |
| 2026-11-13 01:36:00 | [Euonia.Endpoint.SourceGenerator](https://www.nuget.org/packages/Euonia.Endpoint.SourceGenerator) | 2026.5.0 | damon | Euonia development framework and toolkit library for .NET application/service.… |
| 2026-11-13 01:36:04 | [Euonia.Telemetry](https://www.nuget.org/packages/Euonia.Telemetry) | 2026.5.0 | damon | Euonia 遥测能力内核：Activity/Meter 源、标签脱敏、上下文、W3C 传播与日志 Scope，不依赖 OTel SDK。 / Telemet… |
| 2026-11-13 01:36:05 | [Euonia.Telemetry.Otel](https://www.nuget.org/packages/Euonia.Telemetry.Otel) | 2026.5.0 | damon | Euonia 遥测的 OpenTelemetry 适配：显式源目录、Resource、OTLP 导出与传播器桥接。 / OpenTelemetry adapt… |
| 2026-11-13 01:36:05 | [Euonia.Tenancy](https://www.nuget.org/packages/Euonia.Tenancy) | 2026.5.0 | damon | Euonia 多租户能力内核：租户上下文、解析链、存储、隔离模式、EF/Mongo/消息/后台任务的租户适配契约与消息匿名化默认实现。 / Multi-ten… |
| 2026-11-13 01:41:21 | [Kebechet.Maui.Hybrid.YouTube.Embed](https://www.nuget.org/packages/Kebechet.Maui.Hybrid.YouTube.Embed) | 1.0.0 | Kebechet | Plays YouTube videos inside .NET MAUI hybrid apps (BlazorWebView, HybridWebView… |
| 2026-11-13 01:50:35 | [Loom.Schema](https://www.nuget.org/packages/Loom.Schema) | 2026.11.13 | ehncraft | SpiceDB-style schema language for Loom: lexer, parser, and AST for definitions,… |
| 2026-11-13 01:50:35 | [Loom.Testing](https://www.nuget.org/packages/Loom.Testing) | 2026.11.13 | ehncraft | Framework-agnostic assertion helpers for Loom -- ShouldPermitAsync/ShouldDenyAs… |
| 2026-11-13 01:50:36 | [Loom.Relationships](https://www.nuget.org/packages/Loom.Relationships) | 2026.11.13 | ehncraft | Mutable relation-tuple storage for Loom: read/write/delete and namespace enumer… |
| 2026-11-13 01:50:36 | [Loom.Evaluator](https://www.nuget.org/packages/Loom.Evaluator) | 2026.11.13 | ehncraft | The Check algorithm: resolves a Loom schema's permission rewrite tree against s… |
| 2026-11-13 01:50:37 | [Loom.Caveats](https://www.nuget.org/packages/Loom.Caveats) | 2026.11.13 | ehncraft | A CEL-subset expression engine for Loom caveats: parameterized ABAC conditions… |
| 2026-11-13 01:50:38 | [Loom.Spool](https://www.nuget.org/packages/Loom.Spool) | 2026.11.13 | ehncraft | SQL Server-backed relation-tuple and schema storage for Loom, with configurable… |
| 2026-11-13 01:50:38 | [Loom.AspNetCore](https://www.nuget.org/packages/Loom.AspNetCore) | 2026.11.13 | ehncraft | ASP.NET Core DI integration for Loom -- services.AddLoom(...) registration and… |
| 2026-11-13 01:50:39 | [Loom.AuthZen](https://www.nuget.org/packages/Loom.AuthZen) | 2026.11.13 | ehncraft | AuthZEN Authorization API 1.0-compatible HTTP endpoint (MapAuthZenEndpoints) in… |
| 2026-11-13 01:50:39 | [Loom.Core](https://www.nuget.org/packages/Loom.Core) | 2026.11.13 | ehncraft | Core value types for Loom: ObjectRef, SubjectRef, RelationTuple, and CheckResul… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
