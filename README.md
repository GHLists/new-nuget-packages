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

## Latest list — 2026-10-06 05:19 UTC

New packages created between 2026-10-06 04:21 UTC and 2026-10-06 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T05-19-49-63251Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 04:31:06 | [DataAccessProvider.Oracle](https://www.nuget.org/packages/DataAccessProvider.Oracle) | 1.4.0 | Habib Shakibanejad | Package Description |
| 2026-10-06 04:47:07 | [Exsited](https://www.nuget.org/packages/Exsited) | 0.0.1 | WebAlive | .NET SDK for the Exsited REST API. |
| 2026-10-06 04:47:11 | [WebCommander](https://www.nuget.org/packages/WebCommander) | 0.0.1 | WebAlive | .NET SDK for the WebCommander REST API. |
| 2026-10-06 04:47:12 | [EventBookings](https://www.nuget.org/packages/EventBookings) | 0.0.1 | WebAlive | .NET SDK for the EventBookings REST API. |
| 2026-10-06 04:47:12 | [Novolis.Rendering.Appearance](https://www.nuget.org/packages/Novolis.Rendering.Appearance) | 2026.1.1.76 | Novolis | Declarative appearance stacks (surface, volume, light, effect, post) with a CPU… |
| 2026-10-06 04:47:13 | [Umerang](https://www.nuget.org/packages/Umerang) | 0.0.1 | WebAlive | .NET SDK for the Umerang REST API. |
| 2026-10-06 05:09:15 | [DataverseToCode.Cli](https://www.nuget.org/packages/DataverseToCode.Cli) | 0.16.1 | Simon Allport | dvschema: Dataverse schema as YAML in Git (pull, validate, plan, push, drift, d… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
