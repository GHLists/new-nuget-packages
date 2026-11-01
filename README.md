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

## Latest list — 2026-11-01 14:18 UTC

New packages created between 2026-11-01 13:20 UTC and 2026-11-01 14:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T14-18-57-942098Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 13:33:38 | [NewBeeVG.Common](https://www.nuget.org/packages/NewBeeVG.Common) | 1.0.1.28 | NewBeeVG.Common | Package Description |
| 2026-11-01 13:35:11 | [PolyPartitionSharp](https://www.nuget.org/packages/PolyPartitionSharp) | 0.1.0 | HanJaeJoon | Polygon triangulation and convex partitioning in C#. A port of the polypartitio… |
| 2026-11-01 13:35:16 | [QuickHullSharp](https://www.nuget.org/packages/QuickHullSharp) | 0.1.0 | HanJaeJoon | 3D convex hull of a point cloud using the QuickHull algorithm. A C# port of aku… |
| 2026-11-01 13:35:30 | [JqSharp](https://www.nuget.org/packages/JqSharp) | 0.1.0 | HanJaeJoon | A pure C# implementation of the jq JSON filter language, ported from gojq. |
| 2026-11-01 13:36:58 | [TaffySharp](https://www.nuget.org/packages/TaffySharp) | 0.1.0 | HanJaeJoon | A pure C# port of taffy, the Rust flexbox, CSS grid and block layout engine. |
| 2026-11-01 13:37:03 | [Synvro.Modulus.Notifications.EntityFrameworkCore](https://www.nuget.org/packages/Synvro.Modulus.Notifications.EntityFrameworkCore) | 1.8.2 | synvro | Entity Framework Core stores for Modulus notifications: the inbox and channel p… |
| 2026-11-01 13:37:06 | [Synvro.Modulus.Media.EntityFrameworkCore](https://www.nuget.org/packages/Synvro.Modulus.Media.EntityFrameworkCore) | 1.8.2 | synvro | Entity Framework Core store for the Modulus media library. The application deri… |
| 2026-11-01 13:37:52 | [Synvro.Modulus.Media](https://www.nuget.org/packages/Synvro.Modulus.Media) | 1.8.2 | synvro | Media library for Modulus: validated uploads (images and PDF, checked by conten… |
| 2026-11-01 13:37:58 | [Synvro.Modulus.Identity.IntegrationEvents](https://www.nuget.org/packages/Synvro.Modulus.Identity.IntegrationEvents) | 1.8.2 | synvro | Integration events the Identity module publishes. Other modules reference this… |
| 2026-11-01 13:49:27 | [Soml.Extensions.Configuration](https://www.nuget.org/packages/Soml.Extensions.Configuration) | 0.0.1 | Sindre Sorhus | SOML configuration files for Microsoft.Extensions.Configuration: AddSomlFile an… |
| 2026-11-01 13:49:27 | [Soml.Cli](https://www.nuget.org/packages/Soml.Cli) | 0.0.1 | Sindre Sorhus | The decoder and encoder of the SOML conformance suite, for test harnesses: SOML… |
| 2026-11-01 13:49:28 | [Soml](https://www.nuget.org/packages/Soml) | 0.0.1 | Sindre Sorhus | A strict reader, writer, formatter, and editor for SOML, a config format for hu… |
| 2026-11-01 14:06:22 | [Appliman.TrackR.Client](https://www.nuget.org/packages/Appliman.TrackR.Client) | 5.0.0 | TrackR.Client | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
