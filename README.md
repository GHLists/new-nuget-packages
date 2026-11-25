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

## Latest list — 2026-11-25 08:21 UTC

New packages created between 2026-11-25 07:19 UTC and 2026-11-25 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T08-21-53-701264Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 07:23:48 | [Win32BlazorWebViewAot](https://www.nuget.org/packages/Win32BlazorWebViewAot) | 1.0.0 | Yaser Aldubaisi | Host Blazor (Razor components) or plain HTML + JS in a native Win32 window — no… |
| 2026-11-25 07:28:24 | [FrameFlux.Capture](https://www.nuget.org/packages/FrameFlux.Capture) | 0.2.0 | FrameFlux | Local USB camera and capture device media engine for FrameFlux (Windows Media F… |
| 2026-11-25 07:57:02 | [Cornhsu.XamlA11y](https://www.nuget.org/packages/Cornhsu.XamlA11y) | 0.1.0 | 許彧銘 (Cornhsu) | XamlA11y — static accessibility audit for WPF XAML. Finds controls a screen rea… |
| 2026-11-25 07:57:08 | [Termin.Engine](https://www.nuget.org/packages/Termin.Engine) | 0.5.4 | Termin contributors | Full Termin C# scene and rendering runtime for Linux Vulkan and Windows D3D11. |
| 2026-11-25 08:06:10 | [Intropy.Telemetry.AspNetCore](https://www.nuget.org/packages/Intropy.Telemetry.AspNetCore) | 0.2.0 | Integrio | Simplified OpenTelemetry configuration for ASP.NET Core applications with pre-c… |
| 2026-11-25 08:06:10 | [Intropy.Telemetry.ConsoleApp](https://www.nuget.org/packages/Intropy.Telemetry.ConsoleApp) | 0.2.0 | Integrio | Simplified OpenTelemetry configuration for .NET console applications with pre-c… |
| 2026-11-25 08:08:16 | [Fuaran.Compute.GeometricAlgebra](https://www.nuget.org/packages/Fuaran.Compute.GeometricAlgebra) | 0.47.0 | Andrew J. Willshire | Fuaran.Compute.GeometricAlgebra — a pinned conformal geometric algebra, Cl(4,1)… |
| 2026-11-25 08:08:16 | [Fuaran.Compute.GeometricAlgebraOps](https://www.nuget.org/packages/Fuaran.Compute.GeometricAlgebraOps) | 0.47.0 | Andrew J. Willshire | Fuaran.Compute.GeometricAlgebraOps — geometric transforms as a parametric op al… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
