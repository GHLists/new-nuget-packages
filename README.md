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

## Latest list — 2026-11-25 20:22 UTC

New packages created between 2026-11-25 19:20 UTC and 2026-11-25 20:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T20-22-17-612381Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 19:43:40 | [DiasparkGenPackageLiveV10](https://www.nuget.org/packages/DiasparkGenPackageLiveV10) | 10.0.1 | Sourabh Tokkar / Divyanshi | 11252026 Sourabh/Divyanshi : Created new .Net V10 Genpackage with latest Genser… |
| 2026-11-25 19:49:49 | [AWSSDK.ELBProxy](https://www.nuget.org/packages/AWSSDK.ELBProxy) | 4.1.0 | Amazon Web Services | The Amazon Web Services SDK for .NET - Elastic Load Balancing for Envoy |
| 2026-11-25 20:01:57 | [bogzxo.Horizon.Shaders.Build](https://www.nuget.org/packages/bogzxo.Horizon.Shaders.Build) | 1.5.1 | bogzxo | Makes a Horizon shader pack out of a manifest, for a platform with no Slang to… |
| 2026-11-25 20:01:58 | [bogzxo.Horizon.Platform.Android](https://www.nuget.org/packages/bogzxo.Horizon.Platform.Android) | 1.5.1 | bogzxo | The Horizon engine on Android: the SurfaceView's window for Vulkan, the APK's a… |
| 2026-11-25 20:01:59 | [bogzxo.Horizon.Platform.iOS](https://www.nuget.org/packages/bogzxo.Horizon.Platform.iOS) | 1.5.1 | bogzxo | The Horizon engine on iOS: the Metal view for Vulkan over MoltenVK, touch, keyb… |
| 2026-11-25 20:02:01 | [bogzxo.Horizon.Terminal](https://www.nuget.org/packages/bogzxo.Horizon.Terminal) | 1.5.1 | bogzxo | The Horizon engine's terminal: the VT parser, the screen, the views and panes,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
