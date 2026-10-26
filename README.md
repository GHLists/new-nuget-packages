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

## Latest list — 2026-10-26 11:20 UTC

New packages created between 2026-10-26 10:21 UTC and 2026-10-26 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T11-20-20-319591Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 10:33:51 | [AdvancedComponents.NET](https://www.nuget.org/packages/AdvancedComponents.NET) | 1.0.0 | Cristian Caciagli | Libreria di componenti Blazor riutilizzabili. |
| 2026-10-26 10:34:57 | [ProtoCross](https://www.nuget.org/packages/ProtoCross) | 0.8.0 | Isaac Sherman | The ProtoCross compiler. Write the business methods of your protobuf messages o… |
| 2026-10-26 10:41:56 | [Render.NET](https://www.nuget.org/packages/Render.NET) | 0.1.1 | Vadim Belov | Foundation package for Render.NET, a .NET rendering library. This initial relea… |
| 2026-10-26 10:54:03 | [BBTree](https://www.nuget.org/packages/BBTree) | 0.1.0 | Lukasz Rozmej | Fast ordered maps for .NET on a B+-tree whose nodes search inline keys with SIM… |
| 2026-10-26 10:55:52 | [Render.NET.Mesh](https://www.nuget.org/packages/Render.NET.Mesh) | 0.1.1 | Vadim Belov | Foundation package for fully managed 3D model rendering with Render.NET. This i… |
| 2026-10-26 10:59:06 | [Konstera.Sdk](https://www.nuget.org/packages/Konstera.Sdk) | 0.3.0 | Konstera | Konstera Agent SDK for .NET. Mirror of konstera-sdk (Python). Wraps the MCP cal… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
