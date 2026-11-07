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

## Latest list — 2026-11-07 22:21 UTC

New packages created between 2026-11-07 21:20 UTC and 2026-11-07 22:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T22-21-11-687912Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 21:39:21 | [soso.serialization](https://www.nuget.org/packages/soso.serialization) | 1.0.0 | Ky Price | A reasonably lightweight binary serialization library |
| 2026-11-07 21:40:20 | [Shiny.Mediator.Avalonia](https://www.nuget.org/packages/Shiny.Mediator.Avalonia) | 6.13.0-beta-0001 | Allan Ritchie | Shiny Mediator - Avalonia integration (view/view model event collection, main t… |
| 2026-11-07 22:08:44 | [TotalSerializer](https://www.nuget.org/packages/TotalSerializer) | 0.1.0-alpha | astropiano | Serializes the complete state of .NET object graphs - including private fields,… |
| 2026-11-07 22:08:44 | [TotalSerializer.ReflectionTools](https://www.nuget.org/packages/TotalSerializer.ReflectionTools) | 0.1.0-alpha | astropiano | Efficient reflection helpers used by TotalSerializer: cached member access, fas… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
