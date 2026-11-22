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

## Latest list — 2026-11-22 00:20 UTC

New packages created between 2026-11-21 23:19 UTC and 2026-11-22 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T00-20-44-054055Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 23:55:12 | [JQuants.Net](https://www.nuget.org/packages/JQuants.Net) | 0.2.0 | Yusuke Masuda | A modern .NET client library for the J-Quants API with rate limiting and async… |
| 2026-11-22 00:04:43 | [equip-sw-lint](https://www.nuget.org/packages/equip-sw-lint) | 1.0.0 | mhbae-semi-lab | Command-line runner for EquipSwLint analyzers: analyzes C# sources without buil… |
| 2026-11-22 00:04:44 | [EquipSwLint.Analyzers](https://www.nuget.org/packages/EquipSwLint.Analyzers) | 1.0.0 | mhbae-semi-lab | Roslyn analyzers for long-running equipment control software in C#: 32-bit tick… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
