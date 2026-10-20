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

## Latest list — 2026-10-20 05:19 UTC

New packages created between 2026-10-20 04:21 UTC and 2026-10-20 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T05-19-27-947222Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 04:42:06 | [NexusSdk.Contracts](https://www.nuget.org/packages/NexusSdk.Contracts) | 1.0.0 | NexusCLI | Contratos compartidos de la API pública Nexus v1. |
| 2026-10-20 04:42:08 | [NexusSdk.DotNet](https://www.nuget.org/packages/NexusSdk.DotNet) | 1.0.0 | NexusCLI | Cliente tipado de la API propia Nexus v1, con streaming y operaciones cancelabl… |
| 2026-10-20 04:42:51 | [NUnit.Extension.Net10PluggableAgent](https://www.nuget.org/packages/NUnit.Extension.Net10PluggableAgent) | 4.0.0 | Charlie Poole, Rob Prouse | This extension allow the NUnit engine to run tests under .NET 10.0. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
