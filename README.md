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

## Latest list — 2026-09-28 19:21 UTC

New packages created between 2026-09-28 18:22 UTC and 2026-09-28 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T19-21-16-031354Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 18:25:52 | [Kevlar.Extensions.Diagnostics.HealthChecks](https://www.nuget.org/packages/Kevlar.Extensions.Diagnostics.HealthChecks) | 1.2.0 | Tom Longhurst | Health checks for registered Kevlar shields, circuit breaker monitors, and part… |
| 2026-09-28 18:25:53 | [Kevlar.Extensions.EntityFrameworkCore](https://www.nuget.org/packages/Kevlar.Extensions.EntityFrameworkCore) | 1.2.0 | Tom Longhurst | Sequential Kevlar execution strategies for Entity Framework Core. |
| 2026-09-28 18:25:57 | [Kevlar.Extensions.Tracing](https://www.nuget.org/packages/Kevlar.Extensions.Tracing) | 1.2.0 | Tom Longhurst | Opt-in enrichment of application activities with Kevlar telemetry events. |
| 2026-09-28 18:27:48 | [ESRP.Release.NuGet.ESRPRelease-BVT.Prod.Build196784](https://www.nuget.org/packages/ESRP.Release.NuGet.ESRPRelease-BVT.Prod.Build196784) | 1.0.196784 | Microsoft | Disposable package used to validate NuGet publishing through ESRP Release. |
| 2026-09-28 18:28:23 | [FFmpeg.Interop](https://www.nuget.org/packages/FFmpeg.Interop) | 0.1.0-dev1 | Agash | .NET bindings for FFmpeg 9: a managed API for encoding, decoding, hardware acce… |
| 2026-09-28 18:29:39 | [RoushTech.Asio.S3](https://www.nuget.org/packages/RoushTech.Asio.S3) | 0.5.0 | William Roush | S3-compatible archive for completed RoushTech.Asio sessions via the Minio clien… |
| 2026-09-28 18:33:37 | [AwadyLab.HttpKit](https://www.nuget.org/packages/AwadyLab.HttpKit) | 1.0.0 | Mohamed Elawady | Typed HttpClient framework for .NET: source-generated registration, Polly v8 re… |
| 2026-09-28 18:33:39 | [AwadyLab.HttpKit.AspNetCore](https://www.nuget.org/packages/AwadyLab.HttpKit.AspNetCore) | 1.0.0 | Mohamed Elawady | ASP.NET Core integration for AwadyLab.HttpKit: header propagation bridge, HttpC… |
| 2026-09-28 18:33:43 | [AwadyLab.HttpKit.Testing](https://www.nuget.org/packages/AwadyLab.HttpKit.Testing) | 1.0.0 | Mohamed Elawady | Testing support for AwadyLab.HttpKit: test doubles, mock handlers from .json/.h… |
| 2026-09-28 18:40:05 | [Soenneker.TikTok.HttpClients](https://www.nuget.org/packages/Soenneker.TikTok.HttpClients) | 4.0.1 | Jake Soenneker | A thread-safe singleton HttpClient for TikTok's OpenAPI integration. |
| 2026-09-28 18:42:04 | [Soenneker.TikTok.OpenApiClient](https://www.nuget.org/packages/Soenneker.TikTok.OpenApiClient) | 4.0.1 | Jake Soenneker | A generated OpenAPI client for TikTok developer APIs. |
| 2026-09-28 18:59:24 | [Tauri.Plugin.DotNet](https://www.nuget.org/packages/Tauri.Plugin.DotNet) | 0.1.1 | George Samartzidis | Typed RPC bridge between a Tauri frontend and .NET services, with auto-generate… |
| 2026-09-28 19:04:22 | [EraTech.Shared.Hosting.Authentication](https://www.nuget.org/packages/EraTech.Shared.Hosting.Authentication) | 2.2.24 | EraTech | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
