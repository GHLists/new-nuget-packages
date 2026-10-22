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

## Latest list — 2026-10-22 23:21 UTC

New packages created between 2026-10-22 22:22 UTC and 2026-10-22 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T23-21-56-23101Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 22:24:42 | [StructuredConcurrency.Hosting](https://www.nuget.org/packages/StructuredConcurrency.Hosting) | 0.6.0 | Gokhan Ertogan | A BackgroundService whose work runs in a StructuredConcurrency TaskGroup: on sh… |
| 2026-10-22 22:34:26 | [CuteDB.Browser](https://www.nuget.org/packages/CuteDB.Browser) | 2.2.0 | Gravicode Studios, Kang Fadhil | CuteDB Browser: a desktop workbench for CuteDB databases. Browse collections an… |
| 2026-10-22 22:36:14 | [Lissic](https://www.nuget.org/packages/Lissic) | 0.1.0 | Gary Gende | A templating library for .NET |
| 2026-10-22 22:42:27 | [Microsoft.Agents.CopilotStudio.Sync](https://www.nuget.org/packages/Microsoft.Agents.CopilotStudio.Sync) | 1.9.19 | Microsoft | Shared library for cloning, synchronizing, and projecting Microsoft Copilot Stu… |
| 2026-10-22 22:44:15 | [Coss](https://www.nuget.org/packages/Coss) | 0.1.0 | coss.com | The coss.com SDK for .NET: every endpoint of the coss.com API, typed, with retr… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
