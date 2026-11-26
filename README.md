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

## Latest list — 2026-11-26 07:21 UTC

New packages created between 2026-11-26 06:19 UTC and 2026-11-26 07:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T07-21-07-215259Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 06:47:57 | [SDS.Outbox.NHibernate.Redis](https://www.nuget.org/packages/SDS.Outbox.NHibernate.Redis) | 1.3.0 | Hieu Doan | Redis distributed notification and partition lease for the NHibernate transacti… |
| 2026-11-26 07:05:16 | [JJ.Framework.Xml.Legacy](https://www.nuget.org/packages/JJ.Framework.Xml.Legacy) | 0.262.7664 | JJ van Zon | XmlToObjectConverter converts an XmlDocument or string to an object graph. The… |
| 2026-11-26 07:09:11 | [Magic.IndexedDb.Cli](https://www.nuget.org/packages/Magic.IndexedDb.Cli) | 3.0.0 | Magic Man | Code-first, language-independent migration planning, validation, and static pub… |
| 2026-11-26 07:13:54 | [Fork.EFCore.BulkExtensions.MIT.SqlServer](https://www.nuget.org/packages/Fork.EFCore.BulkExtensions.MIT.SqlServer) | 11.22.0 | borisdj, Jindrich Cincibuch,… | EF Core 11 build of EFCore.BulkExtensions.MIT.SqlServer (bulk Insert, Update, D… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
