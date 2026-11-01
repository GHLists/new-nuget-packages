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

## Latest list — 2026-11-01 08:20 UTC

New packages created between 2026-11-01 07:19 UTC and 2026-11-01 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T08-20-08-424236Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 07:34:17 | [ArmadaMVVMToolkit](https://www.nuget.org/packages/ArmadaMVVMToolkit) | 1.0.0 | Armada | A minimal, dependency-free MVVM toolkit (ObservableObject, AsyncObservableObjec… |
| 2026-11-01 07:57:05 | [SapphireGuard.AgentEvals.Xunit](https://www.nuget.org/packages/SapphireGuard.AgentEvals.Xunit) | 0.3.0 | Anil Kerai | Runs a SapphireGuard.AgentEvals evaluation as an xUnit v3 test project: one Rea… |
| 2026-11-01 08:12:02 | [CloudGround.Templates](https://www.nuget.org/packages/CloudGround.Templates) | 0.1.0 | Q-Sharp | dotnet new template for container-based .NET solutions with Aspire, Angular and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
