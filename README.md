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

## Latest list — 2026-10-03 14:22 UTC

New packages created between 2026-10-03 13:18 UTC and 2026-10-03 14:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T14-22-44-799589Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 13:23:09 | [QuestViva.Legacy](https://www.nuget.org/packages/QuestViva.Legacy) | 6.0.0 | Alex Warren | Quest 4 and earlier backward-compatibility layer for Quest Viva, an open-source… |
| 2026-10-03 13:23:09 | [QuestViva.PlayerCore](https://www.nuget.org/packages/QuestViva.PlayerCore) | 6.0.0 | Alex Warren | Game player runtime for Quest Viva — load and query .aslx text adventure game f… |
| 2026-10-03 13:23:09 | [QuestViva.Common](https://www.nuget.org/packages/QuestViva.Common) | 6.0.0 | Alex Warren | Shared types and interfaces for Quest Viva, an open-source text adventure game… |
| 2026-10-03 13:23:10 | [QuestViva.Engine](https://www.nuget.org/packages/QuestViva.Engine) | 6.0.0 | Alex Warren | Core game interpreter for Quest Viva — script execution, expression evaluation,… |
| 2026-10-03 13:25:07 | [Anton.CodingRules](https://www.nuget.org/packages/Anton.CodingRules) | 0.1.0 | Anton C. | C# coding rules with Roslyn diagnostics and code fixes. |
| 2026-10-03 14:11:28 | [Valhalla.Bindings](https://www.nuget.org/packages/Valhalla.Bindings) | 0.1.3 | Valhalla.Bindings | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
