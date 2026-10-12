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

## Latest list — 2026-10-12 19:20 UTC

New packages created between 2026-10-12 18:22 UTC and 2026-10-12 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T19-20-00-785385Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 18:34:41 | [Novolis.Avalonia.AssetStudio](https://www.nuget.org/packages/Novolis.Avalonia.AssetStudio) | 2026.1.6.240 | Novolis | Reusable Avalonia editor surfaces for Asset Studio graph, stack, source, diagno… |
| 2026-10-12 18:34:57 | [Novolis.Avalonia.Modeling](https://www.nuget.org/packages/Novolis.Avalonia.Modeling) | 2026.1.6.240 | Novolis | Avalonia Modeling editor surface: scene hierarchy, OpenGL wireframe viewport, m… |
| 2026-10-12 18:38:17 | [Ruvio.AspNetCore.DistributedLock](https://www.nuget.org/packages/Ruvio.AspNetCore.DistributedLock) | 0.1.0 | Salih Cantekin | Distributed mutual-exclusion locks for Ruvio, plus an ASP.NET Core [RuvioLock]… |
| 2026-10-12 18:41:02 | [Medalbot.Render](https://www.nuget.org/packages/Medalbot.Render) | 0.1.0 | Medalbot | Await CS2 skin renders with typed views, automatic polling, retries, and public… |
| 2026-10-12 18:44:00 | [NextLevel.Tenancy](https://www.nuget.org/packages/NextLevel.Tenancy) | 1.0.0 | NextLevel | Tenancy mode and the current OperatorId (tenant) for NextLevel backend services. |
| 2026-10-12 18:55:44 | [AWSSDK.SageMakerTrainingSessionRuntime](https://www.nuget.org/packages/AWSSDK.SageMakerTrainingSessionRuntime) | 4.0.100 | Amazon Web Services | Amazon SageMaker Training Session Runtime provides APIs for executing operation… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
