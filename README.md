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

## Latest list — 2026-10-09 03:19 UTC

New packages created between 2026-10-09 02:19 UTC and 2026-10-09 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T03-19-03-509844Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 02:22:54 | [FreeDotnetImageSharp](https://www.nuget.org/packages/FreeDotnetImageSharp) | 2.1.14 | Six Labors and contributors,… | Community-maintained, Apache-2.0 licensed fork of SixLabors.ImageSharp 2.1.13 w… |
| 2026-10-09 02:40:38 | [DSLToolsGen](https://www.nuget.org/packages/DSLToolsGen) | 1.0.0 | Ghost4Man | Tool that generates editor support and an AST definition (as C# code) for a DSL… |
| 2026-10-09 02:41:25 | [WolfAuth](https://www.nuget.org/packages/WolfAuth) | 1.0.0 | Elysium Coding | Core authentication subject contracts, claims mapping, and in-memory support fo… |
| 2026-10-09 02:41:26 | [WolfAuth.AspNetCore](https://www.nuget.org/packages/WolfAuth.AspNetCore) | 1.0.0 | Elysium Coding | ASP.NET Core authentication subject binding, current-subject access, and middle… |
| 2026-10-09 02:41:28 | [WolfAuth.Microsoft.EntraId](https://www.nuget.org/packages/WolfAuth.Microsoft.EntraId) | 1.0.0 | Elysium Coding | Microsoft Entra ID claims and group mapping adapter for WolfAuth authentication… |
| 2026-10-09 02:41:29 | [WolfAuth.OpenIdConnect](https://www.nuget.org/packages/WolfAuth.OpenIdConnect) | 1.0.0 | Elysium Coding | OpenID Connect claims-to-subject provisioning mapper for WolfAuth authenticatio… |
| 2026-10-09 02:49:46 | [Foxit.PDFConversionSDK.Dotnet.Linux64](https://www.nuget.org/packages/Foxit.PDFConversionSDK.Dotnet.Linux64) | 4.0.0 | Foxit Software Incorporated | Foxit PDF Conversion SDK managed and native libraries for .NET Core on Linux x6… |
| 2026-10-09 02:50:05 | [FreeDotnetPOI](https://www.nuget.org/packages/FreeDotnetPOI) | 2.7.7 | Tony Qu,NPOI Contributors,Fre… | Community-maintained, Apache-2.0 licensed fork of NPOI 2.7.6 (.NET port of Apac… |
| 2026-10-09 02:50:59 | [Thunderduck.Data](https://www.nuget.org/packages/Thunderduck.Data) | 0.1.0 | thunderduck | ADO.NET provider and async client for thunderduck (Dapper-compatible). |
| 2026-10-09 02:56:46 | [Foxit.PDFConversionSDK.Dotnet.LinuxArm](https://www.nuget.org/packages/Foxit.PDFConversionSDK.Dotnet.LinuxArm) | 4.0.0 | Foxit Software Incorporated | Foxit PDF Conversion SDK managed and native libraries for .NET Core on Linux AR… |
| 2026-10-09 02:58:00 | [CustomWin.Utils](https://www.nuget.org/packages/CustomWin.Utils) | 3.0.0 | 鱼塘泛舟、404 | CustomWin.Utils 是一个 C# WinForms 控件与工具库，聚合 Core / Drawing / Interop / WinForms 四… |
| 2026-10-09 03:05:45 | [Foxit.PDFConversionSDK.Dotnet.Windows](https://www.nuget.org/packages/Foxit.PDFConversionSDK.Dotnet.Windows) | 4.0.0 | Foxit Software Incorporated | Foxit PDF Conversion SDK managed and native libraries for .NET Core on Windows… |
| 2026-10-09 03:07:59 | [Nooks](https://www.nuget.org/packages/Nooks) | 0.0.1 | Nooks | lib |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
