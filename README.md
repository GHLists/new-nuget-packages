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

## Latest list — 2026-10-01 07:18 UTC

New packages created between 2026-10-01 06:19 UTC and 2026-10-01 07:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T07-18-56-10299Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 06:20:22 | [Prism8.Avalonia](https://www.nuget.org/packages/Prism8.Avalonia) | 8.1.97.12100 | Damian Suess, various contrib… | Prism.Avalonia is a fully open source version of the Prism guidance originally… |
| 2026-10-01 06:21:04 | [Prism8.DryIoc.Avalonia](https://www.nuget.org/packages/Prism8.DryIoc.Avalonia) | 8.1.97.12100 | Damian Suess, various contrib… | This extension is used to build Prism.Avalonia applications based on DryIoc. Us… |
| 2026-10-01 06:29:58 | [Mcps.Server.AspNetCore](https://www.nuget.org/packages/Mcps.Server.AspNetCore) | 1.0.0 | Vishram Singh | Streamable HTTP transport for Mcps.Server: host an MCP server in ASP.NET Core w… |
| 2026-10-01 06:29:58 | [Mcps.Server](https://www.nuget.org/packages/Mcps.Server) | 1.0.0 | Vishram Singh | A lightweight library for building Model Context Protocol (MCP) servers in .NET… |
| 2026-10-01 06:38:10 | [SLVZ.Billing](https://www.nuget.org/packages/SLVZ.Billing) | 1.0.0 | Ashkan SLVZ | A lightweight library for Android developers that make you able to purchase in… |
| 2026-10-01 06:45:35 | [TiverGroup.PluginUpdater](https://www.nuget.org/packages/TiverGroup.PluginUpdater) | 2.2.1 | sb1rnik | Methods to connect with server using URL, check versions with JSONs and downloa… |
| 2026-10-01 07:04:30 | [MajWebSocket](https://www.nuget.org/packages/MajWebSocket) | 0.0.1 | MajWebSocket | Majdata WebSocket wire-protocol types. |
| 2026-10-01 07:04:57 | [SeoToolkit.Umbraco.Deploy](https://www.nuget.org/packages/SeoToolkit.Umbraco.Deploy) | 1.0.0-beta1 | SeoToolkit.Umbraco.Deploy | Connectors to transfer SeoToolkit settings and content data with Umbraco Deploy |
| 2026-10-01 07:06:21 | [AceReports.MSTest](https://www.nuget.org/packages/AceReports.MSTest) | 1.0.0 | Harshad Lambate | Turn MSTest runs into actionable HTML reports with zero code in your tests. Aut… |
| 2026-10-01 07:07:16 | [AceReports.NUnit](https://www.nuget.org/packages/AceReports.NUnit) | 1.0.0 | Harshad Lambate | Turn NUnit test runs into actionable HTML reports with zero code in your tests.… |
| 2026-10-01 07:07:58 | [AceReports.Reqnroll](https://www.nuget.org/packages/AceReports.Reqnroll) | 1.0.0 | Harshad Lambate | Turn Reqnroll (Gherkin/BDD) runs into actionable HTML reports with zero code in… |
| 2026-10-01 07:08:42 | [AceReports.Xunit](https://www.nuget.org/packages/AceReports.Xunit) | 1.0.0 | Harshad Lambate | Turn xUnit test runs into actionable HTML reports with zero code in your tests.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
