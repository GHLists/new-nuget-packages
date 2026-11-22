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

## Latest list — 2026-11-22 20:19 UTC

New packages created between 2026-11-22 19:19 UTC and 2026-11-22 20:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T20-19-57-154033Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 19:23:19 | [TheNerdCollective.Integrations.Mollie](https://www.nuget.org/packages/TheNerdCollective.Integrations.Mollie) | 0.1.0 | The Nerd Collective | Typed Mollie Payments API client and dependency injection integration. |
| 2026-11-22 19:23:54 | [TheNerdCollective.Cli.Mollie](https://www.nuget.org/packages/TheNerdCollective.Cli.Mollie) | 0.1.0 | The Nerd Collective | Mollie Payments API CLI and local payment-template catalog. |
| 2026-11-22 19:30:04 | [WxKit.Native.linux-arm64](https://www.nuget.org/packages/WxKit.Native.linux-arm64) | 0.1.0 | Quin Gillespie | wxWidgets and the WxKit shim for linux-arm64: a shared library, and static libr… |
| 2026-11-22 19:30:06 | [WxKit.Native.linux-x64](https://www.nuget.org/packages/WxKit.Native.linux-x64) | 0.1.0 | Quin Gillespie | wxWidgets and the WxKit shim for linux-x64: a shared library, and static librar… |
| 2026-11-22 19:30:08 | [WxKit.Native.osx-arm64](https://www.nuget.org/packages/WxKit.Native.osx-arm64) | 0.1.0 | Quin Gillespie | wxWidgets and the WxKit shim for osx-arm64: a shared library, and static librar… |
| 2026-11-22 19:30:09 | [WxKit.Native.osx-x64](https://www.nuget.org/packages/WxKit.Native.osx-x64) | 0.1.0 | Quin Gillespie | wxWidgets and the WxKit shim for osx-x64: a shared library, and static librarie… |
| 2026-11-22 19:30:12 | [WxKit.Native.win-arm64](https://www.nuget.org/packages/WxKit.Native.win-arm64) | 0.1.0 | Quin Gillespie | wxWidgets and the WxKit shim for win-arm64: a shared library, and static librar… |
| 2026-11-22 19:30:14 | [WxKit.Native.win-x64](https://www.nuget.org/packages/WxKit.Native.win-x64) | 0.1.0 | Quin Gillespie | wxWidgets and the WxKit shim for win-x64: a shared library, and static librarie… |
| 2026-11-22 19:30:15 | [WxKit](https://www.nuget.org/packages/WxKit) | 0.1.0 | Quin Gillespie | .NET bindings to wxWidgets, for native desktop applications. Links wxWidgets in… |
| 2026-11-22 19:30:17 | [WxKit.FSharp](https://www.nuget.org/packages/WxKit.FSharp) | 0.1.0 | Quin Gillespie | WxKit for F#: translation functions that gettext finds, and computation express… |
| 2026-11-22 19:30:18 | [WxKit.Templates](https://www.nuget.org/packages/WxKit.Templates) | 0.1.0 | Quin Gillespie | dotnet new templates for WxKit: a desktop application with native, accessible c… |
| 2026-11-22 19:48:08 | [Marqdouj.DotNet.Gaming.PlayingCards](https://www.nuget.org/packages/Marqdouj.DotNet.Gaming.PlayingCards) | 11.0.0 | Douglas Marquardt | .NET library for a deck of playing cards |
| 2026-11-22 20:08:28 | [DylansTechStack.Pro.Tenancy.Abstractions](https://www.nuget.org/packages/DylansTechStack.Pro.Tenancy.Abstractions) | 0.6.0 | Dylan Snel | Tenancy's markers for domain classes, such as [OfTenant] on the property that s… |
| 2026-11-22 20:08:30 | [DylansTechStack.Pro.Tenancy.AspNetCore](https://www.nuget.org/packages/DylansTechStack.Pro.Tenancy.AspNetCore) | 0.6.0 | Dylan Snel | Tenancy in an ASP.NET Core host: the middleware UseTenantSelection reads the te… |
| 2026-11-22 20:08:32 | [DylansTechStack.Pro.Tenancy](https://www.nuget.org/packages/DylansTechStack.Pro.Tenancy) | 0.6.0 | Dylan Snel | Tenants, their organization tree, seats with placements and role grants, roles… |
| 2026-11-22 20:08:34 | [DylansTechStack.Pro.Tenancy.EntityFramework](https://www.nuget.org/packages/DylansTechStack.Pro.Tenancy.EntityFramework) | 0.6.0 | Dylan Snel | Stores Tenancy with Entity Framework Core: the tables of the application's tena… |
| 2026-11-22 20:08:37 | [DylansTechStack.Pro.Tenancy.Postgres](https://www.nuget.org/packages/DylansTechStack.Pro.Tenancy.Postgres) | 0.6.0 | Dylan Snel | Tenancy on Postgres with row level security: the tenant of the current Tenancy… |
| 2026-11-22 20:08:40 | [DylansTechStack.Pro.Membership.Abstractions](https://www.nuget.org/packages/DylansTechStack.Pro.Membership.Abstractions) | 0.6.0 | Dylan Snel | Membership's markers for domain classes, such as [At] on the property that says… |
| 2026-11-22 20:08:43 | [DylansTechStack.Pro.Membership](https://www.nuget.org/packages/DylansTechStack.Pro.Membership) | 0.6.0 | Dylan Snel | Access to a resource through its members: a member class an application declare… |
| 2026-11-22 20:08:45 | [DylansTechStack.Pro.Membership.Postgres](https://www.nuget.org/packages/DylansTechStack.Pro.Membership.Postgres) | 0.6.0 | Dylan Snel | Membership on Postgres with row level security: the four set functions that ans… |
| 2026-11-22 20:08:48 | [DylansTechStack.Pro.Membership.EntityFramework](https://www.nuget.org/packages/DylansTechStack.Pro.Membership.EntityFramework) | 0.6.0 | Dylan Snel | Stores Membership with Entity Framework Core: the two member tables of a resour… |
| 2026-11-22 20:08:50 | [DylansTechStack.Pro.Licensing](https://www.nuget.org/packages/DylansTechStack.Pro.Licensing) | 0.6.0 | Dylan Snel | Reads the DTS Pro licence key from the configuration at start-up, checks its si… |
| 2026-11-22 20:10:09 | [Close.DotNet](https://www.nuget.org/packages/Close.DotNet) | 1.0.0 | Peter Schroeder | Independent .NET SDK for the Close CRM REST API. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
