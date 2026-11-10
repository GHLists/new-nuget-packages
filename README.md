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

## Latest list — 2026-11-10 06:19 UTC

New packages created between 2026-11-10 05:21 UTC and 2026-11-10 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T06-19-10-371818Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 05:42:55 | [RuneForBlazor.Desktop.Maui](https://www.nuget.org/packages/RuneForBlazor.Desktop.Maui) | 0.15.0 | kenconnet666 | Rune 的 .NET MAUI 桌面适配（Windows）：AppShell 的顶栏就是窗口的标题栏（拖动、双击最大化、窗口按钮），WebView2 按桌面… |
| 2026-11-10 05:43:40 | [Navs.Goo](https://www.nuget.org/packages/Navs.Goo) | 2.1.0 | Angel Munoz and contributors | Package Description |
| 2026-11-10 05:49:46 | [Zumen](https://www.nuget.org/packages/Zumen) | 0.2.0 | Zumen | 日本の建設の図面（DXF・DWG・SXF・JWW）を読み書きする zumen の、.NET のラッパー |
| 2026-11-10 05:51:12 | [Google.Cloud.SaasPlatform.SaasServiceMgmt.V1](https://www.nuget.org/packages/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1) | 1.0.0-beta01 | Google LLC | Model, deploy, and operate your SaaS at scale. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
