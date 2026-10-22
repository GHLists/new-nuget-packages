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

## Latest list — 2026-10-22 17:19 UTC

New packages created between 2026-10-22 16:20 UTC and 2026-10-22 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T17-19-31-277928Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 16:22:15 | [Rag.NET.Parsers.AzureDocumentIntelligence](https://www.nuget.org/packages/Rag.NET.Parsers.AzureDocumentIntelligence) | 1.2.0 | Marcel Roozekrans | Azure Document Intelligence document parser for Rag.NET: TIFF and HEIF scans, w… |
| 2026-10-22 16:26:37 | [wwosik.DocLibs.DocumentConversions](https://www.nuget.org/packages/wwosik.DocLibs.DocumentConversions) | 2610.22.18.1 | Wojciech Wosik | Converts .pdf, .docx and .pptx into Markdown plus their images, and Markdown to… |
| 2026-10-22 16:26:38 | [wwosik.DocLibs.DocumentGeneration.Pptx](https://www.nuget.org/packages/wwosik.DocLibs.DocumentGeneration.Pptx) | 2610.22.18.1 | Wojciech Wosik | Generates PowerPoint presentations (.pptx) from Markdown, on the built-in maste… |
| 2026-10-22 16:26:39 | [wwosik.DocLibs.DocumentGeneration.Diagrams](https://www.nuget.org/packages/wwosik.DocLibs.DocumentGeneration.Diagrams) | 2610.22.18.1 | Wojciech Wosik | Mermaid diagrams for the wwosik.DocLibs document generators: vector graphics in… |
| 2026-10-22 16:26:39 | [wwosik.DocLibs.DocumentGeneration](https://www.nuget.org/packages/wwosik.DocLibs.DocumentGeneration) | 2610.22.18.1 | Wojciech Wosik | Brands for the wwosik.DocLibs document generators: colours, fonts, logo, footer… |
| 2026-10-22 16:26:40 | [wwosik.DocLibs.DocumentGeneration.Pdf](https://www.nuget.org/packages/wwosik.DocLibs.DocumentGeneration.Pdf) | 2610.22.18.1 | Wojciech Wosik | Generates PDF/A-2b documents from Markdown in a brand's colours, fonts and imag… |
| 2026-10-22 16:26:41 | [wwosik.DocLibs.DocumentConversions.WindowsOnly](https://www.nuget.org/packages/wwosik.DocLibs.DocumentConversions.WindowsOnly) | 2610.22.18.1 | Wojciech Wosik | Converts .doc, .rtf, .xls and .xlsx into Markdown through Office automation. Wi… |
| 2026-10-22 16:41:25 | [CamusDB.Aspire.Client](https://www.nuget.org/packages/CamusDB.Aspire.Client) | 0.1.0 | CamusDB | Aspire client integration for CamusDB: AddCamusDBClient() registers CamusDB.Cli… |
| 2026-10-22 16:41:44 | [CamusDB.Aspire.EntityFrameworkCore](https://www.nuget.org/packages/CamusDB.Aspire.EntityFrameworkCore) | 0.1.0 | CamusDB | Aspire client integration for the CamusDB Entity Framework Core provider: AddCa… |
| 2026-10-22 16:44:24 | [CamusDB.Aspire.Hosting](https://www.nuget.org/packages/CamusDB.Aspire.Hosting) | 0.1.0 | CamusDB | Aspire hosting integration for CamusDB: AddCamusDB() runs a CamusDB server cont… |
| 2026-10-22 16:44:58 | [Seq.App.Nebula](https://www.nuget.org/packages/Seq.App.Nebula) | 0.1.0 | Nebula | Turn Seq errors into deduplicated Jira bugs using Codex CLI through OpenRouter. |
| 2026-10-22 16:53:42 | [DotQR.Core](https://www.nuget.org/packages/DotQR.Core) | 1.0.0 | Edgar Aquino | DotQR.Core generates QR code module data. It has no graphics dependencies; pair… |
| 2026-10-22 16:54:47 | [DotQR.ByteRenderers](https://www.nuget.org/packages/DotQR.ByteRenderers) | 1.0.0 | Edgar Aquino | DotQR.ByteRenderers renders QR codes to PNG, BMP, PDF, SVG, PostScript and ASCI… |
| 2026-10-22 16:55:06 | [DotQR.SkiaSharp](https://www.nuget.org/packages/DotQR.SkiaSharp) | 1.0.0 | Edgar Aquino | DotQR.SkiaSharp renders QR codes to SKBitmap using SkiaSharp, including icon co… |
| 2026-10-22 17:04:37 | [Vetta.Connector](https://www.nuget.org/packages/Vetta.Connector) | 0.1.0 | Vettvangur | Auðkenni app and phone authentication for .NET websites using Vetta. |
| 2026-10-22 17:04:38 | [Vetta.Connector.AspNetCore](https://www.nuget.org/packages/Vetta.Connector.AspNetCore) | 0.1.0 | Vettvangur | ASP.NET Core endpoints and a browser helper for Vetta authentication. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
