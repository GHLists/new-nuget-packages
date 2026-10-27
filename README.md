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

## Latest list — 2026-10-27 10:20 UTC

New packages created between 2026-10-27 09:20 UTC and 2026-10-27 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T10-20-54-743379Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 09:30:03 | [Pycom.RAG.Platform](https://www.nuget.org/packages/Pycom.RAG.Platform) | 0.1.0 | Pycom | Strongly typed client for the Pycom Knowledge Platform query API. |
| 2026-10-27 09:31:01 | [CefSharp.Avalonia.Linux](https://www.nuget.org/packages/CefSharp.Avalonia.Linux) | 1.2.6 | CefBrowser | Linux (x64) native binaries (CEF runtime + CefBrowser.Native host) for CefSharp… |
| 2026-10-27 09:38:29 | [CounterStrikeSharpDBLib](https://www.nuget.org/packages/CounterStrikeSharpDBLib) | 0.0.1 | Lukseh | API for sharing database connections between CounterStrikeSharp plugins. |
| 2026-10-27 09:49:20 | [DEM.Blazor3D](https://www.nuget.org/packages/DEM.Blazor3D) | 2.0.0 | HOMAG-Group | This Razor class library (RCL) contains the Blazor component which allows you c… |
| 2026-10-27 09:49:33 | [GitLabSearch.Cli](https://www.nuget.org/packages/GitLabSearch.Cli) | 2.0.1 | GitLabSearch | Search code across GitLab group repositories. |
| 2026-10-27 09:51:20 | [Fitko.FitConnect.Core](https://www.nuget.org/packages/Fitko.FitConnect.Core) | 4.0.0 | Fitko | Reusable building blocks for the FIT-Connect .NET SDK: JWE/AES-GCM crypto, SHA-… |
| 2026-10-27 09:51:23 | [Fitko.FitConnect.VirusScanning](https://www.nuget.org/packages/Fitko.FitConnect.VirusScanning) | 4.0.0 | Fitko | Optional malware-scanning module for the FIT-Connect .NET SDK. Scans streams an… |
| 2026-10-27 09:51:35 | [Fitko.FitConnect.Client](https://www.nuget.org/packages/Fitko.FitConnect.Client) | 4.0.0 | Fitko | High-level .NET client for the FIT-Connect platform: sending submissions and re… |
| 2026-10-27 09:51:37 | [Fitko.FitConnect.Zbp](https://www.nuget.org/packages/Fitko.FitConnect.Zbp) | 4.0.0 | Fitko | ZBP module for the FIT-Connect .NET SDK. Client for sending messages and status… |
| 2026-10-27 09:51:39 | [Fitko.FitConnect.Postfach](https://www.nuget.org/packages/Fitko.FitConnect.Postfach) | 4.0.0 | Fitko | Postfach module for the FIT-Connect .NET SDK. Provides the ELSTER-Transfer Post… |
| 2026-10-27 10:04:29 | [ipsis.Licensing](https://www.nuget.org/packages/ipsis.Licensing) | 2.1.0 | ipsis | The licence check used by ipsis products for Umbraco: verifying a signed licenc… |
| 2026-10-27 10:04:43 | [Aivie.Content](https://www.nuget.org/packages/Aivie.Content) | 17.0.0 | ipsis | From keyword to published page, without leaving Umbraco. Aivie researches keywo… |
| 2026-10-27 10:08:16 | [GianFossi.Geometry](https://www.nuget.org/packages/GianFossi.Geometry) | 2.0.0 | GianFossi | An F# geometry library for 2D and 3D geometric primitives and operations, inclu… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
