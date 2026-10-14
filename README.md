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

## Latest list — 2026-10-14 14:20 UTC

New packages created between 2026-10-14 13:20 UTC and 2026-10-14 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T14-20-08-036435Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 13:39:58 | [Switchknife.Testing.Http](https://www.nuget.org/packages/Switchknife.Testing.Http) | 0.1.0 | Yehor Hrabovskyi | A stub HttpMessageHandler for tests: answers each request from a function or a… |
| 2026-10-14 13:40:01 | [Switchknife.Migrations](https://www.nuget.org/packages/Switchknife.Migrations) | 0.1.0 | Yehor Hrabovskyi | Applies SQL scripts embedded in an assembly to PostgreSQL with DbUp, once each,… |
| 2026-10-14 13:40:05 | [Switchknife.Testing.Postgres](https://www.nuget.org/packages/Switchknife.Testing.Postgres) | 0.1.0 | Yehor Hrabovskyi | A PostgreSQL server in a Testcontainers container for integration tests: starte… |
| 2026-10-14 13:40:06 | [Switchknife.Hosting](https://www.nuget.org/packages/Switchknife.Hosting) | 0.1.0 | Yehor Hrabovskyi | A polling BackgroundService that never stops the host: polls on start and then… |
| 2026-10-14 13:49:44 | [RonSijm.FluidHumidifier](https://www.nuget.org/packages/RonSijm.FluidHumidifier) | 0.1.26700 | Ron Sijm | A fluent factory API for composing AWS CloudFormation resources with RonSijm.Hu… |
| 2026-10-14 13:57:20 | [SshSharp](https://www.nuget.org/packages/SshSharp) | 0.3.0 | SshSharp | Managed-only, async-first SSH client library for .NET with known_hosts and ssh_… |
| 2026-10-14 14:05:57 | [DatabaseSharp.SQLServer](https://www.nuget.org/packages/DatabaseSharp.SQLServer) | 1.0.1 | Kristian Skov Johansen | A DatabaseSharp connector for SQL Server |
| 2026-10-14 14:06:01 | [DatabaseSharp.PostgreSQL](https://www.nuget.org/packages/DatabaseSharp.PostgreSQL) | 1.0.1 | Kristian Skov Johansen | A DatabaseSharp connector for PostgreSQL |
| 2026-10-14 14:06:06 | [DatabaseSharp.MySQL](https://www.nuget.org/packages/DatabaseSharp.MySQL) | 1.0.1 | Kristian Skov Johansen | A DatabaseSharp connector for MySQL |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
