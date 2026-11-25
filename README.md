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

## Latest list — 2026-11-25 12:20 UTC

New packages created between 2026-11-25 11:21 UTC and 2026-11-25 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T12-20-01-937228Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 11:48:19 | [Donkeh.Llm](https://www.nuget.org/packages/Donkeh.Llm) | 1.0.53 | barely-sentient | Donkeh.Llm module for Donkeh, a CSS-driven UI engine for .NET. |
| 2026-11-25 11:48:55 | [GetCNPJ.Community](https://www.nuget.org/packages/GetCNPJ.Community) | 1.1.0 | Bruno da Cunha Felipe,Thaliso… | Fork independente do GetCNPJ de Bruno da Cunha Felipe, mantido por Thalison San… |
| 2026-11-25 11:55:26 | [Iyu.UBoard](https://www.nuget.org/packages/Iyu.UBoard) | 0.1.0 | iyulab | Host-neutral board storage and screen for embedding a board viewer and editor -… |
| 2026-11-25 11:55:28 | [Iyu.UBoard.EntityFrameworkCore](https://www.nuget.org/packages/Iyu.UBoard.EntityFrameworkCore) | 0.1.0 | iyulab | Entity Framework Core board store behind Iyu.UBoard - the boards, their revisio… |
| 2026-11-25 11:56:47 | [Olax.Auditing.Abstractions](https://www.nuget.org/packages/Olax.Auditing.Abstractions) | 1.0.0 | OLAX Innovative Lab | Audit contracts for the Application layer of OLAX services: IAuditLog records b… |
| 2026-11-25 11:56:50 | [Olax.Auditing.EntityFrameworkCore](https://www.nuget.org/packages/Olax.Auditing.EntityFrameworkCore) | 1.0.0 | OLAX Innovative Lab | Audit trail for an OLAX service's EF Core DbContext (PostgreSQL): every insert,… |
| 2026-11-25 11:59:13 | [Olax.Correlation](https://www.nuget.org/packages/Olax.Correlation) | 1.0.0 | OLAX Innovative Lab | The operation context of OLAX services: who is acting (user, service, on behalf… |
| 2026-11-25 12:08:52 | [Iyu.UBoard.IronHive](https://www.nuget.org/packages/Iyu.UBoard.IronHive) | 0.51.0 | iyulab | Fills the Iyu.UBoard assistant port with IronHive.Agent and IronProw: a board's… |
| 2026-11-25 12:09:02 | [Iyu.UBoard.MainServer](https://www.nuget.org/packages/Iyu.UBoard.MainServer) | 0.51.0 | iyulab | Connects the Iyu.UBoard source catalog to Iyu.MainServer: what a board can be b… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
