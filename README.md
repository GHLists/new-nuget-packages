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

## Latest list — 2026-11-26 02:20 UTC

New packages created between 2026-11-26 01:19 UTC and 2026-11-26 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T02-20-22-510539Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 02:10:01 | [Xibalbalabs.Enumeration](https://www.nuget.org/packages/Xibalbalabs.Enumeration) | 1.0.0 | Xibalba Labs | A high-performance, modern .NET Standard 2.0 / .NET 9 smart enum library and dr… |
| 2026-11-26 02:10:16 | [Xibalbalabs.Enumeration.AspNetCore](https://www.nuget.org/packages/Xibalbalabs.Enumeration.AspNetCore) | 1.0.0 | Xibalba Labs | A DataAnnotations ValidationAttribute that validates a DTO property/parameter v… |
| 2026-11-26 02:10:27 | [Xibalbalabs.Enumeration.Dapper](https://www.nuget.org/packages/Xibalbalabs.Enumeration.Dapper) | 1.0.0 | Xibalba Labs | A Dapper SqlMapper.TypeHandler that maps Xibalbalabs.Enumeration smart enums to… |
| 2026-11-26 02:10:37 | [Xibalbalabs.Enumeration.EntityFrameworkCore](https://www.nuget.org/packages/Xibalbalabs.Enumeration.EntityFrameworkCore) | 1.0.0 | Xibalba Labs | ValueConverter implementations that map Xibalbalabs.Enumeration smart enums to/… |
| 2026-11-26 02:10:49 | [Xibalbalabs.Enumeration.Json](https://www.nuget.org/packages/Xibalbalabs.Enumeration.Json) | 1.0.0 | Xibalba Labs | System.Text.Json converters for Xibalbalabs.Enumeration smart enums, with Nativ… |
| 2026-11-26 02:12:58 | [Mavalonia](https://www.nuget.org/packages/Mavalonia) | 0.8.0 | MagnusLidbom | Controls for Avalonia for writing and reading messages in markdown, such as in… |
| 2026-11-26 02:14:06 | [Zyborg.EFCore.RevTracking](https://www.nuget.org/packages/Zyborg.EFCore.RevTracking) | 0.2.1 | Zyborg.EFCore.RevTracking | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
