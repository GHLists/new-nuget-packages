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

## Latest list — 2026-11-16 00:19 UTC

New packages created between 2026-11-15 23:20 UTC and 2026-11-16 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T00-19-39-590134Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 23:31:11 | [PaymentSystem.Generic](https://www.nuget.org/packages/PaymentSystem.Generic) | 1.0.0 | PaymentSystem.Generic | Package Description |
| 2026-11-15 23:45:33 | [ShadowDusk.SkSL](https://www.nuget.org/packages/ShadowDusk.SkSL) | 0.26.0 | ShadowDusk Contributors | ShadowDusk SkSL front-end: a pure-managed, zero-native converter that translate… |
| 2026-11-15 23:58:06 | [GCR.Capabilities.Audit](https://www.nuget.org/packages/GCR.Capabilities.Audit) | 0.2.0 | GCR | 审计能力层：审计仓储与 AuditService，跨应用统一轨迹格式。不依赖宿主，可被独立引用。 |
| 2026-11-15 23:58:08 | [GCR.Capabilities.Identity](https://www.nuget.org/packages/GCR.Capabilities.Identity) | 0.2.0 | GCR | 身份能力层：账号、角色、权限仓储与服务，认证方案，Blazor 认证状态提供者。不依赖宿主，可被独立引用。 |
| 2026-11-15 23:58:10 | [GCR.Capabilities.Security](https://www.nuget.org/packages/GCR.Capabilities.Security) | 0.2.0 | GCR | 安全能力层：API 暴露面策略、限流、集成凭据与 OAuth 2.1 / OIDC 授权服务器。不依赖宿主，可被独立引用。 |
| 2026-11-16 00:03:35 | [StemMqtt](https://www.nuget.org/packages/StemMqtt) | 0.9.0 | Sorin Irimies | MQTT 3.1.1 / 5.0 client and broker (Rust core, UniFFI C# bindings) |
| 2026-11-16 00:09:59 | [SynthEHR.Core](https://www.nuget.org/packages/SynthEHR.Core) | 3.0.0 | Health Informatics Centre - U… | Library and CLI for randomly generating medical data like you might get out of… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
