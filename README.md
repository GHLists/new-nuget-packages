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

## Latest list — 2026-10-08 14:24 UTC

New packages created between 2026-10-08 13:22 UTC and 2026-10-08 14:24 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T14-24-40-408684Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 13:22:47 | [Allpaqa.MultilingualKatakana](https://www.nuget.org/packages/Allpaqa.MultilingualKatakana) | 0.5.0 | allpaqa | Zero-dependency, ultra-fast multilingual (English/Chinese/Korean/Russian/Spanis… |
| 2026-10-08 13:24:11 | [KD.Avalonia.Rice](https://www.nuget.org/packages/KD.Avalonia.Rice) | 26.10.3 | k0zi | Frameless Avalonia window with a custom title bar and Linux distro inspired the… |
| 2026-10-08 13:33:48 | [InfiniAnalytics.Sdk](https://www.nuget.org/packages/InfiniAnalytics.Sdk) | 0.1.0 | InfiniAnalytics | Official .NET SDK for InfiniAnalytics: registers the start, events, warnings, e… |
| 2026-10-08 13:35:43 | [RoushTech.Asio.Forwarding](https://www.nuget.org/packages/RoushTech.Asio.Forwarding) | 0.6.0 | William Roush | Satellite-to-host log forwarding for RoushTech.Asio over any transport: streams… |
| 2026-10-08 13:37:51 | [Notato.Maui](https://www.nuget.org/packages/Notato.Maui) | 0.1.0 | Notato contributors | Figma-style comments for a running .NET MAUI app. Tap an element, write a note,… |
| 2026-10-08 13:45:29 | [RekTHOR.TypedSettings](https://www.nuget.org/packages/RekTHOR.TypedSettings) | 0.1.0 | RekTHOR | Strongly typed, validated settings on top of the Options pattern: the type name… |
| 2026-10-08 13:59:15 | [pvNugsLoggerNc10Hybrid](https://www.nuget.org/packages/pvNugsLoggerNc10Hybrid) | 10.0.0 | Pierre Van Wallendael | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
