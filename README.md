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

## Latest list — 2026-10-10 09:21 UTC

New packages created between 2026-10-10 08:21 UTC and 2026-10-10 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T09-21-59-239282Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 08:26:05 | [DBAClientX.Dbf](https://www.nuget.org/packages/DBAClientX.Dbf) | 1.0.11 | Przemyslaw Klys | Bounded, forward-only DBF/xBase table and memo reading without database drivers. |
| 2026-10-10 08:27:58 | [PersianInputValidator](https://www.nuget.org/packages/PersianInputValidator) | 0.1.0 | Shahinhmpgit | A lightweight .NET library for Persian and Arabic-Indic digit normalization, Ir… |
| 2026-10-10 08:35:23 | [SharedAuth](https://www.nuget.org/packages/SharedAuth) | 1.0.0 | Local | Shared authentication/authorization helpers and HttpClient token handler. |
| 2026-10-10 09:11:14 | [yojimbo](https://www.nuget.org/packages/yojimbo) | 1.13.500 | Glenn Fiedler,Sky Morey,Claude | C# port of yojimbo, a network library for client/server games with dedicated se… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
