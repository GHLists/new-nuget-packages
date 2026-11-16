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

## Latest list — 2026-11-16 01:21 UTC

New packages created between 2026-11-16 00:19 UTC and 2026-11-16 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T01-21-35-223386Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 00:29:26 | [AdaskoTheBeAsT.Gu.Analyzers](https://www.nuget.org/packages/AdaskoTheBeAsT.Gu.Analyzers) | 2.0.3.300 | Johan Larsson, milleniumbug | Roslyn analyzers and fixes. |
| 2026-11-16 00:35:18 | [StudioXid.OmniAdapter](https://www.nuget.org/packages/StudioXid.OmniAdapter) | 0.1.0 | Studio XID, Inc. | Omni Adapter for .NET — join a Connect Omni stage from services, desktop apps a… |
| 2026-11-16 00:40:22 | [Refit.HttpClientFactory.Reflection](https://www.nuget.org/packages/Refit.HttpClientFactory.Reflection) | 17.0.0 | ReactiveUI and Contributors | The opt-in reflection registration methods for Refit and HttpClientFactory. Ins… |
| 2026-11-16 00:41:05 | [Joinery.Dovetail.ModularPipelines](https://www.nuget.org/packages/Joinery.Dovetail.ModularPipelines) | 0.6.0 | David Driscoll,Rocket Surgeon… | Applies Dovetail joints to a ModularPipelines PipelineBuilder: the configuratio… |
| 2026-11-16 00:41:07 | [Joinery.Dovetail.Sdk.Worker](https://www.nuget.org/packages/Joinery.Dovetail.Sdk.Worker) | 0.6.0 | David Driscoll,Rocket Surgeon… | Microsoft.NET.Sdk.Worker with Dovetail: a drop-in replacement for the Microsoft… |
| 2026-11-16 00:41:07 | [Joinery.Dovetail.Sdk.WebAssembly](https://www.nuget.org/packages/Joinery.Dovetail.Sdk.WebAssembly) | 0.6.0 | David Driscoll,Rocket Surgeon… | Microsoft.NET.Sdk.WebAssembly with Dovetail: a drop-in replacement for the Micr… |
| 2026-11-16 00:41:08 | [Joinery.Dovetail.Sdk.BlazorWebAssembly](https://www.nuget.org/packages/Joinery.Dovetail.Sdk.BlazorWebAssembly) | 0.6.0 | David Driscoll,Rocket Surgeon… | Microsoft.NET.Sdk.BlazorWebAssembly with Dovetail: a drop-in replacement for th… |
| 2026-11-16 00:41:10 | [Joinery.Dovetail.Sdk.Web](https://www.nuget.org/packages/Joinery.Dovetail.Sdk.Web) | 0.6.0 | David Driscoll,Rocket Surgeon… | Microsoft.NET.Sdk.Web with Dovetail: a drop-in replacement for the Microsoft SD… |
| 2026-11-16 00:41:11 | [Joinery.Dovetail.Sdk.Razor](https://www.nuget.org/packages/Joinery.Dovetail.Sdk.Razor) | 0.6.0 | David Driscoll,Rocket Surgeon… | Microsoft.NET.Sdk.Razor with Dovetail: a drop-in replacement for the Microsoft… |
| 2026-11-16 00:41:14 | [Joinery.Dovetail.Sdk.WindowsDesktop](https://www.nuget.org/packages/Joinery.Dovetail.Sdk.WindowsDesktop) | 0.6.0 | David Driscoll,Rocket Surgeon… | Microsoft.NET.Sdk.WindowsDesktop with Dovetail: a drop-in replacement for the M… |
| 2026-11-16 00:41:16 | [Joinery.Dovetail.Sdk.Aspire.AppHost](https://www.nuget.org/packages/Joinery.Dovetail.Sdk.Aspire.AppHost) | 0.6.0 | David Driscoll,Rocket Surgeon… | Aspire.AppHost.Sdk with Dovetail: a drop-in replacement for the Microsoft SDK t… |
| 2026-11-16 00:55:20 | [GrayMint.Identity](https://www.nuget.org/packages/GrayMint.Identity) | 1.0.2 | GrayMint | An OpenID Connect identity service with pools, tenants and apps: accounts by AS… |
| 2026-11-16 01:07:02 | [Winche.Core](https://www.nuget.org/packages/Winche.Core) | 1.0.0 | Ehsan Rashidi | What every Winche package shares: the error every Winche API answers with (Winc… |
| 2026-11-16 01:07:03 | [Winche.Core.AspNetCore](https://www.nuget.org/packages/Winche.Core.AspNetCore) | 1.0.0 | Ehsan Rashidi | Winche.Core for ASP.NET Core: who is calling (the request's claims, set once fo… |
| 2026-11-16 01:14:59 | [Eternet.Data.PostgreSql](https://www.nuget.org/packages/Eternet.Data.PostgreSql) | 1.0.0 | Eternet.Data.PostgreSql | Lets EF Core contexts and raw connections wait out a short PostgreSQL or PgBoun… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
