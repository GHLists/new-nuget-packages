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

## Latest list — 2026-11-28 03:21 UTC

New packages created between 2026-11-28 02:20 UTC and 2026-11-28 03:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-28T03-21-13-023355Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-28 02:25:21 | [Provident.Foundations.Wpf.Controls](https://www.nuget.org/packages/Provident.Foundations.Wpf.Controls) | 11.98.3 | Sam Jones | A small WPF controls library. |
| 2026-11-28 02:30:50 | [CSharpEssentials.Results.Testing](https://www.nuget.org/packages/CSharpEssentials.Results.Testing) | 9.0.0 | senrecep | Assertion helpers for Result, Result<T>, the typed Result<T, E1..E3>, Maybe<T>… |
| 2026-11-28 02:30:55 | [CSharpEssentials.Mediator.Testing](https://www.nuget.org/packages/CSharpEssentials.Mediator.Testing) | 9.0.0 | senrecep | Contract scenarios for IResourceLock implementations of CSharpEssentials.Mediat… |
| 2026-11-28 02:30:55 | [CSharpEssentials.EntityFrameworkCore.Hosting](https://www.nuget.org/packages/CSharpEssentials.EntityFrameworkCore.Hosting) | 9.0.0 | senrecep | Hosted service for the CSharpEssentials.EntityFrameworkCore outbox: drains IOut… |
| 2026-11-28 02:30:57 | [CSharpEssentials.EntityFrameworkCore.HealthChecks](https://www.nuget.org/packages/CSharpEssentials.EntityFrameworkCore.HealthChecks) | 9.0.0 | senrecep | Readiness health check for EF Core: reports Unhealthy while a DbContext has pen… |
| 2026-11-28 02:31:00 | [CSharpEssentials.EntityFrameworkCore.Locking](https://www.nuget.org/packages/CSharpEssentials.EntityFrameworkCore.Locking) | 9.0.0 | senrecep | Distributed IResourceLock for CSharpEssentials.Mediator over an EF Core relatio… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
