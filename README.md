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

## Latest list — 2026-10-15 08:19 UTC

New packages created between 2026-10-15 07:21 UTC and 2026-10-15 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T08-19-24-00641Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 07:25:39 | [DotJpegli](https://www.nuget.org/packages/DotJpegli) | 1.0.0 | Edward Miller | Safe, portable managed JPEG encoder based on Google's Jpegli, compatible with t… |
| 2026-10-15 07:32:26 | [Webority.Diagnostics](https://www.nuget.org/packages/Webority.Diagnostics) | 0.2.1 | Webority Technologies | The Diagnostics engine for Webority products: the build-time infra slice, secre… |
| 2026-10-15 07:32:29 | [Webority.Diagnostics.Abstractions](https://www.nuget.org/packages/Webority.Diagnostics.Abstractions) | 0.2.1 | Webority Technologies | The contract a Webority library implements to report into a product's Diagnosti… |
| 2026-10-15 07:32:31 | [Webority.Diagnostics.Admin](https://www.nuget.org/packages/Webority.Diagnostics.Admin) | 0.2.1 | Webority Technologies | The Diagnostics console for Webority admin portals: overview, runtime, edge, mo… |
| 2026-10-15 07:32:55 | [FxLink.EntityFramework](https://www.nuget.org/packages/FxLink.EntityFramework) | 2.0.0 | Quy Vu | EF Core backend for FxLink's reliable-messaging patterns (Outbox, Inbox) and st… |
| 2026-10-15 07:45:40 | [Access.It.Mcp](https://www.nuget.org/packages/Access.It.Mcp) | 10.9.0 | Access-It Tech Lead Task Force | Serveur MCP exposant la documentation des packages Access.It (catalogue, API pu… |
| 2026-10-15 07:45:43 | [Kai.Shared.Logging](https://www.nuget.org/packages/Kai.Shared.Logging) | 0.1.0 | Kai | Host-owned Serilog JSON console logging for shared .NET services. |
| 2026-10-15 07:45:46 | [Kai.Shared.Oracle](https://www.nuget.org/packages/Kai.Shared.Oracle) | 0.1.0 | Kai.Shared.Oracle | Scoped Oracle repositories, audit, transactions and data operations for consume… |
| 2026-10-15 07:45:49 | [Kai.Shared.Postgres](https://www.nuget.org/packages/Kai.Shared.Postgres) | 0.1.0 | Kai.Shared.Postgres | PostgreSQL repositories, audit, transactions, SQL, batch and atomic COPY for co… |
| 2026-10-15 07:53:53 | [qdrant_edge_cs](https://www.nuget.org/packages/qdrant_edge_cs) | 0.10.0 | electroglyph | Idiomatic C# interface for qdrant_edge (embedded single-shard vector search). N… |
| 2026-10-15 08:03:10 | [Cumber](https://www.nuget.org/packages/Cumber) | 0.1.0 | Mark Wrenford | Hierarchical command-line parsing driven by readable help text. |
| 2026-10-15 08:04:46 | [2dog.gdunit](https://www.nuget.org/packages/2dog.gdunit) | 4.7.2.120 | Moritz Voss | Run isolated GDScript gdUnit tests through embedded Godot and Microsoft.Testing… |
| 2026-10-15 08:04:47 | [2dog.gdunit.double](https://www.nuget.org/packages/2dog.gdunit.double) | 4.7.2.120 | Moritz Voss | Run isolated GDScript gdUnit tests through embedded Godot and Microsoft.Testing… |
| 2026-10-15 08:07:08 | [Drawspan.Client.V1](https://www.nuget.org/packages/Drawspan.Client.V1) | 1.0.0 | Coded Constructs | Drawspan licensing client for AEC desktop plugins (Revit, Rhino/Grasshopper). O… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
