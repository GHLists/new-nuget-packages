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

## Latest list — 2026-10-12 22:20 UTC

New packages created between 2026-10-12 21:20 UTC and 2026-10-12 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T22-20-20-965226Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 21:22:44 | [TheBuilder.SchemaCity](https://www.nuget.org/packages/TheBuilder.SchemaCity) | 0.1.2 | Daniel Schmidt | See your Umbraco content model as a 3D city in the backoffice, with the relatio… |
| 2026-10-12 21:58:44 | [G9SyncData.Server.SnapshotFiles](https://www.nuget.org/packages/G9SyncData.Server.SnapshotFiles) | 1.3.0 | Iman Kari | G9SyncData snapshot files for the server (ADR-0072): a subscription's large fir… |
| 2026-10-12 22:02:58 | [Squirrel.Integration.Wolverine](https://www.nuget.org/packages/Squirrel.Integration.Wolverine) | 1.0.0-preview-0007 | Squirrel.Integration.Wolverine | Reusable .NET building blocks for cloud-native applications. |
| 2026-10-12 22:03:00 | [Squirrel.Integration.Wolverine.InMemory](https://www.nuget.org/packages/Squirrel.Integration.Wolverine.InMemory) | 1.0.0-preview-0007 | Squirrel.Integration.Wolverin… | Reusable .NET building blocks for cloud-native applications. |
| 2026-10-12 22:03:02 | [Squirrel.Web](https://www.nuget.org/packages/Squirrel.Web) | 1.0.0-preview-0007 | Squirrel.Web | Reusable .NET building blocks for cloud-native applications. |
| 2026-10-12 22:03:05 | [Squirrel.SerilogLogging](https://www.nuget.org/packages/Squirrel.SerilogLogging) | 1.0.0-preview-0007 | Squirrel.SerilogLogging | Reusable .NET building blocks for cloud-native applications. |
| 2026-10-12 22:03:06 | [Squirrel.Security](https://www.nuget.org/packages/Squirrel.Security) | 1.0.0-preview-0007 | Squirrel.Security | Reusable .NET building blocks for cloud-native applications. |
| 2026-10-12 22:14:58 | [Gripe.QualityAssurancePack.Github](https://www.nuget.org/packages/Gripe.QualityAssurancePack.Github) | 2.1.34 | dpvreony | Collection of packages for assisting in QA during .NET software development on… |
| 2026-10-12 22:15:00 | [Gripe.TestAssurancePack.GithubActions](https://www.nuget.org/packages/Gripe.TestAssurancePack.GithubActions) | 2.1.34 | dpvreony | Collection of packages for assisting in Testing .NET Code on Github Actions. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
