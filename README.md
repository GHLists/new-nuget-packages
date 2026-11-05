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

## Latest list — 2026-11-05 04:21 UTC

New packages created between 2026-11-05 03:20 UTC and 2026-11-05 04:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T04-21-09-610541Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 03:46:33 | [MofonCode.Sdlc.Cli](https://www.nuget.org/packages/MofonCode.Sdlc.Cli) | 0.36.1-preview | MofonCode | The gate for an ai-sdlc governed solution. A change moves through intent, spec,… |
| 2026-11-05 03:55:32 | [WaxUI](https://www.nuget.org/packages/WaxUI) | 1.0.0 | lllggghhhaaaa | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
