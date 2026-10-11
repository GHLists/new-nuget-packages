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

## Latest list — 2026-10-11 21:19 UTC

New packages created between 2026-10-11 20:20 UTC and 2026-10-11 21:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T21-19-50-730615Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 20:29:27 | [KetPsi.Extensions.Logging.Abstractions](https://www.nuget.org/packages/KetPsi.Extensions.Logging.Abstractions) | 1.0.0 | KetPsi ,MohamadArsalan Imamve… | Core interfaces, compile-time interpolated string handlers, and types for KetPs… |
| 2026-10-11 20:31:23 | [KetPsi.Extensions.Logging.OpenTelemetry](https://www.nuget.org/packages/KetPsi.Extensions.Logging.OpenTelemetry) | 1.0.0 | KetPsi ,MohamadArsalan Imamve… | A zero-allocation OpenTelemetry (OTLP) log exporter for .NET. Bypasses the offi… |
| 2026-10-11 20:31:27 | [TencentCloudSDKIntlEN.Databuddy](https://www.nuget.org/packages/TencentCloudSDKIntlEN.Databuddy) | 3.0.1407 | Tencent Cloud API Team | Tencent Cloud API 3.0 SDK for .NET |
| 2026-10-11 20:32:24 | [KetPsi.Extensions.Logging.Console](https://www.nuget.org/packages/KetPsi.Extensions.Logging.Console) | 1.0.0 | KetPsi ,MohamadArsalan Imamve… | A hyper-optimized, zero-allocation console logger for .NET. Writes structured l… |
| 2026-10-11 20:41:27 | [ManagedCompressions.Lz4](https://www.nuget.org/packages/ManagedCompressions.Lz4) | 0.1.0 | Evariops | The LZ4 block format in fully managed C#: no native code, no P/Invoke. |
| 2026-10-11 20:41:28 | [ManagedCompressions.Zstd](https://www.nuget.org/packages/ManagedCompressions.Zstd) | 0.1.0 | Evariops | A Zstandard (RFC 8878) decompressor and compressor in fully managed C#: no nati… |
| 2026-10-11 20:49:57 | [AhmedHakami](https://www.nuget.org/packages/AhmedHakami) | 1.0.0 | Ahmed Hakami | Official author metadata and core .NET library by Ahmed Hakami. |
| 2026-10-11 20:56:44 | [Bobcat.NUnit](https://www.nuget.org/packages/Bobcat.NUnit) | 0.39.0 | Jeremy D. Miller | Bobcat + NUnit — projects ordinary [Test] methods into the Bobcat model, so an… |
| 2026-10-11 20:56:46 | [Bobcat.MSTest](https://www.nuget.org/packages/Bobcat.MSTest) | 0.39.0 | Jeremy D. Miller | Bobcat + MSTest — projects ordinary [TestMethod] methods into the Bobcat model,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
