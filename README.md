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

## Latest list — 2026-10-21 18:22 UTC

New packages created between 2026-10-21 17:21 UTC and 2026-10-21 18:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T18-22-25-370498Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 17:21:29 | [CanFxGen](https://www.nuget.org/packages/CanFxGen) | 0.2.0 | Oğuzhan Can | canfxgen: CanFx çözümlerinde entity'den CRUD (CQRS) kodu üreten komut satırı ar… |
| 2026-10-21 17:30:02 | [JagPav.Pipeline](https://www.nuget.org/packages/JagPav.Pipeline) | 1.0.0 | Mario Pavlović | A compensable pipeline for .NET, built on TPL Dataflow: thread a model through… |
| 2026-10-21 17:30:39 | [WarpClient.DependencyInjection](https://www.nuget.org/packages/WarpClient.DependencyInjection) | 26.10.21.7751 | Vitalii Kotenko | Dependency injection and IHttpClientFactory integration for WarpClient. |
| 2026-10-21 17:30:40 | [WarpClient](https://www.nuget.org/packages/WarpClient) | 26.10.21.7751 | Vitalii Kotenko | Cloudflare WARP for .NET: send TCP, UDP, and HTTP traffic through WARP over MAS… |
| 2026-10-21 17:35:12 | [Irihi.Branding](https://www.nuget.org/packages/Irihi.Branding) | 0.1.0 | IRIHI Technology Co., Ltd. | Irihi brand icon library: native Avalonia drawing with built-in light/dark pale… |
| 2026-10-21 17:39:52 | [NewLife.AI.Extensions](https://www.nuget.org/packages/NewLife.AI.Extensions) | 1.6.2026.1021-beta1… | 新生命开发团队 | 基于 NewLife.AI 基础库的扩展模块，提供中间件、依赖注入、缓存等企业级扩展能力 |
| 2026-10-21 18:02:27 | [Rayscale.Web.Styles](https://www.nuget.org/packages/Rayscale.Web.Styles) | 1.0.0 | Rayscale | Shared styles and design tokens implementing the Human Interface Guidelines. |
| 2026-10-21 18:11:56 | [MorseCode.Analyzers](https://www.nuget.org/packages/MorseCode.Analyzers) | 0.1.0 | MorseCode Software LLC | Roslyn analyzers for the conventions that MorseCode Software writes C# with, su… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
