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

## Latest list — 2026-10-01 17:19 UTC

New packages created between 2026-10-01 16:20 UTC and 2026-10-01 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T17-19-34-763356Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 16:28:18 | [GargiolasTech.MigrationToolkit](https://www.nuget.org/packages/GargiolasTech.MigrationToolkit) | 0.1.0 | gtm | gtm: creates EF Core migrations and generates idempotent SQL scripts. |
| 2026-10-01 16:43:07 | [Cratis.Arc.Screenplay.Embedded](https://www.nuget.org/packages/Cratis.Arc.Screenplay.Embedded) | 22.44.0 | all contributors | Embeds generated Screenplay documents and hosts an opt-in event-model explorer… |
| 2026-10-01 16:50:56 | [DeepSharp.Backends.TorchSharp](https://www.nuget.org/packages/DeepSharp.Backends.TorchSharp) | 0.5.0 | H.P. Gansevoort | A DeepSharp network's arithmetic on libtorch, through TorchSharp: TorchBackend.… |
| 2026-10-01 16:50:58 | [DeepSharp.Import.Keras](https://www.nuget.org/packages/DeepSharp.Import.Keras) | 0.5.0 | H.P. Gansevoort | Reads a model Keras 3 saved into a DeepSharp network: the .keras archive it sav… |
| 2026-10-01 16:50:59 | [DeepSharp.Import.Onnx](https://www.nuget.org/packages/DeepSharp.Import.Onnx) | 0.5.0 | H.P. Gansevoort | Reads an ONNX graph into a DeepSharp network: the one PyTorch's torch.onnx.expo… |
| 2026-10-01 16:51:01 | [DeepSharp.Import.PyTorch](https://www.nuget.org/packages/DeepSharp.Import.PyTorch) | 0.5.0 | H.P. Gansevoort | Reads a network PyTorch trained into the same network written with DeepSharp: n… |
| 2026-10-01 16:51:04 | [DeepSharp.Pipelines.Excel](https://www.nuget.org/packages/DeepSharp.Pipelines.Excel) | 0.5.0 | H.P. Gansevoort | Reads a DeepSharp pipeline's rows out of an Excel workbook, .xlsx, .xls or .xls… |
| 2026-10-01 16:51:06 | [DeepSharp.Pipelines.Json](https://www.nuget.org/packages/DeepSharp.Pipelines.Json) | 0.5.0 | H.P. Gansevoort | Reads a DeepSharp pipeline's rows out of a JSON file holding an array of record… |
| 2026-10-01 16:51:07 | [DeepSharp.Pipelines.Parquet](https://www.nuget.org/packages/DeepSharp.Pipelines.Parquet) | 0.5.0 | H.P. Gansevoort | Reads a DeepSharp pipeline's rows out of an Apache Parquet file: .ReadParquet(p… |
| 2026-10-01 17:07:59 | [CMK.UK.BankModulus](https://www.nuget.org/packages/CMK.UK.BankModulus) | 0.0.1 | Chris McKee | .NET Library to provide modulus checking of bank account numbers against sort-c… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
