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

## Latest list — 2026-10-01 04:22 UTC

New packages created between 2026-10-01 03:21 UTC and 2026-10-01 04:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T04-22-04-599282Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 03:33:06 | [XlsxCrypt.NativeExcelEncryption](https://www.nuget.org/packages/XlsxCrypt.NativeExcelEncryption) | 1.0.0 | Sujit Tamang | Native .NET library for Excel workbook password encryption. |
| 2026-10-01 03:46:54 | [Invex.Extensions.Logging.FancyConsole](https://www.nuget.org/packages/Invex.Extensions.Logging.FancyConsole) | 0.4.0 | Declan Smith | Useful utilities for Microsoft.Extensions.Logging |
| 2026-10-01 03:47:14 | [Numerics.NET.Native.Accelerate](https://www.nuget.org/packages/Numerics.NET.Native.Accelerate) | 10.8.0 | ExoAnalytics Inc. | Native macOS acceleration for Numerics.NET using Apple's system Accelerate fram… |
| 2026-10-01 03:48:12 | [Numerics.NET.Native.OpenBlas.linux-x64](https://www.nuget.org/packages/Numerics.NET.Native.OpenBlas.linux-x64) | 10.8.0 | ExoAnalytics Inc. | Native Linux x64 dense BLAS and LAPACK for Numerics.NET using OpenBLAS, with si… |
| 2026-10-01 03:48:39 | [Numerics.NET.Native.OpenBlas.win-x64](https://www.nuget.org/packages/Numerics.NET.Native.OpenBlas.win-x64) | 10.8.0 | ExoAnalytics Inc. | Native Windows x64 dense BLAS and LAPACK for Numerics.NET using OpenBLAS, with… |
| 2026-10-01 03:49:05 | [Numerics.NET.Native.OpenBlas.osx-x64](https://www.nuget.org/packages/Numerics.NET.Native.OpenBlas.osx-x64) | 10.8.0 | ExoAnalytics Inc. | Native macOS Intel x64 dense BLAS and LAPACK for Numerics.NET using OpenBLAS, w… |
| 2026-10-01 03:49:32 | [Numerics.NET.Native.OpenBlas.osx-arm64](https://www.nuget.org/packages/Numerics.NET.Native.OpenBlas.osx-arm64) | 10.8.0 | ExoAnalytics Inc. | Native macOS Apple Silicon ARM64 dense BLAS and LAPACK for Numerics.NET using O… |
| 2026-10-01 03:49:51 | [Numerics.NET.osx](https://www.nuget.org/packages/Numerics.NET.osx) | 10.8.0 | ExoAnalytics Inc. | Numerics.NET (formerly Extreme Optimization Numerical Libraries for .NET) are a… |
| 2026-10-01 04:15:26 | [Lingara](https://www.nuget.org/packages/Lingara) | 0.0.0 | Spinning Cat Studios | Reserved for the official Lingara .NET library (under development). |
| 2026-10-01 04:15:46 | [Lingara.Embed](https://www.nuget.org/packages/Lingara.Embed) | 0.0.0 | Spinning Cat Studios | Official .NET SDK for embedding Lingara in games and other platforms (under dev… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
