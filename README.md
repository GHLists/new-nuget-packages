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

## Latest list — 2026-10-31 20:18 UTC

New packages created between 2026-10-31 19:21 UTC and 2026-10-31 20:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T20-18-18-08974Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 19:24:35 | [LucasVerissimo.XrmToolBox.DataverseMappingManager](https://www.nuget.org/packages/LucasVerissimo.XrmToolBox.DataverseMappingManager) | 1.0.1 | Lucas Verissimo | Review, validate, create, edit and remove Dataverse column mappings with staged… |
| 2026-10-31 19:31:09 | [NyssaAI.DbGateway](https://www.nuget.org/packages/NyssaAI.DbGateway) | 0.1.0 | jamaynor | AOT-compatible dual-engine database gateway with typed commands, automatic para… |
| 2026-10-31 19:44:39 | [QxTui](https://www.nuget.org/packages/QxTui) | 0.1.0 | pmp | A terminal UI framework for .NET with fine-grained reactivity and damage isolat… |
| 2026-10-31 19:48:40 | [FastGeneration.Generator](https://www.nuget.org/packages/FastGeneration.Generator) | 0.1.0 | swedishkid | Source generator for immutable partial entities, read-only interfaces, and type… |
| 2026-10-31 19:55:42 | [NyssaAI.Logging](https://www.nuget.org/packages/NyssaAI.Logging) | 0.2.2 | jamaynor | Rotating structured JSON file logging and standard-error setup for Microsoft.Ex… |
| 2026-10-31 19:58:34 | [Lockflight.Cli.linux-arm64](https://www.nuget.org/packages/Lockflight.Cli.linux-arm64) | 0.3.0 | Bohdan Ivaniichuk | Lockflight engine for Claude Code agents on .NET projects: deterministic qualit… |
| 2026-10-31 19:58:36 | [Lockflight.Cli.linux-x64](https://www.nuget.org/packages/Lockflight.Cli.linux-x64) | 0.3.0 | Bohdan Ivaniichuk | Lockflight engine for Claude Code agents on .NET projects: deterministic qualit… |
| 2026-10-31 19:58:37 | [Lockflight.Cli.osx-arm64](https://www.nuget.org/packages/Lockflight.Cli.osx-arm64) | 0.3.0 | Bohdan Ivaniichuk | Lockflight engine for Claude Code agents on .NET projects: deterministic qualit… |
| 2026-10-31 19:58:38 | [Lockflight.Cli.osx-x64](https://www.nuget.org/packages/Lockflight.Cli.osx-x64) | 0.3.0 | Bohdan Ivaniichuk | Lockflight engine for Claude Code agents on .NET projects: deterministic qualit… |
| 2026-10-31 19:58:39 | [Lockflight.Cli.win-x64](https://www.nuget.org/packages/Lockflight.Cli.win-x64) | 0.3.0 | Bohdan Ivaniichuk | Lockflight engine for Claude Code agents on .NET projects: deterministic qualit… |
| 2026-10-31 19:58:40 | [Lockflight.Cli](https://www.nuget.org/packages/Lockflight.Cli) | 0.3.0 | Bohdan Ivaniichuk | Lockflight engine for Claude Code agents on .NET projects: deterministic qualit… |
| 2026-10-31 20:00:36 | [TurtleRoute.OpenCage](https://www.nuget.org/packages/TurtleRoute.OpenCage) | 0.18.0 | Dime Software | OpenCage geocoding provider for Turtle Route |
| 2026-10-31 20:00:36 | [TurtleRoute.Here](https://www.nuget.org/packages/TurtleRoute.Here) | 0.18.0 | Dime Software | HERE routing provider for Turtle Route |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
