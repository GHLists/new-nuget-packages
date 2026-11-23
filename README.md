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

## Latest list — 2026-11-23 15:22 UTC

New packages created between 2026-11-23 14:19 UTC and 2026-11-23 15:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T15-22-29-401433Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 14:39:20 | [OpenCAD2D.Core](https://www.nuget.org/packages/OpenCAD2D.Core) | 1.0.0 | Nguyen Thang | The engine of OpenCAD2D, a 2D CAD app that works like AutoCAD 2021, with no UI:… |
| 2026-11-23 14:39:21 | [OpenCAD2D.Remote](https://www.nuget.org/packages/OpenCAD2D.Remote) | 1.0.0 | Nguyen Thang | Drives a running OpenCAD2D from another program: finds the app, lists its drawi… |
| 2026-11-23 14:46:13 | [ANcpLua.Fprog.Analyzers](https://www.nuget.org/packages/ANcpLua.Fprog.Analyzers) | 0.1.0 | Alexander Nachtmann | Roslyn analyzers that hold C# 15 code to functional-programming rules: purity,… |
| 2026-11-23 14:46:53 | [RefTrace](https://www.nuget.org/packages/RefTrace) | 0.11.0 | Alexander Nachtmann | Trace resolved .NET dependencies and inspect assembly metadata without loading… |
| 2026-11-23 14:50:11 | [Plugin.Maui.Spine.Purchases](https://www.nuget.org/packages/Plugin.Maui.Spine.Purchases) | 0.261123.1608 | Jonatan Söderberg | Subscriptions and one-time purchases for a Spine app: IAppPurchases with typed… |
| 2026-11-23 14:50:12 | [Plugin.Maui.Spine.Purchases.RevenueCat](https://www.nuget.org/packages/Plugin.Maui.Spine.Purchases.RevenueCat) | 0.261123.1608 | Jonatan Söderberg | The RevenueCat store for Plugin.Maui.Spine.Purchases on iOS, Mac Catalyst and A… |
| 2026-11-23 14:51:18 | [Gurux.Compression.Net](https://www.nuget.org/packages/Gurux.Compression.Net) | 1.0.2611.2301 | Gurux Ltd | V.44 compression and decompression for binary data, including stream support. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
