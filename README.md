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

## Latest list — 2026-11-10 09:22 UTC

New packages created between 2026-11-10 08:21 UTC and 2026-11-10 09:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T09-22-00-216209Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 08:25:19 | [WoW2.Sdk.Beta.Be.Events.Testing](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Events.Testing) | 10.0.0-beta | WoW 2.0 | Events test kit: a conformance suite per Events broker that every implementatio… |
| 2026-11-10 08:25:20 | [WoW2.Sdk.Beta.Be.Events.Module](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Events.Module) | 10.0.0-beta | WoW 2.0 | Events Form 1: the in-process greetings module over the consumer's PostgreSQL d… |
| 2026-11-10 08:25:20 | [WoW2.Sdk.Beta.Be.Events.Abstractions](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Events.Abstractions) | 10.0.0-beta | WoW 2.0 | Events contract: the catalog, review, tracking, import, calendar and intake bro… |
| 2026-11-10 08:25:21 | [WoW2.Sdk.Beta.Be.Events.Client](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Events.Client) | 10.0.0-beta | WoW 2.0 | Events Forms 2 and 3: every Events broker over the running Events service's HTT… |
| 2026-11-10 08:41:03 | [Xp.DvtReportWorkbookToolkit](https://www.nuget.org/packages/Xp.DvtReportWorkbookToolkit) | 0.0.2 | Abdul Wafiy Bin Abdul Rahim (… | Excel workbook operations and DVT report management toolkit. |
| 2026-11-10 08:42:23 | [PdfPecker.Cli.any](https://www.nuget.org/packages/PdfPecker.Cli.any) | 1.24.0 | Moonwalker1307 | The pdfpecker command-line tool: HTML and Markdown to PDF (with wkhtmltopdf-com… |
| 2026-11-10 08:42:24 | [PdfPecker.Cli.linux-arm64](https://www.nuget.org/packages/PdfPecker.Cli.linux-arm64) | 1.24.0 | Moonwalker1307 | The pdfpecker command-line tool: HTML and Markdown to PDF (with wkhtmltopdf-com… |
| 2026-11-10 08:42:25 | [PdfPecker.Cli.linux-musl-arm64](https://www.nuget.org/packages/PdfPecker.Cli.linux-musl-arm64) | 1.24.0 | Moonwalker1307 | The pdfpecker command-line tool: HTML and Markdown to PDF (with wkhtmltopdf-com… |
| 2026-11-10 08:42:27 | [PdfPecker.Cli.linux-musl-x64](https://www.nuget.org/packages/PdfPecker.Cli.linux-musl-x64) | 1.24.0 | Moonwalker1307 | The pdfpecker command-line tool: HTML and Markdown to PDF (with wkhtmltopdf-com… |
| 2026-11-10 08:42:28 | [PdfPecker.Cli.linux-x64](https://www.nuget.org/packages/PdfPecker.Cli.linux-x64) | 1.24.0 | Moonwalker1307 | The pdfpecker command-line tool: HTML and Markdown to PDF (with wkhtmltopdf-com… |
| 2026-11-10 08:42:30 | [PdfPecker.Cli.osx-arm64](https://www.nuget.org/packages/PdfPecker.Cli.osx-arm64) | 1.24.0 | Moonwalker1307 | The pdfpecker command-line tool: HTML and Markdown to PDF (with wkhtmltopdf-com… |
| 2026-11-10 08:42:32 | [PdfPecker.Cli.osx-x64](https://www.nuget.org/packages/PdfPecker.Cli.osx-x64) | 1.24.0 | Moonwalker1307 | The pdfpecker command-line tool: HTML and Markdown to PDF (with wkhtmltopdf-com… |
| 2026-11-10 08:42:33 | [PdfPecker.Cli.win-arm64](https://www.nuget.org/packages/PdfPecker.Cli.win-arm64) | 1.24.0 | Moonwalker1307 | The pdfpecker command-line tool: HTML and Markdown to PDF (with wkhtmltopdf-com… |
| 2026-11-10 08:42:34 | [PdfPecker.Cli.win-x64](https://www.nuget.org/packages/PdfPecker.Cli.win-x64) | 1.24.0 | Moonwalker1307 | The pdfpecker command-line tool: HTML and Markdown to PDF (with wkhtmltopdf-com… |
| 2026-11-10 08:49:04 | [wh7r4bb17.SharedRuntimes](https://www.nuget.org/packages/wh7r4bb17.SharedRuntimes) | 1.3.1 | wh7r4bb17 | Load centrally installed .NET assemblies and shared files at runtime without co… |
| 2026-11-10 08:55:08 | [Kaladel.Kiota.NullabilityFix.CSharp](https://www.nuget.org/packages/Kaladel.Kiota.NullabilityFix.CSharp) | 1.0.0 | Kaladel | Post-processes Kiota-generated C# models so that properties marked as "required… |
| 2026-11-10 09:08:34 | [ForkForward.Mapper](https://www.nuget.org/packages/ForkForward.Mapper) | 14.1.0 | ForkForward | ForkForward.Mapper is a community fork of AutoMapper, the convention-based obje… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
