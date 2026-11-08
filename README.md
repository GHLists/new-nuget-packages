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

## Latest list — 2026-11-08 12:20 UTC

New packages created between 2026-11-08 11:20 UTC and 2026-11-08 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T12-20-36-517377Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 11:33:05 | [Poshteh.Core.ModuleKernel](https://www.nuget.org/packages/Poshteh.Core.ModuleKernel) | 10.0.2 | Poshteh | Poshteh's module descriptor/registration contract for composing bounded capabil… |
| 2026-11-08 11:33:06 | [Poshteh.Templates](https://www.nuget.org/packages/Poshteh.Templates) | 10.0.2 | Poshteh | dotnet new templates for applications built on the Poshteh framework (DDD, CQRS… |
| 2026-11-08 11:33:06 | [Poshteh.Testing.Kit](https://www.nuget.org/packages/Poshteh.Testing.Kit) | 10.0.2 | Poshteh | Contract-test bases and in-memory port implementations for consumers' own test… |
| 2026-11-08 11:33:07 | [Poshteh.Infra.Data.Sql.Query](https://www.nuget.org/packages/Poshteh.Infra.Data.Sql.Query) | 10.0.2 | Poshteh | Poshteh's EF Core no-tracking read-side persistence adapter: BaseQueryDbContext… |
| 2026-11-08 11:33:08 | [Poshteh.Core.ApplicationService](https://www.nuget.org/packages/Poshteh.Core.ApplicationService) | 10.0.2 | Poshteh | Poshteh's CQRS core: command/query dispatchers, pipeline behaviors, and the in-… |
| 2026-11-08 11:33:08 | [Poshteh.Endpoint.Api](https://www.nuget.org/packages/Poshteh.Endpoint.Api) | 10.0.2 | Poshteh | Poshteh's HTTP adapter helpers: Result-to-HTTP mapping and the global exception… |
| 2026-11-08 11:33:09 | [Poshteh.Shared.Kernel](https://www.nuget.org/packages/Poshteh.Shared.Kernel) | 10.0.2 | Poshteh | Dependency-free shared primitives (Clock, correlation accessor) used across eve… |
| 2026-11-08 11:33:10 | [Poshteh.Core.Domain](https://www.nuget.org/packages/Poshteh.Core.Domain) | 10.0.2 | Poshteh | Poshteh's rich domain model kernel: AggregateRoot, BaseEntity, ValueObject, Dom… |
| 2026-11-08 11:33:11 | [Poshteh.Core.Contract](https://www.nuget.org/packages/Poshteh.Core.Contract) | 10.0.2 | Poshteh | Poshteh's ports (repositories, outbox, domain event dispatch) — the sole mediat… |
| 2026-11-08 11:33:11 | [Poshteh.Infra.Data.Sql.Command](https://www.nuget.org/packages/Poshteh.Infra.Data.Sql.Command) | 10.0.2 | Poshteh | Poshteh's EF Core write-side persistence adapter: BaseCommandDbContext, Command… |
| 2026-11-08 11:34:37 | [TelegramBotForge.Testing](https://www.nuget.org/packages/TelegramBotForge.Testing) | 0.2.0 | VAXA99 | Test TelegramBotForge bots without Telegram: send messages, press buttons and p… |
| 2026-11-08 11:37:41 | [YappersHQ.HudKit.Shared](https://www.nuget.org/packages/YappersHQ.HudKit.Shared) | 1.0.0 | yappershq | Public contract (IHudKit, surfaces, templates, player card) for drawing center-… |
| 2026-11-08 11:46:28 | [Themia.SecondFactor.PostgreSql](https://www.nuget.org/packages/Themia.SecondFactor.PostgreSql) | 0.57.2 | Sarawut Phaekuntod | PostgreSQL (15+) Dapper store + FluentMigrator runner for Themia.SecondFactor. |
| 2026-11-08 11:46:42 | [Themia.SecondFactor](https://www.nuget.org/packages/Themia.SecondFactor) | 0.57.2 | Sarawut Phaekuntod | Themia multi-method second-factor layer — credential store contract, method str… |
| 2026-11-08 11:48:30 | [Lengko.Chart.WinForm](https://www.nuget.org/packages/Lengko.Chart.WinForm) | 1.0.0 | LengkoDev, Cas | Modern, high-performance charting and data visualization library for Windows Fo… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
