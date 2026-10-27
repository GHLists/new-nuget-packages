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

## Latest list — 2026-10-27 04:20 UTC

New packages created between 2026-10-27 03:20 UTC and 2026-10-27 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T04-20-07-869238Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 03:25:42 | [RytaPDF](https://www.nuget.org/packages/RytaPDF) | 0.1.0 | ryantavan | A lightweight, QuestPDF-inspired PDF document layout engine for .NET with a flu… |
| 2026-10-27 03:43:21 | [CSJS.Templates](https://www.nuget.org/packages/CSJS.Templates) | 0.2.0 | Gravicode Studios | `dotnet new` templates for CSJS, the C#-to-JavaScript transpiler: a browser app… |
| 2026-10-27 03:43:23 | [CSJS.Build](https://www.nuget.org/packages/CSJS.Build) | 0.2.0 | Gravicode Studios | MSBuild integration for CSJS: `dotnet build` transpiles the project's C# to mod… |
| 2026-10-27 03:48:07 | [PeroTools2.AccessKing](https://www.nuget.org/packages/PeroTools2.AccessKing) | 0.3.0 | PeroperoGames | Event Bus & Command Bus |
| 2026-10-27 03:50:50 | [SolariumDb](https://www.nuget.org/packages/SolariumDb) | 0.1.1 | Andres Gutierrez | An embedded key-value store for .NET with RocksDB's API and semantics: column f… |
| 2026-10-27 03:51:03 | [SolariumDb.Kommander](https://www.nuget.org/packages/SolariumDb.Kommander) | 0.1.1 | Andres Gutierrez | A Kommander write-ahead log (IWAL) on Solarium, an embedded key-value store for… |
| 2026-10-27 03:51:12 | [SolariumDb.Kahuna](https://www.nuget.org/packages/SolariumDb.Kahuna) | 0.1.1 | Andres Gutierrez | A Kahuna storage engine on Solarium, an embedded key-value store for .NET with… |
| 2026-10-27 03:51:22 | [SolariumDb.IoUring](https://www.nuget.org/packages/SolariumDb.IoUring) | 0.1.1 | Andres Gutierrez | An io_uring storage environment for Solarium on Linux 6.1 or later, on the ioxi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
