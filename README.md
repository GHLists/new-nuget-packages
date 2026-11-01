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

## Latest list — 2026-11-01 06:20 UTC

New packages created between 2026-11-01 05:20 UTC and 2026-11-01 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T06-20-27-109809Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 05:29:47 | [AurorisNet.InteractiveReports](https://www.nuget.org/packages/AurorisNet.InteractiveReports) | 1.0.1 | auroris | JSON and browser client adapter for Interactive Reports: REST routes, saved rep… |
| 2026-11-01 05:29:47 | [AurorisNet.InteractiveReports.AspNetCore](https://www.nuget.org/packages/AurorisNet.InteractiveReports.AspNetCore) | 1.0.1 | auroris | Interactive Reports server integration for ASP.NET Core: configuration, persist… |
| 2026-11-01 05:29:48 | [AurorisNet.InteractiveReports.Client.FileDownload](https://www.nuget.org/packages/AurorisNet.InteractiveReports.Client.FileDownload) | 1.0.1 | auroris | File-download client adapter for Interactive Reports, including CSV and self-co… |
| 2026-11-01 05:29:49 | [AurorisNet.InteractiveReports.Client.GraphQL](https://www.nuget.org/packages/AurorisNet.InteractiveReports.Client.GraphQL) | 1.0.1 | auroris | GraphQL.NET client adapter for executing saved Interactive Report documents thr… |
| 2026-11-01 05:29:49 | [AurorisNet.InteractiveReports.Core](https://www.nuget.org/packages/AurorisNet.InteractiveReports.Core) | 1.0.1 | auroris | Interactive Reports engine: report state model, validation, portable expression… |
| 2026-11-01 05:32:52 | [AurorisNet.Pressroom.Client](https://www.nuget.org/packages/AurorisNet.Pressroom.Client) | 1.1.2 | Pressroom | HTTP client for Pressroom. Does not install or depend on Playwright. |
| 2026-11-01 05:48:30 | [Disharmony](https://www.nuget.org/packages/Disharmony) | 1.0.0 | Ross Morgan-Linial | A Harmony-based framework for patching methods and individual calls, member acc… |
| 2026-11-01 05:57:43 | [Leaf.Sdk](https://www.nuget.org/packages/Leaf.Sdk) | 0.1.6 | RedBamboo Interactive | The plugin contract for RedLeaf extensions. A plugin references only this packa… |
| 2026-11-01 06:01:14 | [AurorisNet.ActiveDirectory](https://www.nuget.org/packages/AurorisNet.ActiveDirectory) | 1.0.1 | AurorisNet | Windows Active Directory wrappers used by AurorisNet.IdentityServer, with helpe… |
| 2026-11-01 06:01:16 | [AurorisNet.IdentityServer](https://www.nuget.org/packages/AurorisNet.IdentityServer) | 1.0.1 | AurorisNet | Embeddable OpenID Connect server for ASP.NET Core, backed by Active Directory,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
