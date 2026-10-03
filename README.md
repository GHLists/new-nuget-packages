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

## Latest list — 2026-10-03 02:20 UTC

New packages created between 2026-10-03 01:19 UTC and 2026-10-03 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T02-20-31-653596Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 01:36:49 | [Shiny.Controls.Keyboard.Shared](https://www.nuget.org/packages/Shiny.Controls.Keyboard.Shared) | 1.6.0-beta-0006 | Allan Ritchie | Host-neutral keyboard shortcut engine — gesture parsing and platform display (C… |
| 2026-10-03 01:49:44 | [EasyAdminBlazor.Upgrade](https://www.nuget.org/packages/EasyAdminBlazor.Upgrade) | 2.4.0-preview | gudufy | EasyAdminBlazor 应用在线升级扩展：逐版本增量升级、发布即出包。 不引用本扩展就没有升级功能（footer 不出现「检查更新」、不注册 /hea… |
| 2026-10-03 02:01:33 | [Novolis.Storage.AzureTables](https://www.nuget.org/packages/Novolis.Storage.AzureTables) | 2026.1.1.42 | Novolis | Azure Table Storage IRepository provider. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
