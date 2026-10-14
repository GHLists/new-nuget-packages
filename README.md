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

## Latest list — 2026-10-14 17:21 UTC

New packages created between 2026-10-14 16:20 UTC and 2026-10-14 17:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T17-21-55-624114Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 16:28:16 | [SchlumpfSoft.GeometryNET](https://www.nuget.org/packages/SchlumpfSoft.GeometryNET) | 1.2026.1 | Andreas Sauer | NET-Bibliothek für mathematische Berechnungen in der Ebenen- und Raumgeometrie |
| 2026-10-14 16:39:50 | [FryWorld.Sdk](https://www.nuget.org/packages/FryWorld.Sdk) | 0.0.1 | Code Fry Dev | Cross-platform SDK and microkernel for building plugins, workspaces, and tools… |
| 2026-10-14 16:41:25 | [JAPagination](https://www.nuget.org/packages/JAPagination) | 1.0.0 | José Augusto | Simple, immutable pagination results for collections and synchronous LINQ queri… |
| 2026-10-14 16:50:12 | [JAPagination.EntityFrameworkCore](https://www.nuget.org/packages/JAPagination.EntityFrameworkCore) | 1.0.0 | José Augusto | Optional asynchronous Entity Framework Core integration for JAPagination, prese… |
| 2026-10-14 16:50:35 | [SheetStream.NET](https://www.nuget.org/packages/SheetStream.NET) | 0.4.0 | P4 Software | Lightweight, dependency-free, MIT-licensed .xlsx library for .NET: streaming wr… |
| 2026-10-14 17:12:01 | [Allors.Documents.Reflection](https://www.nuget.org/packages/Allors.Documents.Reflection) | 2.1.0 | allors | Bind Allors Documents templates to plain classes and dictionaries through refle… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
