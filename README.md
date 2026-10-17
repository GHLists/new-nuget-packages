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

## Latest list — 2026-10-17 21:20 UTC

New packages created between 2026-10-17 20:18 UTC and 2026-10-17 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T21-20-41-760724Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 20:20:33 | [Neomoth.RTLogging](https://www.nuget.org/packages/Neomoth.RTLogging) | 1.0.1 | neomoth | Hierarchical, named "sawmill" loggers built on Serilog, with console and file h… |
| 2026-10-17 20:21:14 | [SaneTui.Sane](https://www.nuget.org/packages/SaneTui.Sane) | 0.1.0 | Mark Parker | Scan from .NET on Linux through SANE, the scanner framework most Linux scanner… |
| 2026-10-17 20:25:32 | [PaperDoll.Core](https://www.nuget.org/packages/PaperDoll.Core) | 1.0.0 | Rathinosk | Engine-free 2D puppet runtime: loads Inochi2D INP1 puppets (.inp, .inx). |
| 2026-10-17 20:25:33 | [PaperDoll.MonoGame](https://www.nuget.org/packages/PaperDoll.MonoGame) | 1.0.0 | Rathinosk | Draws PaperDoll puppets through MonoGame (DesktopGL or WindowsDX). |
| 2026-10-17 20:25:33 | [PaperDoll.FNA](https://www.nuget.org/packages/PaperDoll.FNA) | 1.0.0 | Rathinosk | Draws PaperDoll puppets through FNA. |
| 2026-10-17 20:26:30 | [IBeam.Management](https://www.nuget.org/packages/IBeam.Management) | 2.15.0 | MedPACTech | Reusable IBeam management contracts. |
| 2026-10-17 20:26:30 | [IBeam.Management.Api](https://www.nuget.org/packages/IBeam.Management.Api) | 2.15.0 | MedPACTech | Reusable IBeam management API endpoints. |
| 2026-10-17 20:26:31 | [IBeam.Management.Diagnostics.Api](https://www.nuget.org/packages/IBeam.Management.Diagnostics.Api) | 2.15.0 | MedPACTech | Reusable IBeam management API endpoints. |
| 2026-10-17 20:26:31 | [IBeam.Management.Identity.Api](https://www.nuget.org/packages/IBeam.Management.Identity.Api) | 2.15.0 | MedPACTech | Optional support-only Identity HTTP and JWT authentication adapter. |
| 2026-10-17 20:26:32 | [IBeam.Management.Identity.Services](https://www.nuget.org/packages/IBeam.Management.Identity.Services) | 2.15.0 | MedPACTech | Optional isolated IBeam Identity integration for management hosts. |
| 2026-10-17 20:26:32 | [IBeam.Management.Repositories.AzureTable](https://www.nuget.org/packages/IBeam.Management.Repositories.AzureTable) | 2.15.0 | MedPACTech | Entity-focused Azure Table repositories for IBeam Management. |
| 2026-10-17 20:26:33 | [IBeam.Management.Secrets.AzureKeyVault](https://www.nuget.org/packages/IBeam.Management.Secrets.AzureKeyVault) | 2.15.0 | MedPACTech | Optional Azure Key Vault secret store for IBeam Management connections. |
| 2026-10-17 20:26:33 | [IBeam.Management.Services](https://www.nuget.org/packages/IBeam.Management.Services) | 2.15.0 | MedPACTech | Reusable IBeam management services. |
| 2026-10-17 20:27:31 | [VetCore.Bdpm](https://www.nuget.org/packages/VetCore.Bdpm) | 0.1.0 | VetCoreSolution | Modèles immutables et lecture des cinq fichiers structurés de la Base de donnée… |
| 2026-10-17 20:39:13 | [Flare.Components.Gantt](https://www.nuget.org/packages/Flare.Components.Gantt) | 0.45.0 | FrigaT | Flare Gantt timeline for the Flare Blazor component library: task trees, resour… |
| 2026-10-17 20:39:40 | [MusicTheory.Guitar.Blazor](https://www.nuget.org/packages/MusicTheory.Guitar.Blazor) | 1.7.0 | phmatray | Blazor add-on for MusicTheory.Guitar: light chord playback (plucked-string Web… |
| 2026-10-17 20:40:34 | [Patware.Diagnostics.ApplicationEvents.Core](https://www.nuget.org/packages/Patware.Diagnostics.ApplicationEvents.Core) | 0.0.1 | Patware | Package Description |
| 2026-10-17 20:40:35 | [Patware.Diagnostics.ApplicationEvents.Hosting](https://www.nuget.org/packages/Patware.Diagnostics.ApplicationEvents.Hosting) | 0.0.1 | Patware | Automatic application lifecycle events for the .NET Generic Host. |
| 2026-10-17 20:54:32 | [Bfs.Seed.Extension](https://www.nuget.org/packages/Bfs.Seed.Extension) | 0.7.0 | Black Forest Sentinel | Update-Endpunkt für selbst gehostete Browser-Erweiterungen (Edge, Chrome) in Se… |
| 2026-10-17 21:00:28 | [AllFromZero.Core](https://www.nuget.org/packages/AllFromZero.Core) | 0.0.3 | AllFromZero | AllFromZero.Core是一个通用的C#库，基于.net开发 |
| 2026-10-17 21:06:28 | [aweXpect.Snapshots](https://www.nuget.org/packages/aweXpect.Snapshots) | 0.2.0 | aweXpect | Snapshot testing for aweXpect. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
