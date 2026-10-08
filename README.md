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

## Latest list — 2026-10-08 09:22 UTC

New packages created between 2026-10-08 08:21 UTC and 2026-10-08 09:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T09-22-00-546039Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 08:24:09 | [BcsUniversal.EntityFrameworkCore.SqlServer](https://www.nuget.org/packages/BcsUniversal.EntityFrameworkCore.SqlServer) | 1.3.3 | cmm | MicroCloud SqlServer 数据库组件，封装基于 Microsoft.EntityFrameworkCore.SqlServer 的数据访问功能… |
| 2026-10-08 08:30:04 | [NKChinh.WinFormMarkup](https://www.nuget.org/packages/NKChinh.WinFormMarkup) | 0.2.1 | nkchinh | Fluent markup syntax for Windows Forms creation with localization support. Fork… |
| 2026-10-08 08:33:35 | [chd.Hub.Base.Server](https://www.nuget.org/packages/chd.Hub.Base.Server) | 2.0.26281.157 | chd.Hub.Base.Server | Package Description |
| 2026-10-08 08:39:48 | [FrameFlux.FFmpeg.NativeAssets.Android](https://www.nuget.org/packages/FrameFlux.FFmpeg.NativeAssets.Android) | 0.1.3 | FrameFlux | Android native FFmpeg runtime assets for FrameFlux. |
| 2026-10-08 08:39:51 | [FrameFlux.FFmpeg.NativeAssets.Linux](https://www.nuget.org/packages/FrameFlux.FFmpeg.NativeAssets.Linux) | 0.1.3 | FrameFlux | Linux native FFmpeg runtime assets for FrameFlux. |
| 2026-10-08 08:39:53 | [FrameFlux.FFmpeg.NativeAssets.Windows](https://www.nuget.org/packages/FrameFlux.FFmpeg.NativeAssets.Windows) | 0.1.3 | FrameFlux | Windows native FFmpeg runtime assets for FrameFlux. |
| 2026-10-08 08:48:24 | [Camcs](https://www.nuget.org/packages/Camcs) | 0.0.1 | Camcs | actor |
| 2026-10-08 08:51:03 | [Speechwarp](https://www.nuget.org/packages/Speechwarp) | 0.3.4 | The speechwarp contributors | Nonlinear speed-up for speech: listen faster and still follow it. Packages Goog… |
| 2026-10-08 08:52:34 | [SAEA.Socket5](https://www.nuget.org/packages/SAEA.Socket5) | 26.10.8.1 | yswenli | SOCKS5 Server and Client Based on SAEA.Socket.SAEA.Socket5是基于SAEA.Socket实现的SOCK… |
| 2026-10-08 08:58:04 | [Nryan.TimeManager.Exceptions](https://www.nuget.org/packages/Nryan.TimeManager.Exceptions) | 1.0.0 | nryan201 | Exceptions métier de TimeManager (introuvable, conflit, validation, règle métie… |
| 2026-10-08 09:07:46 | [DuraIT.FastBinaryJson](https://www.nuget.org/packages/DuraIT.FastBinaryJson) | 0.1.0 | Ben de Bruijn | Binary JSON serializer for .NET with attribute-free runtime polymorphism. Maint… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
