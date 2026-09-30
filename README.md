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

## Latest list — 2026-09-30 05:20 UTC

New packages created between 2026-09-30 04:20 UTC and 2026-09-30 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T05-20-04-932412Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 04:21:35 | [FsForge](https://www.nuget.org/packages/FsForge) | 0.0.1-beta1 | Devon Burriss | Provider-agnostic git and pull request write-back for F#: clone, worktree, comm… |
| 2026-09-30 04:27:16 | [Scaidome.Logging](https://www.nuget.org/packages/Scaidome.Logging) | 1.1.0 | Nicklas Hammer Thygesen | A rolling-file logging provider for Microsoft.Extensions.Logging. |
| 2026-09-30 04:27:17 | [Scaidome.Dapper](https://www.nuget.org/packages/Scaidome.Dapper) | 1.1.0 | Nicklas Hammer Thygesen | Dapper type handlers for Scaidome's SQLite stores: reading identities and times… |
| 2026-09-30 04:27:18 | [Scaidome.Json](https://www.nuget.org/packages/Scaidome.Json) | 1.1.0 | Nicklas Hammer Thygesen | JSON rules for Scaidome typed documents: a codec for settings stored as JSON an… |
| 2026-09-30 04:27:19 | [Scaidome.Channels](https://www.nuget.org/packages/Scaidome.Channels) | 1.1.0 | Nicklas Hammer Thygesen | Action queues for Scaidome: unbounded in-memory queues with many producers and… |
| 2026-09-30 04:37:21 | [RevolutionaryStuff.BlazorWasm](https://www.nuget.org/packages/RevolutionaryStuff.BlazorWasm) | 4.200.100 | jason@jasonthomas.com | Package Description |
| 2026-09-30 04:38:29 | [mathsolver-help](https://www.nuget.org/packages/mathsolver-help) | 0.2.0 | mathsolver.help | BYOK AI math solver with execution-based verification (PAL-style) — bring your… |
| 2026-09-30 04:43:07 | [AnointedAutomation.Optimization](https://www.nuget.org/packages/AnointedAutomation.Optimization) | 1.0.0 | Anointed Automation LLC, Alex… | Reusable optimization utilities: CSV/DataTable/DataReader helpers, chunking, st… |
| 2026-09-30 04:44:10 | [ContentCalendar.V18](https://www.nuget.org/packages/ContentCalendar.V18) | 1.0.0 | ZAAKS! | A content calendar for the Umbraco 18 backoffice. A Content section dashboard a… |
| 2026-09-30 04:46:11 | [Nabs.Launchpad.Core.MigrationsCli](https://www.nuget.org/packages/Nabs.Launchpad.Core.MigrationsCli) | 10.1.2 | Darrel Schreyer | Package Description |
| 2026-09-30 04:53:56 | [DeepSharp.Charts](https://www.nuget.org/packages/DeepSharp.Charts) | 0.4.0 | H.P. Gansevoort | The charts of a DeepSharp run, drawn from what the training loop and the measur… |
| 2026-09-30 04:53:56 | [DeepSharp.Learners.Networks](https://www.nuget.org/packages/DeepSharp.Learners.Networks) | 0.4.0 | H.P. Gansevoort | Where a DeepSharp network meets a DeepSharp pipeline: a network learns from the… |
| 2026-09-30 05:11:45 | [NetOpenEditor](https://www.nuget.org/packages/NetOpenEditor) | 1.0.0 | jfrancoInteriano | Inline line editor for header-detail forms in ASP.NET Core MVC (.NET 10). Colum… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
