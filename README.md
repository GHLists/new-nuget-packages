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

## Latest list — 2026-10-06 16:22 UTC

New packages created between 2026-10-06 15:22 UTC and 2026-10-06 16:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T16-22-02-515804Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 15:26:51 | [AlchiwebApp](https://www.nuget.org/packages/AlchiwebApp) | 0.6.2.4 | Alchiweb | AlchiwebApp |
| 2026-10-06 15:29:52 | [ModelingEvolution.GenericAxis](https://www.nuget.org/packages/ModelingEvolution.GenericAxis) | 0.1.0 | ModelingEvolution | Generic external axis (linear track or rotary positioner) behind a PLC over Mod… |
| 2026-10-06 15:29:53 | [ModelingEvolution.GenericAxis.Plugin](https://www.nuget.org/packages/ModelingEvolution.GenericAxis.Plugin) | 0.1.0 | ModelingEvolution | RocketWelder device plugin for a generic external axis over Modbus TCP (epic-06… |
| 2026-10-06 15:33:48 | [Kahuna.Client.AspNetCore](https://www.nuget.org/packages/Kahuna.Client.AspNetCore) | 1.11.2 | Andres Gutierrez | ASP.NET Core rate-limiting policies backed by Kahuna, so every replica of an ap… |
| 2026-10-06 15:42:25 | [PG410.OfflineScaffolder](https://www.nuget.org/packages/PG410.OfflineScaffolder) | 0.0.1 | 410th | Educational ASP.NET Core MVC project generator with PostgreSQL initialization o… |
| 2026-10-06 15:42:51 | [PowerForge.IndexNow](https://www.nuget.org/packages/PowerForge.IndexNow) | 3.0.158 | Przemyslaw Klys | Host-independent IndexNow URL submission, batching, retries, and checkpoint nor… |
| 2026-10-06 15:50:51 | [UKHO.ADDS.Infrastructure.Pipelines](https://www.nuget.org/packages/UKHO.ADDS.Infrastructure.Pipelines) | 1.0.61006 | Abzu | ADDS Shared Infrastructure |
| 2026-10-06 15:50:52 | [UKHO.ADDS.Infrastructure.Results](https://www.nuget.org/packages/UKHO.ADDS.Infrastructure.Results) | 1.0.61006 | Abzu | ADDS Shared Infrastructure |
| 2026-10-06 15:50:54 | [UKHO.ADDS.Infrastructure.Serialization](https://www.nuget.org/packages/UKHO.ADDS.Infrastructure.Serialization) | 1.0.61006 | Abzu | ADDS Shared Infrastructure |
| 2026-10-06 15:52:43 | [FathomCharts](https://www.nuget.org/packages/FathomCharts) | 0.2.0 | Adrien Insights | Fathom Charts client: real-time order-flow indicator streams (WebSocket) and hi… |
| 2026-10-06 15:53:11 | [FathomCharts.Types](https://www.nuget.org/packages/FathomCharts.Types) | 0.2.0 | Adrien Insights | Generates C# types of Fathom Charts indicator parameters and data from the indi… |
| 2026-10-06 15:59:02 | [Mailcycle](https://www.nuget.org/packages/Mailcycle) | 0.1.0 | Northlab Studios Ltd | .NET client for the Mailcycle API. Create addresses that receive mail, read and… |
| 2026-10-06 16:02:44 | [Chovameo352.Common](https://www.nuget.org/packages/Chovameo352.Common) | 1.0.0 | Chovameo352.Common | Dependency-free entity identity, UTC audit timestamp contracts, and soft-deleti… |
| 2026-10-06 16:12:29 | [Telerik.Documents.JpxDecodeUtils](https://www.nuget.org/packages/Telerik.Documents.JpxDecodeUtils) | 2026.3.1006 | Progress Software Corporation | JPEG 2000 decoding support for PDF processing. Part of Telerik Document Process… |
| 2026-10-06 16:13:14 | [Telerik.Windows.Documents.JpxDecodeUtils](https://www.nuget.org/packages/Telerik.Windows.Documents.JpxDecodeUtils) | 2026.3.1006 | Progress Software Corporation | JPEG 2000 decoding support for PDF processing. Part of Telerik Document Process… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
