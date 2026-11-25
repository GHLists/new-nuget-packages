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

## Latest list — 2026-11-25 05:19 UTC

New packages created between 2026-11-25 04:21 UTC and 2026-11-25 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T05-19-59-678527Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 04:34:45 | [Ashishkamat](https://www.nuget.org/packages/Ashishkamat) | 1.0.0 | Ashish Kamat — full-stack dev… | Ashish Kamat cafe Kathmandu, Nepal constants. Official: https://ashishkamat.com… |
| 2026-11-25 04:51:53 | [DualBrain.Templates](https://www.nuget.org/packages/DualBrain.Templates) | 0.1.0 | Cory Smith | dotnet new templates for Visual Basic projects: programs that use QB.Compatibil… |
| 2026-11-25 05:03:30 | [DocWright.Spreadsheet.Security](https://www.nuget.org/packages/DocWright.Spreadsheet.Security) | 2.0.0 | DocWright contributors | Opens a password-encrypted Excel workbook (DocWright.Spreadsheet) and saves one… |
| 2026-11-25 05:03:32 | [DocWright.Word.Html](https://www.nuget.org/packages/DocWright.Word.Html) | 2.0.0 | DocWright contributors | HTML import and export for DocWright: a tolerant, dependency-free HTML5 parser… |
| 2026-11-25 05:03:37 | [DocWright.Word.Text](https://www.nuget.org/packages/DocWright.Word.Text) | 2.0.0 | DocWright contributors | Plain-text import and export for DocWright: configurable encoding detection, li… |
| 2026-11-25 05:03:38 | [DocWright.Spreadsheet.Xls](https://www.nuget.org/packages/DocWright.Spreadsheet.Xls) | 2.0.0 | DocWright contributors | Opens a legacy binary Excel workbook (.xls, BIFF8: Excel 97 to 2003 and later E… |
| 2026-11-25 05:03:40 | [DocWright.Word.Docx](https://www.nuget.org/packages/DocWright.Word.Docx) | 2.0.0 | DocWright contributors | DOCX reader and writer for DocWright: single-pass WordprocessingML parsing into… |
| 2026-11-25 05:03:42 | [DocWright.Word.Rdl](https://www.nuget.org/packages/DocWright.Word.Rdl) | 2.0.0 | DocWright contributors | SSRS Report Definition Language (.rdl) export for DocWright: turns a document i… |
| 2026-11-25 05:03:43 | [DocWright.Word.Epub](https://www.nuget.org/packages/DocWright.Word.Epub) | 2.0.0 | DocWright contributors | EPUB 3 export for DocWright: a dependency-free packager producing a conforming,… |
| 2026-11-25 05:03:44 | [DocWright.Word.Doc](https://www.nuget.org/packages/DocWright.Word.Doc) | 2.0.0 | DocWright contributors | Legacy Word 97-2003 (.doc) reader for DocWright, including files encrypted with… |
| 2026-11-25 05:03:51 | [DocWright.Spreadsheet.Rendering](https://www.nuget.org/packages/DocWright.Spreadsheet.Rendering) | 2.0.0 | DocWright contributors | Lays a worksheet of an opened workbook (DocWright.Spreadsheet) out as Excel pri… |
| 2026-11-25 05:03:55 | [DocWright.Word.Odt](https://www.nuget.org/packages/DocWright.Word.Odt) | 2.0.0 | DocWright contributors | OpenDocument Text (.odt) export for DocWright: a dependency-free ODF 1.3 writer… |
| 2026-11-25 05:03:57 | [DocWright.Word.Markdown](https://www.nuget.org/packages/DocWright.Word.Markdown) | 2.0.0 | DocWright contributors | Markdown import and export for DocWright: a dependency-free CommonMark 0.31.2 p… |
| 2026-11-25 05:04:12 | [DocWright.Word.MailMerge](https://www.nuget.org/packages/DocWright.Word.MailMerge) | 2.0.0 | DocWright contributors | Mail merge for DocWright: merge-field discovery and substitution (including fie… |
| 2026-11-25 05:04:16 | [DocWright.Spreadsheet](https://www.nuget.org/packages/DocWright.Spreadsheet) | 2.0.0 | DocWright contributors | SpreadsheetML (.xlsx) for DocWright, dependency-free. Writes a workbook from yo… |
| 2026-11-25 05:04:19 | [DocWright.Word](https://www.nuget.org/packages/DocWright.Word) | 2.0.0 | DocWright contributors | The mutable document model and editing API for DocWright: sections, paragraphs,… |
| 2026-11-25 05:04:21 | [DocWright.Word.Composition](https://www.nuget.org/packages/DocWright.Word.Composition) | 2.0.0 | DocWright contributors | Build a document from code with a fluent, declarative API for DocWright — pages… |
| 2026-11-25 05:04:22 | [DocWright.Word.Compare](https://www.nuget.org/packages/DocWright.Word.Compare) | 2.0.0 | DocWright contributors | Compare two Word documents with DocWright and get one document back carrying th… |
| 2026-11-25 05:04:25 | [DocWright.Word.Layout](https://www.nuget.org/packages/DocWright.Word.Layout) | 2.0.0 | DocWright contributors | Style resolution and page layout for DocWright: flattens document defaults, sty… |
| 2026-11-25 05:04:27 | [DocWright.Word.Rtf](https://www.nuget.org/packages/DocWright.Word.Rtf) | 2.0.0 | DocWright contributors | Rich Text Format (RTF 1.9) import and export for DocWright: a dependency-free t… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
