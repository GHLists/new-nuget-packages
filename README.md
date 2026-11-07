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

## Latest list — 2026-11-07 21:20 UTC

New packages created between 2026-11-07 20:18 UTC and 2026-11-07 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T21-20-40-062719Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 20:21:50 | [LogQuill](https://www.nuget.org/packages/LogQuill) | 3.0.0 | Nikhil Arora | Structured, agent-aware logging for .NET on a Rust core: the same record shape,… |
| 2026-11-07 20:28:45 | [Pervaxis.Core.Data.EntityFrameworkCore](https://www.nuget.org/packages/Pervaxis.Core.Data.EntityFrameworkCore) | 1.7.0 | Clarivex Technologies | Entity Framework Core integration for tenant isolation: composite tenant keys,… |
| 2026-11-07 20:38:46 | [SadPencil.Ra2CsfFile.Ini](https://www.nuget.org/packages/SadPencil.Ra2CsfFile.Ini) | 3.0.0 | sadpencil | (De)serialize the string table of Red Alert 2 from/to .ini files, on top of Sad… |
| 2026-11-07 20:38:50 | [FrigaT.Weir.Caching.Redis](https://www.nuget.org/packages/FrigaT.Weir.Caching.Redis) | 3.2.0 | FrigaT | Redis response caching for Weir with binary payload leases and atomic invalidat… |
| 2026-11-07 20:40:28 | [CrackDiggerEngine](https://www.nuget.org/packages/CrackDiggerEngine) | 2.0.0 | @m51v5 | Search game listings on several public game sites and get the title, link and i… |
| 2026-11-07 20:41:44 | [FusionModules.EntityFrameworkCore](https://www.nuget.org/packages/FusionModules.EntityFrameworkCore) | 0.3.0 | Stanislav Vyshchepan | An EF Core model composed from the FusionModules modules a host loads: UseModul… |
| 2026-11-07 20:41:45 | [FusionModules.Testing](https://www.nuget.org/packages/FusionModules.Testing) | 0.3.0 | Stanislav Vyshchepan | Integration tests for a FusionModules host, one topology at a time: a WebApplic… |
| 2026-11-07 20:47:23 | [HoneyDrunk.Capabilities.Abstractions](https://www.nuget.org/packages/HoneyDrunk.Capabilities.Abstractions) | 0.1.0 | HoneyDrunk Studios | Dependency-light contracts for registering, resolving, authorizing and invoking… |
| 2026-11-07 20:48:14 | [HoneyDrunk.Capabilities.Testing](https://www.nuget.org/packages/HoneyDrunk.Capabilities.Testing) | 0.1.0 | HoneyDrunk Studios | Test fixtures for HoneyDrunk Grid capabilities: a harness over the real registr… |
| 2026-11-07 20:48:28 | [HoneyDrunk.Memory.Abstractions](https://www.nuget.org/packages/HoneyDrunk.Memory.Abstractions) | 0.1.0 | HoneyDrunk Studios | Contracts for HoneyDrunk agent memory: scope keys, entries, the scoped store, s… |
| 2026-11-07 20:48:38 | [HoneyDrunk.Memory.Providers.InMemory](https://www.nuget.org/packages/HoneyDrunk.Memory.Providers.InMemory) | 0.1.0 | HoneyDrunk Studios | In-memory HoneyDrunk agent-memory store for tests and local development. Not fo… |
| 2026-11-07 20:54:18 | [Webority.Ads.Admin](https://www.nuget.org/packages/Webority.Ads.Admin) | 0.18.0 | Webority Technologies | Ads pages for Webority admin portals: campaign figures by platform, conversions… |
| 2026-11-07 21:07:31 | [AuditLoggingPipeline.Telemetry.Sql](https://www.nuget.org/packages/AuditLoggingPipeline.Telemetry.Sql) | 0.1.0 | Troy Crowe | SQL Server sink for AuditLoggingPipeline.Telemetry. Writes usage events in batc… |
| 2026-11-07 21:14:17 | [Lengko.Alert.WinForm](https://www.nuget.org/packages/Lengko.Alert.WinForm) | 1.0.0 | LengkoDev, Cas | Modern, responsive, zero-dependency alert dialogs and toast notifications for W… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
