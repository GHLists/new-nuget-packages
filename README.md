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

## Latest list — 2026-10-13 09:19 UTC

New packages created between 2026-10-13 08:19 UTC and 2026-10-13 09:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T09-19-11-019337Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 08:34:47 | [Wiknap.Testcontainers.GreenMail](https://www.nuget.org/packages/Wiknap.Testcontainers.GreenMail) | 1.0.2 | Wiknap | Testcontainers for GreenMail |
| 2026-10-13 08:43:26 | [NtvLibs.OnnxRuntime.CPU.cuda12.Tensorrt.onnxruntime_providers_cuda.runtime.linux-x64.f02](https://www.nuget.org/packages/NtvLibs.OnnxRuntime.CPU.cuda12.Tensorrt.onnxruntime_providers_cuda.runtime.linux-x64.f02) | 1.31.0 | nietras | native library runtime specific fragment 2/3 package |
| 2026-10-13 08:47:06 | [Dot0.Jibit](https://www.nuget.org/packages/Dot0.Jibit) | 10.0.1 | Dot0.Jibit | Jibit.ir HTTP client for .NET |
| 2026-10-13 08:51:06 | [Fungusware.Nfs](https://www.nuget.org/packages/Fungusware.Nfs) | 2026.10.13.850 | Fungusware | A managed, async NFS client for .NET. Connect to NFSv3 servers and NAS devices,… |
| 2026-10-13 08:55:21 | [RestExceptions.FluentValidation](https://www.nuget.org/packages/RestExceptions.FluentValidation) | 10.1.0 | Stratis-Dermanoutsos | FluentValidation integration for RestExceptions. Maps ValidationException to RF… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
