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

## Latest list — 2026-10-30 02:20 UTC

New packages created between 2026-10-30 01:21 UTC and 2026-10-30 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T02-20-47-649042Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 01:24:08 | [BrunoCPF.Modifiable.Core](https://www.nuget.org/packages/BrunoCPF.Modifiable.Core) | 0.5.0 | Bruno Fernandes | Engine-free modifier math for RPG-style stat systems: modifier stacks, delta pi… |
| 2026-10-30 01:24:58 | [TKWF.Ext.AuthCenter.Abstractions](https://www.nuget.org/packages/TKWF.Ext.AuthCenter.Abstractions) | 0.2.0 | LoongBa.cn 龙爸出品 | TKWF 认证中心契约抽象（SSO 消费面：ISsoAccountQueryService / ISsoChannelMapService + DTO）——依… |
| 2026-10-30 01:30:01 | [Superroute.SLocker](https://www.nuget.org/packages/Superroute.SLocker) | 0.1.0 | Superroute | sLocker: deliver to Superroute smart lockers. The partner locker delivery API a… |
| 2026-10-30 01:41:23 | [Okisioli.Teacups.Store](https://www.nuget.org/packages/Okisioli.Teacups.Store) | 0.10.0 | Okisioli.Teacups.Store | Provider-neutral contracts for securely storing sensitive application values. |
| 2026-10-30 01:41:24 | [Okisioli.Teacups.Store.Maui](https://www.nuget.org/packages/Okisioli.Teacups.Store.Maui) | 0.10.0 | Okisioli.Teacups.Store.Maui | .NET MAUI Essentials-backed secure key/value storage for Okisioli.Teacups.Store. |
| 2026-10-30 01:55:15 | [X-Ray.3D](https://www.nuget.org/packages/X-Ray.3D) | 26.10.7520 | Curiosity GmbH | Dependency-free .NET library for 3D and CAD files: identifies the format, extra… |
| 2026-10-30 01:56:27 | [victor-wiki.EdgeTtsSharp](https://www.nuget.org/packages/victor-wiki.EdgeTtsSharp) | 1.0.0 | victor-wiki | Text to voice using Microsoft's Edge voices. |
| 2026-10-30 01:59:59 | [Raims](https://www.nuget.org/packages/Raims) | 0.1.4 | Raims | Official .NET SDK for the Raims public API. |
| 2026-10-30 02:00:08 | [Extension.BaGet.Api.Base](https://www.nuget.org/packages/Extension.BaGet.Api.Base) | 1.0.0.26303 | Piero Viano | BaGet Extension's shared base of the web APIs: the /api/ui twin controllers' ba… |
| 2026-10-30 02:00:28 | [Extension.BaGet.Frontend.Base](https://www.nuget.org/packages/Extension.BaGet.Frontend.Base) | 1.0.0.26303 | Piero Viano | BaGet Extension's shared MVC infrastructure for the screens: view controller ba… |
| 2026-10-30 02:00:33 | [Extension.BaGet.Identity.Api](https://www.nuget.org/packages/Extension.BaGet.Identity.Api) | 1.0.0.26303 | Piero Viano | BaGet Extension's user accounts, package owners and per-user API keys. |
| 2026-10-30 02:00:37 | [Extension.BaGet.Identity.Application](https://www.nuget.org/packages/Extension.BaGet.Identity.Application) | 1.0.0.26303 | Piero Viano | BaGet Extension's account and administration use cases: business services, the… |
| 2026-10-30 02:00:40 | [Extension.BaGet.Identity.FrontEnd](https://www.nuget.org/packages/Extension.BaGet.Identity.FrontEnd) | 1.0.0.26303 | Piero Viano | BaGet Extension's account and administration screens: the view controllers and… |
| 2026-10-30 02:00:50 | [Extension.BaGet.Web.Application](https://www.nuget.org/packages/Extension.BaGet.Web.Application) | 1.0.0.26303 | Piero Viano | BaGet Extension's web use cases: the data of the browse, upload and legal scree… |
| 2026-10-30 02:00:52 | [Extension.BaGet.Web.FrontEnd](https://www.nuget.org/packages/Extension.BaGet.Web.FrontEnd) | 1.0.0.26303 | Piero Viano | BaGet Extension's package browsing screens: the view controllers and views of t… |
| 2026-10-30 02:00:58 | [Extension.BaGet.Web.V3](https://www.nuget.org/packages/Extension.BaGet.Web.V3) | 1.0.0.26303 | Piero Viano | BaGet Extension's NuGet server implementation |
| 2026-10-30 02:13:29 | [UniversalOffice.Xlsx](https://www.nuget.org/packages/UniversalOffice.Xlsx) | 0.9.1 | Eric Kono | Excel workbooks in pure .NET: lossless .xlsx reading (cells, shared strings, st… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
