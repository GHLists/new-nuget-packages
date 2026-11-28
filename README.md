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

## Latest list — 2026-11-28 01:21 UTC

New packages created between 2026-11-28 00:19 UTC and 2026-11-28 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-28T01-21-14-783914Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-28 00:31:30 | [Messager.NET.PureDI](https://www.nuget.org/packages/Messager.NET.PureDI) | 2.1.0 | NovoDwarf | Pure.DI pub/sub integration for Messager.NET. |
| 2026-11-28 00:38:07 | [MicroWeave.Core](https://www.nuget.org/packages/MicroWeave.Core) | 0.1.0 | MicroWeave.NET contributors | Application contracts and result types for MicroWeave.NET services. |
| 2026-11-28 00:38:08 | [MicroWeave.Messaging.MassTransit](https://www.nuget.org/packages/MicroWeave.Messaging.MassTransit) | 0.1.0 | MicroWeave.NET contributors | RabbitMQ and PostgreSQL outbox integration for MicroWeave services. |
| 2026-11-28 00:38:09 | [MicroWeave.ServiceDefaults](https://www.nuget.org/packages/MicroWeave.ServiceDefaults) | 0.1.0 | MicroWeave.NET contributors | OpenTelemetry and health check defaults for MicroWeave .NET applications. |
| 2026-11-28 00:38:09 | [MicroWeave.Gateway](https://www.nuget.org/packages/MicroWeave.Gateway) | 0.1.0 | MicroWeave.NET contributors | HTTP correlation and Aspire service discovery for MicroWeave Ocelot gateways. |
| 2026-11-28 00:38:10 | [MicroWeave.Templates](https://www.nuget.org/packages/MicroWeave.Templates) | 0.1.0 | MicroWeave.NET contributors | Generate a MicroWeave .NET system or service. |
| 2026-11-28 00:42:46 | [EgyptianId.AspNetCore](https://www.nuget.org/packages/EgyptianId.AspNetCore) | 1.0.0 | Ahmed Mohamed Gaber | ASP.NET Core integration for EgyptianId: bind the 14-digit Egyptian national ID… |
| 2026-11-28 00:42:47 | [EgyptianId.FluentValidation](https://www.nuget.org/packages/EgyptianId.FluentValidation) | 1.0.0 | Ahmed Mohamed Gaber | FluentValidation rule for the 14-digit Egyptian national ID number. One call ad… |
| 2026-11-28 00:51:38 | [TBJ.Integrations.PublicRegisters](https://www.nuget.org/packages/TBJ.Integrations.PublicRegisters) | 1.0.0 | TBJ | Typed clients for Polish public registers: REGON (GUS BIR), CEIDG, VAT whitelis… |
| 2026-11-28 01:08:35 | [Provident.Foundations](https://www.nuget.org/packages/Provident.Foundations) | 11.98.3 | Sam Jones | A general-purpose, portable .NET class library for application development on .… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
