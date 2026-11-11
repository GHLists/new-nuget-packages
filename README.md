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

## Latest list — 2026-11-11 08:21 UTC

New packages created between 2026-11-11 07:21 UTC and 2026-11-11 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T08-21-56-677956Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 07:28:27 | [EonaCat.Docs](https://www.nuget.org/packages/EonaCat.Docs) | 1.0.0 | EonaCat | Office Open XML documents and native Outlook MSG/MIME mail. |
| 2026-11-11 07:44:23 | [Thll.Index.Ef](https://www.nuget.org/packages/Thll.Index.Ef) | 3.0.0 | Daniele Fusi | Entity Framework Entities for ThlL index. |
| 2026-11-11 07:44:32 | [Thll.Index.Api.Controllers](https://www.nuget.org/packages/Thll.Index.Api.Controllers) | 3.0.0 | Daniele Fusi | API controllers for ThlL index browser. |
| 2026-11-11 07:48:38 | [FunAsrNet](https://www.nuget.org/packages/FunAsrNet) | 1.0.1 | donet-org-cn | Independent managed C# speech inference for fixed Fun-ASR and Chinese VITS mode… |
| 2026-11-11 07:48:40 | [FunAsrNet.Vulkan](https://www.nuget.org/packages/FunAsrNet.Vulkan) | 1.0.1 | donet-org-cn | Optional Vulkan GPU backend for FunAsrNet: FP32 projections, convolutions and a… |
| 2026-11-11 07:49:53 | [DataFac.ProjScan](https://www.nuget.org/packages/DataFac.ProjScan) | 2.0.1 | DataFac Contributors | Experimental project scanning tool |
| 2026-11-11 07:53:22 | [PANiXiDA.Core.Presentation.Scalar](https://www.nuget.org/packages/PANiXiDA.Core.Presentation.Scalar) | 1.0.2 | PANiXiDA | Shared Scalar UI hosting for modular OpenAPI and AsyncAPI documents. |
| 2026-11-11 07:55:56 | [WASU.Abstraction.RPC](https://www.nuget.org/packages/WASU.Abstraction.RPC) | 26.1111.15 | WASU.Abstraction.RPC | Package Description |
| 2026-11-11 07:59:17 | [Fiskit](https://www.nuget.org/packages/Fiskit) | 0.1.0 | FisKit | Official .NET client for the FisKit API: Argentine electronic invoices with ARC… |
| 2026-11-11 08:00:32 | [Eigenverft.NetLib.SqliteHotBackup](https://www.nuget.org/packages/Eigenverft.NetLib.SqliteHotBackup) | 1.0.0.3 | Eigenverft | Scheduler-independent SQLite online backups with EF Core discovery, explicit fi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
