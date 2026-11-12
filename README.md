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

## Latest list — 2026-11-12 19:21 UTC

New packages created between 2026-11-12 18:21 UTC and 2026-11-12 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T19-21-19-776502Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 18:23:08 | [Webority.Analytics.Diagnostics](https://www.nuget.org/packages/Webority.Analytics.Diagnostics) | 0.39.0 | Webority Technologies | Server analytics health for the Webority Diagnostics console: one section that… |
| 2026-11-12 18:25:12 | [Joinery.Dovetail](https://www.nuget.org/packages/Joinery.Dovetail) | 0.5.0 | David Driscoll,Rocket Surgeon… | Adds support for loading configuration, services, logging, command line and mor… |
| 2026-11-12 18:25:13 | [Joinery.Dovetail.Configuration.Yaml](https://www.nuget.org/packages/Joinery.Dovetail.Configuration.Yaml) | 0.5.0 | David Driscoll,Rocket Surgeon… | Adds support for loading yaml configuration files |
| 2026-11-12 18:25:17 | [Joinery.Dovetail.Configuration.Json](https://www.nuget.org/packages/Joinery.Dovetail.Configuration.Json) | 0.5.0 | David Driscoll,Rocket Surgeon… | Adds support for loading json configuration files |
| 2026-11-12 18:25:18 | [Joinery.Dovetail.Configuration.Toml](https://www.nuget.org/packages/Joinery.Dovetail.Configuration.Toml) | 0.5.0 | David Driscoll,Rocket Surgeon… | Adds support for loading toml configuration files |
| 2026-11-12 18:48:52 | [AbpCluster.Sites](https://www.nuget.org/packages/AbpCluster.Sites) | 0.2.1 | AbpCluster contributors | AbpCluster.Sites: two sites for an ABP site on .NET 10 and PostgreSQL, one acti… |
| 2026-11-12 18:49:43 | [RestFetch.Common](https://www.nuget.org/packages/RestFetch.Common) | 0.2.8 | al0rid4l | RestFetch common symbols definition. |
| 2026-11-12 19:01:32 | [Bashka.Helpers](https://www.nuget.org/packages/Bashka.Helpers) | 1.0.1 | Evgeny Gorbovoy | Package Description |
| 2026-11-12 19:01:33 | [Bashka.Launcher](https://www.nuget.org/packages/Bashka.Launcher) | 1.0.1 | Evgeny Gorbovoy | Package Description |
| 2026-11-12 19:01:33 | [Bashka.Plugins](https://www.nuget.org/packages/Bashka.Plugins) | 1.0.1 | Evgeny Gorbovoy | Shared Bashka plugin APIs and built-in plugins. |
| 2026-11-12 19:01:34 | [Bashka.Plugins.Archives](https://www.nuget.org/packages/Bashka.Plugins.Archives) | 1.0.1 | Evgeny Gorbovoy | Package Description |
| 2026-11-12 19:01:35 | [Bashka.Plugins.Archives.Bsdtar](https://www.nuget.org/packages/Bashka.Plugins.Archives.Bsdtar) | 1.0.1 | Evgeny Gorbovoy | Package Description |
| 2026-11-12 19:01:35 | [Bashka.Plugins.Core](https://www.nuget.org/packages/Bashka.Plugins.Core) | 1.0.1 | Evgeny Gorbovoy | Package Description |
| 2026-11-12 19:01:36 | [Bashka.Plugins.Foundation](https://www.nuget.org/packages/Bashka.Plugins.Foundation) | 1.0.1 | Evgeny Gorbovoy | Package Description |
| 2026-11-12 19:01:36 | [Bashka.Templates](https://www.nuget.org/packages/Bashka.Templates) | 1.0.1 | Evgeny Gorbovoy | Executable, packable Bashka plugin project template. |
| 2026-11-12 19:02:09 | [XDev.Extensions](https://www.nuget.org/packages/XDev.Extensions) | 0.1.0-alpha001 | jasells,XDevApps | Dependency-free extension methods for ObservableCollection<T> and IList<T>: key… |
| 2026-11-12 19:08:47 | [Musoq.Formatter](https://www.nuget.org/packages/Musoq.Formatter) | 17.0.17 | Jakub Puchała | Source-preserving formatting of complete raw Musoq scripts using only Musoq.Par… |
| 2026-11-12 19:08:49 | [Musoq.Benchmarks.Scenarios](https://www.nuget.org/packages/Musoq.Benchmarks.Scenarios) | 17.0.17 | Jakub Puchała | Reusable deterministic SQL workloads and typed benchmark fixtures for Musoq hos… |
| 2026-11-12 19:11:27 | [Shiny.AiConversation.AgUi](https://www.nuget.org/packages/Shiny.AiConversation.AgUi) | 3.1.0-beta-0001 | Allan Ritchie | AG-UI for Shiny AI Conversation - run a session as an AG-UI event stream (so AG… |
| 2026-11-12 19:14:39 | [NymBroker.Outbox.SqlServer](https://www.nuget.org/packages/NymBroker.Outbox.SqlServer) | 0.23.0 | nymankla@gmail.com | Transactional outbox in SQL Server for NymBroker: post messages in your own dat… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
