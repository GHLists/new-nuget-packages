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

## Latest list — 2026-10-23 07:20 UTC

New packages created between 2026-10-23 06:20 UTC and 2026-10-23 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T07-20-32-31257Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 06:30:54 | [ZYC.TilePyramid.Annotations](https://www.nuget.org/packages/ZYC.TilePyramid.Annotations) | 0.9.0 | ZYC.TilePyramid.Annotations | Package Description |
| 2026-10-23 06:31:14 | [ZYC.TilePyramid.Annotations.Wpf](https://www.nuget.org/packages/ZYC.TilePyramid.Annotations.Wpf) | 0.9.0 | ZYC.TilePyramid.Annotations.W… | Package Description |
| 2026-10-23 06:31:30 | [ZYC.TilePyramid.Core](https://www.nuget.org/packages/ZYC.TilePyramid.Core) | 0.9.0 | ZYC.TilePyramid.Core | Package Description |
| 2026-10-23 06:31:43 | [ZYC.TilePyramid.Wpf](https://www.nuget.org/packages/ZYC.TilePyramid.Wpf) | 0.9.0 | ZYC.TilePyramid.Wpf | Package Description |
| 2026-10-23 06:33:03 | [SaaSify.HealthChecks.NpgSql](https://www.nuget.org/packages/SaaSify.HealthChecks.NpgSql) | 10.0.0 | SaaSify Platform | Drop-in replacement for the upstream AspNetCore.HealthChecks.NpgSql package, re… |
| 2026-10-23 06:35:34 | [WebFilez.Storage.AzureFiles](https://www.nuget.org/packages/WebFilez.Storage.AzureFiles) | 1.0.0 | Matt Gordon | Azure Files provider for WebFilez. Register it with AddWebFilezAzureFiles(). |
| 2026-10-23 06:36:31 | [ApiFeatures.Mqtt.Cores](https://www.nuget.org/packages/ApiFeatures.Mqtt.Cores) | 9.0.0 | ApiFeatures.Mqtt.Cores | Package Description |
| 2026-10-23 06:36:32 | [ApiFeatures.Mqtt.MongoDatabases](https://www.nuget.org/packages/ApiFeatures.Mqtt.MongoDatabases) | 9.0.0 | ApiFeatures.Mqtt.MongoDatabas… | Package Description |
| 2026-10-23 06:36:33 | [ApiFeatures.Mqtt.Postgresqls](https://www.nuget.org/packages/ApiFeatures.Mqtt.Postgresqls) | 9.0.0 | ApiFeatures.Mqtt.Postgresqls | Package Description |
| 2026-10-23 06:45:52 | [NexMesh.AI](https://www.nuget.org/packages/NexMesh.AI) | 0.0.2 | NexMesh Team | NexMesh v2.0 AI:NexMeshChatFactory(预构建管道) / [NexMeshTool] 注册与安全门 / gen_ai 遥测。零… |
| 2026-10-23 06:45:54 | [NexMesh.AI.Approval](https://www.nuget.org/packages/NexMesh.AI.Approval) | 0.0.2 | NexMesh Team | NexMesh v2.0 审批门:High 风险工具挂起拦截 + 持久化审批队列(幂等键/上下文快照随队列落地)+ 批准后快照再水化执行 + 审批中心端点 |
| 2026-10-23 06:45:55 | [NexMesh.AI.SemanticCache](https://www.nuget.org/packages/NexMesh.AI.SemanticCache) | 0.0.2 | NexMesh Team | NexMesh v2.0 语义缓存:嵌入向量→余弦相似命中→秒回缓存(成本降50%+);内存暴力/Redis FT.SEARCH 双实现;ChatClient… |
| 2026-10-23 06:45:56 | [NexMesh.AI.Workflow](https://www.nuget.org/packages/NexMesh.AI.Workflow) | 0.0.2 | NexMesh Team | NexMesh v2.0 工作流引擎:多步骤 DAG + Checkpoint 持久化(Memory/FreeSql) + HITL 挂起恢复 + Backg… |
| 2026-10-23 06:45:57 | [NexMesh.Auth](https://www.nuget.org/packages/NexMesh.Auth) | 0.0.2 | NexMesh Team | NexMesh v2.0 认证:不透明 Token(登录路由/滑动续期/吊销) + 统一 401 + AutoApi 授权标注打通 ICurrentUser… |
| 2026-10-23 06:45:58 | [NexMesh.Cache](https://www.nuget.org/packages/NexMesh.Cache) | 0.0.2 | NexMesh Team | NexMesh v2.0 缓存:L1(Memory)+L2(StackExchange.Redis) 双层统一治理——命名源/单飞防击穿/分布式锁(SET N… |
| 2026-10-23 06:46:02 | [NexMesh.Core](https://www.nuget.org/packages/NexMesh.Core) | 0.0.2 | NexMesh Team | NexMesh v2.0 Core:约定注入 / AutoApi / ApiResult / 全局异常 / 配置占位符 / 健康与文档总装 |
| 2026-10-23 06:46:03 | [NexMesh.Data.FreeSql](https://www.nuget.org/packages/NexMesh.Data.FreeSql) | 0.0.2 | NexMesh Team | NexMesh v2.0 数据层:多库命名注册 + 软删全局过滤 + 审计自动填充 + 雪花 ID + 乐观并发(→409) + IRepository 仓储 |
| 2026-10-23 06:46:05 | [NexMesh.Host](https://www.nuget.org/packages/NexMesh.Host) | 0.0.2 | NexMesh Team | NexMesh v2.0 服务宿主总装:一行 AddNexMeshService/UseNexMeshService 装配 配置/约定注入/FreeSql/A… |
| 2026-10-23 06:46:06 | [NexMesh.Toolbox](https://www.nuget.org/packages/NexMesh.Toolbox) | 0.0.2 | NexMesh Team | NexMesh v2.0 工具箱:MiniExcel 导入导出 / 文件 Blob 存储(Db+Local)/ SMTP 邮件 / 数据脱敏 |
| 2026-10-23 06:46:07 | [NexMesh.Worker](https://www.nuget.org/packages/NexMesh.Worker) | 0.0.2 | NexMesh Team | NexMesh v2.0 定时调度:Cron/Interval 双基类(替代 Hangfire 的轻量自研)——异常隔离不停摆/退避等待/优雅停机/系统身份快… |
| 2026-10-23 06:48:03 | [EFCoreTerminalUI](https://www.nuget.org/packages/EFCoreTerminalUI) | 1.0.0 | Alican Aydın | Interactive terminal UI for EF Core migrations: pick projects and migrations wi… |
| 2026-10-23 06:50:25 | [M0LTE.Ms110d](https://www.nuget.org/packages/M0LTE.Ms110d) | 0.1.0 | Tom Fanning M0LTE | A managed MIL-STD-188-110D Appendix D 3 kHz serial-tone HF modem for .NET: wave… |
| 2026-10-23 06:53:18 | [Cratis.Specifications.Runner](https://www.nuget.org/packages/Cratis.Specifications.Runner) | 4.3.0 | Cratis | Experimental: Specification by Example (BDD) for .NET with a native runner on M… |
| 2026-10-23 07:12:17 | [BarakoCMS.Qr](https://www.nuget.org/packages/BarakoCMS.Qr) | 5.2.0 | Arnel Robles | QR codes for barakoCMS delivery: renders one field of a public entry as a PNG o… |
| 2026-10-23 07:12:28 | [BarakoCMS.Comments](https://www.nuget.org/packages/BarakoCMS.Comments) | 5.2.0 | Arnel Robles | Comments and notes for barakoCMS: a threaded comment on any record. A comment n… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
