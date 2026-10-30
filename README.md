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

## Latest list — 2026-10-30 22:21 UTC

New packages created between 2026-10-30 21:21 UTC and 2026-10-30 22:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T22-21-03-488014Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 21:27:00 | [G9AppDiagnostic.Shared](https://www.nuget.org/packages/G9AppDiagnostic.Shared) | 0.1.0 | Iman Kari | The wire contract of G9AppDiagnostic: the live channel's hub interfaces and pay… |
| 2026-10-30 21:27:07 | [G9AppDiagnostic.Client](https://www.nuget.org/packages/G9AppDiagnostic.Client) | 0.1.0 | Iman Kari | Device diagnostics client for apps in the field: tester reports (resumable uplo… |
| 2026-10-30 21:27:10 | [G9AppDiagnostic.Gateway](https://www.nuget.org/packages/G9AppDiagnostic.Gateway) | 0.1.0 | Iman Kari | The G9AppDiagnostic gateway: devices connect to it (live channel, logs, screens… |
| 2026-10-30 21:27:13 | [G9AppDiagnostic.Maui](https://www.nuget.org/packages/G9AppDiagnostic.Maui) | 0.1.0 | Iman Kari | Tester mode for .NET MAUI apps: capture panel, screen and voice recording, scre… |
| 2026-10-30 21:37:43 | [RobotForce.Pdf](https://www.nuget.org/packages/RobotForce.Pdf) | 1.0.5 | RobotForce | Sophona Studio nodes for reading PDF files: info, text, text for LLMs, search;… |
| 2026-10-30 21:40:20 | [RobotForce.Utilities](https://www.nuget.org/packages/RobotForce.Utilities) | 1.0.0 | RobotForce | Sophona Studio utility nodes: JSON, dates, text, regex, math, hashes, IDs, vali… |
| 2026-10-30 21:44:45 | [zivalix](https://www.nuget.org/packages/zivalix) | 0.0.1 | ZIVALIX Founders | Official reserved package for ZIVALIX Agency. Defensive registration. |
| 2026-10-30 22:04:34 | [Semi.Avalonia.Recolor](https://www.nuget.org/packages/Semi.Avalonia.Recolor) | 1.0.0 | zxcdenjir | Runtime Semi.Avalonia theme recoloring with ImagePicker and Android haptic feed… |
| 2026-10-30 22:04:35 | [Semi.Avalonia.Recolor.Ursa](https://www.nuget.org/packages/Semi.Avalonia.Recolor.Ursa) | 1.0.0 | zxcdenjir | Optional Ursa page dialog-host integration and Semi/Avalonia title-bar adjustme… |
| 2026-10-30 22:10:57 | [Lobasoft.Identity.EntityFrameworkCore](https://www.nuget.org/packages/Lobasoft.Identity.EntityFrameworkCore) | 2.0.0 | Lobasoft.Identity.EntityFrame… | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
