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

## Latest list — 2026-10-03 12:20 UTC

New packages created between 2026-10-03 11:20 UTC and 2026-10-03 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T12-20-48-479745Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 11:22:51 | [RtspViewer](https://www.nuget.org/packages/RtspViewer) | 1.0.2 | GreatBear | RTSP视频显示与录制控件(纯FFmpeg实现,零第三方依赖,H.264高压缩录制,自带ffmpeg.exe,装包即用) |
| 2026-10-03 11:26:18 | [PRC.Server.Bundle](https://www.nuget.org/packages/PRC.Server.Bundle) | 1.746.0 | Johannes Braumann | Parametric Robot Control (PRC) Server, bundled: the complete, runnable PRC Serv… |
| 2026-10-03 11:28:54 | [DataFac.Storage.LocalFS](https://www.nuget.org/packages/DataFac.Storage.LocalFS) | 4.0.15-dev | DataFac Contributors | Storage interfaces, types and helpers. |
| 2026-10-03 11:38:39 | [SumOffice](https://www.nuget.org/packages/SumOffice) | 2026.4.3 | Office SDK | Create and edit XLSX, DOCX and PPTX without Office; use the server to show them… |
| 2026-10-03 11:46:56 | [AndroidLibrary](https://www.nuget.org/packages/AndroidLibrary) | 0.1.0 | dong | phục vụ cho tool android. c#: u2, advancedshaftadbclient, adb, cdp |
| 2026-10-03 12:04:23 | [SubZeroDev.Platform.Updater](https://www.nuget.org/packages/SubZeroDev.Platform.Updater) | 0.1.0 | SubZeroDev | UI-independent update lifecycle for Windows .NET applications using public GitH… |
| 2026-10-03 12:06:30 | [LukasMoeller.Configuration.Toml](https://www.nuget.org/packages/LukasMoeller.Configuration.Toml) | 1.0.0 | Lukas Moeller | TOML configuration provider for Microsoft.Extensions.Configuration, built on To… |
| 2026-10-03 12:13:20 | [JdkFind](https://www.nuget.org/packages/JdkFind) | 0.1.0 | ghostflyby | Locate installed JDKs across Windows, macOS and Linux. |
| 2026-10-03 12:14:47 | [Rony.Net.Cli](https://www.nuget.org/packages/Rony.Net.Cli) | 1.4.0 | Mojtaba Kiani | The rony command-line tool for Rony.Net: run a TCP, TLS, UDP or Unix socket moc… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
