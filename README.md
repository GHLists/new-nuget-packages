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

## Latest list — 2026-11-08 18:21 UTC

New packages created between 2026-11-08 17:19 UTC and 2026-11-08 18:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T18-21-27-40166Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 17:22:45 | [ScriptFoundry](https://www.nuget.org/packages/ScriptFoundry) | 0.1.1 | Federico Alterio | Compile a restricted subset of C# into delegates with explicit type and member… |
| 2026-11-08 17:37:24 | [ThunderPipe.Cli](https://www.nuget.org/packages/ThunderPipe.Cli) | 1.0.5 | WarperSan | A CLI tool for building and publishing Thunderstore packages |
| 2026-11-08 17:38:35 | [Lengko.Ribbon.WinForm](https://www.nuget.org/packages/Lengko.Ribbon.WinForm) | 1.0.0 | LengkoDev, Cas | Modern, high-performance, and responsive Ribbon UI toolbar control for Windows… |
| 2026-11-08 17:49:54 | [Blink1.Api](https://www.nuget.org/packages/Blink1.Api) | 1.0.3 | Panoramic Data Limited | A typed, modern .NET client for the ThingM blink(1) USB RGB LED: device enumera… |
| 2026-11-08 17:51:56 | [Vibeniq.BaaS.Core.Testing](https://www.nuget.org/packages/Vibeniq.BaaS.Core.Testing) | 10.0.0.16 | Vibeniq | Test-only architecture-check helpers for services built on Vibeniq.BaaS.Core (A… |
| 2026-11-08 17:53:39 | [Motorbay.Client](https://www.nuget.org/packages/Motorbay.Client) | 0.4.2 | Motorbay | C# client for the Motorbay API: Danish vehicle data from Motorstyrelsen's publi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
