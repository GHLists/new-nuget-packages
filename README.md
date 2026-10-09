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

## Latest list — 2026-10-09 02:19 UTC

New packages created between 2026-10-09 01:19 UTC and 2026-10-09 02:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T02-19-53-561425Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 01:20:57 | [PdfiumWrapper.Processing](https://www.nuget.org/packages/PdfiumWrapper.Processing) | 2.0.1 | Emmanuel Hameyie | Worker pool for PdfiumWrapper: runs PDF conversions in a dynamically sized set… |
| 2026-10-09 01:23:07 | [Iyu.MainServer.GraphQL](https://www.nuget.org/packages/Iyu.MainServer.GraphQL) | 0.37.0 | iyulab | iyu-framework-v5: OData + GraphQL runtime framework for .NET 10. |
| 2026-10-09 01:40:27 | [QuartzPlugin](https://www.nuget.org/packages/QuartzPlugin) | 1.0.0 | Dio Liew | A package to simplify the setting of Quartz v3 into main project of appsettings… |
| 2026-10-09 01:43:55 | [Wslc.Testcontainers.Modules.Kafka](https://www.nuget.org/packages/Wslc.Testcontainers.Modules.Kafka) | 0.5.0 | Nick Nadolski | Kafka module for Wslc.Testcontainers: typed single-node builder and bootstrap s… |
| 2026-10-09 01:52:38 | [SourceGenerators.Toolkit.Prism](https://www.nuget.org/packages/SourceGenerators.Toolkit.Prism) | 1.0.5 | Carlos | SourceGenerators.Toolkit.Prism |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
