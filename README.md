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

## Latest list — 2026-11-20 22:21 UTC

New packages created between 2026-11-20 21:22 UTC and 2026-11-20 22:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T22-21-54-055247Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 21:29:51 | [VersionFlow](https://www.nuget.org/packages/VersionFlow) | 1.1.0 | Bradley Ables | Strongly typed configuration-driven service and method version routing. |
| 2026-11-20 21:40:10 | [GHIElectronics.Endpoint.Pins](https://www.nuget.org/packages/GHIElectronics.Endpoint.Pins) | 0.5.4-preview | GHI Electronics, LLC | Pin constants, bus tables, and board support for every GHI Electronics Endpoint… |
| 2026-11-20 21:40:41 | [GHIElectronics.Endpoint.Drivers.RaspberryPi](https://www.nuget.org/packages/GHIElectronics.Endpoint.Drivers.RaspberryPi) | 0.5.4-preview | GHI Electronics, LLC | Raspberry Pi board support for Endpoint. One package covers every Pi model this… |
| 2026-11-20 21:56:25 | [Ming.NET.Sdk](https://www.nuget.org/packages/Ming.NET.Sdk) | 0.1.1 | ZhouShangLi | MSBuild SDK for Ming C# projects targeting .NET 9. |
| 2026-11-20 22:08:47 | [Anarchy.Toolkit.Automation](https://www.nuget.org/packages/Anarchy.Toolkit.Automation) | 1.0.0 | Leandro Melão Medeiros | Command-line foundations for Anarchy solutions: starter solution scaffolding, b… |
| 2026-11-20 22:08:48 | [Anarchy.Toolkit.Core.Telemetry](https://www.nuget.org/packages/Anarchy.Toolkit.Core.Telemetry) | 1.0.0 | Leandro Melão Medeiros | Provider-neutral telemetry primitives (ICoreTelemetry, IMetricRecorder) and the… |
| 2026-11-20 22:08:50 | [Anarchy.Toolkit.Infrastructure.Telemetry.Serilog](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Telemetry.Serilog) | 1.0.0 | Leandro Melão Medeiros | Optional Serilog integration for Anarchy telemetry: logging provider registrati… |
| 2026-11-20 22:08:52 | [Anarchy.Toolkit.Automation.Build](https://www.nuget.org/packages/Anarchy.Toolkit.Automation.Build) | 1.0.0 | Leandro Melão Medeiros | Anarchy automation components, powered by Fallout Build: solution/test conventi… |
| 2026-11-20 22:09:03 | [Anarchy.Toolkit.Infrastructure.Persistence.Db.Mysql](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Persistence.Db.Mysql) | 1.0.0 | Leandro Melão Medeiros | MySQL relational persistence adapter with connection pools, unit of work, resil… |
| 2026-11-20 22:09:04 | [Anarchy.Toolkit.Infrastructure.Persistence.Db.Oracle](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Persistence.Db.Oracle) | 1.0.0 | Leandro Melão Medeiros | Oracle implementation of the relational persistence layer: dialect, connection… |
| 2026-11-20 22:09:06 | [Anarchy.Toolkit.Infrastructure.Persistence.Db.Postgres](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Persistence.Db.Postgres) | 1.0.0 | Leandro Melão Medeiros | PostgreSQL implementation of the relational persistence layer: dialect, connect… |
| 2026-11-20 22:09:10 | [Anarchy.Toolkit.Testing.Db.Mysql](https://www.nuget.org/packages/Anarchy.Toolkit.Testing.Db.Mysql) | 1.0.0 | Leandro Melão Medeiros | MySQL integration-test fixtures, settings mapping, enum handlers and table rese… |
| 2026-11-20 22:09:11 | [Anarchy.Toolkit.Testing.Db.Oracle](https://www.nuget.org/packages/Anarchy.Toolkit.Testing.Db.Oracle) | 1.0.0 | Leandro Melão Medeiros | Oracle integration-test fixtures: connection string, connection pool, retry/res… |
| 2026-11-20 22:09:12 | [Anarchy.Toolkit.Testing.Db.Postgres](https://www.nuget.org/packages/Anarchy.Toolkit.Testing.Db.Postgres) | 1.0.0 | Leandro Melão Medeiros | PostgreSQL integration-test fixtures: connection string, connection pool, retry… |
| 2026-11-20 22:15:46 | [Tiresias.Extensions.Configuration](https://www.nuget.org/packages/Tiresias.Extensions.Configuration) | 0.2.0 | Steve Hansen | User secrets encrypted at rest and released per process by the tir agent after… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
