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

## Latest list — 2026-11-10 07:21 UTC

New packages created between 2026-11-10 06:19 UTC and 2026-11-10 07:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T07-21-45-034784Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 06:50:25 | [DeviceSpecs.Mcp](https://www.nuget.org/packages/DeviceSpecs.Mcp) | 0.1.0 | GranTurismo | MCP server for the Device Specs API: look up, search and compare normalized sma… |
| 2026-11-10 07:00:47 | [Zyker.Core.ExceptionHandling](https://www.nuget.org/packages/Zyker.Core.ExceptionHandling) | 1.0.0 | Daniel Nashokin | Exception handling filters and extension methods for dependency injection. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
