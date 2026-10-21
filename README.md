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

## Latest list — 2026-10-21 17:21 UTC

New packages created between 2026-10-21 16:21 UTC and 2026-10-21 17:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T17-21-17-519675Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 16:33:27 | [DevXStream.DADS.Cli](https://www.nuget.org/packages/DevXStream.DADS.Cli) | 1.0.1 | DevXStream | Package Description |
| 2026-10-21 16:35:52 | [Stellaegis.Access.PostgreSQL](https://www.nuget.org/packages/Stellaegis.Access.PostgreSQL) | 5.0.0 | FRi | The PostgreSQL stores of Stellaegis.Access: the effective rights of the three d… |
| 2026-10-21 16:35:53 | [Stellaegis.Access.Client](https://www.nuget.org/packages/Stellaegis.Access.Client) | 5.0.0 | FRi | Stellaegis Access for a resource server apart: the decision asked over HTTP of… |
| 2026-10-21 16:35:53 | [Stellaegis.Access](https://www.nuget.org/packages/Stellaegis.Access) | 5.0.0 | FRi | Stellaegis Access: the decision point of an application assembled on Stellaegis… |
| 2026-10-21 16:35:53 | [Stellaegis.Access.AspNetCore](https://www.nuget.org/packages/Stellaegis.Access.AspNetCore) | 5.0.0 | FRi | Stellaegis Access in an ASP.NET Core host: the rights system that answers the p… |
| 2026-10-21 16:38:58 | [MuteDeck.PluginClient](https://www.nuget.org/packages/MuteDeck.PluginClient) | 1.0.2 | MuteDeck | Client for the MuteDeck plugin protocol v2 (WebSocket), with fallback to v1. |
| 2026-10-21 16:40:40 | [T.Molodoy.Compose.Net.Navigation](https://www.nuget.org/packages/T.Molodoy.Compose.Net.Navigation) | 0.0.2 | T. Molodoy | Navigation for Compose.Net. |
| 2026-10-21 16:40:50 | [Nt.Parser](https://www.nuget.org/packages/Nt.Parser) | 1.0.4 | Domain | Parser that can be customized |
| 2026-10-21 16:50:49 | [SoriTrading.WatchTogether](https://www.nuget.org/packages/SoriTrading.WatchTogether) | 0.1.1 | Value Connect Global Inc. | Client for the SoriTrading agent's local API: WATCH TOGETHER signals and exchan… |
| 2026-10-21 17:04:12 | [PiiMask](https://www.nuget.org/packages/PiiMask) | 0.1.0 | Rahul | Dependency-free PII masking for strings, log text, and System.Text.Json on .NET… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
