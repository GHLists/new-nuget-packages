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

## Latest list — 2026-10-05 03:20 UTC

New packages created between 2026-10-05 02:19 UTC and 2026-10-05 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T03-20-34-840411Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 02:49:07 | [SatBridge](https://www.nuget.org/packages/SatBridge) | 0.1.0 | José Chávez | Biblioteca .NET para consumir los servicios de Descarga Masiva de CFDI del SAT… |
| 2026-10-05 03:13:48 | [SereinFlow.AspNetCore](https://www.nuget.org/packages/SereinFlow.AspNetCore) | 0.1.0 | SereinFlow | ASP.NET Core hosting for SereinFlow REST API, SignalR and HTTP MCP. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
