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

## Latest list — 2026-10-28 20:20 UTC

New packages created between 2026-10-28 19:19 UTC and 2026-10-28 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T20-20-08-314745Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 19:23:48 | [Mp4BoxKit](https://www.nuget.org/packages/Mp4BoxKit) | 1.0.0 | Mp4BoxKit contributors | ISO-BMFF MP4 and fragmented MP4 packaging for .NET with streaming segment deliv… |
| 2026-10-28 19:25:19 | [ZeppelinForms.Templates](https://www.nuget.org/packages/ZeppelinForms.Templates) | 0.19.0 | YD359Team | Templates of ZeppelinForms for dotnet new, Rider and Visual Studio: zf-app — an… |
| 2026-10-28 19:28:30 | [DevErrorAssistant](https://www.nuget.org/packages/DevErrorAssistant) | 1.0.0 | DevErrorAssistant Contributors | Developer-friendly ASP.NET Core exception-handling middleware supporting .NET 8… |
| 2026-10-28 19:34:08 | [ZkLink](https://www.nuget.org/packages/ZkLink) | 0.1.0 | Aleksandr Pavlov | A managed asynchronous .NET client for Apache ZooKeeper. Under development. |
| 2026-10-28 19:39:11 | [AstraFlow.Security](https://www.nuget.org/packages/AstraFlow.Security) | 2.0.0 | AstraFlow Contributors | Shared secure DTO governance and redaction policy primitives for AstraFlow diag… |
| 2026-10-28 19:43:20 | [pengdows.crud.opentelemetry](https://www.nuget.org/packages/pengdows.crud.opentelemetry) | 2.0.6-rc4 | Pengdows | OpenTelemetry adapter for pengdows.crud |
| 2026-10-28 19:43:22 | [pengdows.stormgate.EntityFrameworkCore](https://www.nuget.org/packages/pengdows.stormgate.EntityFrameworkCore) | 2.0.6-rc4 | Pengdows | Entity Framework Core connection admission control via a DbConnectionIntercepto… |
| 2026-10-28 20:00:21 | [FPH.Telemetry.Common](https://www.nuget.org/packages/FPH.Telemetry.Common) | 2026.10.0 | Freie Programme Hohenstein | Gemeinsamer Spielzugriff des FPH TelemetryServers (ETS2/ATS, OMSI, TruckersMP)… |
| 2026-10-28 20:11:48 | [IBeam.Management.Licensing](https://www.nuget.org/packages/IBeam.Management.Licensing) | 2.17.0 | MedPACTech | Optional typed Management licence and seat adapters over native conditional Lic… |
| 2026-10-28 20:11:49 | [IBeam.Management.Operations.Target.Api](https://www.nuget.org/packages/IBeam.Management.Operations.Target.Api) | 2.17.0 | MedPACTech | Optional typed signed Management target dispatch, independent of customer Ident… |
| 2026-10-28 20:11:52 | [IBeam.Management.TenantData.Identity](https://www.nuget.org/packages/IBeam.Management.TenantData.Identity) | 2.17.0 | MedPACTech | Optional verified tenant-scoped Identity cleanup for Management purge jobs. |
| 2026-10-28 20:11:54 | [IBeam.Management.TenantData.Target.Api](https://www.nuget.org/packages/IBeam.Management.TenantData.Target.Api) | 2.17.0 | MedPACTech | Optional scoped tenant export target API composition over signed Management dis… |
| 2026-10-28 20:11:59 | [IBeam.Management.TenantData.Target.Services](https://www.nuget.org/packages/IBeam.Management.TenantData.Target.Services) | 2.17.0 | MedPACTech | Optional app-owned tenant export contracts and safe signed target adapters. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
