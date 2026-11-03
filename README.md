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

## Latest list — 2026-11-03 12:19 UTC

New packages created between 2026-11-03 11:21 UTC and 2026-11-03 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T12-19-52-888117Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 11:25:14 | [Winterborn.Tools.Vee](https://www.nuget.org/packages/Winterborn.Tools.Vee) | 21.3.3 | Winterborn.Tools.Vee | Package Description |
| 2026-11-03 11:54:30 | [Lindekilde.Blazor.Cruddy](https://www.nuget.org/packages/Lindekilde.Blazor.Cruddy) | 0.9.1-alpha | JakobLindekilde | Simple ASP.NET Blazor component that does database table CRUD |
| 2026-11-03 12:01:26 | [DataverseLogicDependencyExplorer](https://www.nuget.org/packages/DataverseLogicDependencyExplorer) | 1.2026.11.11 | Gagan Deep Singh | An XrmToolBox tool that finds where a Dataverse table or column is referenced b… |
| 2026-11-03 12:04:32 | [SignalSpec.AspNetCore](https://www.nuget.org/packages/SignalSpec.AspNetCore) | 0.1.0 | IvanKobtsev | Standalone SignalR client contract specifications and automatic hub mapping. |
| 2026-11-03 12:09:35 | [dotnet-cockpit](https://www.nuget.org/packages/dotnet-cockpit) | 0.1.0 | Jan Ruhlaender | A local browser cockpit for your .NET installations. |
| 2026-11-03 12:14:27 | [FastSI.DispatchR](https://www.nuget.org/packages/FastSI.DispatchR) | 1.0.0 | FastSI Team | Mediator for .NET: CQRS, pub/sub, streaming and pipeline behaviors. MediatR-com… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
