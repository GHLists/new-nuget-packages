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

## Latest list — 2026-10-03 21:18 UTC

New packages created between 2026-10-03 20:19 UTC and 2026-10-03 21:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T21-18-43-46128Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 20:22:56 | [Tenantry.Caching](https://www.nuget.org/packages/Tenantry.Caching) | 0.6.0 | Tenantry Contributors | Tenant-aware caching for Tenantry: tenant.IsolateCaches() keys HybridCache entr… |
| 2026-10-03 20:22:57 | [Tenantry.Http](https://www.nuget.org/packages/Tenantry.Http) | 0.6.0 | Tenantry Contributors | HTTP and gRPC integration for Tenantry: UseTenantry() on an HttpClient or gRPC… |
| 2026-10-03 20:22:58 | [Tenantry.Options](https://www.nuget.org/packages/Tenantry.Options) | 0.6.0 | Tenantry Contributors | Per-tenant options for Tenantry: tenant.ConfigurePerTenant(...) makes IOptionsS… |
| 2026-10-03 20:23:48 | [SunamoUwpApps](https://www.nuget.org/packages/SunamoUwpApps) | 26.10.3.1 | www.sunamo.cz | Helpers, popups and controls from the legacy UWP apps library, ported to WinUI 3 |
| 2026-10-03 20:57:45 | [FullBleed.DotNet](https://www.nuget.org/packages/FullBleed.DotNet) | 0.1.1 | Fullbleed contributors | Idiomatic, dependency-free managed bindings for Fullbleed PDF Engine, including… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
