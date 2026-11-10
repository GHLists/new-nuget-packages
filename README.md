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

## Latest list — 2026-11-10 11:21 UTC

New packages created between 2026-11-10 10:22 UTC and 2026-11-10 11:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T11-21-02-884464Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 10:26:33 | [EpochSim.Analyzers](https://www.nuget.org/packages/EpochSim.Analyzers) | 0.3.1 | Echways | Roslyn analyzers that report constructs breaking determinism inside EpochSim si… |
| 2026-11-10 10:26:38 | [EpochSim.Testing](https://www.nuget.org/packages/EpochSim.Testing) | 0.3.1 | Echways | Framework-agnostic assertions for EpochSim: check determinism and invariants ov… |
| 2026-11-10 10:31:32 | [redmine-api.http](https://www.nuget.org/packages/redmine-api.http) | 0.1.0 | Adrian Popescu | HttpClient transport for the Redmine .NET API client. |
| 2026-11-10 10:31:34 | [redmine-api.http-signed](https://www.nuget.org/packages/redmine-api.http-signed) | 0.1.0 | Adrian Popescu | HttpClient transport for the Redmine .NET API client. |
| 2026-11-10 10:31:59 | [Scarlet.Extensions.Hosting.Avalonia](https://www.nuget.org/packages/Scarlet.Extensions.Hosting.Avalonia) | 1.0.0 | ScarletKuro | Microsoft.Extensions.Hosting (Generic Host) integration for Avalonia desktop ap… |
| 2026-11-10 10:32:00 | [Scarlet.Extensions.Hosting.Avalonia.Threading](https://www.nuget.org/packages/Scarlet.Extensions.Hosting.Avalonia.Threading) | 1.0.0 | ScarletKuro | Thread switching for Scarlet.Extensions.Hosting.Avalonia: JoinableTaskFactory a… |
| 2026-11-10 10:42:57 | [NathbrokRestSdk](https://www.nuget.org/packages/NathbrokRestSdk) | 1.0.3 | Nathbrok | Server-side .NET SDK for Nathbrok REST APIs. |
| 2026-11-10 10:44:34 | [DecentralizedBradleyTerry](https://www.nuget.org/packages/DecentralizedBradleyTerry) | 1.0.0 | Calbona | Decentralized Bradley–Terry rating updates from pairwise match results. |
| 2026-11-10 10:54:46 | [PdfPecker.Ocr](https://www.nuget.org/packages/PdfPecker.Ocr) | 1.24.0 | Moonwalker1307 | Dependency-free OCR for .NET: reads text from scanned PDFs and images and makes… |
| 2026-11-10 10:56:40 | [Clikgate](https://www.nuget.org/packages/Clikgate) | 2.0.0 | Clikgate | The official Clikgate server SDK for .NET: send goals in three lines, keep the… |
| 2026-11-10 10:56:41 | [Clikgate.AspNetCore](https://www.nuget.org/packages/Clikgate.AspNetCore) | 2.0.0 | Clikgate | ASP.NET Core integration for the Clikgate .NET SDK: AddClikgate() (options from… |
| 2026-11-10 10:58:00 | [Limbo.Integrations.DetDigitaleFolkebibliotek](https://www.nuget.org/packages/Limbo.Integrations.DetDigitaleFolkebibliotek) | 1.0.0-alpha001 | Eyðun Ellendersen | .NET integration package for Det Digitale Folkebibliotek. |
| 2026-11-10 11:01:09 | [ZX.Folio](https://www.nuget.org/packages/ZX.Folio) | 1.0.0 | Folio contributors | Folio's document engine for .NET, in one package: Word-like documents with real… |
| 2026-11-10 11:07:12 | [PocketCsvReader.Indexing](https://www.nuget.org/packages/PocketCsvReader.Indexing) | 2.69.0 | Cédric L. Charlier | Exact-key lookup with sparse indexes for sorted files and an opt-in scan fallba… |
| 2026-11-10 11:07:24 | [PdfPecker.Fonts.Emoji](https://www.nuget.org/packages/PdfPecker.Fonts.Emoji) | 1.24.0 | Moonwalker1307 | Noto Color Emoji for PdfPecker: colour emoji, including flags, skin tones and Z… |
| 2026-11-10 11:07:25 | [PdfPecker.Fonts.Scripts](https://www.nuget.org/packages/PdfPecker.Fonts.Scripts) | 1.24.0 | Moonwalker1307 | Noto Sans fonts for PdfPecker in 17 scripts the base library has no font for: A… |
| 2026-11-10 11:07:41 | [PdfPecker.Email](https://www.nuget.org/packages/PdfPecker.Email) | 1.24.0 | Moonwalker1307 | Convert e-mail (.eml, MIME, Outlook .msg and winmail.dat) to PDF and PDF/A-3 wi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
