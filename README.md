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

## Latest list — 2026-11-18 22:21 UTC

New packages created between 2026-11-18 21:20 UTC and 2026-11-18 22:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T22-21-55-704093Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 21:23:31 | [BellaBaxter.Cli](https://www.nuget.org/packages/BellaBaxter.Cli) | 0.1.2 | bella | Package Description |
| 2026-11-18 21:32:18 | [EconomyApi.Extensions.DependencyInjection](https://www.nuget.org/packages/EconomyApi.Extensions.DependencyInjection) | 1.3.1 | Sveinung,ThomasP | IHttpClientFactory / dependency injection registration for the EconomyApi V2 cl… |
| 2026-11-18 21:37:03 | [FControls3d](https://www.nuget.org/packages/FControls3d) | 1.0.0 | Fabio Gordiano | Custom 3D hardware-style controls for Windows Forms (Slider3d, V-Meters, LCD di… |
| 2026-11-18 21:48:13 | [Shorthand.UmbracoHelpers](https://www.nuget.org/packages/Shorthand.UmbracoHelpers) | 18.0.0 | Karl-Johan Sjögren | Provides helpers for Umbraco development. |
| 2026-11-18 21:49:14 | [Stet](https://www.nuget.org/packages/Stet) | 0.0.1 | rthomasv3 | A spelling and grammar checker built for fiction. Offline, pure managed C#, no… |
| 2026-11-18 21:53:38 | [Heroicsoft.NetForge.WebAssets](https://www.nuget.org/packages/Heroicsoft.NetForge.WebAssets) | 1.2.6 | Matt Gordon | Serves a library's wwwroot from the assembly at the usual _content path, for ho… |
| 2026-11-18 22:01:53 | [ITHit.FileSystem.IOS](https://www.nuget.org/packages/ITHit.FileSystem.IOS) | 9.2.29685 | IT Hit, Ltd | IT Hit User File System Engine for iOS provides a high-level API for creating a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
