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

## Latest list — 2026-10-15 14:22 UTC

New packages created between 2026-10-15 13:23 UTC and 2026-10-15 14:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T14-22-09-341699Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 13:32:27 | [Org.Cdk8s.Plus36](https://www.nuget.org/packages/Org.Cdk8s.Plus36) | 2.0.0 | Amazon Web Services | cdk8s+ is a software development framework that provides high level abstraction… |
| 2026-10-15 13:43:27 | [SaxonCS-HE](https://www.nuget.org/packages/SaxonCS-HE) | 13.1.0 | Saxonica Ltd. | SaxonCS-HE is a high-performance XPath, XQuery, and XSLT processor. |
| 2026-10-15 13:49:46 | [Aml.Editor.Plugin.MtpVerification](https://www.nuget.org/packages/Aml.Editor.Plugin.MtpVerification) | 1.0.1 | Vincent Schmitt | This plugin provides tools to open MTP files and validate them against the Semo… |
| 2026-10-15 13:53:34 | [Muslim.GenericService.Interface](https://www.nuget.org/packages/Muslim.GenericService.Interface) | 10.0.1 | mazen | Service abstraction for Muslim.GenericService: IService<TEntity> and the interf… |
| 2026-10-15 14:01:58 | [DotCourier.Caching](https://www.nuget.org/packages/DotCourier.Caching) | 0.4.0 | Valossa515 | Query caching, idempotent commands and cache invalidation for DotCourier, on Mi… |
| 2026-10-15 14:04:31 | [PolishOpenData.Geo.Core](https://www.nuget.org/packages/PolishOpenData.Geo.Core) | 1.4.0 | JacekSmi | Typed Polish coordinates: PL-1992 (EPSG:2180) and WGS-84 points with a built-in… |
| 2026-10-15 14:04:32 | [PolishOpenData.Uug](https://www.nuget.org/packages/PolishOpenData.Uug) | 1.4.0 | JacekSmi | Typed .NET client for UUG (the address geocoder at services.gugik.gov.pl/uug) o… |
| 2026-10-15 14:04:33 | [PolishOpenData.Uldk](https://www.nuget.org/packages/PolishOpenData.Uldk) | 1.4.0 | JacekSmi | Typed .NET client for ULDK (Usługa Lokalizacji Działek Katastralnych, uldk.gugi… |
| 2026-10-15 14:04:56 | [FellowshipAnalyzer.Codex.SDK](https://www.nuget.org/packages/FellowshipAnalyzer.Codex.SDK) | 1.0.12 | Seriousnes | The documents the Fellowship data export is written as and read back through, t… |
| 2026-10-15 14:14:16 | [MIPIDesignSystem.ext2](https://www.nuget.org/packages/MIPIDesignSystem.ext2) | 1.0.7.5 | Berezhnoi A.I. | Дизайн-система для WPF-приложений Pilot-BIM: контролы, стили, токены и встроенн… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
