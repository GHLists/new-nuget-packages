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

## Latest list — 2026-10-20 14:20 UTC

New packages created between 2026-10-20 13:21 UTC and 2026-10-20 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T14-20-05-182952Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 13:33:38 | [Projection.DependencyInjection](https://www.nuget.org/packages/Projection.DependencyInjection) | 1.0.0 | HashGrove | Microsoft.Extensions.DependencyInjection integration for the Projection object… |
| 2026-10-20 13:33:39 | [Projection](https://www.nuget.org/packages/Projection) | 1.0.0 | HashGrove | A simple, fast object-to-object mapper for .NET. Map entities to DTOs by conven… |
| 2026-10-20 13:35:08 | [Tlib.Diagnostics](https://www.nuget.org/packages/Tlib.Diagnostics) | 0.19.0 | Tomm2000 | Package Description |
| 2026-10-20 13:35:10 | [Tlib.Utils](https://www.nuget.org/packages/Tlib.Utils) | 0.19.0 | Tomm2000 | Package Description |
| 2026-10-20 13:50:53 | [AvaloniaFluentUI.Fonts](https://www.nuget.org/packages/AvaloniaFluentUI.Fonts) | 1.0.0 | AvaloniaFluentUI.Fonts | Package Description |
| 2026-10-20 13:50:54 | [DataStreamGenerator](https://www.nuget.org/packages/DataStreamGenerator) | 1.0.0 | DataStreamGenerator | Package Description |
| 2026-10-20 13:52:54 | [VMA.ImageProcessor](https://www.nuget.org/packages/VMA.ImageProcessor) | 1.0.0 | VMA | SkiaSharp-based image resizing for .NET. Provides a low-level ImageResizer (fit… |
| 2026-10-20 14:00:09 | [Regira.Web.HTML.RazorComponents](https://www.nuget.org/packages/Regira.Web.HTML.RazorComponents) | 6.6.0 | Regira bv | Renders compiled Razor components to HTML with ASP.NET Core's HtmlRenderer for… |
| 2026-10-20 14:00:48 | [SjolystInnovation.AppKit.Pdf](https://www.nuget.org/packages/SjolystInnovation.AppKit.Pdf) | 1.0.0 | Sjølyst Innovation AS | HTML to PDF through headless Chromium with PuppeteerSharp: A4 with backgrounds,… |
| 2026-10-20 14:01:35 | [Regira.Office.Mail.MailKit](https://www.nuget.org/packages/Regira.Office.Mail.MailKit) | 6.6.0 | Regira bv | Mail sending to any SMTP server via MailKit for Regira Office. |
| 2026-10-20 14:02:16 | [Regira.Office.PDF.Gotenberg](https://www.nuget.org/packages/Regira.Office.PDF.Gotenberg) | 6.6.0 | Regira bv | HTML to PDF conversion through the Chromium route of a Gotenberg server for Reg… |
| 2026-10-20 14:02:25 | [Regira.Office.PDF.MiniPdf](https://www.nuget.org/packages/Regira.Office.PDF.MiniPdf) | 6.6.0 | Regira bv | Word, Excel and PowerPoint to PDF conversion in-process using MiniPdf for Regir… |
| 2026-10-20 14:02:33 | [Regira.Office.PDF.PdfPig](https://www.nuget.org/packages/Regira.Office.PDF.PdfPig) | 6.6.0 | Regira bv | PDF operations for Regira Office: merge, split, page removal, text extraction a… |
| 2026-10-20 14:02:59 | [PulseSharp.Testing](https://www.nuget.org/packages/PulseSharp.Testing) | 0.6.0-alpha | Waqas Ahmad | Test helpers for apps that use PulseSharp: a recording IPulse, ready-made handl… |
| 2026-10-20 14:04:19 | [Regira.Entities.Mediator](https://www.nuget.org/packages/Regira.Entities.Mediator) | 6.6.0 | Regira bv | HTTP-neutral entity operations for Regira entities: details, list, search, save… |
| 2026-10-20 14:04:39 | [Xalosoftware.Sekiwa](https://www.nuget.org/packages/Xalosoftware.Sekiwa) | 0.1.0 | Xalo Software | Sekiwa licensing SDK for .NET: offline-verified, signed licences for desktop an… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
