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

## Latest list — 2026-11-11 13:21 UTC

New packages created between 2026-11-11 12:20 UTC and 2026-11-11 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T13-21-22-24939Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 12:21:51 | [miPDFlib.PostScript](https://www.nuget.org/packages/miPDFlib.PostScript) | 1.3.0 | Wolfgang Mitterbucher | Converts PostScript and EPS to PDF and places EPS graphics in PDF documents. Pu… |
| 2026-11-11 12:46:17 | [BSynchro.Clauses.Public](https://www.nuget.org/packages/BSynchro.Clauses.Public) | 8.4.0 | BSynchro | Client for the clauses service: master clause DTO, IClausesClient and AddClause… |
| 2026-11-11 12:46:20 | [BSynchro.Options.Public](https://www.nuget.org/packages/BSynchro.Options.Public) | 8.4.0 | BSynchro | Client for the options service: request and clause snapshot DTOs, IOptionsClien… |
| 2026-11-11 12:50:25 | [Bitavu.Client](https://www.nuget.org/packages/Bitavu.Client) | 0.1.1 | bitavu.com | PDF generation for .NET. Generate PDFs from Bitavu templates and JSON data with… |
| 2026-11-11 12:50:30 | [ErCreatorCore](https://www.nuget.org/packages/ErCreatorCore) | 1.3.1 | Rintaro Sugishita | ErCreator のデータモデル契約（EntityData / RelationData / ColumnData 等）と ermlx シリアライザ。WPF… |
| 2026-11-11 12:51:34 | [WorkManage.Contracts](https://www.nuget.org/packages/WorkManage.Contracts) | 1.0.6 | R.Sugishita | WorkManage 拡張機能開発用の共有コントラクトライブラリ。データモデル・入出力データ・拡張イベント定義を含みます。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
