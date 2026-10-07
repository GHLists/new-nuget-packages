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

## Latest list — 2026-10-07 12:20 UTC

New packages created between 2026-10-07 11:20 UTC and 2026-10-07 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T12-20-51-160502Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 11:21:16 | [PaySuite.Sdk](https://www.nuget.org/packages/PaySuite.Sdk) | 0.1.1 | Lazaro Magaia | SDK .NET não oficial (comunitário) para a API PaySuite: pagamentos (M-Pesa, e-M… |
| 2026-10-07 11:29:17 | [Mizzle.Generators](https://www.nuget.org/packages/Mizzle.Generators) | 0.1.0 | Jeff Sheldon | Roslyn generators and analyzers for Mizzle schema records, ordinal mappers, Hyb… |
| 2026-10-07 11:29:17 | [Mizzle.Postgres](https://www.nuget.org/packages/Mizzle.Postgres) | 0.1.0 | Jeff Sheldon | PostgreSQL dialect, emitter, and Npgsql execute path for Mizzle. |
| 2026-10-07 11:29:18 | [Mizzle.SqlServer](https://www.nuget.org/packages/Mizzle.SqlServer) | 0.1.0 | Jeff Sheldon | SQL Server dialect, emitter, and SqlClient execute path for Mizzle. |
| 2026-10-07 11:29:18 | [Mizzle](https://www.nuget.org/packages/Mizzle) | 0.1.0 | Jeff Sheldon | Fluent SQL compiler core for Mizzle: immutable IR, builders, and dialect capabi… |
| 2026-10-07 11:29:19 | [Mizzle.Cli](https://www.nuget.org/packages/Mizzle.Cli) | 0.1.0 | Jeff Sheldon | Command line tools for inspecting databases and generating Mizzle table classes. |
| 2026-10-07 11:46:20 | [Xylocopadream.UI.Avalonia](https://www.nuget.org/packages/Xylocopadream.UI.Avalonia) | 0.1.5 | Xylocopadream | Avalonia theme and controls inspired by JetBrains Rider: dark palette, 16 px li… |
| 2026-10-07 12:02:42 | [mu88.Shared.Testing](https://www.nuget.org/packages/mu88.Shared.Testing) | 8.5.0 | mu88 | This is a little helper NuGet package providing reusable test infrastructure sh… |
| 2026-10-07 12:12:19 | [Durable.CosmosDb](https://www.nuget.org/packages/Durable.CosmosDb) | 0.7.0 | jchristn,joshclopton | Azure Cosmos DB for NoSQL backend for Durable ORM: store entities as JSON docum… |
| 2026-10-07 12:12:20 | [Durable.DuckDb](https://www.nuget.org/packages/Durable.DuckDb) | 0.7.0 | jchristn,joshclopton | DuckDB provider for the Durable ORM (DuckDB.NET): dialect, embedded in-process… |
| 2026-10-07 12:12:25 | [Durable.MongoDb](https://www.nuget.org/packages/Durable.MongoDb) | 0.7.0 | jchristn,joshclopton | MongoDB backend for Durable ORM: store entities in MongoDB collections with the… |
| 2026-10-07 12:12:27 | [Durable.Oracle](https://www.nuget.org/packages/Durable.Oracle) | 0.7.0 | jchristn,joshclopton | Oracle Database provider for the Durable ORM (Oracle.ManagedDataAccess.Core): d… |
| 2026-10-07 12:12:39 | [EpubManager.Writers.Literotica](https://www.nuget.org/packages/EpubManager.Writers.Literotica) | 1.0.0 | IrisDev | Literotica writer plugin for EpubManager. Auto-discovered; no setup needed. |
| 2026-10-07 12:13:16 | [EpubManager](https://www.nuget.org/packages/EpubManager) | 1.0.0 | IrisDev | Build EPUBs from online stories. Install an EpubManager.Writers.* package for e… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
