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

## Latest list — 2026-11-10 17:20 UTC

New packages created between 2026-11-10 16:20 UTC and 2026-11-10 17:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T17-20-40-190545Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 16:24:55 | [PosInformatique.Foundations.Linq.Expressions](https://www.nuget.org/packages/PosInformatique.Foundations.Linq.Expressions) | 1.5.0 | Gilles TOURREAU | Provides expression tree utilities, including OrExpressionBuilder<T> to combine… |
| 2026-11-10 16:35:55 | [Aiursoft.PipelineWatchDog](https://www.nuget.org/packages/Aiursoft.PipelineWatchDog) | 10.0.0 | Aiursoft | Monitors GitLab pipelines and stalled dependency updates through AlertCenter. |
| 2026-11-10 16:36:03 | [Aiursoft.LogWatchDog](https://www.nuget.org/packages/Aiursoft.LogWatchDog) | 10.0.0 | Aiursoft | Monitors HTTP request errors and abnormal traffic through AlertCenter. |
| 2026-11-10 16:38:55 | [Rylogic.Audio.Authoring](https://www.nuget.org/packages/Rylogic.Audio.Authoring) | 2.3.1 | Rylogic | Non-destructive game audio preparation: sources, variants, processing recipes,… |
| 2026-11-10 16:52:12 | [Cosmos.Types.TributosDeAutoridad](https://www.nuget.org/packages/Cosmos.Types.TributosDeAutoridad) | 1.0.0 | Cosmos | Value Object TributoDeAutoridad para el ERP Cosmos: el tributo tal como lo nomb… |
| 2026-11-10 16:54:52 | [UnionNarrowing](https://www.nuget.org/packages/UnionNarrowing) | 0.2.0 | Ian Wold | Narrowing for C# 15 unions (discriminated unions) and closed hierarchies: suppr… |
| 2026-11-10 17:00:05 | [FastHg-Android](https://www.nuget.org/packages/FastHg-Android) | 0.40.0 | FastHg | Native Mercurial (hg) client for Android: libfasthg.so per ABI for .NET Android… |
| 2026-11-10 17:07:10 | [Uno.WinUI.Composition.Skia](https://www.nuget.org/packages/Uno.WinUI.Composition.Skia) | 7.0.32 | Uno Platform | The SkiaSharp drawing backend for Uno Platform. Referenced by the 'Skia' UnoFea… |
| 2026-11-10 17:07:42 | [Uno.WinUI.Graphics3DWebGpu](https://www.nuget.org/packages/Uno.WinUI.Graphics3DWebGpu) | 7.0.32 | Uno Platform | WebGpuCanvasElement: draw with your own WebGPU commands inside an Uno Platform… |
| 2026-11-10 17:07:46 | [Uno.WinUI.MediaPlayer.Win32](https://www.nuget.org/packages/Uno.WinUI.MediaPlayer.Win32) | 7.0.32 | Uno Platform | This package provides support for MediaPlayerElement for Uno Platform Win32 apps |
| 2026-11-10 17:07:47 | [Uno.WinUI.MediaPlayer.X11](https://www.nuget.org/packages/Uno.WinUI.MediaPlayer.X11) | 7.0.32 | Uno Platform | This package provides support for MediaPlayerElement for Uno Platform X11 apps |
| 2026-11-10 17:07:50 | [Uno.WinUI.Runtime.Android](https://www.nuget.org/packages/Uno.WinUI.Runtime.Android) | 7.0.32 | Uno Platform | This package provides the Android host for Uno Platform projects. |
| 2026-11-10 17:07:51 | [Uno.WinUI.Runtime.AppleUIKit](https://www.nuget.org/packages/Uno.WinUI.Runtime.AppleUIKit) | 7.0.32 | Uno Platform | This package provides the iOS and tvOS host for Uno Platform projects. |
| 2026-11-10 17:07:57 | [Uno.WinUI.Runtime.WebAssembly.Browser](https://www.nuget.org/packages/Uno.WinUI.Runtime.WebAssembly.Browser) | 7.0.32 | Uno Platform | This package provides the WebAssembly browser host for Uno Platform projects. |
| 2026-11-10 17:08:00 | [Uno.WinUI.Runtime.X11](https://www.nuget.org/packages/Uno.WinUI.Runtime.X11) | 7.0.32 | Uno Platform | This package provides the X11 host for Uno Platform projects. |
| 2026-11-10 17:08:01 | [Lokad.Bash](https://www.nuget.org/packages/Lokad.Bash) | 0.1.0 | Lokad | Embeddable non-interactive Bash interpreter for .NET with application-controlle… |
| 2026-11-10 17:08:05 | [Uno.WinUI.WebView.X11](https://www.nuget.org/packages/Uno.WinUI.WebView.X11) | 7.0.32 | Uno Platform | This package provides support for WebView for Uno Platform X11 apps |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
