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

## Latest list — 2026-11-26 16:19 UTC

New packages created between 2026-11-26 15:20 UTC and 2026-11-26 16:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T16-19-00-574145Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 15:26:26 | [SoulConverter.Tool](https://www.nuget.org/packages/SoulConverter.Tool) | 0.0.11 | José Manuel Nieto | The soulconverter command: converts VGM music and sound-effect logs between the… |
| 2026-11-26 15:26:28 | [SoulConverter](https://www.nuget.org/packages/SoulConverter) | 0.0.11 | José Manuel Nieto | Converts VGM music and sound-effect logs between the NES 2A03, the Game Boy DMG… |
| 2026-11-26 15:26:29 | [PermissionsInspector](https://www.nuget.org/packages/PermissionsInspector) | 1.0.1 | Apoorv Gupta | Diagnose 'Why Can't John Edit This Record?' in Microsoft Dataverse across Secur… |
| 2026-11-26 15:33:20 | [Velle.Tool](https://www.nuget.org/packages/Velle.Tool) | 0.3.1 | Velle.Tool | Install Velle CSS components and browser behaviors into a project. |
| 2026-11-26 15:47:27 | [Fdo](https://www.nuget.org/packages/Fdo) | 0.1.0-preview | marcschier | Standalone FIDO Device Onboard 2.0 library for .NET. |
| 2026-11-26 15:48:27 | [SysadminsLV.WPF](https://www.nuget.org/packages/SysadminsLV.WPF) | 2.0.0-preview | Vadims Podāns | This package contains a custom OfficeBlue WPF theme. |
| 2026-11-26 15:53:57 | [Linker.KurrentDB](https://www.nuget.org/packages/Linker.KurrentDB) | 1.2.1 | Linker.Core | Replicate data between KurrentDb (former EventStore) instances |
| 2026-11-26 15:55:27 | [RestSimple](https://www.nuget.org/packages/RestSimple) | 0.1.0 | RestSimple | A dependency-light REST client for .NET with one-line JSON calls. Wraps HttpCli… |
| 2026-11-26 15:56:19 | [Rodrigosdk.CleanApi.Templates](https://www.nuget.org/packages/Rodrigosdk.CleanApi.Templates) | 1.0.0 | Rodrigosdk | Template do dotnet new (cleanapi) para Web API em Clean Architecture com .NET 1… |
| 2026-11-26 15:59:59 | [Myle](https://www.nuget.org/packages/Myle) | 0.1.0 | Myle | The official .NET SDK of the Myle API (https://api.myleapp.fr): typed resources… |
| 2026-11-26 16:00:08 | [QMGateway](https://www.nuget.org/packages/QMGateway) | 0.1.0 | QMGateway | Send SMS and one-time passwords with QMGateway. No dependencies. |
| 2026-11-26 16:00:08 | [QMGateway.Cli](https://www.nuget.org/packages/QMGateway.Cli) | 0.1.0 | QMGateway.Cli | Command-line tool for QMGateway. |
| 2026-11-26 16:05:28 | [Acme.Sdk](https://www.nuget.org/packages/Acme.Sdk) | 1.0.0 | Muhammad Sajjad | Official .NET Client SDK for the Acme REST API with built-in Dependency Injecti… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
