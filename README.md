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

## Latest list — 2026-11-20 00:20 UTC

New packages created between 2026-11-19 23:20 UTC and 2026-11-20 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T00-20-26-701199Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 23:22:15 | [Sattleme.Checkout](https://www.nuget.org/packages/Sattleme.Checkout) | 1.0.0 | sattle.me | Take Lightning and on-chain payments for a sattle.me merchant from an online sh… |
| 2026-11-19 23:30:00 | [Sidub.Platform.Payments.Finix](https://www.nuget.org/packages/Sidub.Platform.Payments.Finix) | 1.22.0 | Sidub Inc. | Package Description |
| 2026-11-19 23:31:46 | [ForEach.Sms.Abstractions](https://www.nuget.org/packages/ForEach.Sms.Abstractions) | 0.1.0 | For-Each Smederevo | ISmsSender and ISmsGateway: the vendor-neutral contracts for sending a text mes… |
| 2026-11-19 23:31:47 | [ForEach.Sms.SmsBox](https://www.nuget.org/packages/ForEach.Sms.SmsBox) | 0.1.0 | For-Each Smederevo | SMSBOX implementation of ForEach.Sms.Abstractions: AddSmsBox registers ISmsSend… |
| 2026-11-19 23:32:25 | [ParadeDB.VectorData](https://www.nuget.org/packages/ParadeDB.VectorData) | 0.6.0 | ParadeDB | Microsoft.Extensions.VectorData cosine search over ParadeDB Entity Framework Co… |
| 2026-11-19 23:40:28 | [VPet-Simulator.Unified](https://www.nuget.org/packages/VPet-Simulator.Unified) | 1.0.0 | LorisYounger | 虚拟桌宠模拟器（VPet）的跨平台代码 MOD 开发包。使用 UnifiedPlugin 编写一份插件 DLL，在支持 Unified 的 Windows 本… |
| 2026-11-19 23:42:48 | [ForEach.Storage.S3](https://www.nuget.org/packages/ForEach.Storage.S3) | 0.1.0 | For-Each Smederevo | S3-compatible implementation of IFileBlobStore (AWS S3, Hetzner Object Storage,… |
| 2026-11-19 23:42:49 | [ForEach.Storage.AzureBlob](https://www.nuget.org/packages/ForEach.Storage.AzureBlob) | 0.1.0 | For-Each Smederevo | Azure Blob Storage implementation of IFileBlobStore: key prefix, SDK retries, c… |
| 2026-11-19 23:42:49 | [ForEach.Storage.Abstractions](https://www.nuget.org/packages/ForEach.Storage.Abstractions) | 0.1.0 | For-Each Smederevo | IFileBlobStore: the vendor-neutral contract for storing, reading, listing and d… |
| 2026-11-19 23:46:19 | [SoftwareExtravaganza.Whizbang.Rules](https://www.nuget.org/packages/SoftwareExtravaganza.Whizbang.Rules) | 0.4457.0 | Phil Carbone | The eligibility rules storage cleanup and stream integrity share: the per-type… |
| 2026-11-19 23:51:13 | [GCR.Domains.Core.Notification](https://www.nuget.org/packages/GCR.Domains.Core.Notification) | 0.4.0 | GCR | Core 模块领域层：通知引擎实体（邮件服务配置、通道配置、通知模板、发送记录、站内信） |
| 2026-11-19 23:51:34 | [McpEssentials.Analyzers](https://www.nuget.org/packages/McpEssentials.Analyzers) | 1.0.0 | CloudNimble | Catch broken MCP forms at compile time. Warns on unmappable properties, collidi… |
| 2026-11-19 23:51:35 | [McpEssentials.Core](https://www.nuget.org/packages/McpEssentials.Core) | 1.0.0 | CloudNimble | Build multi-user MCP servers in .NET. Isolate long-running tasks per user, elic… |
| 2026-11-19 23:51:35 | [McpEssentials.Cosmos](https://www.nuget.org/packages/McpEssentials.Cosmos) | 1.0.0 | CloudNimble | Run MCP tasks on Azure Cosmos DB for NoSQL. Point reads by owner, native docume… |
| 2026-11-19 23:51:36 | [McpEssentials.EntityFrameworkCore](https://www.nuget.org/packages/McpEssentials.EntityFrameworkCore) | 1.0.0 | CloudNimble | Persist MCP tasks in the database you already run. Works with any EF Core provi… |
| 2026-11-19 23:51:36 | [McpEssentials.PostgreSQL](https://www.nuget.org/packages/McpEssentials.PostgreSQL) | 1.0.0 | CloudNimble | Run MCP tasks on PostgreSQL without EF. Npgsql owns the row; LISTEN/NOTIFY wake… |
| 2026-11-19 23:51:37 | [McpEssentials.Redis](https://www.nuget.org/packages/McpEssentials.Redis) | 1.0.0 | CloudNimble | Run MCP tasks on Redis. Keys expire on their own, and pub/sub wakes every node… |
| 2026-11-19 23:58:10 | [ECMAScript.Vue](https://www.nuget.org/packages/ECMAScript.Vue) | 2.2.0 | hanxj | Shared Vue 3 type bindings and runtime resource metadata for Jazor. |
| 2026-11-19 23:58:26 | [Jazor.Jolt](https://www.nuget.org/packages/Jazor.Jolt) | 2.2.0 | hanxj | Build and edit Jolt .jazor Vue components written in C#. |
| 2026-11-19 23:58:29 | [Jazor.Jolt.linux-arm64](https://www.nuget.org/packages/Jazor.Jolt.linux-arm64) | 2.2.0 | hanxj | Build and edit Jolt .jazor Vue components written in C#. |
| 2026-11-19 23:58:33 | [Jazor.Jolt.linux-x64](https://www.nuget.org/packages/Jazor.Jolt.linux-x64) | 2.2.0 | hanxj | Build and edit Jolt .jazor Vue components written in C#. |
| 2026-11-19 23:58:37 | [Jazor.Jolt.win-arm64](https://www.nuget.org/packages/Jazor.Jolt.win-arm64) | 2.2.0 | hanxj | Build and edit Jolt .jazor Vue components written in C#. |
| 2026-11-19 23:58:40 | [Jazor.Jolt.win-x64](https://www.nuget.org/packages/Jazor.Jolt.win-x64) | 2.2.0 | hanxj | Build and edit Jolt .jazor Vue components written in C#. |
| 2026-11-20 00:10:17 | [DMXControl3-Network-Interface](https://www.nuget.org/packages/DMXControl3-Network-Interface) | 3.3.3 | DMXControl Projects e.V. | gRPC client library for the DMXControl 3 network interface |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
