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

## Latest list — 2026-11-04 05:20 UTC

New packages created between 2026-11-04 04:18 UTC and 2026-11-04 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T05-20-04-616985Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 04:24:24 | [OxyKit.Observability](https://www.nuget.org/packages/OxyKit.Observability) | 0.1.1 | OxyKit | JSON console logging and X-Correlation-Id helpers for OxyKit ASP.NET Core hosts. |
| 2026-11-04 04:24:24 | [OxyKit.OpenTelemetry](https://www.nuget.org/packages/OxyKit.OpenTelemetry) | 0.1.1 | OxyKit | Optional OpenTelemetry OTLP wiring for OxyKit ASP.NET Core hosts (off by defaul… |
| 2026-11-04 04:29:44 | [MemoryPack.Generator.Patched](https://www.nuget.org/packages/MemoryPack.Generator.Patched) | 1.21.4.3 | aminparsa18,Cysharp | Unofficial patched build of the MemoryPack source generator (based on Cysharp/M… |
| 2026-11-04 04:50:38 | [Simular.Sai](https://www.nuget.org/packages/Simular.Sai) | 0.1.0 | Simular | .NET SDK for the Sai API: delegate desktop work to Sai, or drive a cloud comput… |
| 2026-11-04 04:51:11 | [specht.tool](https://www.nuget.org/packages/specht.tool) | 0.4.2-preview | Rodney Littles, II | A dotnet tool that checks a repository's specification documents against a vers… |
| 2026-11-04 04:51:13 | [Specht.CodeAnalysis](https://www.nuget.org/packages/Specht.CodeAnalysis) | 0.4.2-preview | codeanalysis | Specht analyzer, code fixes and consumer build integration. |
| 2026-11-04 04:55:36 | [AJut.UX.Android](https://www.nuget.org/packages/AJut.UX.Android) | 2.0.0 | AJ Badarni | C# / dotnet 10 / Android Views controls & utility library, created by AJ Badarni |
| 2026-11-04 04:55:45 | [AJut.UX.AppKit](https://www.nuget.org/packages/AJut.UX.AppKit) | 2.0.0 | AJ Badarni | C# / dotnet 10 / AppKit (macOS) controls & utility library, created by AJ Badar… |
| 2026-11-04 04:55:55 | [AJut.UX.UIKit](https://www.nuget.org/packages/AJut.UX.UIKit) | 2.0.0 | AJ Badarni | C# / dotnet 10 / UIKit (iOS) controls & utility library, created by AJ Badarni |
| 2026-11-04 05:00:52 | [Sdcb.SimdCodecs.Heif](https://www.nuget.org/packages/Sdcb.SimdCodecs.Heif) | 1.4.0 | sdcb | Pure-managed HEIF / HEIC decoder for .NET: ISOBMFF container (ISO/IEC 14496-12)… |
| 2026-11-04 05:09:55 | [Beatd](https://www.nuget.org/packages/Beatd) | 0.0.1 | nuskey | beatd(a cross-platform audio analysis library) binding for .NET |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
