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

## Latest list — 2026-11-27 20:20 UTC

New packages created between 2026-11-27 19:20 UTC and 2026-11-27 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T20-20-53-433648Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 19:25:10 | [VNCore](https://www.nuget.org/packages/VNCore) | 1.0.0 | VNCore | Package Description |
| 2026-11-27 19:28:48 | [Everlong.CommandLine](https://www.nuget.org/packages/Everlong.CommandLine) | 0.2.1 | Richard Zheng | Everlong.CommandLine — command-tree based CLI framework built on System.Command… |
| 2026-11-27 19:45:43 | [B4n1.Telemetry](https://www.nuget.org/packages/B4n1.Telemetry) | 0.1.1 | B4N1 | Drop-in error reporting to your own b4n1-telemetry collector. Zero dependencies. |
| 2026-11-27 19:46:01 | [B4n1.Notary](https://www.nuget.org/packages/B4n1.Notary) | 0.2.1 | b4n1-notary | Authorship integrity and sealing: stamp, verify and list the proofs of a projec… |
| 2026-11-27 19:56:43 | [WebTools.StcCommon](https://www.nuget.org/packages/WebTools.StcCommon) | 10.0.0 | WebTools.StcCommon | Package Description |
| 2026-11-27 19:57:17 | [Shoko.QueueProcessor](https://www.nuget.org/packages/Shoko.QueueProcessor) | 6.0.0 | Shoko Team | A lightweight, persistent, attribute-driven background job queue for .NET, the… |
| 2026-11-27 19:57:18 | [Shoko.Abstractions](https://www.nuget.org/packages/Shoko.Abstractions) | 6.0.0 | Shoko Team | The contract between Shoko Server and its plugins: the interfaces, models and e… |
| 2026-11-27 20:06:04 | [VNCore.Godot](https://www.nuget.org/packages/VNCore.Godot) | 1.0.0 | ManWithBaguette | Godot integration for VNCore. |
| 2026-11-27 20:09:37 | [WebTools.StcData](https://www.nuget.org/packages/WebTools.StcData) | 10.0.0 | WebTools.StcData | Package Description |
| 2026-11-27 20:12:08 | [Shoko.Plugin.OfflineImporter.Abstractions](https://www.nuget.org/packages/Shoko.Plugin.OfflineImporter.Abstractions) | 2.0.1 | Shoko Team | The contracts another Shoko plugin uses to run the Offline Importer's file name… |
| 2026-11-27 20:12:59 | [LANCommander.Server.Plugins](https://www.nuget.org/packages/LANCommander.Server.Plugins) | 2.2.0 | pathartl | The contracts a LANCommander server plugin builds against: navigation, routes,… |
| 2026-11-27 20:14:44 | [InfraBase](https://www.nuget.org/packages/InfraBase) | 5.14.0 | Kerberos SA | EF Core data-access, multi-tenant and RBAC infrastructure for SQL Server, host-… |
| 2026-11-27 20:15:33 | [Metigator.NumberSystem.Mahmoud](https://www.nuget.org/packages/Metigator.NumberSystem.Mahmoud) | 1.0.0 | Mahmoud Ashraf | Convert Between Numbers From Different Bases |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
