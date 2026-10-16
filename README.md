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

## Latest list — 2026-10-16 08:23 UTC

New packages created between 2026-10-16 07:22 UTC and 2026-10-16 08:23 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T08-23-09-797421Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 07:44:33 | [Plugboard.Endpoints](https://www.nuget.org/packages/Plugboard.Endpoints) | 0.1.0 | Nouwan | Source-generated endpoint registration for ASP.NET Core minimal APIs |
| 2026-10-16 07:57:36 | [Tessio.Verifier.Core.Mdoc.Zk](https://www.nuget.org/packages/Tessio.Verifier.Core.Mdoc.Zk) | 0.21.0 | Triple Down AB | Zero knowledge age proof verification for Tessio.Verifier.Core.Mdoc: checks Lon… |
| 2026-10-16 08:16:24 | [YtSoft.Gmc.Core.Config](https://www.nuget.org/packages/YtSoft.Gmc.Core.Config) | 1.0.0 | YtSoft | 统一 Nacos 配置中心 SDK。业务服务引用后，从 Nacos 拉取 Database / Gateway / Middleware 三份配置并绑定为强类… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
