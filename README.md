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

## Latest list — 2026-10-02 20:20 UTC

New packages created between 2026-10-02 19:19 UTC and 2026-10-02 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T20-20-56-510358Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 19:20:24 | [KetPsi.Results](https://www.nuget.org/packages/KetPsi.Results) | 1.0.0 | KetPsi | High-performance Result pattern library for application and infrastructure laye… |
| 2026-10-02 19:25:22 | [Nkraft.Mopups](https://www.nuget.org/packages/Nkraft.Mopups) | 1.0.0 | Mark L, Tyson Hooker, Maksym… | Fork of Mopups (LuckyDucko/Mopups) maintained for Android and iOS only |
| 2026-10-02 19:41:53 | [Trax.Effect.Decisions.SystemOne](https://www.nuget.org/packages/Trax.Effect.Decisions.SystemOne) | 1.58.0 | Theauxm,mark-keaton | Typed decision model adapter for Trax.Effect. Adds AddNimbleDecider(...), for B… |
| 2026-10-02 19:57:49 | [GSharp.CodeAnalysis.Analyzers.Testing](https://www.nuget.org/packages/GSharp.CodeAnalysis.Analyzers.Testing) | 0.4.1150 | David Obando | Testing surface (GSharpAnalyzerVerifier) for GSharp diagnostic analyzers (ADR-0… |
| 2026-10-02 19:58:38 | [SqlClone](https://www.nuget.org/packages/SqlClone) | 0.1.0 | Emmz | Clone a SQL Server database, schema and data, from one server to another under… |
| 2026-10-02 20:00:23 | [Novolis.Agent.Core](https://www.nuget.org/packages/Novolis.Agent.Core) | 2026.1.1.31 | Novolis | Agent Surface contracts: IAgentHost, duplex channel frames, shared DTOs, and ag… |
| 2026-10-02 20:00:24 | [Novolis.Agent.Surface](https://www.nuget.org/packages/Novolis.Agent.Surface) | 2026.1.1.31 | Novolis | Attributed agent surfaces: document generation (OpenAPI / MCP / JSON-RPC), anno… |
| 2026-10-02 20:00:25 | [Novolis.Agent.Testing](https://www.nuget.org/packages/Novolis.Agent.Testing) | 2026.1.1.31 | Novolis | Test doubles for Novolis.Agent: fake host, in-memory channel, document asserts. |
| 2026-10-02 20:07:03 | [QueueBox.Inbox.EntityFrameworkCore](https://www.nuget.org/packages/QueueBox.Inbox.EntityFrameworkCore) | 0.5.0 | AlterNayte | Entity Framework Core helper for QueueBox.Inbox. It builds a context on the tra… |
| 2026-10-02 20:13:47 | [Xfs351](https://www.nuget.org/packages/Xfs351) | 1.0.4 | Xfs351 | CEN/XFS 3.00-3.50 runtime binaries and standalone settings editor for Windows x… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
