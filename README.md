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

## Latest list — 2026-11-05 23:20 UTC

New packages created between 2026-11-05 22:20 UTC and 2026-11-05 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T23-20-22-122758Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 22:24:53 | [ZopfliSharp](https://www.nuget.org/packages/ZopfliSharp) | 0.1.0 | Frédéric Derenty | Zopfli compression in pure C#, with no native dependencies at all. A faithful p… |
| 2026-11-05 22:31:36 | [DrifterApps.Seeds.FluentResult.AwesomeAssertions](https://www.nuget.org/packages/DrifterApps.Seeds.FluentResult.AwesomeAssertions) | 1.1.42 | Patrick Moreau | Package Description |
| 2026-11-05 22:37:49 | [Disposed.License](https://www.nuget.org/packages/Disposed.License) | 2026.11.5.223743 | Thijs Janssen | License validation library. Free to use except for commercial use above 1.5 mil… |
| 2026-11-05 22:38:17 | [Lobasoft.SharedAssemblies](https://www.nuget.org/packages/Lobasoft.SharedAssemblies) | 2.0.0 | Lobasoft.SharedAssemblies | Package Description |
| 2026-11-05 22:48:59 | [Lobasoft.Host](https://www.nuget.org/packages/Lobasoft.Host) | 2.0.0 | Lobasoft | Package Description |
| 2026-11-05 22:56:28 | [SpecJumpCdc](https://www.nuget.org/packages/SpecJumpCdc) | 1.0.0 | Whaliin | High-performance Speculative Jump Content-Defined Chunking (JC) for .NET 10, de… |
| 2026-11-05 23:01:22 | [Mediana.Drawing.Emoji.Fluent](https://www.nuget.org/packages/Mediana.Drawing.Emoji.Fluent) | 0.1.20 | Vadim Belov | Optional Microsoft Fluent Flat emoji resources and managed inline rendering. |
| 2026-11-05 23:01:24 | [Mediana.Imaging](https://www.nuget.org/packages/Mediana.Imaging) | 0.1.20 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-05 23:01:38 | [Mediana.Codecs.Webp](https://www.nuget.org/packages/Mediana.Codecs.Webp) | 0.1.20 | Vadim Belov | Managed multimedia building blocks for .NET. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
