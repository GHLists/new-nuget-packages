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

## Latest list — 2026-09-28 16:19 UTC

New packages created between 2026-09-28 15:20 UTC and 2026-09-28 16:19 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T16-19-54-370478Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 15:33:51 | [GameNetworkingSockets.Net.Certificates](https://www.nuget.org/packages/GameNetworkingSockets.Net.Certificates) | 0.3.0 | GameNetworkingSockets.Net con… | Mints and reads GameNetworkingSockets certificates in managed code: a root auth… |
| 2026-09-28 15:38:31 | [UnambitiousFx.Synapse.Outbox.AdoNet](https://www.nuget.org/packages/UnambitiousFx.Synapse.Outbox.AdoNet) | 2.1.0 | UnambitiousFx | A lightweight, performance-oriented library for building message-driven applica… |
| 2026-09-28 15:38:31 | [UnambitiousFx.Synapse.Outbox.EntityFrameworkCore](https://www.nuget.org/packages/UnambitiousFx.Synapse.Outbox.EntityFrameworkCore) | 2.1.0 | UnambitiousFx | A lightweight, performance-oriented library for building message-driven applica… |
| 2026-09-28 16:01:35 | [MDD4All.DME.ViewModels](https://www.nuget.org/packages/MDD4All.DME.ViewModels) | 2.0.0.1 | Dr. Oliver Alt, mDuckLab | The view models of MDD4All.DME, the object graph editor: the tree built from wh… |
| 2026-09-28 16:10:42 | [JCoder.CoreKits.MySql](https://www.nuget.org/packages/JCoder.CoreKits.MySql) | 3.2623.1 | Jackie Law | 一款使用MySql进行辅助的工具库。 |
| 2026-09-28 16:10:43 | [JCoder.CoreKits.NoteTxt](https://www.nuget.org/packages/JCoder.CoreKits.NoteTxt) | 3.2623.1 | Jackie Law | 一款使用本地Txt文件进行辅助的工具库。 |
| 2026-09-28 16:10:46 | [JCoder.CoreKits.SqlServer](https://www.nuget.org/packages/JCoder.CoreKits.SqlServer) | 3.2623.1 | Jackie Law | 一款使用SqlServer进行辅助的工具库。 |
| 2026-09-28 16:11:13 | [Diavasi.Client](https://www.nuget.org/packages/Diavasi.Client) | 0.1.0 | diavasis | Thin client for the Diavasi data plane |
| 2026-09-28 16:11:25 | [PixelmapLibraryNetFramework](https://www.nuget.org/packages/PixelmapLibraryNetFramework) | 1.0.0 | Anders Hesselbom | A .NET Framework version of PixelmapLibrary. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
