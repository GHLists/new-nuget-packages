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

## Latest list — 2026-11-25 03:21 UTC

New packages created between 2026-11-25 02:21 UTC and 2026-11-25 03:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T03-21-12-013966Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 02:35:17 | [NXDO.OPC](https://www.nuget.org/packages/NXDO.OPC) | 1.0.0 | ITKing(ZhuQi) | NCore OPC (Server&Client) With WebApi(mini) support |
| 2026-11-25 02:35:53 | [NXDO.OPC.Admin](https://www.nuget.org/packages/NXDO.OPC.Admin) | 0.9.0 | ITKing(ZhuQi) | NCore OPC.Admin With OPC&WebApi(mini) support |
| 2026-11-25 02:36:13 | [MMacareno.Lib.CQRS](https://www.nuget.org/packages/MMacareno.Lib.CQRS) | 1.0.0 | Marco A Macareno F | Package Description |
| 2026-11-25 02:39:38 | [STS2.RitsuLib.Compat.0.113.0](https://www.nuget.org/packages/STS2.RitsuLib.Compat.0.113.0) | 0.6.16 | OLC | Shared framework library for Slay the Spire 2 mods. |
| 2026-11-25 02:48:02 | [Compze.Teventive.MemoryImageStateStore.MicrosoftSql](https://www.nuget.org/packages/Compze.Teventive.MemoryImageStateStore.MicrosoftSql) | 0.1.0-alpha | Lidbom Solutions AB | The SQL Server tables of Compze's memory image state store: MsSqlMemoryImageSta… |
| 2026-11-25 02:48:06 | [Compze.Teventive.MemoryImageStateStore.MySql](https://www.nuget.org/packages/Compze.Teventive.MemoryImageStateStore.MySql) | 0.1.0-alpha | Lidbom Solutions AB | The MySQL tables of Compze's memory image state store: MySqlMemoryImageStateSto… |
| 2026-11-25 02:48:09 | [Compze.Teventive.MemoryImageStateStore.PostgreSql](https://www.nuget.org/packages/Compze.Teventive.MemoryImageStateStore.PostgreSql) | 0.1.0-alpha | Lidbom Solutions AB | The PostgreSQL tables of Compze's memory image state store: PgSqlMemoryImageSta… |
| 2026-11-25 02:48:12 | [Compze.Teventive.MemoryImageStateStore.Sqlite](https://www.nuget.org/packages/Compze.Teventive.MemoryImageStateStore.Sqlite) | 0.1.0-alpha | Lidbom Solutions AB | The SQLite tables of Compze's memory image state store: SqliteMemoryImageStateS… |
| 2026-11-25 02:59:06 | [Shaunebu.MAUI.FormsManager](https://www.nuget.org/packages/Shaunebu.MAUI.FormsManager) | 1.1.0 | Shaunebu | A powerful, dynamic forms library for .NET MAUI that generates complete user in… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
