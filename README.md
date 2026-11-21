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

## Latest list — 2026-11-21 09:21 UTC

New packages created between 2026-11-21 08:20 UTC and 2026-11-21 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T09-21-35-424401Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 08:42:09 | [Snap7.NetCore](https://www.nuget.org/packages/Snap7.NetCore) | 2.0.0 | Giant150 | Managed Siemens S7 PLC communication component for .NET 10 (byte read/write onl… |
| 2026-11-21 08:58:56 | [Sevencat.ImageFacade.Avalonia.SimdAIO](https://www.nuget.org/packages/Sevencat.ImageFacade.Avalonia.SimdAIO) | 0.1.0 | ImageFacade contributors | ImageFacade 的 Avalonia.SimdAIO 后端：配合 Sevencat.Avalonia.SimdAIO 宿主使用，图像处理走纯托管的 S… |
| 2026-11-21 09:02:24 | [OpenByd](https://www.nuget.org/packages/OpenByd) | 0.1.2 | openbyd contributors | Unofficial client for the BYD overseas app API, with a Rust core |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
