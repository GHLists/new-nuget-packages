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

## Latest list — 2026-10-10 21:20 UTC

New packages created between 2026-10-10 20:21 UTC and 2026-10-10 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T21-20-33-94214Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 20:24:56 | [AppShell.Core](https://www.nuget.org/packages/AppShell.Core) | 0.2.0 | MrMontana1889 | UI-agnostic application-shell contracts and infrastructure. |
| 2026-10-10 20:25:06 | [AppShell.Wpf](https://www.nuget.org/packages/AppShell.Wpf) | 0.2.0 | MrMontana1889 | WPF projections and integrations for the application-shell infrastructure. |
| 2026-10-10 20:28:38 | [Dfx-lite](https://www.nuget.org/packages/Dfx-lite) | 1.0.8 | Atılım Güneş Baydin, Don Syme… | Dfx is a tensor library with support for differentiable programming. It is desi… |
| 2026-10-10 20:28:38 | [dfx-lite](https://www.nuget.org/packages/dfx-lite) | 1.0.8 | Atılım Güneş Baydin, Don Syme… | Dfx is a tensor library with support for differentiable programming. It is desi… |
| 2026-10-10 20:28:39 | [Dfx-cpu](https://www.nuget.org/packages/Dfx-cpu) | 1.0.8 | Atılım Güneş Baydin, Don Syme… | Dfx is a tensor library with support for differentiable programming. It is desi… |
| 2026-10-10 20:28:39 | [dfx-cpu](https://www.nuget.org/packages/dfx-cpu) | 1.0.8 | Atılım Güneş Baydin, Don Syme… | Dfx is a tensor library with support for differentiable programming. It is desi… |
| 2026-10-10 20:29:43 | [Dfx-cuda-windows](https://www.nuget.org/packages/Dfx-cuda-windows) | 1.0.8 | Atılım Güneş Baydin, Don Syme… | Dfx is a tensor library with support for differentiable programming. It is desi… |
| 2026-10-10 20:29:43 | [dfx-cuda-windows](https://www.nuget.org/packages/dfx-cuda-windows) | 1.0.8 | Atılım Güneş Baydin, Don Syme… | Dfx is a tensor library with support for differentiable programming. It is desi… |
| 2026-10-10 20:29:45 | [Dfx-cuda-linux](https://www.nuget.org/packages/Dfx-cuda-linux) | 1.0.8 | Atılım Güneş Baydin, Don Syme… | Dfx is a tensor library with support for differentiable programming. It is desi… |
| 2026-10-10 20:29:45 | [dfx-cuda-linux](https://www.nuget.org/packages/dfx-cuda-linux) | 1.0.8 | Atılım Güneş Baydin, Don Syme… | Dfx is a tensor library with support for differentiable programming. It is desi… |
| 2026-10-10 20:30:41 | [Dfx-cuda](https://www.nuget.org/packages/Dfx-cuda) | 1.0.8 | Atılım Güneş Baydin, Don Syme… | Dfx is a tensor library with support for differentiable programming. It is desi… |
| 2026-10-10 20:30:41 | [dfx-cuda](https://www.nuget.org/packages/dfx-cuda) | 1.0.8 | Atılım Güneş Baydin, Don Syme… | Dfx is a tensor library with support for differentiable programming. It is desi… |
| 2026-10-10 20:53:00 | [YonatanMankovich.WhatsOnLan.Core](https://www.nuget.org/packages/YonatanMankovich.WhatsOnLan.Core) | 1.1.0 | Yonatan Mankovich | A scanner library to find basic networking information about devices on the loc… |
| 2026-10-10 20:54:20 | [Soenneker.JavaScript.Minifier](https://www.nuget.org/packages/Soenneker.JavaScript.Minifier) | 4.0.2 | Jake Soenneker | A utility for minifying JavaScript |
| 2026-10-10 20:58:55 | [CropAndWebP.TagHelper](https://www.nuget.org/packages/CropAndWebP.TagHelper) | 1.0.0 | DraganS | Crop JPG, JPEG, PNG, and GIF images and automatically convert them to WebP. Sup… |
| 2026-10-10 21:04:13 | [InPoint.Cloud.OpenBarcode](https://www.nuget.org/packages/InPoint.Cloud.OpenBarcode) | 0.1.0 | InPoint.Cloud | Pure managed .NET barcode reader for images (PNG, JPEG, BMP, GIF, TIFF, ...) an… |
| 2026-10-10 21:04:47 | [Somepoi.Atlyss.GameLibs](https://www.nuget.org/packages/Somepoi.Atlyss.GameLibs) | 0.21474249.0 | somepoi | All stripped ATLYSS managed game, Unity and third-party compile references from… |
| 2026-10-10 21:11:23 | [KetPsi.Endpoints.Http.Abstractions](https://www.nuget.org/packages/KetPsi.Endpoints.Http.Abstractions) | 1.1.0 | KetPsi ,MohamadArsalan Imamve… | Abstraction for the HTTP endpoint configuration in ASP.NET Core Minimal APIs. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
