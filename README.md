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

## Latest list — 2026-10-09 18:20 UTC

New packages created between 2026-10-09 17:20 UTC and 2026-10-09 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T18-20-55-186976Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 17:22:00 | [KnOwl.WolfAuth](https://www.nuget.org/packages/KnOwl.WolfAuth) | 2.3.0 | Elysium Coding | WolfAuth authentication integration helpers for KnOwl hosts. |
| 2026-10-09 17:36:26 | [Pacem.Domotics.Onvif](https://www.nuget.org/packages/Pacem.Domotics.Onvif) | 0.10.18-venn | Cristian Merighi | Pacem domotics: ONVIF cameras on the LAN — WS-Discovery, their streams and snap… |
| 2026-10-09 17:41:44 | [Devlooped.DataAnnotations.NativeValidation](https://www.nuget.org/packages/Devlooped.DataAnnotations.NativeValidation) | 0.1.0-alpha | Daniel Cazzulino | AOT-safe validation for System.ComponentModel.DataAnnotations attributes. |
| 2026-10-09 17:44:19 | [Glimpse.Capture](https://www.nuget.org/packages/Glimpse.Capture) | 0.1.0 | Purin Tavilsup | Render any UI or diagram to a PNG so an agent can see it, critique it, and iter… |
| 2026-10-09 17:55:22 | [DataForger.CountryProviders](https://www.nuget.org/packages/DataForger.CountryProviders) | 0.1.0 | DataForger Contributors | Country-specific data providers for DataForger (Portugal, Spain, United Kingdom… |
| 2026-10-09 17:55:22 | [DataForger.Generators](https://www.nuget.org/packages/DataForger.Generators) | 0.1.0 | DataForger Contributors | Built-in entity generators for DataForger (person, address, company, customer,… |
| 2026-10-09 17:55:23 | [DataForger.Abstractions](https://www.nuget.org/packages/DataForger.Abstractions) | 0.1.0 | DataForger Contributors | Core abstractions, domain models and extensibility contracts for DataForger, a… |
| 2026-10-09 17:55:23 | [DataForger.Extensions](https://www.nuget.org/packages/DataForger.Extensions) | 0.1.0 | DataForger Contributors | Convenience extensions for DataForger, including string-based deterministic see… |
| 2026-10-09 17:55:24 | [DataForger](https://www.nuget.org/packages/DataForger) | 0.1.0 | DataForger Contributors | DataForger is a lightweight, extensible, enterprise-ready synthetic test data g… |
| 2026-10-09 18:11:39 | [VerifyBlind.Server](https://www.nuget.org/packages/VerifyBlind.Server) | 1.0.0 | VerifyBlind | Server-side verification of VerifyBlind result tokens, webhooks and callbacks f… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
