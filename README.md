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

## Latest list — 2026-10-11 08:22 UTC

New packages created between 2026-10-11 07:22 UTC and 2026-10-11 08:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T08-22-02-111829Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 07:28:35 | [DotNetCore.Collections](https://www.nuget.org/packages/DotNetCore.Collections) | 7.1.0 | AlexLEWIS,dotnetcore | High-performance LINQ engine with value-type enumerators and zero-allocation ho… |
| 2026-10-11 07:48:03 | [ContextKit](https://www.nuget.org/packages/ContextKit) | 1.0.0-preview-0015 | ContextKit.Cli | Package Description |
| 2026-10-11 07:48:04 | [ContextKit.Mcp](https://www.nuget.org/packages/ContextKit.Mcp) | 1.0.0-preview-0015 | ContextKit.Mcp.Host | Package Description |
| 2026-10-11 07:52:26 | [Marey.Sim](https://www.nuget.org/packages/Marey.Sim) | 0.6.0 | Marey contributors | Simulation for Marey: ODE integrators typed by units of measure (Euler, RK4, Do… |
| 2026-10-11 07:57:09 | [Caveman.Compliance](https://www.nuget.org/packages/Caveman.Compliance) | 1.0.0 | Francesco Paolo Passaro | AI compliance engine for LLM gateways: one rule registry (risk, action, scope)… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
