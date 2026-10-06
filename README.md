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

## Latest list — 2026-10-06 06:20 UTC

New packages created between 2026-10-06 05:19 UTC and 2026-10-06 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T06-20-33-505521Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 05:19:53 | [PolyhydraGames.Discord](https://www.nuget.org/packages/PolyhydraGames.Discord) | 1.0.8 | PolyhydraGames | Discord bot integration for Polyhydra/ChannelCheevos. Discord.Net client for re… |
| 2026-10-06 05:55:54 | [Scout.linux-musl-arm64](https://www.nuget.org/packages/Scout.linux-musl-arm64) | 0.7.0 | willibrandon | Feature-complete port of ripgrep to .NET Native AOT. |
| 2026-10-06 05:58:12 | [CalWin.Client](https://www.nuget.org/packages/CalWin.Client) | 8.1.3.3 | CalWin AS | A .NET HTTP client library for consuming the CalWin window and door platform AP… |
| 2026-10-06 05:58:44 | [Asim.CleanArchitecture.Template](https://www.nuget.org/packages/Asim.CleanArchitecture.Template) | 1.0.0 | Asim | A .NET 10 Clean Architecture Web API template with Domain, Application, Infrast… |
| 2026-10-06 06:10:48 | [KeyGrant.Licensing](https://www.nuget.org/packages/KeyGrant.Licensing) | 0.1.0 | KeyGrant | KeyGrant licensing for .NET desktop apps: signed leases verified offline, activ… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
