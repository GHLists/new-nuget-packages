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

## Latest list — 2026-11-12 06:21 UTC

New packages created between 2026-11-12 05:20 UTC and 2026-11-12 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T06-21-04-015315Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 05:28:22 | [Maxine.LibOpenMPT.NET](https://www.nuget.org/packages/Maxine.LibOpenMPT.NET) | 0.8.10 | Xpl0itR | A mostly source-generated, blittable bindings library wrapping libopenmpt using… |
| 2026-11-12 05:45:33 | [M.Simple.Logging](https://www.nuget.org/packages/M.Simple.Logging) | 1.0.1.2 | Mr.MingOuyang | Lightweight SQLite logging and embedded dashboard for ASP.NET Core. |
| 2026-11-12 05:47:18 | [CliqtoMedia.Apify](https://www.nuget.org/packages/CliqtoMedia.Apify) | 1.0.0 | Cliqto Media | Run any Apify Actor from C# and get its dataset items in one call. Ready Actor… |
| 2026-11-12 05:47:45 | [Exchange56.ApiProxy](https://www.nuget.org/packages/Exchange56.ApiProxy) | 1.0.0 | T.J. McNaboe | Proxy client requests to Exchange56 Apis. |
| 2026-11-12 05:52:45 | [CentralLogging.Client](https://www.nuget.org/packages/CentralLogging.Client) | 1.0.1 | Sumit Sahani | Client SDK for the Centralized Logging System: buffered, batched, gzip-compress… |
| 2026-11-12 05:52:51 | [ETG.IAM.Auth](https://www.nuget.org/packages/ETG.IAM.Auth) | 1.1.0 | ETG | Drop-in IAM authentication for ASP.NET Core APIs (.NET 8+). Validates accessTok… |
| 2026-11-12 05:54:51 | [Cron.DevToys](https://www.nuget.org/packages/Cron.DevToys) | 1.0.0 | Cron | Cron expression generator with Chinese description and next-run preview. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
