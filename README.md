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

## Latest list — 2026-10-31 22:18 UTC

New packages created between 2026-10-31 21:19 UTC and 2026-10-31 22:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T22-18-40-286795Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 21:24:22 | [MediaPipeTasksAudio.iOS](https://www.nuget.org/packages/MediaPipeTasksAudio.iOS) | 1.0.0 | Howard Good | .NET iOS bindings for MediaPipe Tasks Audio Library. |
| 2026-10-31 21:26:01 | [Zephyrus.Logging](https://www.nuget.org/packages/Zephyrus.Logging) | 1.0.2 | Amey Sunu | Send logs to Zephyrus |
| 2026-10-31 21:58:19 | [Papuma.Kernel.Core](https://www.nuget.org/packages/Papuma.Kernel.Core) | 3.0.0 | Harald Lapp | The storage-neutral core shared by Papuma.Kernel (PostgreSQL) and Papuma.Kernel… |
| 2026-10-31 22:08:21 | [GM.FileStorage.Domain](https://www.nuget.org/packages/GM.FileStorage.Domain) | 1.2.0 | Giorgi Metskhvarishvili | Domain model for the GM.FileStorage catalog: the StoredFile aggregate (key, nam… |
| 2026-10-31 22:08:22 | [GM.FileStorage.Persistence](https://www.nuget.org/packages/GM.FileStorage.Persistence) | 1.2.0 | Giorgi Metskhvarishvili | EF Core persistence for GM.FileStorage — entity type configurations mapping the… |
| 2026-10-31 22:12:45 | [SoftwareExtravaganza.Whizbang.Archive.AzureBlob](https://www.nuget.org/packages/SoftwareExtravaganza.Whizbang.Archive.AzureBlob) | 0.2626.0 | Phil Carbone | Azure Blob Storage IArchiveStore for Whizbang: archived event streams leave the… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
