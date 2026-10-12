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

## Latest list — 2026-10-12 18:22 UTC

New packages created between 2026-10-12 17:21 UTC and 2026-10-12 18:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T18-22-07-126594Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 17:25:45 | [Fuaran.Core.Unit](https://www.nuget.org/packages/Fuaran.Core.Unit) | 0.37.0 | Andrew J. Willshire | Fuaran.Core.Unit — a unit is a value: the runtime dimension algebra over a stat… |
| 2026-10-12 17:30:46 | [Bfs.Seed.OpenApi](https://www.nuget.org/packages/Bfs.Seed.OpenApi) | 0.5.0 | Black Forest Sentinel | OpenAPI 2.0 (Swagger) für Azure Functions (dotnet-isolated) in Sentinel-Seed-Pr… |
| 2026-10-12 17:32:12 | [XAvalonia.Splashscreen](https://www.nuget.org/packages/XAvalonia.Splashscreen) | 0.2.0 | Karen Liliou | XAvalonia splash screen plugin — displays an image defined in the technical con… |
| 2026-10-12 17:45:04 | [LiteRtLmSharp.runtime.linux-arm64](https://www.nuget.org/packages/LiteRtLmSharp.runtime.linux-arm64) | 1.3.0 | LiteRtLmSharp contributors | Native LiteRT-LM runtime (linux-arm64) for LiteRtLmSharp. Built from LiteRT-LM… |
| 2026-10-12 17:45:07 | [LiteRtLmSharp.runtime.android-x64](https://www.nuget.org/packages/LiteRtLmSharp.runtime.android-x64) | 1.3.0 | LiteRtLmSharp contributors | Native LiteRT-LM runtime (android-x64) for LiteRtLmSharp. Built from LiteRT-LM… |
| 2026-10-12 17:47:17 | [CloudySkySoftware.Pulumi.FlyMachines](https://www.nuget.org/packages/CloudySkySoftware.Pulumi.FlyMachines) | 0.0.8 | Cloudy Sky Software | A Pulumi package for creating and managing FlyMachines resources. |
| 2026-10-12 17:48:10 | [Stellaegis.Blobs](https://www.nuget.org/packages/Stellaegis.Blobs) | 1.0.1 | FRi | A storage abstraction for opaque binary content: IBlobStore, addressed by holde… |
| 2026-10-12 17:48:10 | [Stellaegis.Blobs.FileSystem](https://www.nuget.org/packages/Stellaegis.Blobs.FileSystem) | 1.0.1 | FRi | Filesystem adapter for Stellaegis.Blobs: one directory per holder and blob spac… |
| 2026-10-12 17:53:02 | [DevX.Cli](https://www.nuget.org/packages/DevX.Cli) | 1.7.0 | DevX.Cli | Package Description |
| 2026-10-12 17:54:40 | [Eternet.Data.ReadReplica](https://www.nuget.org/packages/Eternet.Data.ReadReplica) | 1.0.0 | Eternet.Data.ReadReplica | Routes read-only HTTP endpoints (generated OData reads) to the PostgreSQL read-… |
| 2026-10-12 18:12:48 | [Novolis.Transports.Ed2k](https://www.nuget.org/packages/Novolis.Transports.Ed2k) | 2026.1.11.75 | Novolis | Clean-room eD2k server and peer protocol client with file identifiers, source d… |
| 2026-10-12 18:12:51 | [Novolis.Transports.Kad](https://www.nuget.org/packages/Novolis.Transports.Kad) | 2026.1.11.75 | Novolis | Clean-room eMule Kad discovery and routing primitives over UDP. |
| 2026-10-12 18:12:53 | [Novolis.Transports.NetworkPath](https://www.nuget.org/packages/Novolis.Transports.NetworkPath) | 2026.1.11.75 | Novolis | Cross-platform network adapter, route, and bound-path probing. |
| 2026-10-12 18:14:23 | [EasySsf.Receiver.Hosting](https://www.nuget.org/packages/EasySsf.Receiver.Hosting) | 0.6.0 | easyssf contributors | Hosting integration of the easyssf SSF receiver: options, dependency injection,… |
| 2026-10-12 18:14:23 | [EasySsf.Receiver.Data](https://www.nuget.org/packages/EasySsf.Receiver.Data) | 0.6.0 | easyssf contributors | Database stores of the easyssf SSF receiver on ADO.NET: processed SETs, revocat… |
| 2026-10-12 18:14:24 | [EasySsf.Receiver.AspNetCore](https://www.nuget.org/packages/EasySsf.Receiver.AspNetCore) | 0.6.0 | easyssf contributors | ASP.NET Core integration of the easyssf SSF receiver: the push endpoint for SET… |
| 2026-10-12 18:14:24 | [EasySsf.Core](https://www.nuget.org/packages/EasySsf.Core) | 0.6.0 | easyssf contributors | The vocabulary of the OpenID Shared Signals Framework for .NET: Security Event… |
| 2026-10-12 18:14:24 | [EasySsf.Receiver](https://www.nuget.org/packages/EasySsf.Receiver) | 0.6.0 | easyssf contributors | The easyssf SSF receiver without a framework: SET verification, de-duplication,… |
| 2026-10-12 18:14:25 | [EasySsf.Testing](https://www.nuget.org/packages/EasySsf.Testing) | 0.6.0 | easyssf contributors | Test support for easyssf receivers: an in-process transmitter that signs SETs,… |
| 2026-10-12 18:14:39 | [WhatsAppBridge](https://www.nuget.org/packages/WhatsAppBridge) | 1.0.0 | Heavy-Lift | Puente genérico para enviar plantillas de WhatsApp a través de un webhook de n8… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
