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

## Latest list — 2026-10-11 02:19 UTC

New packages created between 2026-10-11 01:21 UTC and 2026-10-11 02:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T02-19-36-5836Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 01:39:50 | [EvaluatedApplications.PleromaMind](https://www.nuget.org/packages/EvaluatedApplications.PleromaMind) | 1.0.0 | Evaluated Applications | A persistent conversational unit built on exact holograms. It speaks with a sub… |
| 2026-10-11 01:42:21 | [Novolis.WorkflowEngine.Flow](https://www.nuget.org/packages/Novolis.WorkflowEngine.Flow) | 2026.1.1.19 | Novolis | Renderer-independent typed ports and flow contracts for Novolis workflows. |
| 2026-10-11 01:42:22 | [Novolis.WorkflowEngine.FlowGraph](https://www.nuget.org/packages/Novolis.WorkflowEngine.FlowGraph) | 2026.1.1.19 | Novolis | Typed immutable flow graphs built from Novolis graph and flow contracts. |
| 2026-10-11 01:42:23 | [Novolis.WorkflowEngine.Graph](https://www.nuget.org/packages/Novolis.WorkflowEngine.Graph) | 2026.1.1.19 | Novolis | Immutable graph topology and deterministic graph analysis for Novolis workflows. |
| 2026-10-11 01:42:26 | [Novolis.WorkflowEngine.Pipeline](https://www.nuget.org/packages/Novolis.WorkflowEngine.Pipeline) | 2026.1.1.19 | Novolis | Typed linear pipeline composition with explicit result short-circuiting. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
