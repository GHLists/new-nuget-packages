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

## Latest list — 2026-10-22 13:20 UTC

New packages created between 2026-10-22 12:22 UTC and 2026-10-22 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T13-20-49-374708Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 12:24:50 | [PdfPinata.ImageSharp4](https://www.nuget.org/packages/PdfPinata.ImageSharp4) | 0.5.0 | Stefan Steiger and Contributo… | ImageSharp 4 imaging and font backend for PdfPinata. Provides ImageSharpImageSo… |
| 2026-10-22 12:33:33 | [Purview.Architecture.Testing.Cli](https://www.nuget.org/packages/Purview.Architecture.Testing.Cli) | 1.2.0 | Kieron Lanning | Runs the Purview architecture policy outside TUnit: validates the policy docume… |
| 2026-10-22 12:40:08 | [AdmiralRadzen.Icons](https://www.nuget.org/packages/AdmiralRadzen.Icons) | 1.0.3 | irlyk | Full Admiral DS SVG icon pack and lazy inline SVG adapter for Radzen Blazor com… |
| 2026-10-22 12:40:09 | [AdmiralRadzen.Themes](https://www.nuget.org/packages/AdmiralRadzen.Themes) | 1.1.2 | irlyk | Admiral Design System light and dark themes for Radzen Blazor. |
| 2026-10-22 12:40:11 | [AdmiralRadzen.Components](https://www.nuget.org/packages/AdmiralRadzen.Components) | 1.2.2 | irlyk | Reusable Admiral Design System compositions for Radzen Blazor. |
| 2026-10-22 12:40:36 | [SyZero.Authentication.ApiKey](https://www.nuget.org/packages/SyZero.Authentication.ApiKey) | 9.1.0 | HaitaoJin | Package Description |
| 2026-10-22 12:40:37 | [SyZero.Authorization](https://www.nuget.org/packages/SyZero.Authorization) | 9.1.0 | HaitaoJin | SyZero 鉴权与授权模块（ASP.NET Core Identity + ABP 风格 RBAC + JWT），存储基于 SyZero.Core 仓储抽象 |
| 2026-10-22 12:40:37 | [SyZero.Authorization.AspNetCore](https://www.nuget.org/packages/SyZero.Authorization.AspNetCore) | 9.1.0 | HaitaoJin | SyZero ASP.NET Core 授权适配：将 [Authorize(Policy = "perm")] 桥接到 SyZero.IPermissionC… |
| 2026-10-22 12:40:38 | [SyZero.BackgroundJobs](https://www.nuget.org/packages/SyZero.BackgroundJobs) | 9.1.0 | HaitaoJin | SyZero 后台任务模块：IBackgroundJobManager 抽象 + 基于 Channel 的内存默认实现 + IHostedService Wo… |
| 2026-10-22 12:40:38 | [SyZero.BackgroundJobs.Quartz](https://www.nuget.org/packages/SyZero.BackgroundJobs.Quartz) | 9.1.0 | HaitaoJin | SyZero 后台任务的 Quartz 适配：Cron / 调度托管，复用 IBackgroundJob<TArgs> 抽象。 |
| 2026-10-22 12:40:38 | [SyZero.Core](https://www.nuget.org/packages/SyZero.Core) | 9.1.0 | HaitaoJin | SyZero Core |
| 2026-10-22 12:40:39 | [SyZero.DataProtection](https://www.nuget.org/packages/SyZero.DataProtection) | 9.1.0 | HaitaoJin | SyZero 数据保护模块：基于 ASP.NET Core Data Protection 提供 IFieldEncryptor 抽象与 [Encrypted… |
| 2026-10-22 12:40:39 | [SyZero.Diagnostics](https://www.nuget.org/packages/SyZero.Diagnostics) | 9.1.0 | HaitaoJin | Package Description |
| 2026-10-22 12:40:39 | [SyZero.DistributedTransaction](https://www.nuget.org/packages/SyZero.DistributedTransaction) | 9.1.0 | HaitaoJin | SyZero 分布式事务：Outbox 投递 + 简易 Saga 编排（基于 IEventBus） |
| 2026-10-22 12:40:40 | [SyZero.DistributedTransaction.EntityFrameworkCore](https://www.nuget.org/packages/SyZero.DistributedTransaction.EntityFrameworkCore) | 9.1.0 | HaitaoJin | Package Description |
| 2026-10-22 12:40:41 | [SyZero.EventBus.Kafka](https://www.nuget.org/packages/SyZero.EventBus.Kafka) | 9.1.0 | HaitaoJin | Package Description |
| 2026-10-22 12:40:41 | [SyZero.EventBus.RabbitMQ](https://www.nuget.org/packages/SyZero.EventBus.RabbitMQ) | 9.1.0 | HaitaoJin | SyZero-RabbitMQ |
| 2026-10-22 12:40:41 | [SyZero.FeatureManagement](https://www.nuget.org/packages/SyZero.FeatureManagement) | 9.1.0 | HaitaoJin | SyZero 特性开关：包装 Microsoft.FeatureManagement，提供 ISyFeatureManager 抽象与默认实现。 |
| 2026-10-22 12:40:42 | [SyZero.Files](https://www.nuget.org/packages/SyZero.Files) | 9.1.0 | HaitaoJin | Package Description |
| 2026-10-22 12:40:42 | [SyZero.Gateway.Abstractions](https://www.nuget.org/packages/SyZero.Gateway.Abstractions) | 9.1.0 | HaitaoJin | SyZero 网关抽象层（IGateway / IGatewayConfigurationStore / IGatewayConfigurationAppli… |
| 2026-10-22 12:40:42 | [SyZero.Gateway.Admin](https://www.nuget.org/packages/SyZero.Gateway.Admin) | 9.1.0 | HaitaoJin | SyZero 网关的可视化管理面板（Routes / SwaggerEndPoints CRUD），含 Razor Pages UI、Basic Auth、配… |
| 2026-10-22 12:40:43 | [SyZero.Gateway.Ocelot](https://www.nuget.org/packages/SyZero.Gateway.Ocelot) | 9.1.0 | HaitaoJin | SyZero 网关模块的 Ocelot 实现，提供 IGateway / IGatewayConfigurationStore / IGatewayConfi… |
| 2026-10-22 12:40:43 | [SyZero.Gateway.YARP](https://www.nuget.org/packages/SyZero.Gateway.YARP) | 9.1.0 | HaitaoJin | SyZero 网关模块的 YARP（Yet Another Reverse Proxy）实现，提供 IGateway / IGatewayConfigurat… |
| 2026-10-22 12:40:43 | [SyZero.GraphQL](https://www.nuget.org/packages/SyZero.GraphQL) | 9.1.0 | HaitaoJin | Package Description |
| 2026-10-22 12:40:43 | [SyZero.HealthChecks](https://www.nuget.org/packages/SyZero.HealthChecks) | 9.1.0 | HaitaoJin | SyZero 健康检查模块：包装 Microsoft.Extensions.Diagnostics.HealthChecks，提供 /health/live… |
| 2026-10-22 12:40:44 | [SyZero.Idempotency](https://www.nuget.org/packages/SyZero.Idempotency) | 9.1.0 | HaitaoJin | SyZero 幂等性中间件 + 抽象存储（默认内存，Redis 后端在 SyZero.Redis 中提供） |
| 2026-10-22 12:40:44 | [SyZero.Localization](https://www.nuget.org/packages/SyZero.Localization) | 9.1.0 | HaitaoJin | SyZero 多语言资源抽象：包装 Microsoft.Extensions.Localization，提供 ISyStringLocalizer。 |
| 2026-10-22 12:40:44 | [SyZero.Logging.Log4Net](https://www.nuget.org/packages/SyZero.Logging.Log4Net) | 9.1.0 | HaitaoJin | SyZero-Log4Net |
| 2026-10-22 12:40:44 | [SyZero.Mail](https://www.nuget.org/packages/SyZero.Mail) | 9.1.0 | HaitaoJin | Package Description |
| 2026-10-22 12:40:45 | [SyZero.MultiTenancy](https://www.nuget.org/packages/SyZero.MultiTenancy) | 9.1.0 | HaitaoJin | SyZero 多租户模块：ICurrentTenant / ITenantStore / ITenantResolver（Header / Domain /… |
| 2026-10-22 12:40:45 | [SyZero.MultiTenancy.EntityFrameworkCore](https://www.nuget.org/packages/SyZero.MultiTenancy.EntityFrameworkCore) | 9.1.0 | HaitaoJin | SyZero 多租户 EF Core 持久化扩展：EfCoreTenantStore + 全局查询过滤辅助。 |
| 2026-10-22 12:40:46 | [SyZero.ObjectMapping.AutoMapper](https://www.nuget.org/packages/SyZero.ObjectMapping.AutoMapper) | 9.1.0 | HaitaoJin | SyZero AutoMapper integration - Object-to-object mapping with automatic profile… |
| 2026-10-22 12:40:46 | [SyZero.ObjectMapping.Mapster](https://www.nuget.org/packages/SyZero.ObjectMapping.Mapster) | 9.1.0 | HaitaoJin | SyZero-Mapster: 基于 Mapster 的 IObjectMapper 实现，作为 SyZero.ObjectMapping.AutoMappe… |
| 2026-10-22 12:40:46 | [SyZero.Observability.OpenTelemetry](https://www.nuget.org/packages/SyZero.Observability.OpenTelemetry) | 9.1.0 | HaitaoJin | SyZero-OpenTelemetry |
| 2026-10-22 12:40:46 | [SyZero.RateLimiting](https://www.nuget.org/packages/SyZero.RateLimiting) | 9.1.0 | HaitaoJin | SyZero 限流模块：包装 .NET 内置 System.Threading.RateLimiting 与 ASP.NET Core RateLimiter… |
| 2026-10-22 12:40:47 | [SyZero.Realtime](https://www.nuget.org/packages/SyZero.Realtime) | 9.1.0 | HaitaoJin | Package Description |
| 2026-10-22 12:40:47 | [SyZero.Resilience](https://www.nuget.org/packages/SyZero.Resilience) | 9.1.0 | HaitaoJin | Package Description |
| 2026-10-22 12:40:48 | [SyZero.Sdk](https://www.nuget.org/packages/SyZero.Sdk) | 9.1.0 | HaitaoJin | Package Description |
| 2026-10-22 12:40:48 | [SyZero.ServiceDiscovery.Consul](https://www.nuget.org/packages/SyZero.ServiceDiscovery.Consul) | 9.1.0 | HaitaoJin | SyZero-Consul |
| 2026-10-22 12:40:48 | [SyZero.ServiceDiscovery.Nacos](https://www.nuget.org/packages/SyZero.ServiceDiscovery.Nacos) | 9.1.0 | HaitaoJin | SyZero-Nacos |
| 2026-10-22 12:40:48 | [SyZero.Sms](https://www.nuget.org/packages/SyZero.Sms) | 9.1.0 | HaitaoJin | Package Description |
| 2026-10-22 12:40:49 | [SyZero.SourceGenerator](https://www.nuget.org/packages/SyZero.SourceGenerator) | 9.1.0 | HaitaoJin | Package Description |
| 2026-10-22 12:44:41 | [DndKit.Blazor](https://www.nuget.org/packages/DndKit.Blazor) | 1.0.0 | DndKit.Blazor contributors | A .NET 10 Razor Class Library adapter for dnd-kit DOM drag-and-drop behavior in… |
| 2026-10-22 12:47:49 | [Elvia.Adms.Events.Switchingplan](https://www.nuget.org/packages/Elvia.Adms.Events.Switchingplan) | 1.0.0 | adms-extensions-lib-switching… | Package Description |
| 2026-10-22 12:54:15 | [BetterRedsys.Simulator](https://www.nuget.org/packages/BetterRedsys.Simulator) | 1.0.0 | Jose Sagasta, BetterRedsys Co… | Interactive in-memory local simulator, UI sandbox, and mock server for Redsys a… |
| 2026-10-22 12:54:15 | [BetterRedsys](https://www.nuget.org/packages/BetterRedsys) | 1.0.0 | Jose Sagasta, BetterRedsys Co… | Modern, strongly-typed, high-performance, and Native AOT library for Redsys and… |
| 2026-10-22 12:57:01 | [VibeDxf.Wpf](https://www.nuget.org/packages/VibeDxf.Wpf) | 0.2.0 | Yoav Miller and contributors | Embeddable Windows/WPF DXF viewer with prepared text geometry, document travers… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
