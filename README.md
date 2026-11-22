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

## Latest list — 2026-11-22 07:18 UTC

New packages created between 2026-11-22 06:21 UTC and 2026-11-22 07:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T07-18-46-970391Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 07:02:45 | [Chaldea.HarfBuzzSharp.NativeAssets.HarmonyOS](https://www.nuget.org/packages/Chaldea.HarfBuzzSharp.NativeAssets.HarmonyOS) | 11.0.0 | OpenHarmony.NET | HarmonyOS API15+ x86_64 and arm64 native assets for HarfBuzzSharp 14.4.0.200. |
| 2026-11-22 07:02:47 | [Chaldea.OpenHarmony.Framework](https://www.nuget.org/packages/Chaldea.OpenHarmony.Framework) | 11.0.0 | OpenHarmony.Framework | C# platform APIs and reusable SurfaceView host for OpenHarmony API 15+. |
| 2026-11-22 07:02:49 | [Chaldea.OpenHarmony.HapTooling](https://www.nuget.org/packages/Chaldea.OpenHarmony.HapTooling) | 11.0.0 | OpenHarmony.NET | Provider-owned HAP/APP packaging tooling for the XEngine HarmonyOS build pipeli… |
| 2026-11-22 07:02:50 | [Chaldea.OpenHarmony.NDK.Bindings](https://www.nuget.org/packages/Chaldea.OpenHarmony.NDK.Bindings) | 11.0.0 | OpenHarmony.NET | OpenHarmony Native SDK bindings for .NET 11. |
| 2026-11-22 07:02:51 | [Chaldea.OpenHarmony.Player.Sdk](https://www.nuget.org/packages/Chaldea.OpenHarmony.Player.Sdk) | 11.0.0 | OpenHarmony.NET | MSBuild SDK for OpenHarmony NativeAOT shared libraries. |
| 2026-11-22 07:02:53 | [Chaldea.OpenHarmony.PublishAotCross](https://www.nuget.org/packages/Chaldea.OpenHarmony.PublishAotCross) | 11.0.0 | OpenHarmony.NET, xljiulang, M… | MSBuild targets to aid in crosscompiling Native AOT publishing. |
| 2026-11-22 07:02:56 | [Chaldea.OpenHarmony.Runtime.NativeAot.arm64-v8a](https://www.nuget.org/packages/Chaldea.OpenHarmony.Runtime.NativeAot.arm64-v8a) | 11.0.0 | OpenHarmony.NET | OpenHarmony .NET 11 NativeAOT API13 baseline runtime for arm64-v8a. |
| 2026-11-22 07:02:59 | [Chaldea.OpenHarmony.Runtime.NativeAot.x86_64](https://www.nuget.org/packages/Chaldea.OpenHarmony.Runtime.NativeAot.x86_64) | 11.0.0 | OpenHarmony.NET | OpenHarmony .NET 11 NativeAOT API13 baseline runtime for x86_64. |
| 2026-11-22 07:03:01 | [Chaldea.OpenHarmony.Sdk](https://www.nuget.org/packages/Chaldea.OpenHarmony.Sdk) | 11.0.0 | OpenHarmony.NET | OpenHarmony .NET 11 workload SDK, NativeAOT application and HAP tooling. |
| 2026-11-22 07:03:02 | [Chaldea.OpenHarmony.Templates](https://www.nuget.org/packages/Chaldea.OpenHarmony.Templates) | 11.0.0 | OpenHarmony.NET | dotnet new ohos application template. |
| 2026-11-22 07:03:05 | [Chaldea.SkiaSharp.NativeAssets.HarmonyOS](https://www.nuget.org/packages/Chaldea.SkiaSharp.NativeAssets.HarmonyOS) | 11.0.0 | OpenHarmony.NET | HarmonyOS API15+ x86_64 and arm64 native assets for SkiaSharp 4.157.0. |
| 2026-11-22 07:03:06 | [Chaldea.OpenHarmony.Workload.Manifest-11.0.100](https://www.nuget.org/packages/Chaldea.OpenHarmony.Workload.Manifest-11.0.100) | 11.0.0 | OpenHarmony.NET | Workload manifest for the harmonyos .NET 11 workload. |
| 2026-11-22 07:03:08 | [Chaldea.OpenHarmony.Workload](https://www.nuget.org/packages/Chaldea.OpenHarmony.Workload) | 11.0.0 | Chaldea,OpenHarmony.NET contr… | Registers the harmonyos workload for a standalone .NET SDK. No PowerShell scrip… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
