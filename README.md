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

## Latest list — 2026-11-13 07:19 UTC

New packages created between 2026-11-13 06:20 UTC and 2026-11-13 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T07-19-40-916098Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 06:23:22 | [LogConverge.Sharp](https://www.nuget.org/packages/LogConverge.Sharp) | 0.7.0 | LogConverge | 基于原生 spdlog 内核的静态日志 SDK；当前支持 Windows x64。 |
| 2026-11-13 06:42:46 | [Fungusware.Mft](https://www.nuget.org/packages/Fungusware.Mft) | 2026.11.13.642 | Fungusware | Reads an NTFS volume's Master File Table directly: every file name and size on… |
| 2026-11-13 06:52:16 | [DBHelper.NetFx](https://www.nuget.org/packages/DBHelper.NetFx) | 2.0.0 | jimmy.pan | .NET Framework 4.8 版数据库访问层：SQL 外置到 XML 配置文件，通过 KEY + 参数字典执行，支持 MySQL/MariaDB/SQ… |
| 2026-11-13 07:08:11 | [GlrParser](https://www.nuget.org/packages/GlrParser) | 2.0.0-develop | Jan B. Freuer | A Generalized LR (GLR) parser framework. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
