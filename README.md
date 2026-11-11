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

## Latest list — 2026-11-11 07:21 UTC

New packages created between 2026-11-11 06:20 UTC and 2026-11-11 07:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T07-21-20-526134Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 06:20:55 | [Aiursoft.AnduinOS.OfflineBundles.Core](https://www.nuget.org/packages/Aiursoft.AnduinOS.OfflineBundles.Core) | 10.0.1 | Aiursoft.AnduinOS.OfflineBund… | Nuget package of 'Core' provided by Aiursoft |
| 2026-11-11 06:41:31 | [NexMesh.Events](https://www.nuget.org/packages/NexMesh.Events) | 0.0.5 | NexMesh Team | NexMesh v2.0 进程内事件总线:有界 Channel(回压)+ 启动期编译委托 + 五步纪律上下文接续 + 停机排干契约 + OTel 指标。零第三… |
| 2026-11-11 06:47:16 | [HAKICODE.Workbench.Plugin.GenerationVideo](https://www.nuget.org/packages/HAKICODE.Workbench.Plugin.GenerationVideo) | 1.0.4 | HAKICODE | Tạo video ngắn từ mô tả hay từ một ảnh trên máy GPU nội bộ, từ trợ lý, giao diệ… |
| 2026-11-11 06:47:18 | [HAKICODE.Workbench.Plugin.GenerationDocument](https://www.nuget.org/packages/HAKICODE.Workbench.Plugin.GenerationDocument) | 1.0.7 | HAKICODE | Dựng tệp Word, Excel, PowerPoint, PDF theo mẫu của đơn vị từ nội dung trợ lý so… |
| 2026-11-11 06:50:47 | [Bit.Bmage.Blazor](https://www.nuget.org/packages/Bit.Bmage.Blazor) | 11.0.0-pre-18 | bit platform | bit Bmage for Blazor: browser-side image processing on the user's device from s… |
| 2026-11-11 06:50:51 | [Bit.Bheadless](https://www.nuget.org/packages/Bit.Bheadless) | 11.0.0-pre-18 | bit platform | Accessible, unstyled UI primitives for Blazor: keyboard interaction, focus mana… |
| 2026-11-11 06:51:19 | [GridKrafter.Core](https://www.nuget.org/packages/GridKrafter.Core) | 1.0.0 | Matt Gordon | The GridKrafter dashboard model, shared by the browser and the server: a pure g… |
| 2026-11-11 06:51:24 | [GridKrafter.Components](https://www.nuget.org/packages/GridKrafter.Components) | 1.0.0 | Matt Gordon | GridKrafter dashboards and widgets for Blazor Server, Blazor WebAssembly and MV… |
| 2026-11-11 06:52:13 | [Olax.Storage.Abstractions](https://www.nuget.org/packages/Olax.Storage.Abstractions) | 1.0.0 | OLAX Innovative Lab | File storage contracts for OLAX services: IFileService, IFileAccessAuthorizer,… |
| 2026-11-11 06:52:17 | [Olax.Storage](https://www.nuget.org/packages/Olax.Storage) | 1.0.0 | OLAX Innovative Lab | Provider-neutral core of OLAX file storage: options, the storage provider contr… |
| 2026-11-11 06:52:21 | [Olax.Storage.EntityFrameworkCore](https://www.nuget.org/packages/Olax.Storage.EntityFrameworkCore) | 1.0.0 | OLAX Innovative Lab | File metadata for OLAX storage on the service's own EF Core DbContext (table st… |
| 2026-11-11 06:52:24 | [Olax.Storage.FileSystem](https://www.nuget.org/packages/Olax.Storage.FileSystem) | 1.0.0 | OLAX Innovative Lab | File system provider for OLAX storage: files on a local disk or a mounted NAS/S… |
| 2026-11-11 06:52:26 | [Olax.Storage.S3](https://www.nuget.org/packages/Olax.Storage.S3) | 1.0.0 | OLAX Innovative Lab | S3 provider for OLAX storage: Amazon S3 and any S3-compatible store (SeaweedFS,… |
| 2026-11-11 06:52:29 | [Olax.Storage.Google](https://www.nuget.org/packages/Olax.Storage.Google) | 1.0.0 | OLAX Innovative Lab | Google Cloud Storage provider for OLAX storage: V4 signed upload and download U… |
| 2026-11-11 06:52:32 | [Olax.Storage.Azure](https://www.nuget.org/packages/Olax.Storage.Azure) | 1.0.0 | OLAX Innovative Lab | Azure Blob Storage provider for OLAX storage: SAS upload and download URLs (acc… |
| 2026-11-11 06:54:54 | [NssStream](https://www.nuget.org/packages/NssStream) | 1.0.0 | Vitaly Yakovlev (optinsoft) | .NET TLS stream backed by Mozilla NSS — the TLS library used by Firefox — with… |
| 2026-11-11 07:05:58 | [FS.GG.Game.Render.Kitty](https://www.nuget.org/packages/FS.GG.Game.Render.Kitty) | 0.23.0 | FS.GG Contributors | Bounded owned SVG rasterization and Kitty terminal graphics host for shared Gam… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
