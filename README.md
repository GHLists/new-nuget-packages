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

## Latest list — 2026-11-04 23:20 UTC

New packages created between 2026-11-04 22:20 UTC and 2026-11-04 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T23-20-25-396694Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 22:39:46 | [Webority.Chat.Support.Admin](https://www.nuget.org/packages/Webority.Chat.Support.Admin) | 0.132.0 | Webority Technologies | The live agent console for Webority Chat support, under a ChatSupport area the… |
| 2026-11-04 22:48:20 | [Flowrensic](https://www.nuget.org/packages/Flowrensic) | 0.6.44 | Flowrensic | Activity interceptor and client for Temporal .NET workers, for use with Flowren… |
| 2026-11-04 22:48:50 | [Typo.Analyzers](https://www.nuget.org/packages/Typo.Analyzers) | 0.1.0 | Nikolay Zdravkov | Roslyn analyzers that find copy-paste and typo bugs. |
| 2026-11-04 22:56:15 | [Tamp.McpScanner](https://www.nuget.org/packages/Tamp.McpScanner) | 0.1.0 | Scott Singleton | Tamp wrapper for Cisco's mcp-scanner. Scans MCP servers (remote, static tool ma… |
| 2026-11-04 22:59:14 | [TannerGooding.SourceBrowser](https://www.nuget.org/packages/TannerGooding.SourceBrowser) | 1.1.0 | tannergooding, kirillosenkov,… | Generates a static HTML website from a managed Visual Studio solution that allo… |
| 2026-11-04 23:06:35 | [SeleniumToPlayWright](https://www.nuget.org/packages/SeleniumToPlayWright) | 1.2.0.26309 | SeleniumToPlayWright | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
