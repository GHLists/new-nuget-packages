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

## Latest list — 2026-11-15 18:21 UTC

New packages created between 2026-11-15 17:21 UTC and 2026-11-15 18:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T18-21-20-484808Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 17:31:27 | [RunConvert](https://www.nuget.org/packages/RunConvert) | 0.1.0 | RunConvert | Official RunConvert SDK for .NET: convert files between 240+ formats. |
| 2026-11-15 17:32:09 | [IcocubeServer.Sdk.Plugin](https://www.nuget.org/packages/IcocubeServer.Sdk.Plugin) | 0.0.1-alpha | Gilles Prevot | Experimental plugin development SDK for IcocubeServer. |
| 2026-11-15 17:32:55 | [Pmad.LocalApi.Client](https://www.nuget.org/packages/Pmad.LocalApi.Client) | 0.1.0 | Julien Etelain | HTTP client helpers for local .NET API services: DelegatingHandler for automati… |
| 2026-11-15 17:32:56 | [Pmad.LocalApi.Security](https://www.nuget.org/packages/Pmad.LocalApi.Security) | 0.1.0 | Julien Etelain | Shared local API key security primitives for .NET local services and companion… |
| 2026-11-15 17:33:54 | [FabrCore.Sdk](https://www.nuget.org/packages/FabrCore.Sdk) | 2.2.0 | Vulcan365 LLC | SDK for building AI agents with the FabrCore framework |
| 2026-11-15 17:33:54 | [PlainToolkit.ObjectiveC](https://www.nuget.org/packages/PlainToolkit.ObjectiveC) | 0.1.0 | PCL Community | A simple, lightweight Objective-C interoperability library. |
| 2026-11-15 17:55:20 | [PolyphenyDotNetDriver](https://www.nuget.org/packages/PolyphenyDotNetDriver) | 2.0.0 | Polypheny | .NET driver for Polypheny-DB with SQL, MongoQL and Prism entity metadata suppor… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
