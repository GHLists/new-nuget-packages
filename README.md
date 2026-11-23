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

## Latest list — 2026-11-23 01:20 UTC

New packages created between 2026-11-23 00:20 UTC and 2026-11-23 01:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T01-20-39-530978Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 00:36:35 | [MiniExcel.Core](https://www.nuget.org/packages/MiniExcel.Core) | 2.0.0 | Wei Lin, Michele Bastione, PI… | Lightweight, fast and simple .NET processing tool for importing, exporting and… |
| 2026-11-23 00:38:59 | [MiniExcel.OpenXml](https://www.nuget.org/packages/MiniExcel.OpenXml) | 2.0.0 | Wei Lin, Michele Bastione, PI… | Lightweight, fast and simple .NET processing tool for importing, exporting and… |
| 2026-11-23 00:39:42 | [SpawnDev.Blazor.BootRecovery](https://www.nuget.org/packages/SpawnDev.Blazor.BootRecovery) | 1.0.0 | LostBeard | Temporary fix for dotnet/runtime#135090: a Blazor WebAssembly app whose browser… |
| 2026-11-23 00:39:58 | [MiniExcel.Csv](https://www.nuget.org/packages/MiniExcel.Csv) | 2.0.0 | Wei Lin, Michele Bastione, PI… | Lightweight, fast and simple .NET processing tool for importing, exporting and… |
| 2026-11-23 00:40:23 | [Lierne.Core](https://www.nuget.org/packages/Lierne.Core) | 0.1.0 | FrigaT | Plugin catalog, contribution registries and composition validation of the Liern… |
| 2026-11-23 00:40:24 | [Lierne.Abstractions](https://www.nuget.org/packages/Lierne.Abstractions) | 0.1.0 | FrigaT | Contracts, identifiers and contribution descriptors of the Lierne IDE compositi… |
| 2026-11-23 00:40:25 | [Lierne](https://www.nuget.org/packages/Lierne) | 0.1.0 | FrigaT | Flare IDE host for Lierne - shell layout, documents, tool windows, ribbon and s… |
| 2026-11-23 00:41:19 | [MiniExcel.OpenXml.FluentMapping](https://www.nuget.org/packages/MiniExcel.OpenXml.FluentMapping) | 2.0.0 | Wei Lin, Michele Bastione, PI… | Lightweight, fast and simple .NET processing tool for importing, exporting and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
