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

## Latest list — 2026-10-04 17:19 UTC

New packages created between 2026-10-04 16:20 UTC and 2026-10-04 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T17-19-20-366273Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 16:33:02 | [DynCMS.Plugins.Sdk](https://www.nuget.org/packages/DynCMS.Plugins.Sdk) | 0.1.0 | DynCMS | The DynCMS plugin SDK: the plugin contract, the shared admin UI building blocks… |
| 2026-10-04 16:33:03 | [DynCMS.Core](https://www.nuget.org/packages/DynCMS.Core) | 0.1.0 | DynCMS | DynCMS core: content model, SQLite/SQL Server persistence, services, registries… |
| 2026-10-04 16:33:05 | [DynCMS.UI](https://www.nuget.org/packages/DynCMS.UI) | 0.1.0 | DynCMS | DynCMS Blazor components: admin back office, property editors and content rende… |
| 2026-10-04 16:33:06 | [DynCMS.Host](https://www.nuget.org/packages/DynCMS.Host) | 0.1.0 | DynCMS | DynCMS host: turns an empty ASP.NET Core web project into a running CMS (servic… |
| 2026-10-04 16:33:35 | [Stride.CrashReporter](https://www.nuget.org/packages/Stride.CrashReporter) | 5.0.0 | Stride contributors | Package Description |
| 2026-10-04 16:38:39 | [IronAuth.Domain](https://www.nuget.org/packages/IronAuth.Domain) | 0.2.2-preview | AfterBurner Team | Reusable authentication library for .NET APIs — Domain layer (entities, enums,… |
| 2026-10-04 16:38:40 | [IronAuth.AspNetCore](https://www.nuget.org/packages/IronAuth.AspNetCore) | 0.2.2-preview | AfterBurner Team | Reusable authentication library for .NET APIs — ASP.NET Core layer (controllers… |
| 2026-10-04 16:38:40 | [IronAuth.Infrastructure](https://www.nuget.org/packages/IronAuth.Infrastructure) | 0.2.2-preview | AfterBurner Team | Reusable authentication library for .NET APIs — Infrastructure layer (EF Core D… |
| 2026-10-04 16:38:41 | [IronAuth.Application](https://www.nuget.org/packages/IronAuth.Application) | 0.2.2-preview | AfterBurner Team | Reusable authentication library for .NET APIs — Application layer (service inte… |
| 2026-10-04 16:58:22 | [Mics.Cli](https://www.nuget.org/packages/Mics.Cli) | 0.1.0 | Eduardo Zitinho | Music In C Sharp. Turn C# source code into music. |
| 2026-10-04 17:03:20 | [Novolis.Testing.Playwright](https://www.nuget.org/packages/Novolis.Testing.Playwright) | 2026.1.1.49 | Novolis | Walkthrough video, frames, and HTML on top of TUnit.Playwright PageTest. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
