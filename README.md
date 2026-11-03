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

## Latest list — 2026-11-03 15:20 UTC

New packages created between 2026-11-03 14:21 UTC and 2026-11-03 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T15-20-26-063265Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 14:24:42 | [Phoenix.Data.Plc.SiAccess](https://www.nuget.org/packages/Phoenix.Data.Plc.SiAccess) | 7.0.0 | Felix Leistner | Base assembly for providing plc communication via siAccess. |
| 2026-11-03 14:26:05 | [Baziness.Server](https://www.nuget.org/packages/Baziness.Server) | 2.1.0 | Baziness | Baziness platform SDK for .NET game servers: client auth, player sessions with… |
| 2026-11-03 14:34:21 | [Muflone.Transport.Kafka](https://www.nuget.org/packages/Muflone.Transport.Kafka) | 10.0.0-alpha | Fabio Della Rosa | Package Description |
| 2026-11-03 14:35:49 | [Senparc.Xncf.FileManager.Abstractions](https://www.nuget.org/packages/Senparc.Xncf.FileManager.Abstractions) | 0.2.0 | Senparc | Contracts for optional integrations with Senparc.Xncf.FileManager. |
| 2026-11-03 14:35:57 | [Senparc.Xncf.Workspace.Abstractions](https://www.nuget.org/packages/Senparc.Xncf.Workspace.Abstractions) | 0.2.0 | Senparc.Xncf.Workspace.Abstra… | Package Description |
| 2026-11-03 14:38:15 | [FaultTrace.AspNetCore](https://www.nuget.org/packages/FaultTrace.AspNetCore) | 0.1.0-alpha | soyprofesor | ASP.NET Core integration for FaultTrace: unified RFC 9457 problem responses for… |
| 2026-11-03 14:38:15 | [FaultTrace.Core](https://www.nuget.org/packages/FaultTrace.Core) | 0.1.0-alpha | soyprofesor | Turns exceptions into safe, localized error responses and rich structured log e… |
| 2026-11-03 14:38:16 | [FaultTrace.Oracle](https://www.nuget.org/packages/FaultTrace.Oracle) | 0.1.0-alpha | soyprofesor | Oracle provider for FaultTrace: classifies ORA errors and parses PL/SQL error s… |
| 2026-11-03 14:49:35 | [OhrTech.Management](https://www.nuget.org/packages/OhrTech.Management) | 1.0.0 | OhrTech | Client for the OhrTech Management API: manage your organisation's devices from… |
| 2026-11-03 15:00:35 | [FixBuild.Gen](https://www.nuget.org/packages/FixBuild.Gen) | 0.1.0 | fixbuild | A C# compatibility nuget for macos. |
| 2026-11-03 15:07:00 | [CodeAnalysisUtills](https://www.nuget.org/packages/CodeAnalysisUtills) | 1.0.0 | vsc | Utilities for loading, compiling, and inspecting .NET projects and types with R… |
| 2026-11-03 15:11:20 | [Linkway.Symplice.Station.Contracts](https://www.nuget.org/packages/Linkway.Symplice.Station.Contracts) | 1.0.0 | Linkway | The envelope and the channel's own message types between Symplice and its stati… |
| 2026-11-03 15:11:20 | [Linkway.Symplice.Station.Connection](https://www.nuget.org/packages/Linkway.Symplice.Station.Connection) | 1.0.0 | Linkway | The connection every Symplice station program includes: pairing, credential, th… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
