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

## Latest list — 2026-11-20 14:21 UTC

New packages created between 2026-11-20 13:20 UTC and 2026-11-20 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T14-21-28-525867Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 13:22:35 | [Keycloak.Net.Sdk.AspNetCore](https://www.nuget.org/packages/Keycloak.Net.Sdk.AspNetCore) | 1.0.0 | Milad.Rv | ASP.NET Core integration for Keycloak: JWT bearer validation, Keycloak realm an… |
| 2026-11-20 13:24:28 | [BIMPlugins.MaterialDesign](https://www.nuget.org/packages/BIMPlugins.MaterialDesign) | 5.3.2.1 | Samir Shibliev, MaterialDesig… | Material Design in XAML Toolkit for Revit add-ins, under assembly names of its… |
| 2026-11-20 13:42:58 | [DotNetRewrite.Engine](https://www.nuget.org/packages/DotNetRewrite.Engine) | 0.1.1 | DotNetRewrite contributors | Host-independent .NET 10 URL rewrite rule parsing and evaluation engine. |
| 2026-11-20 13:42:59 | [DotNetRewrite](https://www.nuget.org/packages/DotNetRewrite) | 0.1.1 | DotNetRewrite contributors | ASP.NET Core middleware for .NET 10 URL rewriting, redirects, and explicitly au… |
| 2026-11-20 13:58:36 | [STI.IT2025.G5.H4T6MQXS](https://www.nuget.org/packages/STI.IT2025.G5.H4T6MQXS) | 1.0.0 | STI.IT2025.G5.H4T6MQXS | Package Description |
| 2026-11-20 14:11:20 | [Anan.Controls.MarkdownTextBlock](https://www.nuget.org/packages/Anan.Controls.MarkdownTextBlock) | 1.0.0 | Ansherly | WinUI 3 的 Markdown 渲染控件，提供Markdig 解析和策略化渲染,支持标题 / 段落 / 引用 / 列表 / 任务列表 / 表格 / 代码… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
