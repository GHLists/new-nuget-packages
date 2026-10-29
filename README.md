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

## Latest list — 2026-10-29 21:19 UTC

New packages created between 2026-10-29 20:19 UTC and 2026-10-29 21:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T21-19-56-197023Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 20:37:21 | [miPDFlib](https://www.nuget.org/packages/miPDFlib) | 0.2.5-alpha | Wolfgang Mitterbucher | Open-source (Apache-2.0) PDF library for .NET: create, read, modify, merge, fil… |
| 2026-10-29 20:44:36 | [NetworkInspector.BuiltInPlugins](https://www.nuget.org/packages/NetworkInspector.BuiltInPlugins) | 0.19.0 | DevAM | Built-in core-tier plugins: standard protocols, file and random sources, and th… |
| 2026-10-29 20:45:14 | [NetworkInspector.Plugins](https://www.nuget.org/packages/NetworkInspector.Plugins) | 0.19.0 | DevAM | Core-tier plugin contract: entry point, builder, context, source and exporter r… |
| 2026-10-29 20:45:21 | [NetworkInspector.Plugins.Loader](https://www.nuget.org/packages/NetworkInspector.Plugins.Loader) | 0.19.0 | DevAM | Plugin pre-scan, scan cache, load contexts, registry, and lifecycle for Network… |
| 2026-10-29 20:48:13 | [ImzaKit](https://www.nuget.org/packages/ImzaKit) | 1.0.0 | ImzaKit contributors | Provider-independent electronic signature toolkit for .NET: PAdES, CAdES, XAdES… |
| 2026-10-29 20:49:38 | [Cratis.Observability.SourceGenerators](https://www.nuget.org/packages/Cratis.Observability.SourceGenerators) | 7.28.0 | Cratis | Roslyn source generators and analyzers for strongly typed metrics and trace spa… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
