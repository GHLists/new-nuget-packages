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

## Latest list — 2026-10-04 11:19 UTC

New packages created between 2026-10-04 10:19 UTC and 2026-10-04 11:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T11-19-38-302765Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 10:21:14 | [Elarion.Migrations.EntityFrameworkCore](https://www.nuget.org/packages/Elarion.Migrations.EntityFrameworkCore) | 0.2.8 | Simon Wimmesberger | EF Core migrations as steps of the Elarion migration plan (ADR-0081): every EF… |
| 2026-10-04 10:21:14 | [Elarion.Settings.DataProtection](https://www.nuget.org/packages/Elarion.Settings.DataProtection) | 0.2.8 | Simon Wimmesberger | ASP.NET Core Data Protection implementation of the Elarion settings protector:… |
| 2026-10-04 10:35:39 | [Mayordomo.Core](https://www.nuget.org/packages/Mayordomo.Core) | 1.0.20261004.17 | Alfonso Lara Ramos and Mayord… | Reusable deterministic server-authoritative board-game engine with replay, simu… |
| 2026-10-04 10:49:17 | [WeApi.Cli](https://www.nuget.org/packages/WeApi.Cli) | 1.0.0 | WeApi Contributors | Production-ready cross-platform CLI tool to generate Clean Architecture .NET 10… |
| 2026-10-04 10:49:17 | [WeApi.Template](https://www.nuget.org/packages/WeApi.Template) | 1.0.0 | WeApi Contributors | Production-ready Clean Architecture .NET 10 Web API template with JWT authentic… |
| 2026-10-04 11:05:35 | [Sujithaa.PalindromeUtility](https://www.nuget.org/packages/Sujithaa.PalindromeUtility) | 1.0.1 | Sujithaa | A reusable C# library for checking palindromes and reversing strings. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
