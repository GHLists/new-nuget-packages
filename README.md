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

## Latest list — 2026-09-29 01:21 UTC

New packages created between 2026-09-29 00:20 UTC and 2026-09-29 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T01-21-04-702327Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 00:30:19 | [Aore.WinKit](https://www.nuget.org/packages/Aore.WinKit) | 1.0.0 | WEI.ZHOU (Willis) | Windows 快速开发工具箱：注册表、事件日志、Windows 用户与组、进程/cmd/bat/PowerShell 执行、环境变量、Windows 服务、… |
| 2026-09-29 00:31:45 | [SendDart](https://www.nuget.org/packages/SendDart) | 1.0.0 | SendDart | Official SendDart .NET SDK — send transactional and marketing email from your o… |
| 2026-09-29 00:38:33 | [Singulink.Globalization.Currency.DataProviders](https://www.nuget.org/packages/Singulink.Globalization.Currency.DataProviders) | 1.0.0 | Singulink | Data provider abstraction for Singulink.Globalization.Currency. Currency data p… |
| 2026-09-29 00:38:34 | [Singulink.Globalization.Currency](https://www.nuget.org/packages/Singulink.Globalization.Currency) | 1.0.0 | Singulink | High-performance and flexible currency support for .NET, done right 🎉 |
| 2026-09-29 00:38:35 | [Singulink.Globalization.Currency.Cldr](https://www.nuget.org/packages/Singulink.Globalization.Currency.Cldr) | 48.0.0 | Singulink | Unicode CLDR 48.0.0 currency data for Singulink.Globalization.Currency: every c… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
