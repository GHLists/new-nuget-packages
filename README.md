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

## Latest list — 2026-11-18 07:19 UTC

New packages created between 2026-11-18 06:20 UTC and 2026-11-18 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T07-19-40-012029Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 06:31:33 | [Irihi.Iconica.Semi](https://www.nuget.org/packages/Irihi.Iconica.Semi) | 1.0.0 | IRIHI Technology Co., Ltd. 上海… | Package Description |
| 2026-11-18 06:31:33 | [Irihi.Iconica.Semi.Lab](https://www.nuget.org/packages/Irihi.Iconica.Semi.Lab) | 1.0.0 | IRIHI Technology Co., Ltd. 上海… | Package Description |
| 2026-11-18 06:32:30 | [Syncfusion.AspNetMvc.PptxEditor](https://www.nuget.org/packages/Syncfusion.AspNetMvc.PptxEditor) | 35.2.12 | Syncfusion Inc. | Syncfusion® ASP.NET MVC PPTX Editor is a feature-rich UI component for viewing,… |
| 2026-11-18 06:34:53 | [Syncfusion.Maui.BottomSheet](https://www.nuget.org/packages/Syncfusion.Maui.BottomSheet) | 35.2.12 | Syncfusion Inc | This package provides the functionality to utilize the features of Syncfusion®… |
| 2026-11-18 06:40:24 | [Octopus.Testing.TeamCityReporter](https://www.nuget.org/packages/Octopus.Testing.TeamCityReporter) | 0.0.4 | Octopus Deploy | A Microsoft Testing Platform extension that reports test results to TeamCity wi… |
| 2026-11-18 06:47:10 | [HXAuth.Client](https://www.nuget.org/packages/HXAuth.Client) | 1.0.0 | HXAuth | 海新统一身份认证（HXAuth）对接客户端。ASP.NET Core 与 .NET Framework(OWIN) 均可用一行代码接入 OIDC 单点登录：内… |
| 2026-11-18 06:48:08 | [Froststrap.LucideAvalonia](https://www.nuget.org/packages/Froststrap.LucideAvalonia) | 2.0.1 | Froststrap,Invra | A fork of library https://github.com/MarwanFr/LucideAvaloniaUI for better inter… |
| 2026-11-18 06:55:35 | [CaptchaN.Drawing.LibVips](https://www.nuget.org/packages/CaptchaN.Drawing.LibVips) | 4.0.0 | LeaFrock | Draw Captcha based on libvips. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
