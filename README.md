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

## Latest list — 2026-10-03 11:20 UTC

New packages created between 2026-10-03 10:19 UTC and 2026-10-03 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T11-20-33-852088Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 10:24:18 | [ChudoObuv.DemoExam2027.Project](https://www.nuget.org/packages/ChudoObuv.DemoExam2027.Project) | 1.0.0 | ChudoObuv | Проект «Чудо Обувь» (WPF .NET Framework 4.8 + Entity Framework 6 + MS SQL Serve… |
| 2026-10-03 10:40:15 | [KeelMatrix.MetricBudget](https://www.nuget.org/packages/KeelMatrix.MetricBudget) | 0.1.0 | KeelMatrix | Verify observed metric cardinality in .NET tests and CI. Observe the metric ser… |
| 2026-10-03 11:02:40 | [isRock.VoiceInput](https://www.nuget.org/packages/isRock.VoiceInput) | 1.0.0 | isRock.VoiceInput | Windows console push-to-talk dictation using MAI-Transcribe-2 with Taiwan Tradi… |
| 2026-10-03 11:11:05 | [Botassembly.ThinkThen](https://www.nuget.org/packages/Botassembly.ThinkThen) | 0.1.1 | ThinkThen contributors | Linux C ABI facade; install matching native archive separately |
| 2026-10-03 11:13:32 | [Novolis.Storage.AzureCombinedStorage](https://www.nuget.org/packages/Novolis.Storage.AzureCombinedStorage) | 2026.1.1.48 | Novolis | Preview aggregate storage over Azure Table Storage and Azure Blob Storage. |
| 2026-10-03 11:13:35 | [Novolis.Storage.Indexing](https://www.nuget.org/packages/Novolis.Storage.Indexing) | 2026.1.1.48 | Novolis | Experimental revision-aware indexing infrastructure for Novolis storage provide… |
| 2026-10-03 11:13:40 | [Novolis.Storage.Query](https://www.nuget.org/packages/Novolis.Storage.Query) | 2026.1.1.48 | Novolis | Provider-independent query contracts and finite query execution for Novolis sto… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
