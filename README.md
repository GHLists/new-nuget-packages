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

## Latest list — 2026-10-22 07:20 UTC

New packages created between 2026-10-22 06:19 UTC and 2026-10-22 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T07-20-27-68346Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 06:36:06 | [AfterBurnerSharp](https://www.nuget.org/packages/AfterBurnerSharp) | 1.0.0 | Magnus Leatti | AfterBurnerSharp is a static class that reads MSI Afterburner's hardware monito… |
| 2026-10-22 06:36:23 | [BimTeam.Markdig](https://www.nuget.org/packages/BimTeam.Markdig) | 1.4.2.1 | Alexandre Mutel,BimTeam | BimTeam fork of Markdig for .NET Framework and modern .NET without runtime pack… |
| 2026-10-22 06:36:25 | [BimTeam.Markdig.Wpf](https://www.nuget.org/packages/BimTeam.Markdig.Wpf) | 1.4.2.1 | BimTeam | Dependency-light Markdown rendering to WPF FlowDocument and a reusable Markdown… |
| 2026-10-22 06:44:49 | [Elync.Mes.Translator.Abstractions](https://www.nuget.org/packages/Elync.Mes.Translator.Abstractions) | 1.0.1 | hans_wen(elync) | elync 内部测试 |
| 2026-10-22 06:57:41 | [PocketCsvReader.Chrononuensis](https://www.nuget.org/packages/PocketCsvReader.Chrononuensis) | 2.49.0 | Cédric L. Charlier | Opt-in span-based Chrononuensis temporal parsers for PocketCsvReader. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
