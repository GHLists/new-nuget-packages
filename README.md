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

## Latest list — 2026-10-30 09:20 UTC

New packages created between 2026-10-30 08:21 UTC and 2026-10-30 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T09-20-47-138499Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 08:55:14 | [T.Molodoy.Compose.Net.Kaspresso](https://www.nuget.org/packages/T.Molodoy.Compose.Net.Kaspresso) | 0.0.2 | T. Molodoy | A small Kaspresso-inspired UI testing DSL for Compose.Net. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
