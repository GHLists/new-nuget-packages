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

## Latest list — 2026-10-06 21:18 UTC

New packages created between 2026-10-06 20:19 UTC and 2026-10-06 21:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T21-18-56-595636Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 20:22:17 | [Dloizides.Analyzers](https://www.nuget.org/packages/Dloizides.Analyzers) | 0.1.0 | DLoizides | Roslyn analyzers for a no-comments code style: DLZ0001 bans line/block comments… |
| 2026-10-06 20:34:56 | [TheoryNexus.Helm](https://www.nuget.org/packages/TheoryNexus.Helm) | 0.1.0 | Theory Nexus | Report a product's usage, payments, subscriptions and costs to Helm in one stan… |
| 2026-10-06 20:53:29 | [Soenneker.Librarian.IndexedDb](https://www.nuget.org/packages/Soenneker.Librarian.IndexedDb) | 4.0.68 | Jake Soenneker | Librarian document storage for IndexedDb. |
| 2026-10-06 20:55:41 | [Soenneker.Librarian.LocalStorage](https://www.nuget.org/packages/Soenneker.Librarian.LocalStorage) | 4.0.68 | Jake Soenneker | Librarian document storage for LocalStorage. |
| 2026-10-06 20:56:33 | [Soenneker.Librarian.SessionStorage](https://www.nuget.org/packages/Soenneker.Librarian.SessionStorage) | 4.0.69 | Jake Soenneker | Librarian document storage for SessionStorage. |
| 2026-10-06 20:56:41 | [Microsoft.AI.IsolationSession.SDK](https://www.nuget.org/packages/Microsoft.AI.IsolationSession.SDK) | 0.202610.5 | Microsoft | Pipeline-generated SDK for Windows.AI.IsolationSession. Contains both WinMD met… |
| 2026-10-06 20:57:25 | [Soenneker.Librarian.Browser](https://www.nuget.org/packages/Soenneker.Librarian.Browser) | 4.0.69 | Jake Soenneker | Librarian document storage for Browser. |
| 2026-10-06 20:57:50 | [Troolio.Agents](https://www.nuget.org/packages/Troolio.Agents) | 10.0.6 | Fifty3North (F3N Limited) | Agent and run event-sourced actor contracts and orchestration primitives for Tr… |
| 2026-10-06 20:57:52 | [Troolio.SqlServer](https://www.nuget.org/packages/Troolio.SqlServer) | 10.0.6 | Fifty3North (F3N Limited) | SQL Server integration components for Troolio event-sourced actor applications. |
| 2026-10-06 20:57:53 | [Troolio.KurrentDB](https://www.nuget.org/packages/Troolio.KurrentDB) | 10.0.6 | Fifty3North (F3N Limited) | KurrentDB integration components for Troolio event-sourced actor applications. |
| 2026-10-06 20:57:55 | [Troolio.KurrentDB.SqlServer](https://www.nuget.org/packages/Troolio.KurrentDB.SqlServer) | 10.0.6 | Fifty3North (F3N Limited) | SQL Server support components for Troolio KurrentDB integrations. |
| 2026-10-06 21:01:45 | [Soenneker.Librarian.Maui.Secure](https://www.nuget.org/packages/Soenneker.Librarian.Maui.Secure) | 4.0.69 | Jake Soenneker | Librarian document storage for Maui.Secure. |
| 2026-10-06 21:07:00 | [Grist4NET.Kiota](https://www.nuget.org/packages/Grist4NET.Kiota) | 1.0.1 | djsime1 | Kiota-generated API client from Grist's OpenAPI spec. |
| 2026-10-06 21:07:33 | [Grist4NET](https://www.nuget.org/packages/Grist4NET) | 0.1.0 | djsime1 | Interface with Grist documents. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
