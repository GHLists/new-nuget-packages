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

## Latest list — 2026-10-16 09:20 UTC

New packages created between 2026-10-16 08:23 UTC and 2026-10-16 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T09-20-21-367596Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 08:23:39 | [ArtCraft.PhotoCraft](https://www.nuget.org/packages/ArtCraft.PhotoCraft) | 0.9.1 | Miroljub Tomic | Locates the PhotoCraft command-line tool (photocraft-cli) shipped by the ArtCra… |
| 2026-10-16 08:23:41 | [ArtCraft.PhotoCraft.Runtime.linux-arm64](https://www.nuget.org/packages/ArtCraft.PhotoCraft.Runtime.linux-arm64) | 0.9.1 | Miroljub Tomic | The PhotoCraft command-line tool (photocraft-cli) 0.9.0 for linux-arm64, unmodi… |
| 2026-10-16 08:23:43 | [ArtCraft.PhotoCraft.Runtime.linux-x64](https://www.nuget.org/packages/ArtCraft.PhotoCraft.Runtime.linux-x64) | 0.9.1 | Miroljub Tomic | The PhotoCraft command-line tool (photocraft-cli) 0.9.0 for linux-x64, unmodifi… |
| 2026-10-16 08:23:46 | [ArtCraft.PhotoCraft.Runtime.osx](https://www.nuget.org/packages/ArtCraft.PhotoCraft.Runtime.osx) | 0.9.1 | Miroljub Tomic | The PhotoCraft command-line tool (photocraft-cli) 0.9.0 for osx, unmodified fro… |
| 2026-10-16 08:23:48 | [ArtCraft.PhotoCraft.Runtime.win-arm64](https://www.nuget.org/packages/ArtCraft.PhotoCraft.Runtime.win-arm64) | 0.9.1 | Miroljub Tomic | The PhotoCraft command-line tool (photocraft-cli) 0.9.0 for win-arm64, unmodifi… |
| 2026-10-16 08:23:50 | [ArtCraft.PhotoCraft.Runtime.win-x64](https://www.nuget.org/packages/ArtCraft.PhotoCraft.Runtime.win-x64) | 0.9.1 | Miroljub Tomic | The PhotoCraft command-line tool (photocraft-cli) 0.9.0 for win-x64, unmodified… |
| 2026-10-16 08:23:52 | [ArtCraft.PhotoCraft.Runtime.win-x86](https://www.nuget.org/packages/ArtCraft.PhotoCraft.Runtime.win-x86) | 0.9.1 | Miroljub Tomic | The PhotoCraft command-line tool (photocraft-cli) 0.9.0 for win-x86, unmodified… |
| 2026-10-16 08:23:53 | [ArtCraft.PhotoCraft.Runtime](https://www.nuget.org/packages/ArtCraft.PhotoCraft.Runtime) | 0.9.1 | Miroljub Tomic | The PhotoCraft command-line tool (photocraft-cli) 0.9.0 for every supported pla… |
| 2026-10-16 08:25:07 | [ARXivar.ArxAI.Plugins](https://www.nuget.org/packages/ARXivar.ArxAI.Plugins) | 2.14.1 | ABLE TECH S.P.A. | ArxAI custom plugin SDK: skill/tool contract and execution context for the Arxi… |
| 2026-10-16 08:29:44 | [HeroKit.FileTypes](https://www.nuget.org/packages/HeroKit.FileTypes) | 3.3.0 | Emre Akdemir | Dependency-free file type detection for .NET: magic bytes for about 70 formats… |
| 2026-10-16 08:29:55 | [Uni.UaClient.Dashboard](https://www.nuget.org/packages/Uni.UaClient.Dashboard) | 1.0.1 | Converter Systems LLC, UPM | Embedded Swagger-like Web UI dashboard for OPC UA client browsing, drag-and-dro… |
| 2026-10-16 08:29:55 | [Uni.UaClient](https://www.nuget.org/packages/Uni.UaClient) | 1.0.1 | Andrew Cullen | A library to browse, read, write and subscribe to the live data published by th… |
| 2026-10-16 08:39:37 | [MuseDash.Mod.Sdk](https://www.nuget.org/packages/MuseDash.Mod.Sdk) | 2.0.0 | lxy | MSBuild SDK for Muse Dash mods. Locates the game, references MelonLoader and th… |
| 2026-10-16 08:40:08 | [Hosihikari.Abstractions](https://www.nuget.org/packages/Hosihikari.Abstractions) | 0.2.2 | HosihikariFramework | Plugin contract for the Hosihikari framework: IPlugin, IPluginContext, IPluginP… |
| 2026-10-16 08:56:24 | [ESRP.Release.NuGet.ESRPRelease-BVT.Prod.Build202095](https://www.nuget.org/packages/ESRP.Release.NuGet.ESRPRelease-BVT.Prod.Build202095) | 1.0.202095 | Microsoft | Disposable package used to validate NuGet publishing through ESRP Release. |
| 2026-10-16 08:59:14 | [ViVaKR.AuthLibrary](https://www.nuget.org/packages/ViVaKR.AuthLibrary) | 1.0.0 | ViVaKR | JWT authentication library |
| 2026-10-16 09:09:03 | [Webority.Insights.Admin](https://www.nuget.org/packages/Webority.Insights.Admin) | 0.7.0 | Webority Technologies | Insights pages for Webority admin portals: the AI review's proposals with their… |
| 2026-10-16 09:09:07 | [Webority.Insights.AspNetCore](https://www.nuget.org/packages/Webority.Insights.AspNetCore) | 0.7.0 | Webority Technologies | The in-product feedback API for Webority products: MapWeborityInsightsFeedbackE… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
