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

## Latest list — 2026-10-18 06:20 UTC

New packages created between 2026-10-18 05:21 UTC and 2026-10-18 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T06-20-01-62347Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 05:29:05 | [Osirion.Blazor.Templates](https://www.nuget.org/packages/Osirion.Blazor.Templates) | 4.2.0 | Dejan Demonjić | Project templates for Osirion.Blazor, served with static server-side rendering:… |
| 2026-10-18 05:34:13 | [Obelisk.Abstractions](https://www.nuget.org/packages/Obelisk.Abstractions) | 0.1.0 | Taegyun Eom | Obelisk.Abstractions for Obelisk Engine, an experimental .NET 10 2D game engine… |
| 2026-10-18 05:34:14 | [Obelisk.Graphics2D](https://www.nuget.org/packages/Obelisk.Graphics2D) | 0.1.0 | Taegyun Eom | Obelisk.Graphics2D for Obelisk Engine, an experimental .NET 10 2D game engine t… |
| 2026-10-18 05:34:16 | [Obelisk.Runtime](https://www.nuget.org/packages/Obelisk.Runtime) | 0.1.0 | Taegyun Eom | Obelisk.Runtime for Obelisk Engine, an experimental .NET 10 2D game engine targ… |
| 2026-10-18 05:34:18 | [Obelisk.Assets](https://www.nuget.org/packages/Obelisk.Assets) | 0.1.0 | Taegyun Eom | Obelisk.Assets for Obelisk Engine, an experimental .NET 10 2D game engine targe… |
| 2026-10-18 05:34:19 | [Obelisk.Plugin](https://www.nuget.org/packages/Obelisk.Plugin) | 0.1.0 | Taegyun Eom | Obelisk.Plugin for Obelisk Engine, an experimental .NET 10 2D game engine targe… |
| 2026-10-18 05:34:22 | [Obelisk.Platform.Sdl3](https://www.nuget.org/packages/Obelisk.Platform.Sdl3) | 0.1.0 | Taegyun Eom | Obelisk.Platform.Sdl3 for Obelisk Engine, an experimental .NET 10 2D game engin… |
| 2026-10-18 05:34:23 | [Obelisk.Plugins.Images](https://www.nuget.org/packages/Obelisk.Plugins.Images) | 0.1.0 | Taegyun Eom | Obelisk.Plugins.Images for Obelisk Engine, an experimental .NET 10 2D game engi… |
| 2026-10-18 05:34:25 | [Obelisk.Vanilla](https://www.nuget.org/packages/Obelisk.Vanilla) | 0.1.0 | Taegyun Eom | Obelisk.Vanilla for Obelisk Engine, an experimental .NET 10 2D game engine targ… |
| 2026-10-18 05:35:11 | [Obelisk.Cli](https://www.nuget.org/packages/Obelisk.Cli) | 0.1.0 | Taegyun Eom | Obelisk Engine project creation and development CLI. |
| 2026-10-18 05:54:53 | [Omasharp.Analyzers](https://www.nuget.org/packages/Omasharp.Analyzers) | 0.1.0 | Luis Rudge | Compile-time checks for omasharp apps (C# + QML on Omarchy): names QML can't ta… |
| 2026-10-18 05:54:54 | [Omasharp.Templates](https://www.nuget.org/packages/Omasharp.Templates) | 0.1.0 | Luis Rudge | dotnet new omarchy-app: C# + QML apps for Omarchy. Window apps compile to one n… |
| 2026-10-18 06:11:38 | [Tezz.Auth](https://www.nuget.org/packages/Tezz.Auth) | 1.0.0 | TezzCorp Pvt. Ltd. | Official .NET Client SDK for Tezz Auth |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
