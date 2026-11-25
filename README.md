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

## Latest list — 2026-11-25 07:19 UTC

New packages created between 2026-11-25 06:19 UTC and 2026-11-25 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T07-19-19-481665Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 06:23:27 | [nuel_CaptchaSqlite](https://www.nuget.org/packages/nuel_CaptchaSqlite) | 1.0.0 | Ako Mahmoodi | A .NET captcha library with file-backed SQLite storage and SixLabors ImageSharp… |
| 2026-11-25 06:36:32 | [LogerReplica.EFCore.Interceptors](https://www.nuget.org/packages/LogerReplica.EFCore.Interceptors) | 1.0.0 | loger | EF Core interceptors for read/write routing and connection failover. |
| 2026-11-25 06:51:39 | [Euonia.Hosting.Azfunc](https://www.nuget.org/packages/Euonia.Hosting.Azfunc) | 2026.5.1 | damon | Euonia Azure Functions 隔离工作进程宿主包：函数基类、统一异常响应、请求追踪、请求上下文中转、Security 与双窗口流控。 / Az… |
| 2026-11-25 06:51:40 | [Euonia.Hosting.Webapi](https://www.nuget.org/packages/Euonia.Hosting.Webapi) | 2026.5.1 | damon | Euonia ASP.NET Core Web API 宿主组合包：控制器、统一异常响应、OpenAPI、健康检查、CORS、权限授权与双窗口流控。 / AS… |
| 2026-11-25 06:55:17 | [AyuUI.Controll](https://www.nuget.org/packages/AyuUI.Controll) | 1.0.0 | yiyangyu | 一套高颜值、零依赖、支持注解IoC、消息总线与丰富UI控件的现代WPF自研框架。 |
| 2026-11-25 07:05:23 | [WEBCON.SDK](https://www.nuget.org/packages/WEBCON.SDK) | 2027.1.1.21 | WEBCON | This package includes the WEBCON assemblies required to develop SDK plugins. Th… |
| 2026-11-25 07:06:41 | [Motion.Avalonia](https://www.nuget.org/packages/Motion.Avalonia) | 1.0.0 | Sylinko | A declarative motion and interaction framework for Avalonia. |
| 2026-11-25 07:10:00 | [PdfFormFiller.Widgets](https://www.nuget.org/packages/PdfFormFiller.Widgets) | 0.7.1 | Haansen | Widget-style form API (PdfDocument, PdfFormWidget, PdfTextBoxFieldWidget ...) o… |
| 2026-11-25 07:10:01 | [PdfFormFiller](https://www.nuget.org/packages/PdfFormFiller) | 0.7.1 | Haansen | Fill, flatten, merge and trim AcroForm PDFs. Self-contained, no third-party dep… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
