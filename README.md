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

## Latest list — 2026-10-27 22:20 UTC

New packages created between 2026-10-27 21:21 UTC and 2026-10-27 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T22-20-46-803041Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 21:34:03 | [MigrationTester](https://www.nuget.org/packages/MigrationTester) | 0.1.0 | Larsenq | Tests EF Core migrations against SQL Server with data that is valid before each… |
| 2026-10-27 21:39:21 | [ConsoleMVC.Testing](https://www.nuget.org/packages/ConsoleMVC.Testing) | 1.18.0 | Mateusz Podeszwa | Test ConsoleMVC applications end to end: run them with scripted lines and keys,… |
| 2026-10-27 21:40:49 | [Reimaginate.ProcessingLockService.Cosmos](https://www.nuget.org/packages/Reimaginate.ProcessingLockService.Cosmos) | 4.0.0 | Reimaginate | Azure Cosmos DB for NoSQL processing lock repository with tenant-scoped atomic… |
| 2026-10-27 21:52:04 | [deeptrace](https://www.nuget.org/packages/deeptrace) | 0.1.0 | DeepTrace.Cli | Local code intelligence for AI-assisted game mod development. Index decompiled… |
| 2026-10-27 21:59:40 | [ModernWpf.Cards](https://www.nuget.org/packages/ModernWpf.Cards) | 1.0.4 | benrisma133 | A modern, lightweight WPF UI component library featuring custom cards and anima… |
| 2026-10-27 22:04:22 | [PixelForge](https://www.nuget.org/packages/PixelForge) | 0.1.0 | Grant Totinov | MIT image processing for .NET on SkiaSharp. Familiar Load/Mutate/Resize/Save AP… |
| 2026-10-27 22:12:29 | [ExperianClient](https://www.nuget.org/packages/ExperianClient) | 1.0.0 | Tuomas Hietanen | Client for the most used Experian UK APIs (not every Experian service): Delphi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
