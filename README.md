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

## Latest list — 2026-10-22 00:19 UTC

New packages created between 2026-10-21 23:18 UTC and 2026-10-22 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T00-19-13-371764Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 23:27:38 | [OwlDomain.SDL3.TTF.Native](https://www.nuget.org/packages/OwlDomain.SDL3.TTF.Native) | 3.2.2 | OwlDomain | Native binaries for SDL3_ttf. |
| 2026-10-21 23:55:22 | [Oicana.Native.linux-x64](https://www.nuget.org/packages/Oicana.Native.linux-x64) | 0.10.0 | Oicana | Native library of Oicana for linux-x64. The Oicana package references it; refer… |
| 2026-10-21 23:57:04 | [Oicana.Native.linux-musl-arm64](https://www.nuget.org/packages/Oicana.Native.linux-musl-arm64) | 0.10.0 | Oicana | Native library of Oicana for linux-musl-arm64. The Oicana package references it… |
| 2026-10-22 00:01:42 | [Oicana.Native.linux-musl-x64](https://www.nuget.org/packages/Oicana.Native.linux-musl-x64) | 0.10.0 | Oicana | Native library of Oicana for linux-musl-x64. The Oicana package references it;… |
| 2026-10-22 00:02:22 | [LsMsgPack.TypeScript](https://www.nuget.org/packages/LsMsgPack.TypeScript) | 2026.10.22.1 | Louis Somers | Writes TypeScript classes for the .NET model classes a server sends and receive… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
