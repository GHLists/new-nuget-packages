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

## Latest list — 2026-10-14 06:20 UTC

New packages created between 2026-10-14 05:21 UTC and 2026-10-14 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T06-20-54-25899Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 05:40:46 | [Blazecoin.ServiceDefaults](https://www.nuget.org/packages/Blazecoin.ServiceDefaults) | 1.0.0 | Blazecoin | Shared service plumbing for the Blazecoin website services: central Serilog log… |
| 2026-10-14 05:48:04 | [LokeshPandey.MyCalc](https://www.nuget.org/packages/LokeshPandey.MyCalc) | 1.0.0 | MyCalc | Package Description |
| 2026-10-14 06:05:16 | [PlatformHeads.Core](https://www.nuget.org/packages/PlatformHeads.Core) | 0.2.0 | https://github.com/SimonCropp… | The managed kernel of an app with one head per platform: the host of its immuta… |
| 2026-10-14 06:07:28 | [Stellaegis.Primitives.AspNetCore](https://www.nuget.org/packages/Stellaegis.Primitives.AspNetCore) | 1.1.0 | FRi | Stellaegis primitives for modules that expose HTTP endpoints: the request conte… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
