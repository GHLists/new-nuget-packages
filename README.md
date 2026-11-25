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

## Latest list — 2026-11-25 11:21 UTC

New packages created between 2026-11-25 10:22 UTC and 2026-11-25 11:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T11-21-10-329671Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 10:27:16 | [AvaloniaUI.Parcel.Deps.AppImageRuntime](https://www.nuget.org/packages/AvaloniaUI.Parcel.Deps.AppImageRuntime) | 2025.11.8-rc1 | AppImage | AvaloniaUI Parcel dependency package for 'appimage-runtime' tool |
| 2026-11-25 10:34:55 | [AvaloniaUI.Parcel.Deps.SquashFsTools](https://www.nuget.org/packages/AvaloniaUI.Parcel.Deps.SquashFsTools) | 4.6.1-rc1 | Phillip Lougher | AvaloniaUI Parcel dependency package for 'mksquashfs' tool |
| 2026-11-25 10:39:44 | [NwUi.Primitives](https://www.nuget.org/packages/NwUi.Primitives) | 0.17.0 | NetWasm.UI contributors | Headless components for NetWasm.UI: disclosure, tabs, focus scope and roving fo… |
| 2026-11-25 10:41:57 | [Apparatus.Diff](https://www.nuget.org/packages/Apparatus.Diff) | 0.0.1 | Stanislav Silin | Source generator that builds reflection-free deep diffs with full paths for [Di… |
| 2026-11-25 10:47:22 | [PrismaData](https://www.nuget.org/packages/PrismaData) | 0.1.0 | PrismaData | Official .NET client for the PrismaData location intelligence API (geospatial,… |
| 2026-11-25 10:50:36 | [flappybonusmodels](https://www.nuget.org/packages/flappybonusmodels) | 1.0.0 | Flappybet | Ready-made, provably fair bonus models for Flappy games: pots, vaults and boost… |
| 2026-11-25 10:55:18 | [PortableTextSearch.EntityFrameworkCore](https://www.nuget.org/packages/PortableTextSearch.EntityFrameworkCore) | 10.0.0 | Jon Lachmann | Portable EF Core text-contains search for PostgreSQL and SQLite. |
| 2026-11-25 10:57:31 | [Moltaro.OnecOutpost.Server](https://www.nuget.org/packages/Moltaro.OnecOutpost.Server) | 0.1.0 | Bijou Solutions | The server of Moltaro.OnecOutpost, embedded in an ASP.NET Core application: it… |
| 2026-11-25 10:58:00 | [Umbraco.Community.AddressLookup](https://www.nuget.org/packages/Umbraco.Community.AddressLookup) | 18.0.0 | Pascal Meyer | An Umbraco Forms address lookup field with Loqate and Ideal Postcodes behind a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
