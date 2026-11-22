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

## Latest list — 2026-11-22 03:19 UTC

New packages created between 2026-11-22 02:19 UTC and 2026-11-22 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T03-19-57-809705Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 02:21:50 | [Sevencat.ImageFacade.SdcbSimdCodecsAio](https://www.nuget.org/packages/Sevencat.ImageFacade.SdcbSimdCodecsAio) | 0.6.0 | ImageFacade contributors | ImageFacade 的纯托管后端「一体化」版：绘制 / 文字 / 缩放沿用 ImageFacade.SdcbSimdCodecs 的自绘渲染（同一份源码）… |
| 2026-11-22 02:43:26 | [MASS4.Guinevere.Charts](https://www.nuget.org/packages/MASS4.Guinevere.Charts) | 7.0.0 | Bruno Massa | Allocation-conscious chart geometry and drawing for Guinevere. |
| 2026-11-22 02:44:53 | [Mediana.Codecs.Alac](https://www.nuget.org/packages/Mediana.Codecs.Alac) | 0.1.34 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-22 02:44:55 | [Mediana.Codecs.ProRes](https://www.nuget.org/packages/Mediana.Codecs.ProRes) | 0.1.34 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-22 02:45:08 | [Mediana.Codecs.Dts](https://www.nuget.org/packages/Mediana.Codecs.Dts) | 0.1.34 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-22 02:55:38 | [Plasm.Sqlite](https://www.nuget.org/packages/Plasm.Sqlite) | 0.3.0 | Plasm contributors | SQLite provider for Plasm (Microsoft.Data.Sqlite). |
| 2026-11-22 03:05:22 | [GrayMint.Common.Blazor](https://www.nuget.org/packages/GrayMint.Common.Blazor) | 2.1.317 | GrayMint | Blazor WebAssembly components on MudBlazor for admin panels: a property list th… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
