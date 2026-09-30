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

## Latest list — 2026-09-30 00:19 UTC

New packages created between 2026-09-29 23:21 UTC and 2026-09-30 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T00-19-06-765381Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 23:24:14 | [NHSOneLondon.AuditAndMetrics.Clients](https://www.nuget.org/packages/NHSOneLondon.AuditAndMetrics.Clients) | 0.1.0 | Intelligence Solutions for Lo… | NHSOneLondon.AuditAndMetrics.Clients provides a Standard compliant client for r… |
| 2026-09-29 23:24:15 | [NHSOneLondon.AuditAndMetrics.Abstractions](https://www.nuget.org/packages/NHSOneLondon.AuditAndMetrics.Abstractions) | 0.1.0 | Intelligence Solutions for Lo… | NHSOneLondon.AuditAndMetrics.Abstractions provides the contracts a host impleme… |
| 2026-09-29 23:32:05 | [Openquote](https://www.nuget.org/packages/Openquote) | 0.2.1 | iyulab | A domain-neutral engine for ongoing records kept as immutable change files: mer… |
| 2026-09-29 23:50:35 | [Plank.Native.Zlib](https://www.nuget.org/packages/Plank.Native.Zlib) | 1.3.1.1 | Kuinox | Native zlib runtime assets for Plank. |
| 2026-09-29 23:50:36 | [Plank.SourceGen](https://www.nuget.org/packages/Plank.SourceGen) | 0.1.0 | Kuinox | Roslyn source generators for high-performance, strongly typed Plank row readers… |
| 2026-09-29 23:50:37 | [Plank](https://www.nuget.org/packages/Plank) | 0.1.0 | Kuinox | A high-performance Apache Parquet reader and writer for .NET. |
| 2026-09-29 23:52:46 | [Shiny.AppFunctions](https://www.nuget.org/packages/Shiny.AppFunctions) | 5.8.0-beta-0009 | Allan Ritchie | Shiny App Functions - declare app functions once in C# and expose them to Siri,… |
| 2026-09-29 23:54:45 | [Further.DbRivet.Contracts](https://www.nuget.org/packages/Further.DbRivet.Contracts) | 1.0.0 | yinchang0626 | Transaction-scoped database locking for ABP applications, independent of ORM an… |
| 2026-09-29 23:54:46 | [Further.DbRivet](https://www.nuget.org/packages/Further.DbRivet) | 1.0.0 | yinchang0626 | Transaction-scoped database locking for ABP applications, independent of ORM an… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
