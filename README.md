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

## Latest list — 2026-11-01 00:18 UTC

New packages created between 2026-10-31 23:18 UTC and 2026-11-01 00:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T00-18-27-65894Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 23:31:19 | [BozForge.Bogus.Validation](https://www.nuget.org/packages/BozForge.Bogus.Validation) | 0.1.0 | Hüseyin Bozdemir | Valid-by-construction test data for Bogus: reads DataAnnotations attributes ([R… |
| 2026-10-31 23:31:20 | [BozForge.Bogus.Validation.FluentValidation](https://www.nuget.org/packages/BozForge.Bogus.Validation.FluentValidation) | 0.1.0 | Hüseyin Bozdemir | FluentValidation support for BozForge.Bogus.Validation: reads the rules of an A… |
| 2026-10-31 23:46:03 | [Tamp.Heft.V1](https://www.nuget.org/packages/Tamp.Heft.V1) | 0.1.0 | Scott Singleton | Tamp CommandPlan wrapper for Rushstack Heft 1.x, the build orchestrator behind… |
| 2026-10-31 23:46:29 | [kgen.ControlCatalog.Extension.Markdown](https://www.nuget.org/packages/kgen.ControlCatalog.Extension.Markdown) | 0.1.0 | Frederic Forjan | Markdown.Avalonia plugin for the Avalonia ControlCatalog / KGen Flavored. |
| 2026-10-31 23:52:53 | [Tamp.Spfx](https://www.nuget.org/packages/Tamp.Spfx) | 0.1.0 | Scott Singleton | Tamp build support for SharePoint Framework (SPFx 1.22+, the Heft toolchain): t… |
| 2026-10-31 23:55:05 | [LANCommander.Plugins.Sync](https://www.nuget.org/packages/LANCommander.Plugins.Sync) | 1.0.0 | LANCommander | Syncs games, redistributables and tools between LANCommander servers. Each serv… |
| 2026-10-31 23:55:44 | [Packata.Arrow](https://www.nuget.org/packages/Packata.Arrow) | 1.22.0 | Cédric L. Charlier | Optional transport-independent conversion of canonical Packata schemas and read… |
| 2026-11-01 00:01:27 | [BorrowedTorch.Nature](https://www.nuget.org/packages/BorrowedTorch.Nature) | 0.0.1 | Vladyslav Pysarenko | Nature for MonoGame (compute fork), generated and drawn on the GPU. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
