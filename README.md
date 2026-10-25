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

## Latest list — 2026-10-25 19:19 UTC

New packages created between 2026-10-25 18:20 UTC and 2026-10-25 19:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T19-19-49-48843Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 18:29:18 | [PCox.Authentication.EntityFrameworkCore](https://www.nuget.org/packages/PCox.Authentication.EntityFrameworkCore) | 0.1.0 | Peter Cox | Shared ASP.NET Core authentication and persisted browser sessions. |
| 2026-10-25 18:29:19 | [PCox.Authentication](https://www.nuget.org/packages/PCox.Authentication) | 0.1.0 | Peter Cox | Shared ASP.NET Core authentication and persisted browser sessions. |
| 2026-10-25 18:29:50 | [Kododo.MonitorWay](https://www.nuget.org/packages/Kododo.MonitorWay) | 2.0.0-preview | Kododo | The telemetry of an ASP.NET Core application in a panel served by the applicati… |
| 2026-10-25 18:29:51 | [Kododo.MonitorWay.Core](https://www.nuget.org/packages/Kododo.MonitorWay.Core) | 2.0.0-preview | Kododo | Core model of MonitorWay: log entries, traces and their queries. |
| 2026-10-25 18:29:52 | [Kododo.MonitorWay.Mcp](https://www.nuget.org/packages/Kododo.MonitorWay.Mcp) | 2.0.0-preview | Kododo | Lets AI agents read the telemetry kept by MonitorWay over the Model Context Pro… |
| 2026-10-25 18:29:52 | [Kododo.MonitorWay.Otlp](https://www.nuget.org/packages/Kododo.MonitorWay.Otlp) | 2.0.0-preview | Kododo | OTLP/HTTP receiver of MonitorWay: other services, in any language, send their t… |
| 2026-10-25 18:29:53 | [Kododo.MonitorWay.UI](https://www.nuget.org/packages/Kododo.MonitorWay.UI) | 2.0.0-preview | Kododo | Web UI of MonitorWay: the telemetry of the application in a panel served by the… |
| 2026-10-25 18:35:22 | [PulseAnalytics.DataIngestor.Contracts](https://www.nuget.org/packages/PulseAnalytics.DataIngestor.Contracts) | 1.0.0 | Ilya Ovsyannikov | Message contracts of the events published by the Pulse Analytics Data Ingestor. |
| 2026-10-25 18:37:44 | [Net.Leksi.Mvc.RegexRouting](https://www.nuget.org/packages/Net.Leksi.Mvc.RegexRouting) | 1.0.0 | Alexey Zakharov <leksi@leksi.… | The package is designed for routing in ASP.NET Core MVC using regular expressio… |
| 2026-10-25 18:38:04 | [TickerQ.Integrations](https://www.nuget.org/packages/TickerQ.Integrations) | 10.5.0 | Arcenox LLC | Optional Slack, Teams and custom webhook integrations for TickerQ, with dynamic… |
| 2026-10-25 18:38:09 | [TickerQ.MongoDB](https://www.nuget.org/packages/TickerQ.MongoDB) | 11.5.0 | Arcenox,Alex Brown | MongoDB persistence provider for TickerQ. Uses the official MongoDB.Driver — no… |
| 2026-10-25 18:47:58 | [Nccurry.MtgMcp.linux-x64](https://www.nuget.org/packages/Nccurry.MtgMcp.linux-x64) | 0.10.0 | Nick Curry | An evidence-first C#/.NET MCP server with revisioned local Magic: The Gathering… |
| 2026-10-25 18:48:00 | [Nccurry.MtgMcp.osx-arm64](https://www.nuget.org/packages/Nccurry.MtgMcp.osx-arm64) | 0.10.0 | Nick Curry | An evidence-first C#/.NET MCP server with revisioned local Magic: The Gathering… |
| 2026-10-25 18:48:03 | [Nccurry.MtgMcp.win-x64](https://www.nuget.org/packages/Nccurry.MtgMcp.win-x64) | 0.10.0 | Nick Curry | An evidence-first C#/.NET MCP server with revisioned local Magic: The Gathering… |
| 2026-10-25 18:50:29 | [Hassle.Free.Galactic.Api](https://www.nuget.org/packages/Hassle.Free.Galactic.Api) | 1.0.67 | Moon Mining Inc. | Клиент галактического сервиса рыночных цен и индексов стоимости производственны… |
| 2026-10-25 19:03:05 | [bc.Combinatorics](https://www.nuget.org/packages/bc.Combinatorics) | 0.0.1 | bc.Combinatorics | Package Description |
| 2026-10-25 19:07:24 | [Kavchat](https://www.nuget.org/packages/Kavchat) | 0.0.5 | maxsave | Kavchat server SDK for .NET: identity tokens, webhook verification and the Serv… |
| 2026-10-25 19:13:00 | [Mecesoft.Data.Abstractions](https://www.nuget.org/packages/Mecesoft.Data.Abstractions) | 1.0.0 | Mecesoft | Provider-independent data access abstractions for Mecesoft.Data. |
| 2026-10-25 19:13:02 | [Mecesoft.Data.EntityFrameworkCore](https://www.nuget.org/packages/Mecesoft.Data.EntityFrameworkCore) | 1.0.0 | Mecesoft | EF Core relational integration for Mecesoft.Data. |
| 2026-10-25 19:13:04 | [Mecesoft.Data.EntityFrameworkCore.SqlServer.Tenancy](https://www.nuget.org/packages/Mecesoft.Data.EntityFrameworkCore.SqlServer.Tenancy) | 1.0.0 | Mecesoft | SQL Server production tenant collation verification for Mecesoft.Data. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
