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

## Latest list — 2026-11-18 09:21 UTC

New packages created between 2026-11-18 08:22 UTC and 2026-11-18 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T09-21-05-702521Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 08:46:28 | [PageRush](https://www.nuget.org/packages/PageRush) | 0.1.0 | Arsi Consultancy | .NET client for the PageRush API: store Typst templates, render them with JSON… |
| 2026-11-18 08:52:07 | [gzSimulation](https://www.nuget.org/packages/gzSimulation) | 2.12.351.1 | Anders Modén @ (Saab AB) | This is the native C++ API for simulation utilities in GizmoSDK |
| 2026-11-18 08:52:13 | [gzDynamics](https://www.nuget.org/packages/gzDynamics) | 2.12.351.1 | Anders Modén @ (Saab AB) | This is the native C++ API for dynamic simulation in GizmoSDK |
| 2026-11-18 08:52:18 | [gzGroundClamp](https://www.nuget.org/packages/gzGroundClamp) | 2.12.351.1 | Anders Modén @ (Saab AB) | This is the native C++ API for map groundclamps in GizmoSDK |
| 2026-11-18 08:52:24 | [gzKML](https://www.nuget.org/packages/gzKML) | 2.12.351.1 | Anders Modén @ (Saab AB) | This is the native C++ API for KML reading in GizmoSDK |
| 2026-11-18 08:52:30 | [gzTest](https://www.nuget.org/packages/gzTest) | 2.12.351.1 | Anders Modén @ (Saab AB) | This is the native C++ API for test methods in GizmoSDK |
| 2026-11-18 08:53:52 | [Ranvier.Keyboard.Dom](https://www.nuget.org/packages/Ranvier.Keyboard.Dom) | 0.1.0 | shayanhabibi | Native .NET DOM adapter bridging Ranvier.Dom.KeyboardEvent to Ranvier.Keyboard… |
| 2026-11-18 08:53:52 | [Fable.Ranvier.Keyboard.Dom](https://www.nuget.org/packages/Fable.Ranvier.Keyboard.Dom) | 0.1.0 | shayanhabibi | Fable (fickl) browser DOM adapter bridging Ranvier.Dom.KeyboardEvent (from Fabl… |
| 2026-11-18 08:53:53 | [Ranvier.Keyboard.Traced](https://www.nuget.org/packages/Ranvier.Keyboard.Traced) | 0.1.0 | shayanhabibi | The traced build of Ranvier.Keyboard: DOM-free keyboard primitives, SIMD W3C/IS… |
| 2026-11-18 08:53:53 | [Fable.Ranvier.Keyboard.Dom.Traced](https://www.nuget.org/packages/Fable.Ranvier.Keyboard.Dom.Traced) | 0.1.0 | shayanhabibi | The traced build of Fable.Ranvier.Keyboard.Dom: Fable browser Ranvier.Dom.Keybo… |
| 2026-11-18 08:53:54 | [Ranvier.Keyboard.Dom.Traced](https://www.nuget.org/packages/Ranvier.Keyboard.Dom.Traced) | 0.1.0 | shayanhabibi | The traced build of Ranvier.Keyboard.Dom: native .NET Ranvier.Dom.KeyboardEvent… |
| 2026-11-18 08:53:55 | [Ranvier.Keyboard](https://www.nuget.org/packages/Ranvier.Keyboard) | 0.1.0 | shayanhabibi | DOM-free keyboard primitives for .NET and Fable (fickl): W3C KeyboardEvent.code… |
| 2026-11-18 09:04:34 | [Nocturne.Wpf](https://www.nuget.org/packages/Nocturne.Wpf) | 0.1.2 | Martin Kirk | Nocturne: a dark theme for WPF on .NET 8+. Windows 11 Acrylic, Mica or Mica Alt… |
| 2026-11-18 09:05:51 | [Matchsalud](https://www.nuget.org/packages/Matchsalud) | 1.0.0 | Match con tu salud — PrEP and… | Match con tu salud PrEP and HIV counseling El Salvador constants. Official: htt… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
