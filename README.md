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

## Latest list — 2026-10-07 23:20 UTC

New packages created between 2026-10-07 22:20 UTC and 2026-10-07 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T23-20-33-88202Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 22:27:01 | [TKWF.Federation.DingTalk](https://www.nuget.org/packages/TKWF.Federation.DingTalk) | 0.2.0 | LoongBa.cn 龙爸出品 | TKWF 平台网关库（纯库——无 Initializer 无 [TKWFExtension] 无持久化）：钉钉开放平台双向网关（新 OAuth2 身份获取 +… |
| 2026-10-07 22:27:01 | [TKWF.Federation.Google](https://www.nuget.org/packages/TKWF.Federation.Google) | 0.2.0 | LoongBa.cn 龙爸出品 | TKWF 平台网关库（纯库——无 Initializer 无 [TKWFExtension] 无持久化）：Google 平台网关——基于通用 OIDC 基座（… |
| 2026-10-07 22:27:01 | [TKWF.Federation.Microsoft](https://www.nuget.org/packages/TKWF.Federation.Microsoft) | 0.2.0 | LoongBa.cn 龙爸出品 | TKWF 平台网关库（纯库——无 Initializer 无 [TKWFExtension] 无持久化）：Microsoft Entra ID 平台网关——基… |
| 2026-10-07 22:27:02 | [TKWF.Federation.Oidc](https://www.nuget.org/packages/TKWF.Federation.Oidc) | 0.2.0 | LoongBa.cn 龙爸出品 | TKWF 平台网关基座库（纯库——无 Initializer 无 [TKWFExtension] 无持久化）：通用 OIDC 通道基座（Discovery 配… |
| 2026-10-07 22:27:02 | [TKWF.Federation.QQ](https://www.nuget.org/packages/TKWF.Federation.QQ) | 0.2.0 | LoongBa.cn 龙爸出品 | TKWF 平台网关库（纯库——无 Initializer 无 [TKWFExtension] 无持久化）：QQ 互联身份获取网关（出站-only——OAuth… |
| 2026-10-07 22:27:02 | [TKWF.Federation.WeChat](https://www.nuget.org/packages/TKWF.Federation.WeChat) | 0.2.0 | LoongBa.cn 龙爸出品 | TKWF 平台网关库（纯库——无 Initializer 无 [TKWFExtension] 无持久化）：微信公众平台双向网关（OAuth 身份获取 + 事件… |
| 2026-10-07 22:27:03 | [TKWF.Federation.WeCom](https://www.nuget.org/packages/TKWF.Federation.WeCom) | 0.2.0 | LoongBa.cn 龙爸出品 | TKWF 平台网关库（纯库——无 Initializer 无 [TKWFExtension] 无持久化）：企业微信（WeCom）双向网关（双授权流 Webvi… |
| 2026-10-07 22:39:44 | [FSharp.Astro.Fits](https://www.nuget.org/packages/FSharp.Astro.Fits) | 0.1.0 | Leo Conforti | A FITS (Flexible Image Transport System) library for F#. Strict by default, laz… |
| 2026-10-07 22:39:44 | [FSharp.Astro.Units](https://www.nuget.org/packages/FSharp.Astro.Units) | 0.1.0 | Leo Conforti | Units of measure for astronomy in F#: parsecs, arcseconds, janskys, solar masse… |
| 2026-10-07 22:41:31 | [Komento.OpenFeature.AspNetCore](https://www.nuget.org/packages/Komento.OpenFeature.AspNetCore) | 0.3.0-alpha | yanpitangui | Per-request OpenFeature transaction context built from Komento's ASP.NET Core e… |
| 2026-10-07 22:41:33 | [Komento.Sinks](https://www.nuget.org/packages/Komento.Sinks) | 0.3.0-alpha | yanpitangui | Batched, isolated sinks for Komento exposures and conversions. |
| 2026-10-07 22:47:45 | [Fable.Giraffe.Beam](https://www.nuget.org/packages/Fable.Giraffe.Beam) | 5.5.1 | Fable.Giraffe.Beam | Giraffe for Fable BEAM (Cowboy) |
| 2026-10-07 22:56:33 | [Snail.Toolkit.SignalR.Reactive.Client](https://www.nuget.org/packages/Snail.Toolkit.SignalR.Reactive.Client) | 2.0.0 | Toolkit | The client side of reactive SignalR transfers: a sender and a receiver over a H… |
| 2026-10-07 22:56:33 | [Snail.Toolkit.SignalR.Reactive.Server](https://www.nuget.org/packages/Snail.Toolkit.SignalR.Reactive.Server) | 2.0.0 | Toolkit | The hub side of reactive SignalR transfers: the routing hub, the transfers it h… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
