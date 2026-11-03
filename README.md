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

## Latest list — 2026-11-03 11:21 UTC

New packages created between 2026-11-03 10:21 UTC and 2026-11-03 11:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T11-21-21-648787Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 10:22:33 | [UaeGoldPrices.GoldCalculator](https://www.nuget.org/packages/UaeGoldPrices.GoldCalculator) | 1.0.0 | UAE Gold Prices | Gold value calculator for the UAE: 24/22/21/18/14K prices per gram, tola and tr… |
| 2026-11-03 10:24:22 | [Sandboa](https://www.nuget.org/packages/Sandboa) | 0.9.1 | Sandboa | Sandboxed CPython and NumPy with managed VFS, generated .NET bindings, and agen… |
| 2026-11-03 10:31:09 | [NeoAstra.Location](https://www.nuget.org/packages/NeoAstra.Location) | 1.11.0 | NeoAstra.Location | Location plugin for NeoAstra: the position of the device and the permission to… |
| 2026-11-03 10:31:12 | [NeoAstra.Passkeys](https://www.nuget.org/packages/NeoAstra.Passkeys) | 1.11.0 | NeoAstra.Passkeys | Passkeys plugin for NeoAstra: WebAuthn passkeys of the platform for a relying p… |
| 2026-11-03 10:31:14 | [NeoAstra.Purchases](https://www.nuget.org/packages/NeoAstra.Purchases) | 1.11.0 | NeoAstra.Purchases | In-app purchases plugin for NeoAstra: the products, purchases, and subscription… |
| 2026-11-03 10:31:16 | [NeoAstra.Push](https://www.nuget.org/packages/NeoAstra.Push) | 1.11.0 | NeoAstra.Push | Push plugin for NeoAstra: remote notifications through the Apple Push Notificat… |
| 2026-11-03 10:34:32 | [SibraSoft.Shared](https://www.nuget.org/packages/SibraSoft.Shared) | 1.0.0 | Sibra-Soft | Shared Windows Forms utilities for Sibra-Soft projects. |
| 2026-11-03 10:36:44 | [MakeenPay.SharedKernel.Domain](https://www.nuget.org/packages/MakeenPay.SharedKernel.Domain) | 1.0.0 | AmirAliKhoshroei | MakeenPay Shared Dependencies |
| 2026-11-03 10:39:11 | [MakeenPay.SharedKernel.App](https://www.nuget.org/packages/MakeenPay.SharedKernel.App) | 1.0.0 | AmirAliKhoshroei | MakeenPay Shared Dependencies |
| 2026-11-03 10:43:44 | [Scarlet.DirectN.Threading](https://www.nuget.org/packages/Scarlet.DirectN.Threading) | 1.0.0 | ScarletKuro | UI-thread message queue and SynchronizationContext for DirectN (Win32) apps, Na… |
| 2026-11-03 10:43:45 | [Scarlet.Extensions.Hosting.DirectN](https://www.nuget.org/packages/Scarlet.Extensions.Hosting.DirectN) | 1.0.0 | ScarletKuro | Microsoft.Extensions.Hosting (Generic Host) integration for DirectN (Win32/Dire… |
| 2026-11-03 10:43:46 | [Scarlet.Extensions.Hosting.DirectN.Threading](https://www.nuget.org/packages/Scarlet.Extensions.Hosting.DirectN.Threading) | 1.0.0 | ScarletKuro | Thread switching for Scarlet.Extensions.Hosting.DirectN: JoinableTaskFactory an… |
| 2026-11-03 10:43:47 | [Scarlet.Extensions.Hosting.DirectN.TrayIcon](https://www.nuget.org/packages/Scarlet.Extensions.Hosting.DirectN.TrayIcon) | 1.0.0 | ScarletKuro | Notification area (tray) icon for Scarlet.Extensions.Hosting.DirectN: a Native… |
| 2026-11-03 10:45:12 | [Dloizides.Registration](https://www.nuget.org/packages/Dloizides.Registration) | 0.1.0 | DLoizides | One registration and account-erase flow for any host: request screen, idempoten… |
| 2026-11-03 10:48:21 | [TradingMonitor.Domain](https://www.nuget.org/packages/TradingMonitor.Domain) | 1.0.0 | Sahib | Shared models and interfaces for TradingMonitor plugins. |
| 2026-11-03 10:51:12 | [Dloizides.Registration.Keycloak](https://www.nuget.org/packages/Dloizides.Registration.Keycloak) | 0.1.0 | DLoizides | Realm-aware Keycloak adapter for Dloizides.Registration: every call acts in the… |
| 2026-11-03 10:51:58 | [Webority.Ads.Insights](https://www.nuget.org/packages/Webority.Ads.Insights) | 0.12.0 | Webority Technologies | Webority.Ads campaign statistics in Webority.Insights: runs each registered ad… |
| 2026-11-03 10:54:21 | [ISCG.ExtensionMethods.SPSE](https://www.nuget.org/packages/ISCG.ExtensionMethods.SPSE) | 2026.11.3.6 | ISCG | ISCG.ExtensionMethods.SPSE signed |
| 2026-11-03 11:02:41 | [Lait.Umbraco.LLMS.Generator](https://www.nuget.org/packages/Lait.Umbraco.LLMS.Generator) | 1.0.0 | LAIT, Anders Bootsmann Overvad | Build your /llms.txt from the Umbraco 17 backoffice. Editors compose it from bl… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
