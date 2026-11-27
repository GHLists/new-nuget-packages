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

## Latest list — 2026-11-27 23:22 UTC

New packages created between 2026-11-27 22:20 UTC and 2026-11-27 23:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T23-22-09-015417Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 22:28:56 | [Tenable.Api](https://www.nuget.org/packages/Tenable.Api) | 1.0.50 | Panoramic Data Limited | A typed, modern .NET client for the Tenable REST APIs: Attack Surface Managemen… |
| 2026-11-27 22:29:41 | [TrueMediator](https://www.nuget.org/packages/TrueMediator) | 3.0.0 | Kamyab Valipour | A free, lightweight MediatR alternative with source-generated dispatch, Native… |
| 2026-11-27 22:29:43 | [TrueMediator.Contracts](https://www.nuget.org/packages/TrueMediator.Contracts) | 3.0.0 | Kamyab Valipour | Contracts for TrueMediator requests, pipelines, and notifications. |
| 2026-11-27 22:29:45 | [TrueMediator.EntityFrameworkCore](https://www.nuget.org/packages/TrueMediator.EntityFrameworkCore) | 3.0.0 | Kamyab Valipour | Attribute-selected Entity Framework Core transactions for TrueMediator requests. |
| 2026-11-27 22:29:46 | [TrueMediator.FluentValidation](https://www.nuget.org/packages/TrueMediator.FluentValidation) | 3.0.0 | Kamyab Valipour | Asynchronous FluentValidation request pipeline integration for TrueMediator. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
