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

## Latest list — 2026-10-01 22:21 UTC

New packages created between 2026-10-01 21:21 UTC and 2026-10-01 22:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T22-21-26-994227Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 21:23:40 | [Cosmos.Executable.Lua](https://www.nuget.org/packages/Cosmos.Executable.Lua) | 1.0.0 | Cosmos | Lua 5.2 interpreter for Cosmos Gen3 kernels, based on UniLua. |
| 2026-10-01 21:38:29 | [OpenExit](https://www.nuget.org/packages/OpenExit) | 0.1.0 | OpenExit | .NET SDK for OpenExit and PASP — the Portable Application State Protocol. |
| 2026-10-01 21:40:39 | [Sms.Debug.Core](https://www.nuget.org/packages/Sms.Debug.Core) | 0.0.3 | SuperJMN | Data model shared by the Sms.Mcp Sega Master System / Game Gear debugger: regis… |
| 2026-10-01 21:41:32 | [D5HU.Utilities.Tasks](https://www.nuget.org/packages/D5HU.Utilities.Tasks) | 0.1.0 | Bernhard Grauer | Asynchronous coordination primitives for .NET. |
| 2026-10-01 21:45:19 | [Sms.Debug.Emulator](https://www.nuget.org/packages/Sms.Debug.Emulator) | 0.0.3 | SuperJMN | Fully managed, headless Sega Master System / Game Gear emulator and debug sessi… |
| 2026-10-01 21:49:02 | [Xake.Hermetic.Dotnet](https://www.nuget.org/packages/Xake.Hermetic.Dotnet) | 0.1.0.22 | OlegZee | Reproducible .NET builds for Xake: lock files, restore, SBOM, verification, pac… |
| 2026-10-01 22:08:24 | [Namh.Configuration.GlobalTemplate](https://www.nuget.org/packages/Namh.Configuration.GlobalTemplate) | 1.0.0 | Nam Hoang | Integrates configuration templates with .NET generic hosts and ASP.NET Core app… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
