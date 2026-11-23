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

## Latest list — 2026-11-23 20:18 UTC

New packages created between 2026-11-23 19:20 UTC and 2026-11-23 20:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T20-18-56-432066Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 19:26:05 | [AiDotNet.CodeAnalysis.TreeSitter](https://www.nuget.org/packages/AiDotNet.CodeAnalysis.TreeSitter) | 0.236.1 | ooples | TreeSitter-backed code analysis for AiDotNet: precise syntax validation for the… |
| 2026-11-23 19:26:11 | [AiDotNet.Resources](https://www.nuget.org/packages/AiDotNet.Resources) | 0.236.1 | ooples | Embedded data for AiDotNet: tokenizer vocabularies and text-to-speech front-end… |
| 2026-11-23 19:35:32 | [BFC.ObisLaser](https://www.nuget.org/packages/BFC.ObisLaser) | 0.2.0 | Bruno F. Cruz | Bonsai operators to control Coherent OBIS LX/LS lasers (unofficial, not affilia… |
| 2026-11-23 19:35:32 | [BFC.ObisLaser.Design](https://www.nuget.org/packages/BFC.ObisLaser.Design) | 0.2.0 | Bruno F. Cruz | Control panel for Coherent OBIS LX/LS lasers in the Bonsai editor (unofficial,… |
| 2026-11-23 19:36:03 | [Softbreak.NuGetLicenseRadar](https://www.nuget.org/packages/Softbreak.NuGetLicenseRadar) | 0.1.1 | Softbreak | Scan .NET projects for NuGet license declarations and evidence-based license te… |
| 2026-11-23 19:48:33 | [EpicMorg.HammerShell.Client](https://www.nuget.org/packages/EpicMorg.HammerShell.Client) | 0.1.0 | EpicMorg | Client for the shell channel of Valve Hammer Editor (Source 1): send entity and… |
| 2026-11-23 19:52:52 | [DsDevelopment.FileZillaServer.AdminClient](https://www.nuget.org/packages/DsDevelopment.FileZillaServer.AdminClient) | 0.1.0 | Philip Hoppe | Client for the administration interface of FileZilla Server 1.x. Manage users a… |
| 2026-11-23 19:54:06 | [JobMaster.Cronos](https://www.nuget.org/packages/JobMaster.Cronos) | 0.0.2-alpha | Hugo Silva | JobMaster is a framework designed to manage and execute background tasks across… |
| 2026-11-23 19:54:08 | [JobMaster.NCrontab](https://www.nuget.org/packages/JobMaster.NCrontab) | 0.0.2-alpha | Hugo Silva | JobMaster is a framework designed to manage and execute background tasks across… |
| 2026-11-23 20:01:28 | [NuExt.Minimal.Mvvm.Desktop.Persistence](https://www.nuget.org/packages/NuExt.Minimal.Mvvm.Desktop.Persistence) | 0.9.5 | ivanvoyager | SQLite persistence layer for desktop MVVM applications, combining NuExt.Minimal… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
