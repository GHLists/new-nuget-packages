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

## Latest list — 2026-10-05 05:21 UTC

New packages created between 2026-10-05 04:20 UTC and 2026-10-05 05:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T05-21-32-94688Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 04:26:38 | [SchemaIR](https://www.nuget.org/packages/SchemaIR) | 0.1.0 | SchemaIR contributors | .NET implementation of the language-independent SchemaIR protocol. |
| 2026-10-05 04:27:49 | [NinePSharp.Core.FSharp](https://www.nuget.org/packages/NinePSharp.Core.FSharp) | 0.2.0 | NinePSharp Contributors | NinePSharp.Core.FSharp is part of NinePSharp, a modular 9P protocol toolkit and… |
| 2026-10-05 04:27:50 | [NinePSharp.Namespaces](https://www.nuget.org/packages/NinePSharp.Namespaces) | 0.2.0 | NinePSharp Contributors | NinePSharp.Namespaces is part of NinePSharp, a modular 9P protocol toolkit and… |
| 2026-10-05 04:27:52 | [NinePSharp.Namespaces.Authorization](https://www.nuget.org/packages/NinePSharp.Namespaces.Authorization) | 0.2.0 | NinePSharp Contributors | NinePSharp.Namespaces.Authorization is part of NinePSharp, a modular 9P protoco… |
| 2026-10-05 04:27:53 | [NinePSharp.Namespaces.Orleans](https://www.nuget.org/packages/NinePSharp.Namespaces.Orleans) | 0.2.0 | NinePSharp Contributors | NinePSharp.Namespaces.Orleans is part of NinePSharp, a modular 9P protocol tool… |
| 2026-10-05 04:27:54 | [NinePSharp.Namespaces.Orleans.Abstractions](https://www.nuget.org/packages/NinePSharp.Namespaces.Orleans.Abstractions) | 0.2.0 | NinePSharp Contributors | NinePSharp.Namespaces.Orleans.Abstractions is part of NinePSharp, a modular 9P… |
| 2026-10-05 04:27:55 | [NinePSharp.Namespaces.Orleans.Server](https://www.nuget.org/packages/NinePSharp.Namespaces.Orleans.Server) | 0.2.0 | NinePSharp Contributors | NinePSharp.Namespaces.Orleans.Server is part of NinePSharp, a modular 9P protoc… |
| 2026-10-05 04:27:58 | [NinePSharp.Server](https://www.nuget.org/packages/NinePSharp.Server) | 0.2.0 | NinePSharp Contributors | NinePSharp.Server is part of NinePSharp, a modular 9P protocol toolkit and back… |
| 2026-10-05 04:28:00 | [NinePSharp.Server.FSharp](https://www.nuget.org/packages/NinePSharp.Server.FSharp) | 0.2.0 | NinePSharp Contributors | NinePSharp.Server.FSharp is part of NinePSharp, a modular 9P protocol toolkit a… |
| 2026-10-05 04:49:21 | [Spider.Pipelines.Web](https://www.nuget.org/packages/Spider.Pipelines.Web) | 2.2.1 | Elysium Coding | Graphical web renderer for Spider.Pipelines architecture manifests. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
