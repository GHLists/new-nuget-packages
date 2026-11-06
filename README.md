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

## Latest list — 2026-11-06 02:21 UTC

New packages created between 2026-11-06 01:19 UTC and 2026-11-06 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T02-21-07-029764Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 01:29:43 | [CoreEx.Azure.Functions](https://www.nuget.org/packages/CoreEx.Azure.Functions) | 4.3.0 | Avanade | CoreEx execution context, HTTP idempotency and Service Bus settlement integrati… |
| 2026-11-06 01:30:06 | [CoreEx.IO](https://www.nuget.org/packages/CoreEx.IO) | 4.3.0 | Avanade | Stream-based file validation and execution with a host-neutral CSV runtime. |
| 2026-11-06 01:30:52 | [Crombolo.SiteMigration](https://www.nuget.org/packages/Crombolo.SiteMigration) | 0.1.0 | Crombolo | Crombolo Site Migration tool for Umbraco: connects an Umbraco site to Crombolo… |
| 2026-11-06 01:42:53 | [NE.Standard.UI.Client](https://www.nuget.org/packages/NE.Standard.UI.Client) | 2.4.0 | Aki Evans | The C# client engine of the NE.Standard UI framework: holds a page's state, app… |
| 2026-11-06 01:42:55 | [NE.Standard.UI.Server](https://www.nuget.org/packages/NE.Standard.UI.Server) | 2.4.0 | Aki Evans | The headless ASP.NET Core server host of the NE.Standard UI framework: serves c… |
| 2026-11-06 01:44:20 | [DBestChatBot.Umbraco](https://www.nuget.org/packages/DBestChatBot.Umbraco) | 1.0.0 | DBestChatBot | Add the DBestChatBot AI assistant to your Umbraco site. It answers visitors 24/… |
| 2026-11-06 01:50:12 | [Umbraco.Community.PackageCheck](https://www.nuget.org/packages/Umbraco.Community.PackageCheck) | 0.1.0 | Pascal Meyer | A dotnet tool that reports which NuGet packages on an Umbraco site are ready fo… |
| 2026-11-06 02:01:28 | [Binod.DataMigrator](https://www.nuget.org/packages/Binod.DataMigrator) | 1.0.0 | Binod | Onprem Server → ETL → CSV → Cloud Server with validation and progress bar. |
| 2026-11-06 02:06:30 | [AndanteTribe.UnityNamespaceSuppressor](https://www.nuget.org/packages/AndanteTribe.UnityNamespaceSuppressor) | 1.0.0 | AndanteTribe | Suppresses IDE0161 for Unity types that require block-scoped namespaces. |
| 2026-11-06 02:09:27 | [Kahuna.Storage.Gcs](https://www.nuget.org/packages/Kahuna.Storage.Gcs) | 1.15.0 | Andres Gutierrez | Google Cloud Storage backup target for Kahuna: stores point-in-time-recovery ma… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
