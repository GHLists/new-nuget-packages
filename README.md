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

## Latest list — 2026-10-24 00:21 UTC

New packages created between 2026-10-23 23:19 UTC and 2026-10-24 00:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T00-21-01-26287Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 23:43:49 | [DesktopHost.Diagnostics](https://www.nuget.org/packages/DesktopHost.Diagnostics) | 0.4.0 | iyulab | What a long-running local .NET host can say about its own health: a monitor, on… |
| 2026-10-23 23:43:50 | [DesktopHost.Signatures](https://www.nuget.org/packages/DesktopHost.Signatures) | 0.4.0 | iyulab | Whether a file a local .NET host is about to run comes from the publisher it ex… |
| 2026-10-24 00:14:13 | [MyWebTree.Core](https://www.nuget.org/packages/MyWebTree.Core) | 1.0.0 | Matt Gordon | Family tree models, layout and the rules for adding and removing relatives. |
| 2026-10-24 00:14:23 | [MyWebTree.Components](https://www.nuget.org/packages/MyWebTree.Components) | 1.0.0 | Matt Gordon | Blazor family tree. Drop it into a Blazor app and hand it a list of people. |
| 2026-10-24 00:14:27 | [MyWebTree.Data](https://www.nuget.org/packages/MyWebTree.Data) | 1.0.0 | Matt Gordon | Provider-agnostic data model for MyWebTree. Tables live in the webtree schema. |
| 2026-10-24 00:14:33 | [MyWebTree.Data.MySql](https://www.nuget.org/packages/MyWebTree.Data.MySql) | 1.0.0 | Matt Gordon | MySQL storage for MyWebTree. |
| 2026-10-24 00:14:38 | [MyWebTree.Data.Npgsql](https://www.nuget.org/packages/MyWebTree.Data.Npgsql) | 1.0.0 | Matt Gordon | PostgreSQL storage for MyWebTree. |
| 2026-10-24 00:14:43 | [MyWebTree.Data.Sql](https://www.nuget.org/packages/MyWebTree.Data.Sql) | 1.0.0 | Matt Gordon | SQL Server storage for MyWebTree. |
| 2026-10-24 00:14:48 | [MyWebTree.Data.Sqlite](https://www.nuget.org/packages/MyWebTree.Data.Sqlite) | 1.0.0 | Matt Gordon | SQLite storage for MyWebTree. |
| 2026-10-24 00:14:52 | [MyWebTree.Services](https://www.nuget.org/packages/MyWebTree.Services) | 1.0.0 | Matt Gordon | Services behind MyWebTree: trees, people and the relationships between them. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
