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

## Latest list — 2026-11-19 20:20 UTC

New packages created between 2026-11-19 19:20 UTC and 2026-11-19 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T20-20-29-984416Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 19:26:05 | [Khalid.Abuhakmeh](https://www.nuget.org/packages/Khalid.Abuhakmeh) | 2026.11.19 | Khalid Abuhakmeh | A fun, branded package: Khalid.Hello() prints a Spectre.Console calling card, a… |
| 2026-11-19 19:28:30 | [Feralin.Sdk](https://www.nuget.org/packages/Feralin.Sdk) | 0.1.0 | Feralin | Feralin .NET server SDK: UTP v1 events, consent passthrough, idempotent batches… |
| 2026-11-19 19:33:04 | [Feralin.Sdk.AspNetCore](https://www.nuget.org/packages/Feralin.Sdk.AspNetCore) | 0.1.0 | Feralin | ASP.NET Core dependency injection registration and graceful shutdown flush for… |
| 2026-11-19 19:37:00 | [DataStudio.Postgres.Diagnostics](https://www.nuget.org/packages/DataStudio.Postgres.Diagnostics) | 2.0.0 | Marko Lahma | The PostgreSQL diagnostics engine of Data Studio, with no ASP.NET Core: the hea… |
| 2026-11-19 19:37:01 | [DataStudio](https://www.nuget.org/packages/DataStudio) | 2.0.0 | Marko Lahma | The shell of Data Studio: an embeddable Blazor Server admin UI a host mounts on… |
| 2026-11-19 19:37:02 | [DataStudio.Postgres](https://www.nuget.org/packages/DataStudio.Postgres) | 2.0.0 | Marko Lahma | The Postgres pages of Data Studio: an embeddable Blazor Server admin UI for the… |
| 2026-11-19 19:37:03 | [DataStudio.Marten](https://www.nuget.org/packages/DataStudio.Marten) | 2.0.0 | Marko Lahma | An embeddable Blazor Server admin UI for MartenDB. Register it with services.Ad… |
| 2026-11-19 19:37:04 | [DataStudio.Kafka.Core](https://www.nuget.org/packages/DataStudio.Kafka.Core) | 2.0.0 | Marko Lahma | The Kafka engine of Data Studio, with no ASP.NET Core: the catalog, window reso… |
| 2026-11-19 19:37:05 | [DataStudio.Kafka](https://www.nuget.org/packages/DataStudio.Kafka) | 2.0.0 | Marko Lahma | Data Studio for Apache Kafka: the Kafka pages of Data Studio, beside the Marten… |
| 2026-11-19 19:37:06 | [DataStudio.Kafka.Wolverine](https://www.nuget.org/packages/DataStudio.Kafka.Wolverine) | 2.0.0 | Marko Lahma | DataStudio.Kafka.Wolverine lists the Kafka clusters and topics of a Wolverine a… |
| 2026-11-19 19:39:52 | [GeoView.Wpf](https://www.nuget.org/packages/GeoView.Wpf) | 1.0.0 | Matthew Muehlhauser | A reusable WebView2-based GeoView map control for WPF. |
| 2026-11-19 19:48:25 | [RailReader.Core.Vlm.Anthropic](https://www.nuget.org/packages/RailReader.Core.Vlm.Anthropic) | 0.94.0 | sjvrensburg | Anthropic (Claude) IVlmService implementation for RailReader, built on the offi… |
| 2026-11-19 19:51:30 | [Informix.Data](https://www.nuget.org/packages/Informix.Data) | 1.0.0 | robsosno | Experimental managed ADO.NET provider for IBM Informix (SQLI protocol). No CSDK… |
| 2026-11-19 19:58:37 | [RESTworld.AspNetCore.AutoMapper](https://www.nuget.org/packages/RESTworld.AspNetCore.AutoMapper) | 1.0.0 | wertzui | Package Description |
| 2026-11-19 19:58:41 | [RESTworld.Business.AutoMapper](https://www.nuget.org/packages/RESTworld.Business.AutoMapper) | 1.0.0 | wertzui | Package Description |
| 2026-11-19 20:07:21 | [GameshowPro.XKeys](https://www.nuget.org/packages/GameshowPro.XKeys) | 2.2.3 | Hamish Barjonas | P.I. Engineering X-keys devices as GameshowPro incoming trigger devices, with t… |
| 2026-11-19 20:07:23 | [GameshowPro.XKeys.Windows](https://www.nuget.org/packages/GameshowPro.XKeys.Windows) | 2.2.3 | Hamish Barjonas | P.I. Engineering X-keys devices as GameshowPro incoming trigger devices, with t… |
| 2026-11-19 20:11:20 | [AWSSDK.PartnerCentralMarketing](https://www.nuget.org/packages/AWSSDK.PartnerCentralMarketing) | 4.1.0 | Amazon Web Services | The Amazon Web Services SDK for .NET - Partner Central Marketing API |
| 2026-11-19 20:15:14 | [VirtoCommerce.ProductComparison.Data.MySql](https://www.nuget.org/packages/VirtoCommerce.ProductComparison.Data.MySql) | 3.1000.0 | VirtoCommerce.ProductComparis… | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
