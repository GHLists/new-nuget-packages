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

## Latest list — 2026-10-26 15:21 UTC

New packages created between 2026-10-26 14:22 UTC and 2026-10-26 15:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T15-21-29-528081Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 14:33:06 | [Tesserae.Lauschwerk](https://www.nuget.org/packages/Tesserae.Lauschwerk) | 26.10.72871 | Curiosity GmbH | Tesserae.Lauschwerk is a Tesserae (Transpose C# to JavaScript) wrapper around t… |
| 2026-10-26 14:38:45 | [Hlibz.Redoc.Extensions.Core](https://www.nuget.org/packages/Hlibz.Redoc.Extensions.Core) | 2.0.0 | Hlib Zinchenko | The host-agnostic engine behind the Hlibz ReDoc extensions: a dark theme with a… |
| 2026-10-26 14:38:45 | [Hlibz.Redoc.Extensions.RedocAspNetCore](https://www.nuget.org/packages/Hlibz.Redoc.Extensions.RedocAspNetCore) | 2.0.0 | Hlib Zinchenko | Add-ons for Redoc.AspNetCore's ReDoc UI middleware: a drop-in dark theme with a… |
| 2026-10-26 14:38:46 | [Hlibz.Redoc.Extensions.Swashbuckle](https://www.nuget.org/packages/Hlibz.Redoc.Extensions.Swashbuckle) | 2.0.0 | Hlib Zinchenko | Add-ons for Swashbuckle.AspNetCore.ReDoc's ReDoc UI middleware: a drop-in dark… |
| 2026-10-26 14:38:47 | [Hlibz.Redoc.AspNetCore](https://www.nuget.org/packages/Hlibz.Redoc.AspNetCore) | 2.0.0 | Hlib Zinchenko | ReDoc 3 for ASP.NET Core: middleware and endpoint routing that serve an embedde… |
| 2026-10-26 14:45:53 | [VirtoCommerce.MFA.Core](https://www.nuget.org/packages/VirtoCommerce.MFA.Core) | 3.1000.0 | VirtoCommerce.MFA.Core | Package Description |
| 2026-10-26 14:45:55 | [VirtoCommerce.MFA.Data](https://www.nuget.org/packages/VirtoCommerce.MFA.Data) | 3.1000.0 | VirtoCommerce.MFA.Data | Package Description |
| 2026-10-26 14:51:37 | [Tedd.SQLite3.Native](https://www.nuget.org/packages/Tedd.SQLite3.Native) | 0.1.15-preview | Tedd | NativeAOT C ABI builds of the C# SQLite engine. Preview compatibility; see READ… |
| 2026-10-26 14:51:37 | [Tedd.SQLite3](https://www.nuget.org/packages/Tedd.SQLite3) | 0.1.17-preview | Tedd | SQLite 3 engine implemented in C# for .NET 10. Preview SQL, storage and C ABI c… |
| 2026-10-26 14:57:54 | [Pipoburgos.SharedKernel.Infrastructure.EntityFrameworkCore.Identity](https://www.nuget.org/packages/Pipoburgos.SharedKernel.Infrastructure.EntityFrameworkCore.Identity) | 10.0.14 | Roberto Fernández Salinas | OpenIddict infrastructure implementations |
| 2026-10-26 15:03:29 | [Amazon.CDK.LambdaLayer.KubectlV37](https://www.nuget.org/packages/Amazon.CDK.LambdaLayer.KubectlV37) | 2.0.0 | Amazon Web Services | A Lambda Layer that contains kubectl v1.37 (Stability: Experimental) |
| 2026-10-26 15:12:13 | [Smaoin.Shared.Imaging](https://www.nuget.org/packages/Smaoin.Shared.Imaging) | 1.0.94 | Smaoin Ltd | Image resizing with auto-orient, EXIF strip, and JPEG + WebP output for ASP.NET… |
| 2026-10-26 15:12:15 | [Smaoin.Shared.QrCode](https://www.nuget.org/packages/Smaoin.Shared.QrCode) | 1.0.94 | Smaoin Ltd | SVG QR code generation for ASP.NET Core. |
| 2026-10-26 15:12:16 | [Smaoin.Shared.SafeBrowsing](https://www.nuget.org/packages/Smaoin.Shared.SafeBrowsing) | 1.0.94 | Smaoin Ltd | Google Safe Browsing API client for ASP.NET Core. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
