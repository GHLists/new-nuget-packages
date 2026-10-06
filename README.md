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

## Latest list — 2026-10-06 18:20 UTC

New packages created between 2026-10-06 17:19 UTC and 2026-10-06 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T18-20-24-170545Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 17:34:04 | [Org.Cdk8s.Plus35](https://www.nuget.org/packages/Org.Cdk8s.Plus35) | 2.0.0 | Amazon Web Services | cdk8s+ is a software development framework that provides high level abstraction… |
| 2026-10-06 17:35:27 | [AXR.FidelityFX](https://www.nuget.org/packages/AXR.FidelityFX) | 3.1.2.1 | Advanced X-Ray contributors | OGSR FidelityFX SDK fork for Advanced X-Ray: DX11 backend, FSR 3 upscaler sourc… |
| 2026-10-06 17:45:41 | [Griffin.Caching](https://www.nuget.org/packages/Griffin.Caching) | 0.1.0 | Griffin.Caching | Package Description |
| 2026-10-06 17:45:42 | [Griffin.Core](https://www.nuget.org/packages/Griffin.Core) | 0.1.0 | Griffin.Core | Package Description |
| 2026-10-06 17:45:43 | [Griffin.EFCore](https://www.nuget.org/packages/Griffin.EFCore) | 0.1.0 | Griffin.EFCore | Package Description |
| 2026-10-06 17:45:44 | [Griffin.EventStoreDB](https://www.nuget.org/packages/Griffin.EventStoreDB) | 0.1.0 | Griffin.EventStoreDB | Package Description |
| 2026-10-06 17:45:45 | [Griffin.HealthCheck](https://www.nuget.org/packages/Griffin.HealthCheck) | 0.1.0 | Griffin.HealthCheck | Package Description |
| 2026-10-06 17:45:46 | [Griffin.Jwt](https://www.nuget.org/packages/Griffin.Jwt) | 0.1.0 | Griffin.Jwt | Package Description |
| 2026-10-06 17:47:08 | [Pixata.AspNetCore.Pdf.Telerik](https://www.nuget.org/packages/Pixata.AspNetCore.Pdf.Telerik) | 1.0.0 | Avrohom Yisroel Silver | Telerik Document Processing PDF converter for Pixata.AspNetCore's DocumentTempl… |
| 2026-10-06 17:48:34 | [Pixata.AspNetCore.Pdf.WkHtmlToPdf](https://www.nuget.org/packages/Pixata.AspNetCore.Pdf.WkHtmlToPdf) | 1.0.0 | Avrohom Yisroel Silver | Obsolete wkhtmltopdf PDF converter for Pixata.AspNetCore's DocumentTemplateHelp… |
| 2026-10-06 17:51:15 | [DesktopAccountingAPI.QuickBooksDesktop](https://www.nuget.org/packages/DesktopAccountingAPI.QuickBooksDesktop) | 0.1.0 | Desktop Accounting API | Official .NET SDK for Desktop Accounting API: a REST API for QuickBooks Desktop… |
| 2026-10-06 17:56:31 | [Marbots.Abstractions](https://www.nuget.org/packages/Marbots.Abstractions) | 0.1.0 | Gravicode Studios (led by Kan… | Core contracts, models and events for the Marbots multi-agent platform. |
| 2026-10-06 17:56:33 | [Marbots.Sdk](https://www.nuget.org/packages/Marbots.Sdk) | 0.1.0 | Gravicode Studios (led by Kan… | .NET SDK for the Marbots multi-agent collaboration platform REST API. |
| 2026-10-06 17:56:36 | [Marbots.Cli](https://www.nuget.org/packages/Marbots.Cli) | 0.1.0 | Gravicode Studios (led by Kan… | Command-line client for Marbots. |
| 2026-10-06 18:04:23 | [Griffin.Log](https://www.nuget.org/packages/Griffin.Log) | 0.1.0 | Griffin.Log | Package Description |
| 2026-10-06 18:04:24 | [Griffin.Mapster](https://www.nuget.org/packages/Griffin.Mapster) | 0.1.0 | Griffin.Mapster | Package Description |
| 2026-10-06 18:04:25 | [Griffin.Mongo](https://www.nuget.org/packages/Griffin.Mongo) | 0.1.0 | Griffin.Mongo | Package Description |
| 2026-10-06 18:04:26 | [Griffin.OpenApi](https://www.nuget.org/packages/Griffin.OpenApi) | 0.1.0 | Griffin.OpenApi | Package Description |
| 2026-10-06 18:04:28 | [Griffin.Polly](https://www.nuget.org/packages/Griffin.Polly) | 0.1.0 | Griffin.Polly | Package Description |
| 2026-10-06 18:04:29 | [Griffin.ProblemDetails](https://www.nuget.org/packages/Griffin.ProblemDetails) | 0.1.0 | Griffin.ProblemDetails | Package Description |
| 2026-10-06 18:04:30 | [Griffin.TestBase](https://www.nuget.org/packages/Griffin.TestBase) | 0.1.0 | Griffin.TestBase | Package Description |
| 2026-10-06 18:04:31 | [Griffin.Utils](https://www.nuget.org/packages/Griffin.Utils) | 0.1.0 | Griffin.Utils | Package Description |
| 2026-10-06 18:04:32 | [Griffin.Validation](https://www.nuget.org/packages/Griffin.Validation) | 0.1.0 | Griffin.Validation | Package Description |
| 2026-10-06 18:04:34 | [Griffin.Web](https://www.nuget.org/packages/Griffin.Web) | 0.1.0 | Griffin.Web | Package Description |
| 2026-10-06 18:04:35 | [Griffin.Wolverine](https://www.nuget.org/packages/Griffin.Wolverine) | 0.1.0 | Griffin.Wolverine | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
