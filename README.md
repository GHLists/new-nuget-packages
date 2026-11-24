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

## Latest list — 2026-11-24 08:19 UTC

New packages created between 2026-11-24 07:22 UTC and 2026-11-24 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T08-19-38-223317Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 07:22:08 | [BulletSharp.PureCSharp.SoftBody.Double](https://www.nuget.org/packages/BulletSharp.PureCSharp.SoftBody.Double) | 0.1.0 | bullet-sharp contributors | Classic btSoftBody module (ropes, cloth, pressure/tetrahedral soft bodies, Spar… |
| 2026-11-24 07:22:09 | [BulletSharp.PureCSharp.SoftBody](https://www.nuget.org/packages/BulletSharp.PureCSharp.SoftBody) | 0.1.0 | bullet-sharp contributors | Classic btSoftBody module (ropes, cloth, pressure/tetrahedral soft bodies, Spar… |
| 2026-11-24 07:22:10 | [BulletSharp.PureCSharp](https://www.nuget.org/packages/BulletSharp.PureCSharp) | 0.1.0 | bullet-sharp contributors | Pure C# port of the Bullet Physics engine, single-precision (float) build (rigi… |
| 2026-11-24 07:22:10 | [BulletSharp.PureCSharp.Double](https://www.nuget.org/packages/BulletSharp.PureCSharp.Double) | 0.1.0 | bullet-sharp contributors | Pure C# port of the Bullet Physics engine, double-precision (double) build (rig… |
| 2026-11-24 07:30:44 | [Gatehouse.Accounts](https://www.nuget.org/packages/Gatehouse.Accounts) | 0.1.0 | KalliMan | Sign-in with Google, Microsoft, Facebook and GitHub for ASP.NET Core Identity (… |
| 2026-11-24 07:35:59 | [Rustorb.Dds](https://www.nuget.org/packages/Rustorb.Dds) | 0.3.0 | rustorb contributors | DDS for .NET on rustorb-dds: a subset of the DDS API after the Java 5 PSM, over… |
| 2026-11-24 07:37:55 | [HanaTech.RTDB.Framework.Api](https://www.nuget.org/packages/HanaTech.RTDB.Framework.Api) | 4.2.1-preview202609… | HanaTech | Package Description |
| 2026-11-24 07:39:03 | [Sencilla.Authentication.Instagram](https://www.nuget.org/packages/Sencilla.Authentication.Instagram) | 11.0.2 | Sencilla | Package Description |
| 2026-11-24 07:39:11 | [Sencilla.Authentication.Telegram](https://www.nuget.org/packages/Sencilla.Authentication.Telegram) | 11.0.2 | Sencilla | Package Description |
| 2026-11-24 07:49:29 | [Niubility.Scaffold.Cli](https://www.nuget.org/packages/Niubility.Scaffold.Cli) | 1.3.0 | Niubility.Scaffold.Cli | Inspect database schemas, review generated C# changes and apply a saved Niubili… |
| 2026-11-24 07:50:14 | [Niubility.Scaffold.Database.PostgreSql](https://www.nuget.org/packages/Niubility.Scaffold.Database.PostgreSql) | 1.3.0 | Niubility.Scaffold.Database.P… | PostgreSQL catalog reader and C# generator for Niubility.Database 1.1.0. |
| 2026-11-24 07:51:00 | [Warungkopipurnama](https://www.nuget.org/packages/Warungkopipurnama) | 1.0.0 | Warung Kopi Purnama — kopi le… | Warung Kopi Purnama cafe Braga, Bandung constants. Official: https://warungkopi… |
| 2026-11-24 08:01:59 | [StarFruit.Nova](https://www.nuget.org/packages/StarFruit.Nova) | 1.0.0 | EpsiRho | Audio feature extraction for C# |
| 2026-11-24 08:12:26 | [Tellurian.Trains.Drawing.Editing](https://www.nuget.org/packages/Tellurian.Trains.Drawing.Editing) | 0.10.0 | Stefan Fjällemark | UI-independent editing for Tellurian Trains drawings: commands, undo/redo, snap… |
| 2026-11-24 08:12:26 | [Tellurian.Trains.Drawing.Model](https://www.nuget.org/packages/Tellurian.Trains.Drawing.Model) | 0.10.0 | Stefan Fjällemark | Domain model for Tellurian Trains drawings: end profiles, modules, halls, hall… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
