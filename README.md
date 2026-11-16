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

## Latest list — 2026-11-16 02:21 UTC

New packages created between 2026-11-16 01:21 UTC and 2026-11-16 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T02-21-43-115466Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 01:46:36 | [MinimalLambda.EventProcessing](https://www.nuget.org/packages/MinimalLambda.EventProcessing) | 2.8.0 | LayeredCraft | Optional scoped event processing for MinimalLambda |
| 2026-11-16 02:00:43 | [Tooark.Http](https://www.nuget.org/packages/Tooark.Http) | 4.9.0 | Paulo Sergio de Freitas Junior | Library for outbound HTTP in .NET projects: a thin JSON service over IHttpClien… |
| 2026-11-16 02:00:46 | [Tooark.Entities.EntityFrameworkCore](https://www.nuget.org/packages/Tooark.Entities.EntityFrameworkCore) | 4.9.0 | Paulo Sergio de Freitas Junior | Library that plugs the Tooark entities into Entity Framework Core: an intercept… |
| 2026-11-16 02:01:31 | [50ea9d18-4c32-47dc-9877-00c0efc34f89](https://www.nuget.org/packages/50ea9d18-4c32-47dc-9877-00c0efc34f89) | 1.0.0 | D3kky | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
