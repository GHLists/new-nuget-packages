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

## Latest list — 2026-10-28 08:19 UTC

New packages created between 2026-10-28 07:19 UTC and 2026-10-28 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T08-19-46-619577Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 07:22:43 | [FFmpeg.Interop.Native.linux-x64](https://www.nuget.org/packages/FFmpeg.Interop.Native.linux-x64) | 0.2.0-dev1 | Agash | FFmpeg 9 shared libraries for linux-x64, the build FFmpeg.Interop is generated… |
| 2026-10-28 07:22:45 | [FFmpeg.Interop.Native.osx-x64](https://www.nuget.org/packages/FFmpeg.Interop.Native.osx-x64) | 0.2.0-dev1 | Agash | FFmpeg 9 shared libraries for osx-x64, the build FFmpeg.Interop is generated fr… |
| 2026-10-28 07:22:47 | [FFmpeg.Interop.Native.win-x64](https://www.nuget.org/packages/FFmpeg.Interop.Native.win-x64) | 0.2.0-dev1 | Agash | FFmpeg 9 shared libraries for win-x64, the build FFmpeg.Interop is generated fr… |
| 2026-10-28 07:22:48 | [FFmpeg.Interop.Native.win-arm64](https://www.nuget.org/packages/FFmpeg.Interop.Native.win-arm64) | 0.2.0-dev1 | Agash | FFmpeg 9 shared libraries for win-arm64, the build FFmpeg.Interop is generated… |
| 2026-10-28 07:22:48 | [FFmpeg.Interop.Native](https://www.nuget.org/packages/FFmpeg.Interop.Native) | 0.2.0-dev1 | Agash | FFmpeg 9 shared libraries for every runtime FFmpeg.Interop supports, the build… |
| 2026-10-28 07:22:51 | [FFmpeg.Interop.Native.linux-arm64](https://www.nuget.org/packages/FFmpeg.Interop.Native.linux-arm64) | 0.2.0-dev1 | Agash | FFmpeg 9 shared libraries for linux-arm64, the build FFmpeg.Interop is generate… |
| 2026-10-28 07:22:54 | [FFmpeg.Interop.Native.osx-arm64](https://www.nuget.org/packages/FFmpeg.Interop.Native.osx-arm64) | 0.2.0-dev1 | Agash | FFmpeg 9 shared libraries for osx-arm64, the build FFmpeg.Interop is generated… |
| 2026-10-28 07:33:27 | [Lavshyak.MimeMaster](https://www.nuget.org/packages/Lavshyak.MimeMaster) | 0.0.0-master-4f8a6b8 | Tobias Lie-Atjam | A fast, accurate .NET library for MIME type detection and file validation using… |
| 2026-10-28 07:35:07 | [Zhai.HikCamera](https://www.nuget.org/packages/Zhai.HikCamera) | 1.0.0 | SPA | 海康 GigE/USB 工业相机设备、参数与回调取图核心库，支持 Windows 和 Linux。 |
| 2026-10-28 07:53:38 | [Didyk.RepairServiceCenter.Common](https://www.nuget.org/packages/Didyk.RepairServiceCenter.Common) | 1.0.0 | Maksym Didyk | Small helpers without dependencies on a domain: display names of enumerations,… |
| 2026-10-28 07:58:52 | [LibOpus.Interop](https://www.nuget.org/packages/LibOpus.Interop) | 0.1.0-dev3 | Agash | .NET bindings for libopus 1.6: an Opus encoder and decoder with every control t… |
| 2026-10-28 08:03:14 | [OODD.Timer](https://www.nuget.org/packages/OODD.Timer) | 0.0.1-preview18 | OODD | 跨平台的亚微秒级高精度定时器库：以单调时钟 + 自旋等待替代系统时钟节拍，摆脱 10~15ms 的定时器粒度。 |
| 2026-10-28 08:09:13 | [cxdbg](https://www.nuget.org/packages/cxdbg) | 2.10.1 | Nikolaos Protopapas | Attach to a running SharpConsoleUI application over its diagnostics socket and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
