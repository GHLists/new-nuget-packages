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

## Latest list — 2026-10-05 00:21 UTC

New packages created between 2026-10-04 23:21 UTC and 2026-10-05 00:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T00-21-40-139143Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 23:31:29 | [Myscotek.DataCompare](https://www.nuget.org/packages/Myscotek.DataCompare) | 1.2026.10.2 | Myscotek | XrmToolBox tool. Connect to the environment the data came from (primary) and th… |
| 2026-10-04 23:47:39 | [Structly.AI.Testing](https://www.nuget.org/packages/Structly.AI.Testing) | 0.4.0 | menk-dev | Typed, structured LLM output for automated .NET workflows. |
| 2026-10-04 23:56:45 | [Atlas.Sdk](https://www.nuget.org/packages/Atlas.Sdk) | 1.0.0 | Atlas | Official .NET / C# backend SDK for the Atlas authentication platform. A typed,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
