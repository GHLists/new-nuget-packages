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

## Latest list — 2026-10-15 06:22 UTC

New packages created between 2026-10-15 05:22 UTC and 2026-10-15 06:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T06-22-01-035534Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 05:24:07 | [Dignite.Vault.Extract.FlexFields](https://www.nuget.org/packages/Dignite.Vault.Extract.FlexFields) | 0.5.0 | Dignite | Vault Extract's own extensions to the Dignite.Abp.FlexFields kernel: field type… |
| 2026-10-15 05:24:50 | [AVEVAServices.FlowModule.PIImport](https://www.nuget.org/packages/AVEVAServices.FlowModule.PIImport) | 1.0.0 | Scott Henderson | Package Description |
| 2026-10-15 05:29:55 | [LANCommander.Server.UI](https://www.nuget.org/packages/LANCommander.Server.UI) | 2.0.0-alpha | pathartl | A Blazor component library for building UIs on the LANCommander platform |
| 2026-10-15 05:45:41 | [SelectPdf.Universal.Windows](https://www.nuget.org/packages/SelectPdf.Universal.Windows) | 26.5.0 | SelectPdf | The SelectPdf PDF library for .NET on Windows x64. This package contains no cod… |
| 2026-10-15 05:45:42 | [SelectPdf.Universal.Linux](https://www.nuget.org/packages/SelectPdf.Universal.Linux) | 26.5.0 | SelectPdf | The SelectPdf PDF library for .NET on Linux x64 and Docker. This package contai… |
| 2026-10-15 05:45:44 | [SelectPdf.Universal.Linux.Arm64](https://www.nuget.org/packages/SelectPdf.Universal.Linux.Arm64) | 26.5.0 | SelectPdf | The SelectPdf PDF library for .NET on Linux ARM64 and Docker. This package cont… |
| 2026-10-15 05:45:47 | [SelectPdf.Universal.MacOS](https://www.nuget.org/packages/SelectPdf.Universal.MacOS) | 26.5.0 | SelectPdf | The SelectPdf PDF library for .NET on macOS on Apple Silicon. This package cont… |
| 2026-10-15 05:45:48 | [SelectPdf.HtmlToPdf.Windows](https://www.nuget.org/packages/SelectPdf.HtmlToPdf.Windows) | 26.5.0 | SelectPdf | Free HTML to PDF converter for .NET on Windows x64. This package contains no co… |
| 2026-10-15 05:45:50 | [SelectPdf.HtmlToPdf.Linux](https://www.nuget.org/packages/SelectPdf.HtmlToPdf.Linux) | 26.5.0 | SelectPdf | Free HTML to PDF converter for .NET on Linux x64 and Docker. This package conta… |
| 2026-10-15 05:45:52 | [SelectPdf.HtmlToPdf.Linux.Arm64](https://www.nuget.org/packages/SelectPdf.HtmlToPdf.Linux.Arm64) | 26.5.0 | SelectPdf | Free HTML to PDF converter for .NET on Linux ARM64 and Docker. This package con… |
| 2026-10-15 05:45:53 | [SelectPdf.HtmlToPdf.MacOS](https://www.nuget.org/packages/SelectPdf.HtmlToPdf.MacOS) | 26.5.0 | SelectPdf | Free HTML to PDF converter for .NET on macOS on Apple Silicon. This package con… |
| 2026-10-15 05:45:55 | [SelectPdf.Compat.DinkToPdf](https://www.nuget.org/packages/SelectPdf.Compat.DinkToPdf) | 1.0.0 | SelectPdf | A free replacement for DinkToPdf that keeps its API (IConverter, SynchronizedCo… |
| 2026-10-15 05:45:57 | [SelectPdf.Compat.DinkToPdf.Licensed](https://www.nuget.org/packages/SelectPdf.Compat.DinkToPdf.Licensed) | 1.0.0 | SelectPdf | The DinkToPdf API (IConverter, SynchronizedConverter, HtmlToPdfDocument, Global… |
| 2026-10-15 05:45:59 | [SelectPdf.Compat.WkHtmlToPdfDotNet](https://www.nuget.org/packages/SelectPdf.Compat.WkHtmlToPdfDotNet) | 1.0.0 | SelectPdf | A free replacement for Haukcode.WkHtmlToPdfDotNet that keeps its API (IConverte… |
| 2026-10-15 05:46:01 | [SelectPdf.Compat.WkHtmlToPdfDotNet.Licensed](https://www.nuget.org/packages/SelectPdf.Compat.WkHtmlToPdfDotNet.Licensed) | 1.0.0 | SelectPdf | The Haukcode.WkHtmlToPdfDotNet API (IConverter, SynchronizedConverter, HtmlToPd… |
| 2026-10-15 05:46:03 | [SelectPdf.Templates](https://www.nuget.org/packages/SelectPdf.Templates) | 1.0.0 | SelectPdf | dotnet new templates for generating PDFs from HTML in .NET with SelectPdf (Chro… |
| 2026-10-15 05:55:24 | [XiHan.Framework.Cli](https://www.nuget.org/packages/XiHan.Framework.Cli) | 4.7.0 | XiHanFun | 曦寒框架命令行与 MCP 服务端：模块、配置节、文档与更新日志的离线知识库 |
| 2026-10-15 05:59:14 | [TruSql.Core](https://www.nuget.org/packages/TruSql.Core) | 1.0.0 | Indra Putra Gemilang | Core expression, parsing, and tokenization components for TruSql. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
