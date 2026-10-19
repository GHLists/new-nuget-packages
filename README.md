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

## Latest list — 2026-10-19 18:22 UTC

New packages created between 2026-10-19 17:22 UTC and 2026-10-19 18:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T18-22-49-526846Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 17:29:41 | [Stormancer.Server.Plugins.Voice](https://www.nuget.org/packages/Stormancer.Server.Plugins.Voice) | 0.1.0-pre | Stormancer | Voice plugin for Stormancer server applications. |
| 2026-10-19 17:43:11 | [AxiosNet](https://www.nuget.org/packages/AxiosNet) | 1.0.0 | sunyuliang | 用 .NET 实现的 axios 风格 HTTP 客户端：API 与 JS axios 一一对应，内置按 origin 隔离的连接池（连接复用、并发上限、空闲… |
| 2026-10-19 17:49:01 | [E2E.Mobile.NUnit](https://www.nuget.org/packages/E2E.Mobile.NUnit) | 0.6.0 | hardkoded | MobileAppTest for the E2E .NET port: a ready base class that installs the app,… |
| 2026-10-19 17:49:04 | [E2E.Mobile.XUnit.V3](https://www.nuget.org/packages/E2E.Mobile.XUnit.V3) | 0.6.0 | hardkoded | MobileAppTest for the E2E .NET port: a ready base class that installs the app,… |
| 2026-10-19 17:55:21 | [DaisyBlazor.Charts.Server](https://www.nuget.org/packages/DaisyBlazor.Charts.Server) | 0.7.0 | DaisyBlazor contributors | Server rendering for DaisyBlazor.Charts: runs the charts' bundled D3 layouts in… |
| 2026-10-19 18:13:46 | [AlphaQuantum.CipaWebFiltering](https://www.nuget.org/packages/AlphaQuantum.CipaWebFiltering) | 1.0.0 | Alpha Quantum | .NET client for the CIPA Web Filtering lookup API: web-filtering categories for… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
