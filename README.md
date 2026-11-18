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

## Latest list — 2026-11-18 23:19 UTC

New packages created between 2026-11-18 22:21 UTC and 2026-11-18 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T23-19-18-497953Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 22:50:34 | [SDL3-CS.Layer](https://www.nuget.org/packages/SDL3-CS.Layer) | 1.0.1 | Jonas S. | C# bindings for SDL_layer, intended for use with SDL3-CS |
| 2026-11-18 22:51:02 | [SDL3-CS.Layer.Linux](https://www.nuget.org/packages/SDL3-CS.Layer.Linux) | 1.0.1 | Jonas S. | Native Linux library for SDL3-CS.Layer |
| 2026-11-18 22:54:07 | [Flowon.Xrm.Tools.PowerShell](https://www.nuget.org/packages/Flowon.Xrm.Tools.PowerShell) | 1.2.0 | Flowon Team | PowerShell module for Logic Fabric: export and import Logic Fabric projects, Da… |
| 2026-11-18 22:58:11 | [Pidief.Client](https://www.nuget.org/packages/Pidief.Client) | 0.1.0 | Milvasoft | Typed .NET client for the pidief PDF API: HTML/template/images to PDF, merge, s… |
| 2026-11-18 23:04:27 | [envparity](https://www.nuget.org/packages/envparity) | 1.0.0 | Jhon Emmir Cundumi Riascos | Validate a .env file against a reference file without ever printing values. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
