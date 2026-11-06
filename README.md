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

## Latest list — 2026-11-06 11:21 UTC

New packages created between 2026-11-06 10:19 UTC and 2026-11-06 11:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T11-21-58-004181Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 10:29:53 | [EnterpriseUI.WinForms](https://www.nuget.org/packages/EnterpriseUI.WinForms) | 1.0.0 | EnterpriseUI Open Source Cont… | Open-source Windows Forms component suite for .NET 8, including data grids, edi… |
| 2026-11-06 10:36:41 | [HAKICODE.Workbench.Plugin.ModelStudio](https://www.nuget.org/packages/HAKICODE.Workbench.Plugin.ModelStudio) | 1.0.25 | HAKICODE | Tạo ảnh và mô hình 3D có xương, chuyển động trên máy GPU nội bộ, từ trợ lý, gia… |
| 2026-11-06 10:39:12 | [OfficeIMO.Pdf.Word](https://www.nuget.org/packages/OfficeIMO.Pdf.Word) | 3.6.0 | Przemyslaw Klys | Reconstruct Word documents from PDF using the first-party OfficeIMO engines. |
| 2026-11-06 10:39:13 | [OfficeIMO.Pdf.PowerPoint](https://www.nuget.org/packages/OfficeIMO.Pdf.PowerPoint) | 3.6.0 | Przemyslaw Klys | Reconstruct PowerPoint presentations from PDF using the first-party OfficeIMO e… |
| 2026-11-06 10:39:16 | [OfficeIMO.Pdf.Excel](https://www.nuget.org/packages/OfficeIMO.Pdf.Excel) | 3.6.0 | Przemyslaw Klys | Reconstruct Excel workbooks from PDF using the first-party OfficeIMO engines. |
| 2026-11-06 10:39:51 | [OfficeIMO.Markup.PowerPoint](https://www.nuget.org/packages/OfficeIMO.Markup.PowerPoint) | 3.6.0 | Przemyslaw Klys | PowerPoint renderer for OfficeIMO Markup semantic AST. |
| 2026-11-06 10:39:53 | [OfficeIMO.Markup](https://www.nuget.org/packages/OfficeIMO.Markup) | 3.6.0 | Przemyslaw Klys | Unified Markdown-inspired OfficeIMO authoring layer with a semantic AST and C#/… |
| 2026-11-06 10:41:02 | [OfficeIMO.Drawing.ImageIO](https://www.nuget.org/packages/OfficeIMO.Drawing.ImageIO) | 3.6.0 | Przemyslaw Klys | Optional Apple system ImageIO raster codec for OfficeIMO.Drawing. |
| 2026-11-06 11:03:35 | [Zemires.Aspire.N8n](https://www.nuget.org/packages/Zemires.Aspire.N8n) | 13.6.0 | zemires, Laurent Christen | A .NET Aspire client integration registering the n8n public API client with hea… |
| 2026-11-06 11:03:36 | [Zemires.Aspire.Hosting.Terraform.Azure](https://www.nuget.org/packages/Zemires.Aspire.Hosting.Terraform.Azure) | 13.6.0 | zemires, Laurent Christen | A .NET Aspire integration that publishes Azure resources and Azure Container Ap… |
| 2026-11-06 11:03:36 | [Zemires.N8n.Api](https://www.nuget.org/packages/Zemires.N8n.Api) | 13.6.0 | zemires, Laurent Christen | A Kiota-generated .NET client for the n8n public REST API. |
| 2026-11-06 11:03:37 | [Zemires.Aspire.Hosting.Terraform](https://www.nuget.org/packages/Zemires.Aspire.Hosting.Terraform) | 13.6.0 | zemires, Laurent Christen | A .NET Aspire integration that publishes the application model as Terraform con… |
| 2026-11-06 11:03:37 | [Zemires.Aspire.Hosting.Zitadel](https://www.nuget.org/packages/Zemires.Aspire.Hosting.Zitadel) | 13.6.0 | zemires, Laurent Christen | A .NET Aspire integration for Zitadel. |
| 2026-11-06 11:03:37 | [Zemires.Aspire.Hosting.N8n](https://www.nuget.org/packages/Zemires.Aspire.Hosting.N8n) | 13.6.0 | zemires, Laurent Christen | A .NET Aspire hosting integration for n8n, including workers, task runners, Pos… |
| 2026-11-06 11:03:38 | [Zemires.Aspire.Zitadel](https://www.nuget.org/packages/Zemires.Aspire.Zitadel) | 13.6.0 | zemires, Laurent Christen | A .NET Aspire client integration registering the Zitadel API service clients. |
| 2026-11-06 11:06:13 | [RecursiveAI.OneImage.Metafile](https://www.nuget.org/packages/RecursiveAI.OneImage.Metafile) | 1.11.0 | Recursive AI, LLC | Windows metafile support for OneImage: reads EMF as an image format, rendered a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
