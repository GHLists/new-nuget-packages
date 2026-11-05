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

## Latest list — 2026-11-05 10:21 UTC

New packages created between 2026-11-05 09:21 UTC and 2026-11-05 10:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T10-21-37-786479Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 09:33:48 | [XmlWeave](https://www.nuget.org/packages/XmlWeave) | 0.1.0 | RRQM | 无运行时反射的强类型 XML 序列化运行时。 |
| 2026-11-05 09:34:07 | [Mkx.Templates.Api](https://www.nuget.org/packages/Mkx.Templates.Api) | 0.8.1 | Mkx | .NET 10 backend-only solution template with Identity, JWT Bearer, rotated refre… |
| 2026-11-05 09:44:39 | [Skakel.Protocol](https://www.nuget.org/packages/Skakel.Protocol) | 0.1.0-preview | Matumi Software | The Skakel protocol: wire constants, discovery packets, the pairing code and th… |
| 2026-11-05 09:44:50 | [Skakel.Client](https://www.nuget.org/packages/Skakel.Client) | 0.1.0-preview | Matumi Software | Reach Skakel servers: discovery, pairing, OAuth tokens over a pinned certificat… |
| 2026-11-05 09:45:03 | [Skakel.Server](https://www.nuget.org/packages/Skakel.Server) | 0.1.0-preview | Matumi Software | Serve Skakel clients from ASP.NET Core: discovery, pairing, OAuth tokens, certi… |
| 2026-11-05 10:16:04 | [StaticNorth.Uhp.Core](https://www.nuget.org/packages/StaticNorth.Uhp.Core) | 1.0.0 | uhp-dotnet contributors | Shared protocol contracts and AOT-compatible serialization for community UHP .N… |
| 2026-11-05 10:16:06 | [StaticNorth.Uhp.Server](https://www.nuget.org/packages/StaticNorth.Uhp.Server) | 1.0.0 | uhp-dotnet contributors | ASP.NET Core endpoints and backend integration for the Unified Harness Protocol. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
