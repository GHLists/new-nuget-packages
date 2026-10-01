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

## Latest list — 2026-10-01 00:22 UTC

New packages created between 2026-09-30 23:19 UTC and 2026-10-01 00:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T00-22-48-944535Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 23:20:21 | [Beryllium.Audio](https://www.nuget.org/packages/Beryllium.Audio) | 0.9.990 | Vladyslav Pysarenko | Beryllium engine audio manager |
| 2026-09-30 23:20:50 | [SunamoGoPayApi](https://www.nuget.org/packages/SunamoGoPayApi) | 26.10.1.1 | www.sunamo.cz | Package Description |
| 2026-09-30 23:21:27 | [Smartstore.TinyImage.Gif.Native.linux-arm64](https://www.nuget.org/packages/Smartstore.TinyImage.Gif.Native.linux-arm64) | 1.96.0 | Eddie Kohler; SmartStore AG | Native gifsicle 1.96 executable for linux-arm64 platform. |
| 2026-09-30 23:25:57 | [Litenova.Fuse.any](https://www.nuget.org/packages/Litenova.Fuse.any) | 5.2.1 | Litenova Solutions | Faster .NET build and test loop for AI coding agents: reports only the compiler… |
| 2026-09-30 23:25:59 | [Litenova.Fuse.linux-arm64](https://www.nuget.org/packages/Litenova.Fuse.linux-arm64) | 5.2.1 | Litenova Solutions | Faster .NET build and test loop for AI coding agents: reports only the compiler… |
| 2026-09-30 23:26:01 | [Litenova.Fuse.linux-musl-arm64](https://www.nuget.org/packages/Litenova.Fuse.linux-musl-arm64) | 5.2.1 | Litenova Solutions | Faster .NET build and test loop for AI coding agents: reports only the compiler… |
| 2026-09-30 23:26:02 | [Litenova.Fuse.linux-musl-x64](https://www.nuget.org/packages/Litenova.Fuse.linux-musl-x64) | 5.2.1 | Litenova Solutions | Faster .NET build and test loop for AI coding agents: reports only the compiler… |
| 2026-09-30 23:26:04 | [Litenova.Fuse.linux-x64](https://www.nuget.org/packages/Litenova.Fuse.linux-x64) | 5.2.1 | Litenova Solutions | Faster .NET build and test loop for AI coding agents: reports only the compiler… |
| 2026-09-30 23:26:06 | [Litenova.Fuse.osx-arm64](https://www.nuget.org/packages/Litenova.Fuse.osx-arm64) | 5.2.1 | Litenova Solutions | Faster .NET build and test loop for AI coding agents: reports only the compiler… |
| 2026-09-30 23:26:07 | [Litenova.Fuse.win-x64](https://www.nuget.org/packages/Litenova.Fuse.win-x64) | 5.2.1 | Litenova Solutions | Faster .NET build and test loop for AI coding agents: reports only the compiler… |
| 2026-09-30 23:31:19 | [Apache.Thrift.Compiler](https://www.nuget.org/packages/Apache.Thrift.Compiler) | 0.25.0 | Apache Thrift Developers | The Apache Thrift IDL compiler for Windows, installable as a .NET tool. Generat… |
| 2026-09-30 23:33:34 | [Blossom](https://www.nuget.org/packages/Blossom) | 0.1.1 | Cosmin Crețu | Retained-mode UI framework for C# (Silk.NET + SkiaSharp), including reactive si… |
| 2026-09-30 23:38:41 | [Brows.Win32.Windows](https://www.nuget.org/packages/Brows.Win32.Windows) | 1.0.0 | Ken Yourek | Package Description |
| 2026-09-30 23:44:45 | [Meteion.Toolkit.WPF.SplashScreen](https://www.nuget.org/packages/Meteion.Toolkit.WPF.SplashScreen) | 1.2.2 | frogcrush | An optional native splash screen (layered window, per-pixel alpha, optional pro… |
| 2026-10-01 00:04:48 | [Oracle.VectorData](https://www.nuget.org/packages/Oracle.VectorData) | 23.26.300 | Oracle | Oracle Database Vector Store Connector helps build AI apps with Microsoft Agent… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
