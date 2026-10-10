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

## Latest list — 2026-10-10 16:20 UTC

New packages created between 2026-10-10 15:20 UTC and 2026-10-10 16:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T16-20-11-101764Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 15:21:32 | [StanzaSharp.Cuda](https://www.nuget.org/packages/StanzaSharp.Cuda) | 1.0.0 | Jakob Boman | The TorchSharp (libtorch) backend for StanzaSharp: runs Stanza's English pipeli… |
| 2026-10-10 15:29:59 | [MarkdownRenderX.Avalonia](https://www.nuget.org/packages/MarkdownRenderX.Avalonia) | 12.1.3.2 | RYCBStudio | 面向 Avalonia 的 Markdown 渲染组件，不依赖 FluentAvalonia。支持标题、列表、引用、代码高亮、图片、内联 HTML、GitHu… |
| 2026-10-10 15:39:23 | [Kun.Authorization](https://www.nuget.org/packages/Kun.Authorization) | 2026.10.9 | Kun Framework Contributors | 权限判定、数据与字段策略端口；权限引擎由宿主提供。 |
| 2026-10-10 15:39:26 | [Kun.Configuration.Apollo](https://www.nuget.org/packages/Kun.Configuration.Apollo) | 2026.10.9 | Kun Framework Contributors | Apollo HTTP 配置源：长轮询、AccessKey 签名、多 namespace 合并与本地缓存。 |
| 2026-10-10 15:54:07 | [DiScope](https://www.nuget.org/packages/DiScope) | 0.1.1 | DiScope contributors | See your .NET dependency injection graph. Finds captive dependencies, missing r… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
