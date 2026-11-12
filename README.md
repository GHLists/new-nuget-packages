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

## Latest list — 2026-11-12 08:20 UTC

New packages created between 2026-11-12 07:21 UTC and 2026-11-12 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T08-20-46-732532Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 07:43:44 | [DataForge.DataPlatform.ScriptHost](https://www.nuget.org/packages/DataForge.DataPlatform.ScriptHost) | 1.1.0 | DataService | DataService JavaScript script host with SQL query execution, debugging, caching… |
| 2026-11-12 07:49:08 | [Fdw.Bundle](https://www.nuget.org/packages/Fdw.Bundle) | 1.5.6 | Fdw.Bundle | Release 1.5.6: pins 287 packages to the exact versions this release shipped. No… |
| 2026-11-12 07:53:18 | [VGrid.Blazor](https://www.nuget.org/packages/VGrid.Blazor) | 1.0.0 | Vijai Aaditya, OpenDen | Ultra-fast, lightweight data grid for Blazor WebAssembly and Blazor Server with… |
| 2026-11-12 07:57:54 | [SuperSemantics.Vsl.AgentFramework](https://www.nuget.org/packages/SuperSemantics.Vsl.AgentFramework) | 0.1.1 | Super Semantics | Microsoft Agent Framework adapter for VSL governance primitives: compiles PreNo… |
| 2026-11-12 07:59:37 | [LibDmd.Core.Native.win-x64](https://www.nuget.org/packages/LibDmd.Core.Native.win-x64) | 2.5.0 | freezy and contributors | This package complements LibDmd.Core and contains the native binaries (libserum… |
| 2026-11-12 07:59:38 | [LibDmd.Core.Native.osx-x64](https://www.nuget.org/packages/LibDmd.Core.Native.osx-x64) | 2.5.0 | freezy and contributors | This package complements LibDmd.Core and contains the native binaries (libserum… |
| 2026-11-12 07:59:41 | [LibDmd.Core.Native.osx-arm64](https://www.nuget.org/packages/LibDmd.Core.Native.osx-arm64) | 2.5.0 | freezy and contributors | This package complements LibDmd.Core and contains the native binaries (libserum… |
| 2026-11-12 07:59:42 | [LibDmd.Core.Native.linux-x64](https://www.nuget.org/packages/LibDmd.Core.Native.linux-x64) | 2.5.0 | freezy and contributors | This package complements LibDmd.Core and contains the native binaries (libserum… |
| 2026-11-12 07:59:43 | [LibDmd.Core.Native](https://www.nuget.org/packages/LibDmd.Core.Native) | 2.5.0 | freezy and contributors | Meta-package that pulls the per-platform native binaries (libserum, libzedmd) u… |
| 2026-11-12 07:59:44 | [LibDmd.Core](https://www.nuget.org/packages/LibDmd.Core) | 2.5.0 | freezy and contributors | Cross-platform (WPF-free) core of dmd-extensions / LibDmd: the reactive frame p… |
| 2026-11-12 08:04:48 | [PlaIO](https://www.nuget.org/packages/PlaIO) | 0.1.0 | mahach666 | Reads the container of Archicad project files (.pla, .pln) and the cover image… |
| 2026-11-12 08:04:50 | [PlaIO.Cli](https://www.nuget.org/packages/PlaIO.Cli) | 0.1.0 | mahach666 | Command line tool that reports the container structure of Archicad files (.pla,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
