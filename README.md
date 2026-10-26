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

## Latest list — 2026-10-26 20:21 UTC

New packages created between 2026-10-26 19:21 UTC and 2026-10-26 20:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T20-21-12-328412Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 19:24:31 | [BinReader.NPoint](https://www.nuget.org/packages/BinReader.NPoint) | 1.0.1 | RobinClaesson | A .NET client for reading and caching JSON bins from https://www.npoint.io/ |
| 2026-10-26 19:42:52 | [NUnit.Tools.TestExplorerDump](https://www.nuget.org/packages/NUnit.Tools.TestExplorerDump) | 1.0.0 | Terje Sandstrom | Internal NUnit tool: dumps the Visual Studio Test Explorer tree as text, and dr… |
| 2026-10-26 19:44:20 | [RecursiveAI.OneGame.Sdk](https://www.nuget.org/packages/RecursiveAI.OneGame.Sdk) | 1.1.0 | Recursive AI, LLC | MSBuild SDK for onegame games: references, rules and export targets, so a game… |
| 2026-10-26 19:44:23 | [RecursiveAI.OneGame.Cli](https://www.nuget.org/packages/RecursiveAI.OneGame.Cli) | 1.1.0 | Recursive AI, LLC | The onegame command: create, build, run, test, capture and replay games. |
| 2026-10-26 19:45:20 | [Bebop.JsonPath](https://www.nuget.org/packages/Bebop.JsonPath) | 1.0.0 | Alexander Jesner | RFC 9535 compliant JSONPath implementation for .NET |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
