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

## Latest list — 2026-10-31 11:19 UTC

New packages created between 2026-10-31 10:20 UTC and 2026-10-31 11:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T11-19-51-669346Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 10:37:38 | [Hexalith.Memories.EventStoreExtensions](https://www.nuget.org/packages/Hexalith.Memories.EventStoreExtensions) | 3.0.12 | ITANEO | Memories-owned local internal EventStore intent adapter enrollment. |
| 2026-10-31 10:40:28 | [Toda.Guard](https://www.nuget.org/packages/Toda.Guard) | 0.1.0 | Toda contributors | toda-guard: accounts, groups with nesting, user directories, sign-in. |
| 2026-10-31 10:40:29 | [Toda.Guard.Contracts](https://www.nuget.org/packages/Toda.Guard.Contracts) | 0.1.0 | Toda contributors | Public contracts of toda-guard: the directory connector SPI, lookups, and accou… |
| 2026-10-31 10:40:29 | [Toda.Guard.Acting](https://www.nuget.org/packages/Toda.Guard.Acting) | 0.1.0 | Toda contributors | toda-guard's acting context (ADR 0042, 0087): whose rights a request uses and w… |
| 2026-10-31 10:49:35 | [Cratis.Showrunner.BoxOffice](https://www.nuget.org/packages/Cratis.Showrunner.BoxOffice) | 1.4.0 | Cratis | Box Office — the Showrunner part a managed product runs to honor what its opera… |
| 2026-10-31 11:07:49 | [DotProlog.Packages.Cli](https://www.nuget.org/packages/DotProlog.Packages.Cli) | 0.17.0 | Aleksandr Pavlov | Restores locked Prolog source packages and runs them with SWI-Prolog or DotProl… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
