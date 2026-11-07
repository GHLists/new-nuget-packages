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

## Latest list — 2026-11-07 00:19 UTC

New packages created between 2026-11-06 23:20 UTC and 2026-11-07 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T00-19-55-19998Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 23:52:24 | [StfsSharp](https://www.nuget.org/packages/StfsSharp) | 1.0.0 | PureLogicCode.com | Read-only .NET library for Xbox 360 STFS packages and GOD/SVOD containers. List… |
| 2026-11-07 00:07:20 | [Corely.IAM.CompiledModel.MySql](https://www.nuget.org/packages/Corely.IAM.CompiledModel.MySql) | 6.8.0 | Corely.IAM.CompiledModel.MySql | Corely.IAM's Entity Framework model built ahead of time for MySQL and MariaDB,… |
| 2026-11-07 00:09:08 | [Corely.IAM.CompiledModel.MsSql](https://www.nuget.org/packages/Corely.IAM.CompiledModel.MsSql) | 6.8.0 | Corely.IAM.CompiledModel.MsSql | Corely.IAM's Entity Framework model built ahead of time for SQL Server, so an a… |
| 2026-11-07 00:09:43 | [Corely.Billing.CompiledModel.MsSql](https://www.nuget.org/packages/Corely.Billing.CompiledModel.MsSql) | 5.1.0 | Corely.Billing.CompiledModel.… | Corely.Billing's Entity Framework model built ahead of time for SQL Server, so… |
| 2026-11-07 00:09:57 | [Corely.Billing.CompiledModel.MySql](https://www.nuget.org/packages/Corely.Billing.CompiledModel.MySql) | 5.1.0 | Corely.Billing.CompiledModel.… | Corely.Billing's Entity Framework model built ahead of time for MySQL and Maria… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
