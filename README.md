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

## Latest list — 2026-10-08 00:18 UTC

New packages created between 2026-10-07 23:20 UTC and 2026-10-08 00:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T00-18-54-334471Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 23:33:49 | [HyperTabular](https://www.nuget.org/packages/HyperTabular) | 0.7.0 | Brian Buvinghausen | Forward-only delimited text (CSV, TSV, any ASCII separator) and workbooks (XLSX… |
| 2026-10-07 23:43:03 | [Narula.Data.Abstractions](https://www.nuget.org/packages/Narula.Data.Abstractions) | 1.0.0 | John Narula | Common contracts for Narula data access: IDataSource, IMigration, MigrationRunn… |
| 2026-10-07 23:43:15 | [Narula.Data.Sqlite](https://www.nuget.org/packages/Narula.Data.Sqlite) | 1.0.0 | John Narula | SQLite implementation of Narula.Data.Abstractions: SqliteDataSource with WAL mo… |
| 2026-10-07 23:48:47 | [AdvanceSoftware.ExcelCreator.Xlsx.CreatorExpress.Linux](https://www.nuget.org/packages/AdvanceSoftware.ExcelCreator.Xlsx.CreatorExpress.Linux) | 12.0.4 | AdvanceSoftware | ExcelCreator は、プログラム上で Excel ファイルを高速に生成する Excel ファイル生成コンポーネントです。独自の技術で Excel ファ… |
| 2026-10-07 23:49:15 | [AdvanceSoftware.ExcelCreator.Creator.Linux](https://www.nuget.org/packages/AdvanceSoftware.ExcelCreator.Creator.Linux) | 12.0.4 | AdvanceSoftware | ExcelCreator は、プログラム上で Excel ファイルを高速に生成する Excel ファイル生成コンポーネントです。独自の技術で Excel ファ… |
| 2026-10-07 23:49:43 | [AdvanceSoftware.ExcelCreator.BarCode.Linux](https://www.nuget.org/packages/AdvanceSoftware.ExcelCreator.BarCode.Linux) | 12.0.4 | AdvanceSoftware | ExcelCreator は、プログラム上で Excel ファイルを高速に生成する Excel ファイル生成コンポーネントです。独自の技術で Excel ファ… |
| 2026-10-07 23:53:32 | [AdvanceSoftware.ASReport.CellReport.Linux](https://www.nuget.org/packages/AdvanceSoftware.ASReport.CellReport.Linux) | 12.0.4 | AdvanceSoftware | AS-Report は、帳票レイアウトを Excel で作成し、プログラム上でデータの差し込みや出力を行う帳票ツールです。帳票ツール独自のデザイナ機能を覚える… |
| 2026-10-07 23:53:59 | [AdvanceSoftware.ASReport.BarCode.Linux](https://www.nuget.org/packages/AdvanceSoftware.ASReport.BarCode.Linux) | 12.0.4 | AdvanceSoftware | AS-Report は、帳票レイアウトを Excel で作成し、プログラム上でデータの差し込みや出力を行う帳票ツールです。帳票ツール独自のデザイナ機能を覚える… |
| 2026-10-07 23:58:45 | [AdvanceSoftware.ASDataReport.Core](https://www.nuget.org/packages/AdvanceSoftware.ASDataReport.Core) | 1.0.0 | AdvanceSoftware | AS-DataReport は、帳票レイアウトを Excel で作成し、プログラム上でデータの差し込みや出力を行う帳票ツールです。帳票ツール独自のデザイナ機能… |
| 2026-10-08 00:01:03 | [CP.ReactiveUI.Primitives.Windows](https://www.nuget.org/packages/CP.ReactiveUI.Primitives.Windows) | 1.0.0 | Chris Pulman | Composable Windows desktop capabilities with observable messages, input, device… |
| 2026-10-08 00:01:05 | [CP.ReactiveUI.Primitives.Windows.Core](https://www.nuget.org/packages/CP.ReactiveUI.Primitives.Windows.Core) | 1.0.0 | Chris Pulman | Foundational Windows primitives, native interop, safe handles, registry monitor… |
| 2026-10-08 00:01:06 | [CP.ReactiveUI.Primitives.Windows.Integrations](https://www.nuget.org/packages/CP.ReactiveUI.Primitives.Windows.Integrations) | 1.0.0 | Chris Pulman | Optional Windows integrations for Citrix lifecycle, virtual-channel IPC, CCM/WT… |
| 2026-10-08 00:01:07 | [CP.ReactiveUI.Primitives.Windows.Reactive](https://www.nuget.org/packages/CP.ReactiveUI.Primitives.Windows.Reactive) | 1.0.0 | Chris Pulman | System.Reactive-flavoured build of the composable Windows desktop capabilities. |
| 2026-10-08 00:11:09 | [TL.KeysetPagination](https://www.nuget.org/packages/TL.KeysetPagination) | 0.5.0 | Thaylon Lopes | Biblioteca para paginação avançada (Offset e Cursor) e composição booleana de f… |
| 2026-10-08 00:12:39 | [Eryri.WriteAheadLog](https://www.nuget.org/packages/Eryri.WriteAheadLog) | 1.0.0 | Osian Linton | A lightweight, high-performance **write-ahead log (WAL)** for .NET applications… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
