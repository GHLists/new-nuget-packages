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

## Latest list — 2026-11-08 19:18 UTC

New packages created between 2026-11-08 18:21 UTC and 2026-11-08 19:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T19-18-50-135228Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 18:38:31 | [OptunaSharp](https://www.nuget.org/packages/OptunaSharp) | 1.0.0 | Eli Belash, SciSharp STACK Te… | OptunaSharp is a .NET port of Optuna 5.x, the define-by-run hyperparameter opti… |
| 2026-11-08 18:38:32 | [OptunaSharp.Artifacts.AzureBlob](https://www.nuget.org/packages/OptunaSharp.Artifacts.AzureBlob) | 1.0.0 | Eli Belash, SciSharp STACK Te… | Azure Blob Storage artifact store for OptunaSharp — an OptunaSharp extension (O… |
| 2026-11-08 18:38:33 | [OptunaSharp.Artifacts.Gcs](https://www.nuget.org/packages/OptunaSharp.Artifacts.Gcs) | 1.0.0 | Eli Belash, SciSharp STACK Te… | Google Cloud Storage (GCS) artifact store for OptunaSharp — a port of optuna.ar… |
| 2026-11-08 18:38:34 | [OptunaSharp.Artifacts.R2](https://www.nuget.org/packages/OptunaSharp.Artifacts.R2) | 1.0.0 | Eli Belash, SciSharp STACK Te… | Cloudflare R2 artifact store for OptunaSharp — an OptunaSharp extension (Optuna… |
| 2026-11-08 18:38:35 | [OptunaSharp.Artifacts.S3](https://www.nuget.org/packages/OptunaSharp.Artifacts.S3) | 1.0.0 | Eli Belash, SciSharp STACK Te… | Amazon S3 (and S3-compatible) artifact store for OptunaSharp — a port of optuna… |
| 2026-11-08 18:38:42 | [OptunaSharp.Cli](https://www.nuget.org/packages/OptunaSharp.Cli) | 1.0.0 | Eli Belash, SciSharp STACK Te… | The OptunaSharp command-line tool — the port of the `optuna` CLI (optuna/cli.py… |
| 2026-11-08 18:38:43 | [OptunaSharp.Integration.LightGbm](https://www.nuget.org/packages/OptunaSharp.Integration.LightGbm) | 1.0.0 | Eli Belash, SciSharp STACK Te… | OptunaSharp's LightGBM integration (a .NET port of Optuna's optuna.integration.… |
| 2026-11-08 18:38:44 | [OptunaSharp.Integration.ML.NET](https://www.nuget.org/packages/OptunaSharp.Integration.ML.NET) | 1.0.0 | Eli Belash, SciSharp STACK Te… | The ML.NET integration for OptunaSharp (a .NET port of Optuna): ML.NET-backed f… |
| 2026-11-08 18:38:46 | [OptunaSharp.Interop.BoTorch](https://www.nuget.org/packages/OptunaSharp.Interop.BoTorch) | 1.0.0 | Eli Belash, SciSharp STACK Te… | BoTorchSampler for OptunaSharp — a native OptunaSharp BaseSampler that drives t… |
| 2026-11-08 18:38:47 | [OptunaSharp.Interop.PyCma](https://www.nuget.org/packages/OptunaSharp.Interop.PyCma) | 1.0.0 | Eli Belash, SciSharp STACK Te… | PyCmaSampler for OptunaSharp — a native OptunaSharp BaseSampler that drives the… |
| 2026-11-08 18:38:48 | [OptunaSharp.Interop.Pymoo](https://www.nuget.org/packages/OptunaSharp.Interop.Pymoo) | 1.0.0 | Eli Belash, SciSharp STACK Te… | PymooSampler for OptunaSharp — a native OptunaSharp BaseSampler that drives the… |
| 2026-11-08 18:38:49 | [OptunaSharp.Interop.pythonnet](https://www.nuget.org/packages/OptunaSharp.Interop.pythonnet) | 1.0.0 | Eli Belash, SciSharp STACK Te… | OptunaSharp's bridge to the live Python Optuna ecosystem via Python.NET (python… |
| 2026-11-08 18:38:50 | [OptunaSharp.Storage.EFCore](https://www.nuget.org/packages/OptunaSharp.Storage.EFCore) | 1.0.0 | Eli Belash, SciSharp STACK Te… | PostgreSQL and MySQL RDB storage for OptunaSharp — the Entity Framework Core po… |
| 2026-11-08 18:38:51 | [OptunaSharp.Storage.Grpc](https://www.nuget.org/packages/OptunaSharp.Storage.Grpc) | 1.0.0 | Eli Belash, SciSharp STACK Te… | gRPC storage proxy for OptunaSharp — the port of optuna.storages.GrpcStoragePro… |
| 2026-11-08 18:38:52 | [OptunaSharp.Storage.NRedisStack](https://www.nuget.org/packages/OptunaSharp.Storage.NRedisStack) | 1.0.0 | Eli Belash, SciSharp STACK Te… | Redis journal-log backend for OptunaSharp on NRedisStack — Redis's official .NE… |
| 2026-11-08 18:38:53 | [OptunaSharp.Storage.Redis](https://www.nuget.org/packages/OptunaSharp.Storage.Redis) | 1.0.0 | Eli Belash, SciSharp STACK Te… | Shared, client-agnostic primitives for the OptunaSharp Redis journal backends:… |
| 2026-11-08 18:38:54 | [OptunaSharp.Storage.ServiceStack.Redis](https://www.nuget.org/packages/OptunaSharp.Storage.ServiceStack.Redis) | 1.0.0 | Eli Belash, SciSharp STACK Te… | Redis journal-log backend for OptunaSharp on ServiceStack.Redis. ServiceStackJo… |
| 2026-11-08 18:38:55 | [OptunaSharp.Storage.Sqlite](https://www.nuget.org/packages/OptunaSharp.Storage.Sqlite) | 1.0.0 | Eli Belash, SciSharp STACK Te… | SQLite RDB storage for OptunaSharp — the port of optuna.storages.RDBStorage on… |
| 2026-11-08 18:38:56 | [OptunaSharp.Storage.StackExchange.Redis](https://www.nuget.org/packages/OptunaSharp.Storage.StackExchange.Redis) | 1.0.0 | Eli Belash, SciSharp STACK Te… | Redis journal-log backend for OptunaSharp on StackExchange.Redis — the de-facto… |
| 2026-11-08 18:38:57 | [OptunaSharp.Visualization.Plotly](https://www.nuget.org/packages/OptunaSharp.Visualization.Plotly) | 1.0.0 | Eli Belash, SciSharp STACK Te… | The plotly visualization backend for OptunaSharp — a raw-C# port of optuna.visu… |
| 2026-11-08 18:47:23 | [JorgeCostaMacia.DDD.Aggregate](https://www.nuget.org/packages/JorgeCostaMacia.DDD.Aggregate) | 11.0.0 | JorgeCostaMacia | DDD Aggregate Root base that accumulates transport-agnostic domain events (IDom… |
| 2026-11-08 18:47:23 | [JorgeCostaMacia.DDD.DomainEvent](https://www.nuget.org/packages/JorgeCostaMacia.DDD.DomainEvent) | 11.0.0 | JorgeCostaMacia | Marker interface for transport-agnostic domain events |
| 2026-11-08 18:47:24 | [JorgeCostaMacia.DDD.Entity](https://www.nuget.org/packages/JorgeCostaMacia.DDD.Entity) | 11.0.0 | JorgeCostaMacia | Marker interface for identity-based domain entities |
| 2026-11-08 18:47:24 | [JorgeCostaMacia.DDD.Exception](https://www.nuget.org/packages/JorgeCostaMacia.DDD.Exception) | 11.0.0 | JorgeCostaMacia | Domain exception hierarchy (Domain / Error / Exist / NotFound / Validation) wit… |
| 2026-11-08 18:47:24 | [JorgeCostaMacia.DDD.ValueObject](https://www.nuget.org/packages/JorgeCostaMacia.DDD.ValueObject) | 11.0.0 | JorgeCostaMacia | Immutable, type-safe value objects with a three-verb creation surface (construc… |
| 2026-11-08 18:49:30 | [Diplo.Translator.Omni](https://www.nuget.org/packages/Diplo.Translator.Omni) | 18.0.0 | DanDiplo | AI translation for Umbraco pages, blocks and Dictionary items. Create drafts fo… |
| 2026-11-08 18:57:33 | [csv2zugferd](https://www.nuget.org/packages/csv2zugferd) | 1.3.0 | Rillsoft GmbH | CSV to ZUGFeRD/Factur-X (EN 16931) converter with PDF/A-3 embedding. Local .NET… |
| 2026-11-08 19:01:36 | [SolPnl.Contracts](https://www.nuget.org/packages/SolPnl.Contracts) | 0.1.0 | Joseph Abreu LLC | Plugin interfaces and models for SolPnl, a self-hosted solar monitoring app. Re… |
| 2026-11-08 19:02:01 | [Arjo.UmbraTranslate](https://www.nuget.org/packages/Arjo.UmbraTranslate) | 1.0.0 | Arjo.dev | Weglot-powered machine translation for Umbraco 17+: translated pages served fro… |
| 2026-11-08 19:08:54 | [Techne.Loom.Runtime.linux-arm64](https://www.nuget.org/packages/Techne.Loom.Runtime.linux-arm64) | 0.5.0-beta | Wayne Wang 韦恩卑鄙 | Self-contained single-file Techne Loom CLI runtime for one supported RID. |
| 2026-11-08 19:08:58 | [Techne.Loom.Runtime.linux-musl-x64](https://www.nuget.org/packages/Techne.Loom.Runtime.linux-musl-x64) | 0.5.0-beta | Wayne Wang 韦恩卑鄙 | Self-contained single-file Techne Loom CLI runtime for one supported RID. |
| 2026-11-08 19:09:03 | [Techne.Loom.Runtime.osx-arm64](https://www.nuget.org/packages/Techne.Loom.Runtime.osx-arm64) | 0.5.0-beta | Wayne Wang 韦恩卑鄙 | Self-contained single-file Techne Loom CLI runtime for one supported RID. |
| 2026-11-08 19:09:09 | [Techne.Loom.Runtime.win-x64](https://www.nuget.org/packages/Techne.Loom.Runtime.win-x64) | 0.5.0-beta | Wayne Wang 韦恩卑鄙 | Self-contained single-file Techne Loom CLI runtime for one supported RID. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
