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

## Latest list — 2026-11-27 05:19 UTC

New packages created between 2026-11-27 04:21 UTC and 2026-11-27 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T05-19-30-512069Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 04:36:57 | [Polhem.Chat.Blazor](https://www.nuget.org/packages/Polhem.Chat.Blazor) | 0.3.0 | Polhem contributors | An AI chat component for Blazor, Server and WebAssembly: streamed replies rende… |
| 2026-11-27 04:37:17 | [OD.AI](https://www.nuget.org/packages/OD.AI) | 1.0.1 | Olivier Dahan | Asynchronous provider clients for .NET applications. |
| 2026-11-27 04:37:18 | [OD.AI.Wpf](https://www.nuget.org/packages/OD.AI.Wpf) | 1.0.1 | Olivier Dahan | Optional WPF profile editor for OD.AI. |
| 2026-11-27 05:08:51 | [Bmailu](https://www.nuget.org/packages/Bmailu) | 0.1.0 | Bmailu | .NET SDK for the Bmailu Email API. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
