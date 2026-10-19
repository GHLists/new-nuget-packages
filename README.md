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

## Latest list — 2026-10-19 16:20 UTC

New packages created between 2026-10-19 15:19 UTC and 2026-10-19 16:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T16-20-06-836973Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 15:36:59 | [Tsfm.Forecasting.T0](https://www.nuget.org/packages/Tsfm.Forecasting.T0) | 0.2.0 | Mark Hammond | Native .NET inference for The Forecasting Company's t0 family (t0-alpha, t0-bet… |
| 2026-10-19 15:37:19 | [Tsfm.Forecasting.Timestral](https://www.nuget.org/packages/Tsfm.Forecasting.Timestral) | 0.2.0 | Mark Hammond | Native .NET inference for Mistral AI's Timestral family (5M, 28M, 123M, 209M):… |
| 2026-10-19 15:39:38 | [AVADS.FlowBuffer](https://www.nuget.org/packages/AVADS.FlowBuffer) | 2.0.0 | АВАДС СОФТ | Вспомогательная библиотека для драйвера для компактной и высокоскоростной базы… |
| 2026-10-19 15:39:53 | [BDTest.Contracts](https://www.nuget.org/packages/BDTest.Contracts) | 3.0.0 | Tom Longhurst | Immutable, versioned BDTest report contracts independent of test execution. |
| 2026-10-19 15:39:54 | [BDTest.Reporting](https://www.nuget.org/packages/BDTest.Reporting) | 3.0.0 | Tom Longhurst | JSON and self-contained HTML reports and report-server uploads for BDTest runs. |
| 2026-10-19 15:39:56 | [BDTest.Reports.Storage.FileSystem](https://www.nuget.org/packages/BDTest.Reports.Storage.FileSystem) | 3.0.0 | Tom Longhurst | Persistent directory-based BDTest report and run index storage with atomic writ… |
| 2026-10-19 15:40:00 | [BDTest.TUnit](https://www.nuget.org/packages/BDTest.TUnit) | 3.0.0 | Tom Longhurst | A TUnit Extension for BDTest |
| 2026-10-19 15:40:02 | [BDTest.Rendering](https://www.nuget.org/packages/BDTest.Rendering) | 3.0.0 | Tom Longhurst | Self-contained HTML reports and shared report fragments over immutable BDTest c… |
| 2026-10-19 15:40:03 | [BDTest.Reports.Storage.AzureBlob](https://www.nuget.org/packages/BDTest.Reports.Storage.AzureBlob) | 3.0.0 | Tom Longhurst | Persistent Azure Blob storage for BDTest reports, run indexes and attachments. |
| 2026-10-19 15:40:40 | [Tsfm.Forecasting.Timestral.Weights.5M](https://www.nuget.org/packages/Tsfm.Forecasting.Timestral.Weights.5M) | 0.2.0 | Mark Hammond | Timestral-5M (5.2M) weights for Tsfm.Forecasting.Timestral, embedded as assembl… |
| 2026-10-19 15:40:40 | [AVADS.TSDBConnector](https://www.nuget.org/packages/AVADS.TSDBConnector) | 2.0.0 | АВАДС СОФТ | Драйвер для компактной и высокоскоростной базы данных временных рядов (TSDB) дл… |
| 2026-10-19 15:40:59 | [Tsfm.Forecasting.Timestral.Weights.28M](https://www.nuget.org/packages/Tsfm.Forecasting.Timestral.Weights.28M) | 0.2.0 | Mark Hammond | Timestral-28M (27.8M) weights for Tsfm.Forecasting.Timestral, embedded as assem… |
| 2026-10-19 15:42:05 | [AVADS.MecTypes](https://www.nuget.org/packages/AVADS.MecTypes) | 2.0.0 | АВАДС СОФТ | Вспомогательная библиотека для драйвера для компактной и высокоскоростной базы… |
| 2026-10-19 15:47:49 | [EcalonIT.Umbraco.Backoffice](https://www.nuget.org/packages/EcalonIT.Umbraco.Backoffice) | 1.0.0 | EcalonIT | Shared Umbraco 17 backoffice foundation for EcalonIT products: a unified sectio… |
| 2026-10-19 15:57:59 | [AVS.Replace](https://www.nuget.org/packages/AVS.Replace) | 9.0.0 | Artem Vertii | Package Description |
| 2026-10-19 15:58:09 | [CamusDB.Extensions.Abstractions](https://www.nuget.org/packages/CamusDB.Extensions.Abstractions) | 0.16.0 | CamusDB | The contract for CamusDB C# extensions: attributes and interfaces for SQL scala… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
