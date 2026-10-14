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

## Latest list — 2026-10-14 00:21 UTC

New packages created between 2026-10-13 23:19 UTC and 2026-10-14 00:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T00-21-04-965772Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 23:31:05 | [Penghou.Workflow.Abstractions](https://www.nuget.org/packages/Penghou.Workflow.Abstractions) | 1.0.0 | Penghou contributors | Product-neutral, bounded execution authorization contracts for replaceable work… |
| 2026-10-13 23:33:32 | [FaroHQ.AspNetCore](https://www.nuget.org/packages/FaroHQ.AspNetCore) | 0.2.1 | FaroHQ | Envia os erros de aplicações ASP.NET Core para o FaroHQ (análise de causa raiz… |
| 2026-10-13 23:34:19 | [Penghou.Cangjie.Sqlite](https://www.nuget.org/packages/Penghou.Cangjie.Sqlite) | 1.0.0 | Penghou.Cangjie contributors | Local-first SQLite and FTS5 implementation of Penghou.Cangjie context storage. |
| 2026-10-13 23:34:19 | [Penghou.Cangjie](https://www.nuget.org/packages/Penghou.Cangjie) | 1.0.0 | Penghou.Cangjie contributors | Framework-agnostic context, provenance, relation, and retrieval abstractions fo… |
| 2026-10-13 23:34:19 | [Penghou.Cangjie.Testing](https://www.nuget.org/packages/Penghou.Cangjie.Testing) | 1.0.0 | Penghou.Cangjie contributors | Reusable conformance tests for Penghou.Cangjie context stores. |
| 2026-10-13 23:35:46 | [OpenDebug.Net.linux-x64](https://www.nuget.org/packages/OpenDebug.Net.linux-x64) | 0.0.2 | OpenDebug.Net contributors | A fast Native AOT Debug Adapter Protocol server for live managed .NET processes. |
| 2026-10-13 23:38:17 | [Penghou.IO.Identity.Abstractions](https://www.nuget.org/packages/Penghou.IO.Identity.Abstractions) | 1.0.0 | Penghou.IO contributors | Data-only request and identity contracts for Penghou I/O protocol schema v1. No… |
| 2026-10-13 23:38:18 | [Penghou.IO.Protocols](https://www.nuget.org/packages/Penghou.IO.Protocols) | 1.0.0 | Penghou.IO contributors | Versioned resource identity and path protocol implementations shared by Penghou… |
| 2026-10-13 23:39:06 | [Penghou.Siming](https://www.nuget.org/packages/Penghou.Siming) | 1.0.0 | Penghou.Siming contributors | Provider-neutral tamper-evident append-only event ledger contracts, canonical p… |
| 2026-10-13 23:39:06 | [Penghou.Siming.Cryptography](https://www.nuget.org/packages/Penghou.Siming.Cryptography) | 1.0.0 | Penghou.Siming contributors | Optional detached Ed25519 checkpoint signing and public-key verification for Pe… |
| 2026-10-13 23:39:07 | [Penghou.Siming.Sqlite](https://www.nuget.org/packages/Penghou.Siming.Sqlite) | 1.0.0 | Penghou.Siming contributors | Transactional SQLite persistence for the Penghou.Siming tamper-evident append-o… |
| 2026-10-13 23:39:08 | [Penghou.Siming.Testing](https://www.nuget.org/packages/Penghou.Siming.Testing) | 1.0.0 | Penghou.Siming contributors | Reusable provider conformance checks for Penghou.Siming ledger implementations. |
| 2026-10-13 23:39:10 | [Penghou.Siming.Verify](https://www.nuget.org/packages/Penghou.Siming.Verify) | 1.0.0 | Penghou.Siming contributors | Command-line verification for Penghou.Siming SQLite ledgers and signed or unsig… |
| 2026-10-14 00:03:32 | [SharpNinja.McpServer.Director](https://www.nuget.org/packages/SharpNinja.McpServer.Director) | 0.6.26 | SharpNinja | CLI management tool for McpServer. Provides workspace management, agent orchest… |
| 2026-10-14 00:10:38 | [SharpNinja.McpServer.Web](https://www.nuget.org/packages/SharpNinja.McpServer.Web) | 0.6.26 | SharpNinja | SharpNinja.McpServer.Web |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
