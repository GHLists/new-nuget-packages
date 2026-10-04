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

## Latest list — 2026-10-04 10:19 UTC

New packages created between 2026-10-04 09:22 UTC and 2026-10-04 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T10-19-52-389207Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 09:37:57 | [SideEffect.Data](https://www.nuget.org/packages/SideEffect.Data) | 0.6.0 | Artsiom Marzavin | A general-purpose library with models for data storage. |
| 2026-10-04 09:41:56 | [Novolis.Time.Workday](https://www.nuget.org/packages/Novolis.Time.Workday) | 2026.1.1.11 | Novolis | Immutable workday calendars and business-day arithmetic. |
| 2026-10-04 09:42:48 | [MTNMoMo.OpenApi](https://www.nuget.org/packages/MTNMoMo.OpenApi) | 1.0.0 | MTNMoMo Contributors | Production-ready MTN Mobile Money (MoMo) Open API .NET SDK — Collection, Disbur… |
| 2026-10-04 09:45:07 | [Beardmouse.Thoth.Json.Core](https://www.nuget.org/packages/Beardmouse.Thoth.Json.Core) | 0.9.1 | Maxime Mangel | Elm-inspired encoder and decoder for JSON, this package is the core library whi… |
| 2026-10-04 10:09:53 | [Packata.DataPackage](https://www.nuget.org/packages/Packata.DataPackage) | 0.45.2 | Cédric L. Charlier | Packata's native Data Package v2 document model, serialization, validation, and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
