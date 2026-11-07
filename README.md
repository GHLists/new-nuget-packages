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

## Latest list — 2026-11-07 05:19 UTC

New packages created between 2026-11-07 04:19 UTC and 2026-11-07 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T05-19-19-227219Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 04:26:35 | [TGateway.RoslynCompletion](https://www.nuget.org/packages/TGateway.RoslynCompletion) | 2.3.28 | TGateway.RoslynCompletion | Package Description |
| 2026-11-07 04:26:38 | [TGateway.Tunnel](https://www.nuget.org/packages/TGateway.Tunnel) | 2.3.28 | TGateway.Tunnel | Package Description |
| 2026-11-07 04:27:00 | [ModelContextProtocol.Extensions.Skills](https://www.nuget.org/packages/ModelContextProtocol.Extensions.Skills) | 2.4.0 | ModelContextProtocol | MCP Skills extension (SEP-2640) for the .NET Model Context Protocol (MCP) SDK |
| 2026-11-07 04:34:13 | [PayKit.Contracts](https://www.nuget.org/packages/PayKit.Contracts) | 1.0.0 | PayKit | Shared request/response contracts for the PayKit payments API (used by PayKit.C… |
| 2026-11-07 04:34:14 | [PayKit.Client](https://www.nuget.org/packages/PayKit.Client) | 1.0.0 | PayKit | Client for the PayKit payments API: check entitlements, verify Google Play purc… |
| 2026-11-07 04:34:14 | [PayKit.Client.Maui](https://www.nuget.org/packages/PayKit.Client.Maui) | 1.0.0 | PayKit | Google Play Billing for .NET MAUI apps backed by the PayKit payments API: load… |
| 2026-11-07 04:59:08 | [StdUnit.AceOne.Core](https://www.nuget.org/packages/StdUnit.AceOne.Core) | 0.1.0 | StdUnit.AceOne.Core | Package Description |
| 2026-11-07 04:59:15 | [StdUnit.AceOne.DAL](https://www.nuget.org/packages/StdUnit.AceOne.DAL) | 0.1.0 | StdUnit.AceOne.DAL | Package Description |
| 2026-11-07 04:59:22 | [StdUnit.AceOne.WebApi](https://www.nuget.org/packages/StdUnit.AceOne.WebApi) | 0.1.0 | StdUnit.AceOne.WebApi | Package Description |
| 2026-11-07 04:59:30 | [StdUnit.AceOne.DAL.MySql](https://www.nuget.org/packages/StdUnit.AceOne.DAL.MySql) | 0.1.0 | StdUnit.AceOne.DAL.MySql | Package Description |
| 2026-11-07 04:59:37 | [StdUnit.AceOne.DAL.PostgreSql](https://www.nuget.org/packages/StdUnit.AceOne.DAL.PostgreSql) | 0.1.0 | StdUnit.AceOne.DAL.PostgreSql | Package Description |
| 2026-11-07 04:59:44 | [StdUnit.AceOne.DAL.Sqlite](https://www.nuget.org/packages/StdUnit.AceOne.DAL.Sqlite) | 0.1.0 | StdUnit.AceOne.DAL.Sqlite | Package Description |
| 2026-11-07 04:59:50 | [StdUnit.AceOne.Mail.Resend](https://www.nuget.org/packages/StdUnit.AceOne.Mail.Resend) | 0.1.0 | StdUnit.AceOne.Mail.Resend | Package Description |
| 2026-11-07 05:14:53 | [Sevencat.GlyphRaster](https://www.nuget.org/packages/Sevencat.GlyphRaster) | 0.1.5 | sevencat | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
