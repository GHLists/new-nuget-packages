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

## Latest list — 2026-10-08 16:21 UTC

New packages created between 2026-10-08 15:20 UTC and 2026-10-08 16:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T16-21-27-519789Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 15:28:53 | [Dramaturge.MSTest](https://www.nuget.org/packages/Dramaturge.MSTest) | 0.0.1 | WebDriverBiDi.NET Committers | Base classes for MSTest tests that use Dramaturge: a browser launched once per… |
| 2026-10-08 15:28:54 | [Dramaturge.Browsers](https://www.nuget.org/packages/Dramaturge.Browsers) | 0.0.1 | WebDriverBiDi.NET Committers | Locates, downloads, and launches browsers for automation over WebDriver BiDi, w… |
| 2026-10-08 15:28:55 | [Dramaturge.TUnit](https://www.nuget.org/packages/Dramaturge.TUnit) | 0.0.1 | WebDriverBiDi.NET Committers | Base classes for TUnit tests that use Dramaturge: a browser launched once per t… |
| 2026-10-08 15:28:56 | [Dramaturge](https://www.nuget.org/packages/Dramaturge) | 0.0.1 | WebDriverBiDi.NET Committers | A high-level browser automation API with automatic waiting, built on WebDriver… |
| 2026-10-08 15:28:57 | [Dramaturge.NUnit](https://www.nuget.org/packages/Dramaturge.NUnit) | 0.0.1 | WebDriverBiDi.NET Committers | Base classes for NUnit tests that use Dramaturge: a browser launched once per t… |
| 2026-10-08 15:28:58 | [Dramaturge.Xunit](https://www.nuget.org/packages/Dramaturge.Xunit) | 0.0.1 | WebDriverBiDi.NET Committers | Base classes for xUnit v3 tests that use Dramaturge: a browser launched once pe… |
| 2026-10-08 15:28:59 | [Dramaturge.Tool](https://www.nuget.org/packages/Dramaturge.Tool) | 0.0.1 | WebDriverBiDi.NET Committers | The dramaturge command-line tool: installs, lists, and removes the browsers and… |
| 2026-10-08 15:43:46 | [LilyDesignSystem.Blazor.MenuPicker](https://www.nuget.org/packages/LilyDesignSystem.Blazor.MenuPicker) | 0.1.0 | Joel Parker Henderson | Lily Design System Blazor menu picker: an icon button (a hamburger icon) openin… |
| 2026-10-08 15:43:49 | [LilyDesignSystem.Blazor.SettingsPicker](https://www.nuget.org/packages/LilyDesignSystem.Blazor.SettingsPicker) | 0.1.0 | Joel Parker Henderson | Lily Design System Blazor settings picker: an icon button (a cog icon) opening… |
| 2026-10-08 15:46:44 | [FakeUserAgents.NET](https://www.nuget.org/packages/FakeUserAgents.NET) | 1.0.0 | Khilaraj Regmi | High-performance .NET library for generating and rotating realistic browser Use… |
| 2026-10-08 16:01:48 | [BitFive.Templates](https://www.nuget.org/packages/BitFive.Templates) | 1.0.0 | BitDEVil2K16 | Projekt-Templates von BitFive |
| 2026-10-08 16:03:24 | [Umbraco.Community.Search.Provider.AzureAI](https://www.nuget.org/packages/Umbraco.Community.Search.Provider.AzureAI) | 18.0.0 | Busra Sengul | An Azure AI Search provider for Umbraco Search. Indexes Umbraco content in Azur… |
| 2026-10-08 16:09:32 | [StockSharp.Odysseus.Cli](https://www.nuget.org/packages/StockSharp.Odysseus.Cli) | 1.0.0 | StockSharp | Local quantitative research with StockSharp, including the worker and deploymen… |
| 2026-10-08 16:09:34 | [StockSharp.Odysseus.Mcp](https://www.nuget.org/packages/StockSharp.Odysseus.Mcp) | 1.0.0 | StockSharp | Local quantitative research with StockSharp, including the worker and deploymen… |
| 2026-10-08 16:10:35 | [Marey.Fields](https://www.nuget.org/packages/Marey.Fields) | 0.4.0 | Marey contributors | Fields for Marey: scalar and vector fields on dimensioned planes, sampled onto… |
| 2026-10-08 16:10:37 | [Marey.Interact](https://www.nuget.org/packages/Marey.Interact) | 0.4.0 | Marey contributors | Interaction for Marey: typed controls (a slider over kelvin hands the view kelv… |
| 2026-10-08 16:15:21 | [Dogabot.Sdk](https://www.nuget.org/packages/Dogabot.Sdk) | 0.1.0 | dogabot | Official dogabot REST API SDK for .NET |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
