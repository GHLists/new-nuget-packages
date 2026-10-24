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

## Latest list — 2026-10-24 10:21 UTC

New packages created between 2026-10-24 09:19 UTC and 2026-10-24 10:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T10-21-33-449944Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 09:20:42 | [DWIS.RigOS.Contracts.WellBoreArchitecture](https://www.nuget.org/packages/DWIS.RigOS.Contracts.WellBoreArchitecture) | 1.0.0 | DWIS.RigOS.Contracts.WellBore… | Versioned OSDC WellBoreArchitecture Blackboard JSON schema, metadata and docume… |
| 2026-10-24 09:33:49 | [Wpf.Zen.Ui](https://www.nuget.org/packages/Wpf.Zen.Ui) | 1.0.0 | thezendev.com | WPF controls, themes, navigation, and dialogs for .NET Framework 4.7.2 and .NET… |
| 2026-10-24 09:33:59 | [Wpf.Zen.Ui.DependencyInjection](https://www.nuget.org/packages/Wpf.Zen.Ui.DependencyInjection) | 1.0.0 | thezendev.com | Dependency injection for the WPF Zen UI. |
| 2026-10-24 09:51:18 | [SlashMark.NuGetSuite](https://www.nuget.org/packages/SlashMark.NuGetSuite) | 1.0.0 | Slash Mark IT Solutions | .NET Package Intelligence Suite: 30 advanced terminal tools for NuGet supply-ch… |
| 2026-10-24 09:57:33 | [OfficeIMO.JavaScript.Assets](https://www.nuget.org/packages/OfficeIMO.JavaScript.Assets) | 3.5.2 | Przemyslaw Klys | Embedded classic scripts and standalone modules built from the OfficeIMO TypeSc… |
| 2026-10-24 10:00:33 | [Tarjamot](https://www.nuget.org/packages/Tarjamot) | 0.1.1 | Filip Navara | Local machine translation with the Firefox Translations (Bergamot) models in pu… |
| 2026-10-24 10:05:43 | [Arc56.Generated.Purnesh24.Pit-Crew](https://www.nuget.org/packages/Arc56.Generated.Purnesh24.Pit-Crew) | 1.0.1.2026102410 | Purnesh24 | Generated ARC-56 Algorand smart-contract clients for Purnesh24/Pit-Crew. |
| 2026-10-24 10:05:58 | [Arc56.Generated.vyas-t.algosphere](https://www.nuget.org/packages/Arc56.Generated.vyas-t.algosphere) | 1.0.1.2026102410 | vyas-t | Generated ARC-56 Algorand smart-contract clients for vyas-t/algosphere. |
| 2026-10-24 10:06:05 | [MitMediator.InMemoryCache.Abstractions](https://www.nuget.org/packages/MitMediator.InMemoryCache.Abstractions) | 10.0.0-alfa | MitMediator.InMemoryCache.Abs… | An attribute-driven in-memory caching extension for the MitMediator |
| 2026-10-24 10:10:42 | [Juice.EventBus.NATS](https://www.nuget.org/packages/Juice.EventBus.NATS) | 10.5.1 | Creatorflow.io | NATS JetStream implementation for EventBus |
| 2026-10-24 10:10:49 | [Bsa.SyslogNet.Client](https://www.nuget.org/packages/Bsa.SyslogNet.Client) | 6.0.0 | Andrew Smith,Bsa | .NET 6 / .NET Standard 2.0 fork of SyslogNet.Client — .Net Syslog client. Suppo… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
