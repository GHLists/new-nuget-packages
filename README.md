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

## Latest list — 2026-10-02 09:19 UTC

New packages created between 2026-10-02 08:22 UTC and 2026-10-02 09:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T09-19-44-152459Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 08:22:21 | [SapPostLog.Core](https://www.nuget.org/packages/SapPostLog.Core) | 1.0.0 | SapPostLog.Core | Idempotent SAP posting guard with PostgreSQL-backed request/response log. Works… |
| 2026-10-02 08:49:01 | [BarisCemant.Verimor](https://www.nuget.org/packages/BarisCemant.Verimor) | 0.1.0 | Baris Cem Ant | Unofficial community .NET SDK for the Verimor SMS, Switch and WhatsApp APIs. No… |
| 2026-10-02 08:51:00 | [VigorGlow.Dapper](https://www.nuget.org/packages/VigorGlow.Dapper) | 1.0.0 | VigorGlow.Orm | 基于 Dapper 的轻量级 ORM 仓储，内置 SQL Server / MySQL / Oracle / PostgreSQL / SQLite 五种数据… |
| 2026-10-02 09:01:07 | [lintent.osx-arm64](https://www.nuget.org/packages/lintent.osx-arm64) | 0.1.1 | pietervp | Plain-language lint rules judged by a model (Jev, by TypeSafe), scoped with tre… |
| 2026-10-02 09:01:08 | [lintent.osx-x64](https://www.nuget.org/packages/lintent.osx-x64) | 0.1.1 | pietervp | Plain-language lint rules judged by a model (Jev, by TypeSafe), scoped with tre… |
| 2026-10-02 09:01:10 | [lintent.linux-arm64](https://www.nuget.org/packages/lintent.linux-arm64) | 0.1.1 | pietervp | Plain-language lint rules judged by a model (Jev, by TypeSafe), scoped with tre… |
| 2026-10-02 09:01:12 | [lintent.linux-x64](https://www.nuget.org/packages/lintent.linux-x64) | 0.1.1 | pietervp | Plain-language lint rules judged by a model (Jev, by TypeSafe), scoped with tre… |
| 2026-10-02 09:01:14 | [lintent.win-x64](https://www.nuget.org/packages/lintent.win-x64) | 0.1.1 | pietervp | Plain-language lint rules judged by a model (Jev, by TypeSafe), scoped with tre… |
| 2026-10-02 09:06:18 | [lintent](https://www.nuget.org/packages/lintent) | 0.1.1 | pietervp | Plain-language lint rules judged by a model (Jev, by TypeSafe), scoped with tre… |
| 2026-10-02 09:06:34 | [BaoXia.Service.ServiceProvider.Defines](https://www.nuget.org/packages/BaoXia.Service.ServiceProvider.Defines) | 10.0.0 | 石家庄宝匣软件科技有限公司 | 宝匣软件，服务提供商服务公共定义库。 |
| 2026-10-02 09:08:18 | [Zolotov.Samotpravil](https://www.nuget.org/packages/Zolotov.Samotpravil) | 1.0.0 | samotpravil | Async .NET client for the Samotpravil email API. |
| 2026-10-02 09:10:20 | [VirtoCommerce.Otp.Core](https://www.nuget.org/packages/VirtoCommerce.Otp.Core) | 3.1000.0 | VirtoCommerce.Otp.Core | Package Description |
| 2026-10-02 09:10:26 | [VirtoCommerce.Otp.Data](https://www.nuget.org/packages/VirtoCommerce.Otp.Data) | 3.1000.0 | VirtoCommerce.Otp.Data | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
