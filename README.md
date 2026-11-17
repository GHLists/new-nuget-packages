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

## Latest list — 2026-11-17 22:22 UTC

New packages created between 2026-11-17 21:22 UTC and 2026-11-17 22:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T22-22-20-781216Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 21:25:19 | [Farol.Mcp](https://www.nuget.org/packages/Farol.Mcp) | 0.1.0 | Farol contributors | Compiler-accurate C# and VB code intelligence for AI agents, from legacy .NET F… |
| 2026-11-17 21:33:15 | [MASS4.Turian.Testing](https://www.nuget.org/packages/MASS4.Turian.Testing) | 5.2.0 | Bruno Massa | Headless component testing with controlled frames and input. |
| 2026-11-17 21:53:46 | [EdiWeave.Next.Healthcare](https://www.nuget.org/packages/EdiWeave.Next.Healthcare) | 9.1.0 | Silvenga,gamingrobot,EdiWeave… | HIPAA 5010 claim workflow for medical software: 837P builder and validator, 999… |
| 2026-11-17 22:05:18 | [GeoPandas.Net.Arrow](https://www.nuget.org/packages/GeoPandas.Net.Arrow) | 0.2.0 | Gravicode Studios (Kang Fadhi… | GeoPandas.Net columnar interchange: GeoParquet 1.1 reader/writer (WKB + bbox co… |
| 2026-11-17 22:05:21 | [GeoPandas.Net.Sql](https://www.nuget.org/packages/GeoPandas.Net.Sql) | 0.2.0 | Gravicode Studios (Kang Fadhi… | GeoPandas.Net spatial databases over plain ADO.NET: read_postgis-style ReadSql… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
