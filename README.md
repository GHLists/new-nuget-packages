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

## Latest list — 2026-11-21 11:20 UTC

New packages created between 2026-11-21 10:20 UTC and 2026-11-21 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T11-20-50-709411Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 10:27:59 | [AsmFoundation.Toolchain.win-arm64](https://www.nuget.org/packages/AsmFoundation.Toolchain.win-arm64) | 0.2.0 | Eli Belash | The assembler and linker AsmFoundation.Sdk runs on win-arm64 build machines: NA… |
| 2026-11-21 10:28:10 | [AsmFoundation.Toolchain.linux-arm64](https://www.nuget.org/packages/AsmFoundation.Toolchain.linux-arm64) | 0.2.0 | Eli Belash | The assembler and linker AsmFoundation.Sdk runs on linux-arm64 build machines:… |
| 2026-11-21 10:28:39 | [Tubatools.StartupDoctor](https://www.nuget.org/packages/Tubatools.StartupDoctor) | 1.0.2 | ZJW | 检查开机启动项、登录计划任务、自启服务与后台内存占用，按风险分级给出建议，支持一键优化与回滚 |
| 2026-11-21 10:36:03 | [JoyZ.ApiResult](https://www.nuget.org/packages/JoyZ.ApiResult) | 1.0.1 | JoyZ | Unified API response result wrapper tool |
| 2026-11-21 10:46:45 | [RuMorpher](https://www.nuget.org/packages/RuMorpher) | 1.0.0 | RuMorpher Contributors | Clean-room, 100% MIT-licensed offline Russian morphological declension, geograp… |
| 2026-11-21 11:02:34 | [Immons.Tools.Maui.Inspector.SignalR](https://www.nuget.org/packages/Immons.Tools.Maui.Inspector.SignalR) | 0.10.0 | Artur Malendowicz "Immons" | SignalR traffic for Immons.Tools.Maui.Inspector: one line on the HubConnectionB… |
| 2026-11-21 11:04:44 | [oneAPI.Embree.NET](https://www.nuget.org/packages/oneAPI.Embree.NET) | 4.4.1 | Chiretallyn | Idiomatic, zero-overhead .NET bindings for Intel Embree 4.4.1 high-performance… |
| 2026-11-21 11:06:12 | [oneAPI.OpenVKL.NET](https://www.nuget.org/packages/oneAPI.OpenVKL.NET) | 2.0.2 | Chiretallyn | Idiomatic, zero-overhead .NET bindings for Intel Open VKL 2.0.2 volume renderin… |
| 2026-11-21 11:08:05 | [AbpCluster.Storage.HttpApi](https://www.nuget.org/packages/AbpCluster.Storage.HttpApi) | 0.6.0 | AbpCluster contributors | AbpCluster.Storage.HttpApi: AbpCluster.Storage's admin API over HTTP, under a r… |
| 2026-11-21 11:08:35 | [Quartz.Aspire.Hosting](https://www.nuget.org/packages/Quartz.Aspire.Hosting) | 4.8.0 | Marko Lahma, Quartz.NET | Quartz.NET Aspire hosting integration - adds the Quartz.NET dashboard to an Asp… |
| 2026-11-21 11:08:41 | [Quartz.Dashboard.Host](https://www.nuget.org/packages/Quartz.Dashboard.Host) | 4.8.0 | Marko Lahma, Quartz.NET | Quartz.NET dashboard host - the dashboard as a dotnet tool, configured entirely… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
