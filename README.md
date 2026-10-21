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

## Latest list — 2026-10-21 09:21 UTC

New packages created between 2026-10-21 08:19 UTC and 2026-10-21 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T09-21-28-923223Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 08:20:28 | [Umbraco.Community.PropertyAuditTool](https://www.nuget.org/packages/Umbraco.Community.PropertyAuditTool) | 0.4.0 | Kim Gordon Taanning | Read-only Umbraco backoffice audit for finding incomplete or matching content a… |
| 2026-10-21 08:29:45 | [VOCsReminder](https://www.nuget.org/packages/VOCsReminder) | 1.0.0 | Estrella Zhang | VOCs色谱设备备忘录中心库可帮助您便捷实现磁盘容量不足告警和设备模块维护到期提醒，并通过清晰的接口与应用层 UI 集成。支持 SQLite 本地数据存储及检… |
| 2026-10-21 08:30:01 | [PCHMI.NativeSQLite](https://www.nuget.org/packages/PCHMI.NativeSQLite) | 1.0.0 | GreatBear | Minimal SQLite wrapper for .NET with win-x64 and win-x86 native binaries. Works… |
| 2026-10-21 08:35:58 | [ProduceSelf.Base.Compression](https://www.nuget.org/packages/ProduceSelf.Base.Compression) | 2.1.0 | 沧海的频道 | 沧海的频道基础工具类库的压缩部分：基于 SharpCompress 的多格式压缩解压与进度回调。 |
| 2026-10-21 08:42:47 | [SourceOrrery](https://www.nuget.org/packages/SourceOrrery) | 0.1.1 | James Melvin | Read secrets from a SourceOrrery vault. Secrets belong to the runtime, not the… |
| 2026-10-21 09:07:20 | [Devinno.Communication](https://www.nuget.org/packages/Devinno.Communication) | 0.1.0 | Devinno | Industrial device communication library for .NET 8 — Modbus RTU/TCP, LS CNet/FE… |
| 2026-10-21 09:08:13 | [Umbraco.Community.Unlog](https://www.nuget.org/packages/Umbraco.Community.Unlog) | 18.0.1 | skttl | Retention rules for Umbraco's Serilog file logs. |
| 2026-10-21 09:09:10 | [NativeSQLite](https://www.nuget.org/packages/NativeSQLite) | 1.0.0 | GreatBear | Minimal SQLite wrapper for .NET with win-x64 and win-x86 native binaries. Works… |
| 2026-10-21 09:12:59 | [NetQuota.Firestore](https://www.nuget.org/packages/NetQuota.Firestore) | 1.0.0 | Mihai Dumitru | Google Cloud Firestore transactional storage adapter for NetQuota with TTL expi… |
| 2026-10-21 09:13:02 | [NetQuota.Postgres](https://www.nuget.org/packages/NetQuota.Postgres) | 1.0.0 | Mihai Dumitru | PostgreSQL storage adapter for NetQuota with row-locked transactions, promotion… |
| 2026-10-21 09:13:03 | [NetQuota](https://www.nuget.org/packages/NetQuota) | 1.0.0 | Mihai Dumitru | Production-ready subscription quota and hybrid rate-limiting engine for .NET (a… |
| 2026-10-21 09:13:03 | [NetQuota.Redis](https://www.nuget.org/packages/NetQuota.Redis) | 1.0.0 | Mihai Dumitru | Redis storage adapter for NetQuota using atomic Lua scripts for quotas, pre-pai… |
| 2026-10-21 09:13:05 | [NetQuota.Billing](https://www.nuget.org/packages/NetQuota.Billing) | 1.0.0 | Mihai Dumitru | Billing webhook integrations for NetQuota: Stripe and RevenueCat parsing, verif… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
