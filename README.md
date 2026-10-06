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

## Latest list — 2026-10-06 08:21 UTC

New packages created between 2026-10-06 07:20 UTC and 2026-10-06 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T08-21-37-93501Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 07:33:26 | [ZL.IotHub.Server](https://www.nuget.org/packages/ZL.IotHub.Server) | 2.2.14 | ZL | SCADA / Web API 实时通信服务端：基于 SignalR Server，对接 ZL.IotHub 采集内核。 |
| 2026-10-06 08:12:28 | [Wslc.Testcontainers](https://www.nuget.org/packages/Wslc.Testcontainers) | 0.2.0 | Nick Nadolski | Testcontainers-style ephemeral WSL containers for .NET integration tests, built… |
| 2026-10-06 08:12:29 | [Wslc.Testcontainers.Modules.MariaDb](https://www.nuget.org/packages/Wslc.Testcontainers.Modules.MariaDb) | 0.2.0 | Nick Nadolski | MariaDB module for Wslc.Testcontainers: typed builder and connection string. |
| 2026-10-06 08:12:30 | [Wslc.Testcontainers.Modules.PostgreSql](https://www.nuget.org/packages/Wslc.Testcontainers.Modules.PostgreSql) | 0.2.0 | Nick Nadolski | PostgreSQL module for Wslc.Testcontainers: typed builder and connection string. |
| 2026-10-06 08:12:32 | [Wslc.Testcontainers.Modules.RabbitMq](https://www.nuget.org/packages/Wslc.Testcontainers.Modules.RabbitMq) | 0.2.0 | Nick Nadolski | RabbitMQ module for Wslc.Testcontainers: typed builder and AMQP connection stri… |
| 2026-10-06 08:12:32 | [Wslc.Testcontainers.Modules.Redis](https://www.nuget.org/packages/Wslc.Testcontainers.Modules.Redis) | 0.2.0 | Nick Nadolski | Redis module for Wslc.Testcontainers: typed builder and connection string. |
| 2026-10-06 08:12:34 | [Wslc.Testcontainers.Modules.Valkey](https://www.nuget.org/packages/Wslc.Testcontainers.Modules.Valkey) | 0.2.0 | Nick Nadolski | Valkey module for Wslc.Testcontainers: typed builder and endpoint helper. |
| 2026-10-06 08:15:25 | [Google.Apis.Compute.preview](https://www.nuget.org/packages/Google.Apis.Compute.preview) | 1.77.0.4282 | Google LLC | Google APIs Client Library for working with Compute preview. Product documentat… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
