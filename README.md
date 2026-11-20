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

## Latest list — 2026-11-20 15:22 UTC

New packages created between 2026-11-20 14:21 UTC and 2026-11-20 15:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T15-22-21-796705Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 14:24:31 | [TzData.Runtime](https://www.nuget.org/packages/TzData.Runtime) | 1.0.0 | DotNet-AGPL | App-local IANA time zone data (tzdata 2026f) for .NET on Linux and macOS. Ships… |
| 2026-11-20 14:24:32 | [TzData.Runtime.AutoInit](https://www.nuget.org/packages/TzData.Runtime.AutoInit) | 1.0.0 | DotNet-AGPL | Opt-in automatic TZDIR setup for TzData.Runtime. Injects a module initializer i… |
| 2026-11-20 14:26:20 | [Integrios.Client](https://www.nuget.org/packages/Integrios.Client) | 0.2.0 | Integrios | Consume an Integrios pull Destination from a .NET generic host. |
| 2026-11-20 14:28:31 | [Nocturne.Web](https://www.nuget.org/packages/Nocturne.Web) | 0.1.0 | Martin Kirk | The Nocturne dark theme of Nocturne.Wpf for ASP.NET Core: CSS for every control… |
| 2026-11-20 14:39:42 | [CoinoLive](https://www.nuget.org/packages/CoinoLive) | 1.0.0 | Coino Live | .NET library for the Coino Live crypto payment API |
| 2026-11-20 14:42:25 | [Vetta.Connector.SqlServer](https://www.nuget.org/packages/Vetta.Connector.SqlServer) | 0.3.0 | Vettvangur | Persistent SQL Server authentication attempt storage for Vetta.Connector.AspNet… |
| 2026-11-20 14:45:34 | [Lab.Socle](https://www.nuget.org/packages/Lab.Socle) | 0.0.1-reserve | Hubaria | Nom réservé. Le paquet Lab.Socle réel est interne au Hubaria Lab et n'est pas p… |
| 2026-11-20 14:45:56 | [Microsoft.JavaScript.NodeApi.Embedding](https://www.nuget.org/packages/Microsoft.JavaScript.NodeApi.Embedding) | 0.9.43 | Microsoft | Embeds Node.js in .NET apps: brings Microsoft.JavaScript.NodeApi and Microsoft.… |
| 2026-11-20 14:53:56 | [HyperDev.Connectors](https://www.nuget.org/packages/HyperDev.Connectors) | 1.0.0 | Ivan Senatore, Wemake Informa… | HyperDev Fatum Framework |
| 2026-11-20 14:54:17 | [HyperDev.Connectors.Editor](https://www.nuget.org/packages/HyperDev.Connectors.Editor) | 1.0.0 | Ivan Senatore, Wemake Informa… | HyperDev Fatum Framework: server side of the connector editor (@wemake4u/connec… |
| 2026-11-20 14:54:31 | [HyperDev.Connectors.Rest](https://www.nuget.org/packages/HyperDev.Connectors.Rest) | 1.0.0 | Ivan Senatore, Wemake Informa… | HyperDev Fatum Framework |
| 2026-11-20 14:54:48 | [HyperDev.Connectors.Soap](https://www.nuget.org/packages/HyperDev.Connectors.Soap) | 1.0.0 | Ivan Senatore, Wemake Informa… | HyperDev Fatum Framework |
| 2026-11-20 14:55:01 | [HyperDev.Connectors.Sql](https://www.nuget.org/packages/HyperDev.Connectors.Sql) | 1.0.0 | Ivan Senatore, Wemake Informa… | HyperDev Fatum Framework |
| 2026-11-20 14:59:59 | [SqlBranch.Testing](https://www.nuget.org/packages/SqlBranch.Testing) | 0.2.0 | SqlBranch contributors | Private SQL Server database branches for automated tests. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
