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

## Latest list — 2026-10-10 06:18 UTC

New packages created between 2026-10-10 05:20 UTC and 2026-10-10 06:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T06-18-52-185731Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 05:33:20 | [TKWF.Ext.TrustCenter](https://www.nuget.org/packages/TKWF.Ext.TrustCenter) | 0.1.0 | LoongBa.cn 龙爸出品 | TKWF 扩展：信任中心（TrustCenter，纯信任内核——2026-10-09 自 Federation 剥离）——应用注册（SsoClientEnti… |
| 2026-10-10 05:33:21 | [TKWF.Ext.TrustCenter.Abstractions](https://www.nuget.org/packages/TKWF.Ext.TrustCenter.Abstractions) | 0.1.0 | LoongBa.cn 龙爸出品 | TKWF 信任中心契约抽象（TrustCenter——ISsoChannel / IToken2Service / IAccessCodeService +… |
| 2026-10-10 05:40:54 | [ProfitDLL4Dotnet](https://www.nuget.org/packages/ProfitDLL4Dotnet) | 1.0.0 | Willisnou | Wrapper .NET não oficial para a ProfitDLL da Nelogica (versão suportada da DLL:… |
| 2026-10-10 05:47:12 | [TKWF.Federation.Alipay](https://www.nuget.org/packages/TKWF.Federation.Alipay) | 0.1.1 | LoongBa.cn 龙爸出品 | TKWF 平台网关库（纯库——无 Initializer 无 [TKWFExtension] 无持久化）：支付宝开放平台身份获取网关（出站-only——OAu… |
| 2026-10-10 05:51:25 | [HHO.LV.NetClaw.Web](https://www.nuget.org/packages/HHO.LV.NetClaw.Web) | 1.0.0 | HuyHo | Package Description |
| 2026-10-10 06:02:30 | [HHO.LV.NetClaw.Testing](https://www.nuget.org/packages/HHO.LV.NetClaw.Testing) | 1.0.0 | HuyHo | Package Description |
| 2026-10-10 06:11:13 | [DotnetBaseKit.Cli](https://www.nuget.org/packages/DotnetBaseKit.Cli) | 1.0.0 | Rafael Fraga | Interactive CLI to initialize and manage projects with the DotnetBaseKit framew… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
