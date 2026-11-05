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

## Latest list — 2026-11-05 03:20 UTC

New packages created between 2026-11-05 02:18 UTC and 2026-11-05 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T03-20-43-442866Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 02:27:11 | [Webority.Pdf.Ocr.Azure](https://www.nuget.org/packages/Webority.Pdf.Ocr.Azure) | 0.6.0 | Webority.Pdf.Ocr.Azure | Reads scanned PDF pages through Azure AI Document Intelligence for Webority.Pdf. |
| 2026-11-05 02:28:20 | [Gengora.Protocol](https://www.nuget.org/packages/Gengora.Protocol) | 2.5.0 | Saqib Javed | Shared protocol message types for Gengora generator host and IDE server communi… |
| 2026-11-05 02:28:20 | [Gengora.Common.Attributes](https://www.nuget.org/packages/Gengora.Common.Attributes) | 2.5.0 | Saqib Javed | Consumer build contract that includes Gengora-owned generated C# files in compi… |
| 2026-11-05 02:28:21 | [Gengora.Comptime](https://www.nuget.org/packages/Gengora.Comptime) | 2.5.0 | Saqib Javed | Reusable compile-time evaluation engine for Gengora generators. |
| 2026-11-05 02:28:21 | [Gengora.Tools](https://www.nuget.org/packages/Gengora.Tools) | 2.5.0 | Saqib Javed | Text-diff and generated-file utility primitives shared by Gengora compiler pack… |
| 2026-11-05 02:28:22 | [Gengora.Compiler](https://www.nuget.org/packages/Gengora.Compiler) | 2.5.0 | Saqib Javed | Typed, in-process compiler lifecycle for Gengora language frontends and provide… |
| 2026-11-05 02:28:22 | [Gengora.Common](https://www.nuget.org/packages/Gengora.Common) | 2.5.0 | Saqib Javed | Compiler workspace, pipeline, and generated-output ownership primitives for Gen… |
| 2026-11-05 02:28:23 | [Gengora.Comptime.Attributes](https://www.nuget.org/packages/Gengora.Comptime.Attributes) | 2.5.0 | Saqib Javed | Public attributes and provider contracts for Gengora compile-time evaluation. |
| 2026-11-05 02:29:06 | [PdfNetStack.Html](https://www.nuget.org/packages/PdfNetStack.Html) | 1.1.0 | Jamal Abdelkhalek, JADEV | Convert HTML and CSS to PDF in .NET without a browser: an HTML5 parser, CSS cas… |
| 2026-11-05 02:29:07 | [PdfNetStack.Ocr](https://www.nuget.org/packages/PdfNetStack.Ocr) | 1.1.0 | Jamal Abdelkhalek, JADEV | OCR for PdfNetStack: finds the scan on each page, recognizes Latin and Arabic t… |
| 2026-11-05 02:29:12 | [PdfNetStack.Ocr.Tool](https://www.nuget.org/packages/PdfNetStack.Ocr.Tool) | 1.1.0 | Jamal Abdelkhalek, JADEV | Command line OCR for PDF files: finds the scan on each page, recognizes Latin a… |
| 2026-11-05 02:29:13 | [PdfNetStack.Ocr.Models](https://www.nuget.org/packages/PdfNetStack.Ocr.Models) | 1.0.0 | Jamal Abdelkhalek, JADEV | The PP-OCRv5 mobile models PdfNetStack.Ocr runs: text detection, line orientati… |
| 2026-11-05 02:33:05 | [JonjubNet.Indicators](https://www.nuget.org/packages/JonjubNet.Indicators) | 2.2.0 | Onuar Jiménez | Fórmulas de mercado puras y reutilizables para .NET: indicadores técnicos (tend… |
| 2026-11-05 02:33:09 | [JonjubNet.Rules](https://www.nuget.org/packages/JonjubNet.Rules) | 1.0.2 | Onuar Jiménez | Motor único de reglas: lee el formato de react-querybuilder, valida campos, tip… |
| 2026-11-05 02:33:10 | [JonjubNet.Messages](https://www.nuget.org/packages/JonjubNet.Messages) | 1.0.0 | Onuar Jiménez | Mensajes por código: la clave estable de un mensaje y la lectura de su texto de… |
| 2026-11-05 02:41:09 | [JonjubNet.Clock](https://www.nuget.org/packages/JonjubNet.Clock) | 1.2.0 | Onuar Jiménez | Reloj por plataforma, puro y sin estado global: sincroniza el cronómetro monotó… |
| 2026-11-05 02:43:21 | [Ofdrw.Net.Cli](https://www.nuget.org/packages/Ofdrw.Net.Cli) | 0.2.0 | whynpc9 | Command-line DOCX, PDF, OFD, and SVG conversion tool for Ofdrw.Net. |
| 2026-11-05 02:43:22 | [Ofdrw.Net.Converter](https://www.nuget.org/packages/Ofdrw.Net.Converter) | 0.2.0 | whynpc9 | Convenience meta-package for Ofdrw.Net DOCX, PDF, and SVG conversion features. |
| 2026-11-05 02:43:23 | [Ofdrw.Net.Converter.Abstractions](https://www.nuget.org/packages/Ofdrw.Net.Converter.Abstractions) | 0.2.0 | whynpc9 | Conversion interfaces for Ofdrw.Net file format converters. |
| 2026-11-05 02:43:24 | [Ofdrw.Net.Converter.Docx](https://www.nuget.org/packages/Ofdrw.Net.Converter.Docx) | 0.2.0 | whynpc9 | Direct DOCX/OpenXML to native OFD text conversion, with optional PDF and dual-l… |
| 2026-11-05 02:43:25 | [Ofdrw.Net.Converter.Pdf](https://www.nuget.org/packages/Ofdrw.Net.Converter.Pdf) | 0.2.0 | whynpc9 | PDF <-> OFD conversion implementation for Ofdrw.Net. |
| 2026-11-05 02:43:26 | [Ofdrw.Net.Converter.Svg](https://www.nuget.org/packages/Ofdrw.Net.Converter.Svg) | 0.2.0 | whynpc9 | OFD to SVG and static HTML vector conversion for Ofdrw.Net. |
| 2026-11-05 02:43:27 | [Ofdrw.Net.Core](https://www.nuget.org/packages/Ofdrw.Net.Core) | 0.2.0 | whynpc9 | Core OFD models, options, interfaces and validation report types for Ofdrw.Net. |
| 2026-11-05 02:43:28 | [Ofdrw.Net.Layout](https://www.nuget.org/packages/Ofdrw.Net.Layout) | 0.2.0 | whynpc9 | Document builder and layout helpers for generating OFD documents in Ofdrw.Net. |
| 2026-11-05 02:43:29 | [Ofdrw.Net.Packaging](https://www.nuget.org/packages/Ofdrw.Net.Packaging) | 0.2.0 | whynpc9 | OFD package ZIP container read/write and structure checks for Ofdrw.Net. |
| 2026-11-05 02:43:30 | [Ofdrw.Net.Reader](https://www.nuget.org/packages/Ofdrw.Net.Reader) | 0.2.0 | whynpc9 | OFD reader/parser for pages, resources, attachments and tags in Ofdrw.Net. |
| 2026-11-05 02:43:31 | [Ofdrw.Net.Signatures](https://www.nuget.org/packages/Ofdrw.Net.Signatures) | 0.2.0 | whynpc9 | OFD digital signature creation, reference integrity verification, and cryptogra… |
| 2026-11-05 02:43:32 | [Ofdrw.Net.Text.HarfBuzz](https://www.nuget.org/packages/Ofdrw.Net.Text.HarfBuzz) | 0.2.0 | whynpc9 | Optional HarfBuzz shaping adapter and native assets for the Ofdrw.Net text prel… |
| 2026-11-05 02:55:09 | [Gengora.CSharp.Formatting](https://www.nuget.org/packages/Gengora.CSharp.Formatting) | 2.5.0 | Saqib Javed | Reusable Roslyn formatting profiles for Gengora. |
| 2026-11-05 02:55:09 | [Gengora.CSharp.Transformations](https://www.nuget.org/packages/Gengora.CSharp.Transformations) | 2.5.0 | Saqib Javed | Compiler-bound C# declaration transformations configured by owning generators. |
| 2026-11-05 02:55:09 | [Gengora.CSharp.Comptime](https://www.nuget.org/packages/Gengora.CSharp.Comptime) | 2.5.0 | Saqib Javed | Roslyn-backed compile-time pipeline and typed result APIs for Gengora C# genera… |
| 2026-11-05 02:55:10 | [Gengora.CSharp](https://www.nuget.org/packages/Gengora.CSharp) | 2.5.0 | Saqib Javed | Roslyn and RazorBlade pipelines for authoring compiler-backed C# generators wit… |
| 2026-11-05 02:55:11 | [Gengora.CSharp.Formatter.Runtime](https://www.nuget.org/packages/Gengora.CSharp.Formatter.Runtime) | 2.5.0 | Saqib Javed | Version-matched C# formatter and semantic MCP executables for Gengora hosts. |
| 2026-11-05 03:09:02 | [FSR.NET](https://www.nuget.org/packages/FSR.NET) | 2.4.0 | qian-o | C# bindings for AMD FSR. |
| 2026-11-05 03:09:25 | [Gengora.Host](https://www.nuget.org/packages/Gengora.Host) | 2.5.0 | Saqib Javed | Generator host process for Gengora code generation framework. Handles protocol,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
