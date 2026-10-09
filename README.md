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

## Latest list — 2026-10-09 17:20 UTC

New packages created between 2026-10-09 16:21 UTC and 2026-10-09 17:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T17-20-17-563909Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 16:21:18 | [Cogworks.Umbraco.FormsGuard.UmbracoAI](https://www.nuget.org/packages/Cogworks.Umbraco.FormsGuard.UmbracoAI) | 1.0.0 | Cogworks | Optional Forms Guard decision provider that answers spam and triage questions w… |
| 2026-10-09 16:30:57 | [Doka.NestedSet](https://www.nuget.org/packages/Doka.NestedSet) | 10.0.0 | Dominic Kalkbrenner | ORM-independent nested-set bounds and node predicates. |
| 2026-10-09 16:30:58 | [Doka.EntityFrameworkCore.NestedSet](https://www.nuget.org/packages/Doka.EntityFrameworkCore.NestedSet) | 10.0.0 | Dominic Kalkbrenner | Nested-set hierarchy operations for Entity Framework Core. |
| 2026-10-09 16:42:25 | [SlideRule.Cli](https://www.nuget.org/packages/SlideRule.Cli) | 0.1.0 | Andrew Gray | SlideRule is a .NET architecture checker that enforces one C# spec and renders… |
| 2026-10-09 16:42:25 | [SlideRule.Analyzers](https://www.nuget.org/packages/SlideRule.Analyzers) | 0.1.0 | Andrew Gray | SlideRule.Analyzers is the SlideRule build analyzer. It reports a broken archit… |
| 2026-10-09 16:42:26 | [SlideRule](https://www.nuget.org/packages/SlideRule) | 0.1.0 | Andrew Gray | SlideRule is the spec contract: the fluent builder and reified rule model an ar… |
| 2026-10-09 16:42:27 | [SlideRule.Xunit](https://www.nuget.org/packages/SlideRule.Xunit) | 0.1.0 | Andrew Gray | SlideRule.Xunit is the SlideRule xUnit adapter: every rule in an architecture s… |
| 2026-10-09 16:45:55 | [SignalGate](https://www.nuget.org/packages/SignalGate) | 0.1.0 | SignalGate | Official .NET backend SDK for SignalGate: send fraud checks and events from you… |
| 2026-10-09 16:51:16 | [PixieLib](https://www.nuget.org/packages/PixieLib) | 0.1.0 | Rafael Sakamoto | Primitives and math with the same names, memory layout and bits as their C++ si… |
| 2026-10-09 16:58:42 | [DataForge.Generators](https://www.nuget.org/packages/DataForge.Generators) | 0.1.0 | DataForge Contributors | Built-in entity generators for DataForge (person, address, company, customer, c… |
| 2026-10-09 16:58:42 | [DataForge.CountryProviders](https://www.nuget.org/packages/DataForge.CountryProviders) | 0.1.0 | DataForge Contributors | Country-specific data providers for DataForge (Portugal, Spain, United Kingdom,… |
| 2026-10-09 17:00:02 | [DataForge.Abstractions](https://www.nuget.org/packages/DataForge.Abstractions) | 0.1.0 | DataForge Contributors | Core abstractions, domain models and extensibility contracts for DataForge, a d… |
| 2026-10-09 17:00:03 | [DataForge.Extensions](https://www.nuget.org/packages/DataForge.Extensions) | 0.1.0 | DataForge Contributors | Convenience extensions for DataForge, including string-based deterministic seed… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
