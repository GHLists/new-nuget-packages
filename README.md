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

## Latest list — 2026-10-02 10:20 UTC

New packages created between 2026-10-02 09:19 UTC and 2026-10-02 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T10-20-20-52006Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 09:23:45 | [PinguApps.Aspire.Hosting.Railway](https://www.nuget.org/packages/PinguApps.Aspire.Hosting.Railway) | 1.0.0 | PinguApps | Railway integration for Aspire. |
| 2026-10-02 09:30:37 | [BaoXia.Service.LogCenter.Defines](https://www.nuget.org/packages/BaoXia.Service.LogCenter.Defines) | 10.0.0 | 石家庄宝匣软件科技有限公司 | 宝匣服务，日志中心公共定义。 |
| 2026-10-02 09:35:44 | [BaoXia.Service.LogCenter.Client](https://www.nuget.org/packages/BaoXia.Service.LogCenter.Client) | 10.0.0 | 石家庄宝匣软件科技有限公司 | 宝匣服务，日志中心客户端。 |
| 2026-10-02 09:49:24 | [NetTriage](https://www.nuget.org/packages/NetTriage) | 0.2.0 | Ema | Deterministic, offline triage for .NET Framework to modern .NET migrations. Fin… |
| 2026-10-02 09:53:26 | [Qianyiaz.Impeller.Static](https://www.nuget.org/packages/Qianyiaz.Impeller.Static) | 1.0.0 | Qianyiaz | Impeller static library |
| 2026-10-02 09:54:04 | [BaoXia.Service.StatisticsService.Defines](https://www.nuget.org/packages/BaoXia.Service.StatisticsService.Defines) | 10.0.0 | 石家庄宝匣软件科技有限公司 | 宝匣服务，日志中心服务公共定义库。 |
| 2026-10-02 10:00:27 | [BaoXia.Service.ServiceProvider.Client](https://www.nuget.org/packages/BaoXia.Service.ServiceProvider.Client) | 10.0.0 | 石家庄宝匣软件科技有限公司 | 宝匣软件，服务提供商服务客户端程序。 |
| 2026-10-02 10:03:54 | [com.EBS.Common.EntityFrameworkCore](https://www.nuget.org/packages/com.EBS.Common.EntityFrameworkCore) | 1.6.8.2 | EBS.Common.EntityFrameworkCore | Encrypted connect string |
| 2026-10-02 10:04:14 | [Zapqio.Runner.Module.Core](https://www.nuget.org/packages/Zapqio.Runner.Module.Core) | 1.2.0 | Zapqio | Core interfaces for creating Zapqio Runner modules. Implement IRunnerMethod to… |
| 2026-10-02 10:07:50 | [Nethereum.AccountAbstraction.WebAuthn](https://www.nuget.org/packages/Nethereum.AccountAbstraction.WebAuthn) | 7.0.0 | Juan Blanco,Nethereum contrib… | Nethereum AccountAbstraction WebAuthn - ERC-7579 WebAuthn (passkey / P-256) val… |
| 2026-10-02 10:08:50 | [Nethereum.CoreChain.Freezer](https://www.nuget.org/packages/Nethereum.CoreChain.Freezer) | 7.0.0 | Juan Blanco,Nethereum contrib… | Nethereum.CoreChain.Freezer - CoreChain adapter for Nethereum.Freezer: typed pe… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
