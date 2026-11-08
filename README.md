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

## Latest list — 2026-11-08 23:19 UTC

New packages created between 2026-11-08 22:21 UTC and 2026-11-08 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T23-19-55-23026Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 22:50:17 | [Stabilt.TellusTalk.Emulator.Aspire](https://www.nuget.org/packages/Stabilt.TellusTalk.Emulator.Aspire) | 0.2.0 | Stabilt AB | Runs TellusTalk Emulator, a local stand-in for TellusTalk's K8 send API, from a… |
| 2026-11-08 22:51:09 | [FontStashSharp.Rasterizers.StbTrueTypeNext](https://www.nuget.org/packages/FontStashSharp.Rasterizers.StbTrueTypeNext) | 1.3.0 | FontStashSharpTeam | Package Description |
| 2026-11-08 23:07:24 | [Th3z.Kanban.Plugins](https://www.nuget.org/packages/Th3z.Kanban.Plugins) | 0.5.1 | Th3shoterZ | The contract for plugins of the TH3Z Kanban desktop app. |
| 2026-11-08 23:12:11 | [ghget](https://www.nuget.org/packages/ghget) | 0.1.0 | haohanyang | A command line tool that downloads files and directories from GitHub by URL. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
