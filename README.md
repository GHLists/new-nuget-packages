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

## Latest list — 2026-11-17 21:22 UTC

New packages created between 2026-11-17 20:20 UTC and 2026-11-17 21:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T21-22-32-832604Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 20:24:13 | [HameedHassan.SolutionConflictFinder](https://www.nuget.org/packages/HameedHassan.SolutionConflictFinder) | 1.2026.11.1 | Hameed Hassan | Compare solutions across environments and review conflicts before you import. S… |
| 2026-11-17 20:28:59 | [Labyrinthe.LabPay](https://www.nuget.org/packages/Labyrinthe.LabPay) | 0.1.0 | Labyrinthe Innovations SARL | Official .NET client for LabPay, the Mobile Money aggregator for Africa (M-Pesa… |
| 2026-11-17 20:29:00 | [Labyrinthe.LabPay.AspNetCore](https://www.nuget.org/packages/Labyrinthe.LabPay.AspNetCore) | 0.1.0 | Labyrinthe Innovations SARL | ASP.NET Core integration of the LabPay SDK: services.AddLabPay(configuration) w… |
| 2026-11-17 20:34:52 | [Activout.DatabaseClient.LibSql](https://www.nuget.org/packages/Activout.DatabaseClient.LibSql) | 5.1.0 | Activout.DatabaseClient.LibSql | libSQL (Turso, Bunny Database) backend for Activout.DatabaseClient. |
| 2026-11-17 20:42:57 | [Lwnrdb.Client](https://www.nuget.org/packages/Lwnrdb.Client) | 0.1.0 | christiancg | The official .NET client for LWNRDB: a connection pool, a fluent query builder,… |
| 2026-11-17 20:45:00 | [BehpardakhtPosClient](https://www.nuget.org/packages/BehpardakhtPosClient) | 0.0.1 | alirezar | Unofficial Behpardakht POS device client for .NET. Speaks protocol revision 4.7… |
| 2026-11-17 20:51:37 | [MediSync](https://www.nuget.org/packages/MediSync) | 0.1.0 | MediSync GmbH | The .NET SDK for the MediSync API: speech to text, clinical notes and letters,… |
| 2026-11-17 21:10:44 | [Themis.Evaluation](https://www.nuget.org/packages/Themis.Evaluation) | 4.5.0 | Themis contributors | Offline decision-provider evaluation and replay for Themis. |
| 2026-11-17 21:10:51 | [Themis.Verdict.Tool](https://www.nuget.org/packages/Themis.Verdict.Tool) | 4.5.0 | Themis contributors | Command-line evaluation and diagnostics for Themis decision inference. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
