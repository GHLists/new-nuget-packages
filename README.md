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

## Latest list — 2026-11-12 03:20 UTC

New packages created between 2026-11-12 02:21 UTC and 2026-11-12 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T03-20-48-983737Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 02:29:44 | [TL.LiteCore.Template](https://www.nuget.org/packages/TL.LiteCore.Template) | 1.0.0 | Thaylon Lopes | Template corporativo .NET 9 para APIs RESTful síncronas, CRUDs transacionais di… |
| 2026-11-12 02:37:57 | [DTZero](https://www.nuget.org/packages/DTZero) | 2.0.0 | Keith Voels | Zero DTOs. A 3-tier client/server data mapper for .NET domain models, powered b… |
| 2026-11-12 02:37:58 | [DTZero.AspNetCore](https://www.nuget.org/packages/DTZero.AspNetCore) | 2.0.0 | Keith Voels | Zero DTOs. ASP.NET Core server library for DTZero. |
| 2026-11-12 03:00:43 | [KinTN.ASRS.SMD.Business.Head.Interfaces](https://www.nuget.org/packages/KinTN.ASRS.SMD.Business.Head.Interfaces) | 1.0.0 | KinTN | 料仓仓头程序（SiloHead）业务扩展接口：入库扫码校验（IVerifyCanStockIn）、第三方完成反馈（IFeedbackNotifier）、条码解… |
| 2026-11-12 03:01:43 | [KinTN.ASRS.SMD.UI.Head.Interfaces](https://www.nuget.org/packages/KinTN.ASRS.SMD.UI.Head.Interfaces) | 1.0.0 | KinTN | 料仓仓头程序（SiloHead）UI 扩展接口（Avalonia）：主界面入库/出库按钮自定义动作（IInboundAction/IOutboundActio… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
