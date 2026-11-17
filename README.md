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

## Latest list — 2026-11-17 09:21 UTC

New packages created between 2026-11-17 08:18 UTC and 2026-11-17 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T09-21-42-817085Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 08:19:39 | [DigiTFactory.Libraries.Analyzers.CrossCutting](https://www.nuget.org/packages/DigiTFactory.Libraries.Analyzers.CrossCutting) | 0.4.0 | DigiTFactory.Libraries.Analyz… | Roslyn analyzers for cross-cutting rules (DigiTFactory EDM quality gates QG-6xx… |
| 2026-11-17 08:19:40 | [DigiTFactory.Libraries.Analyzers.Domain](https://www.nuget.org/packages/DigiTFactory.Libraries.Analyzers.Domain) | 0.6.0 | DigiTFactory.Libraries.Analyz… | Roslyn analyzers for the Domain layer (DigiTFactory EDM quality gates QG-0xx). |
| 2026-11-17 08:19:48 | [DigiTFactory.Libraries.Analyzers.DomainServices](https://www.nuget.org/packages/DigiTFactory.Libraries.Analyzers.DomainServices) | 0.4.0 | DigiTFactory.Libraries.Analyz… | Roslyn analyzers for the DomainServices layer (DigiTFactory EDM quality gates Q… |
| 2026-11-17 08:27:12 | [ParquetNeo.Extensions.DependencyInjection](https://www.nuget.org/packages/ParquetNeo.Extensions.DependencyInjection) | 0.2.0 | Luigi Grilli | Registers the metrics of ParquetNeo with Microsoft.Extensions.DependencyInjecti… |
| 2026-11-17 08:27:13 | [ParquetNeo.Storage.S3](https://www.nuget.org/packages/ParquetNeo.Storage.S3) | 0.2.0 | Luigi Grilli | Reads Parquet files from Amazon S3 (and S3 compatible storage) for ParquetNeo:… |
| 2026-11-17 08:27:15 | [ParquetNeo.Storage.AzureBlobs](https://www.nuget.org/packages/ParquetNeo.Storage.AzureBlobs) | 0.2.0 | Luigi Grilli | Reads Parquet files from Azure Blob Storage for ParquetNeo: only the byte range… |
| 2026-11-17 08:34:31 | [PeroTools2.PeroError](https://www.nuget.org/packages/PeroTools2.PeroError) | 0.2.0 | peropero | Result/Err style error handling for C#. Usable from Unity through Unity/Plugins. |
| 2026-11-17 08:42:03 | [Winche.Assets](https://www.nuget.org/packages/Winche.Assets) | 1.0.0 | Ehsan Rashidi | Versioned app content (translations, pages, media): releases on channels, per-p… |
| 2026-11-17 08:42:04 | [Winche.Assets.AspNetCore](https://www.nuget.org/packages/Winche.Assets.AspNetCore) | 1.0.0 | Ehsan Rashidi | The /assets/v1 endpoints apps read Winche Assets from. |
| 2026-11-17 09:01:25 | [ESRP.Release.NuGet.ESRPRelease-BVT.Prod.Build212760](https://www.nuget.org/packages/ESRP.Release.NuGet.ESRPRelease-BVT.Prod.Build212760) | 1.0.212760 | Microsoft | Disposable package used to validate NuGet publishing through ESRP Release. |
| 2026-11-17 09:04:24 | [LifeOS.Pdf.All](https://www.nuget.org/packages/LifeOS.Pdf.All) | 1.1.0 | Fajararifk | Everything in one command: LifeOS.Pdf plus signing, rendering, barcode scanning… |
| 2026-11-17 09:04:29 | [LifeOS.Pdf.Ocr](https://www.nuget.org/packages/LifeOS.Pdf.Ocr) | 1.1.0 | Fajararifk | OCR text from scanned PDFs and images using Tesseract (Apache-2.0). |
| 2026-11-17 09:04:31 | [LifeOS.Pdf.Rendering](https://www.nuget.org/packages/LifeOS.Pdf.Rendering) | 1.1.0 | Fajararifk | Render PDF pages to PNG using PDFium (Apache-2.0). |
| 2026-11-17 09:04:35 | [LifeOS.Pdf.Signing](https://www.nuget.org/packages/LifeOS.Pdf.Signing) | 1.1.0 | Fajararifk | Digital signatures (PAdES / CMS / PKCS#7) for LifeOS.Pdf documents. |
| 2026-11-17 09:06:07 | [NwUi.AspNetCore](https://www.nuget.org/packages/NwUi.AspNetCore) | 0.12.0 | NetWasm.UI contributors | Hosts a NetWasm.UI app in ASP.NET Core on the same origin: builds the client pr… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
