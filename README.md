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

## Latest list — 2026-10-13 17:19 UTC

New packages created between 2026-10-13 16:21 UTC and 2026-10-13 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T17-19-38-235691Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 16:28:05 | [VideoLAN.LibVLC.Mac.GPL](https://www.nuget.org/packages/VideoLAN.LibVLC.Mac.GPL) | 3.1.3.2 | VideoLAN | LibVLC is a modular multimedia framework that can render video and output audio… |
| 2026-10-13 16:28:05 | [Metalama.Extensions.Interceptors](https://www.nuget.org/packages/Metalama.Extensions.Interceptors) | 2027.0.4-preview | PostSharp Technologies | An extension to Metalama.Framework that lets aspects and fabrics intercept the… |
| 2026-10-13 16:28:06 | [Metalama.Extensions.Interceptors.Redist](https://www.nuget.org/packages/Metalama.Extensions.Interceptors.Redist) | 2027.0.4-preview | PostSharp Technologies | The redistributable package for Metalama.Extensions.Interceptors, which does no… |
| 2026-10-13 16:30:58 | [EggSharp.Storage](https://www.nuget.org/packages/EggSharp.Storage) | 13.0.0 | DavidArthurCole | Byte-level storage envelope with gzip, brotli and dictionary zstd. |
| 2026-10-13 16:31:08 | [HandyUI.Controls](https://www.nuget.org/packages/HandyUI.Controls) | 2.1.0 | davpnuser | Platform-agnostic-at-its-core code-only C# UI framework powered by SkiaSharp. |
| 2026-10-13 16:32:58 | [SjolystInnovation.AppKit.Hosting](https://www.nuget.org/packages/SjolystInnovation.AppKit.Hosting) | 0.1.0 | Sjølyst Innovation AS | Forwarded headers from trusted proxies only, per-IP rate limiting, security hea… |
| 2026-10-13 16:47:50 | [Vortex.Rimworld.Ref](https://www.nuget.org/packages/Vortex.Rimworld.Ref) | 1.7.4977 | Vortex | RimWorld 1.7 reference assemblies. Compile mods without referencing the game. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
