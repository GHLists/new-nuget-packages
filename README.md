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

## Latest list — 2026-09-27 19:20 UTC

New packages created between 2026-09-27 18:20 UTC and 2026-09-27 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-27T19-20-34-611464Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-27 18:23:14 | [EraTech.Host.Shared](https://www.nuget.org/packages/EraTech.Host.Shared) | 2.2.22 | EraTech | Package Description |
| 2026-09-27 18:29:21 | [Meziantou.Framework.Toml](https://www.nuget.org/packages/Meziantou.Framework.Toml) | 1.0.0 | meziantou | A high-performance .NET TOML 1.1 parser, round-trippable syntax tree, and Syste… |
| 2026-09-27 18:39:01 | [Brigade.Net.Core](https://www.nuget.org/packages/Brigade.Net.Core) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 18:44:50 | [Brigade.Net.Partie](https://www.nuget.org/packages/Brigade.Net.Partie) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 18:44:55 | [Brigade.Net.Mise](https://www.nuget.org/packages/Brigade.Net.Mise) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 18:44:56 | [Brigade.Net.Expo](https://www.nuget.org/packages/Brigade.Net.Expo) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 18:50:52 | [Brigade.Net.Expo.Engines.Domain](https://www.nuget.org/packages/Brigade.Net.Expo.Engines.Domain) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 18:51:51 | [Brigade.Net.Mise.SqlServer](https://www.nuget.org/packages/Brigade.Net.Mise.SqlServer) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 18:51:57 | [Brigade.Net.Partie.AspNetCore](https://www.nuget.org/packages/Brigade.Net.Partie.AspNetCore) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 18:52:02 | [CodeBrix.Audio.Android.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.Audio.Android.ApacheLicenseForever) | 1.0.270.1130 | Jeremy Ellis | The Android platform package for CodeBrix.Audio: device playback and capture th… |
| 2026-09-27 18:55:35 | [Brigade.Net.Mise.PostgreSQL](https://www.nuget.org/packages/Brigade.Net.Mise.PostgreSQL) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 18:56:31 | [Brigade.Net.Partie.Engines.AspNetCore](https://www.nuget.org/packages/Brigade.Net.Partie.Engines.AspNetCore) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 18:59:20 | [Brigade.Net.Mise.SQLite](https://www.nuget.org/packages/Brigade.Net.Mise.SQLite) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 19:03:24 | [Brigade.Net.Mise.MySQL](https://www.nuget.org/packages/Brigade.Net.Mise.MySQL) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 19:06:28 | [Brigade.Net.Mise.MariaDb](https://www.nuget.org/packages/Brigade.Net.Mise.MariaDb) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 19:10:22 | [Brigade.Net.Mise.Engines.SqlServer](https://www.nuget.org/packages/Brigade.Net.Mise.Engines.SqlServer) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 19:13:56 | [Brigade.Net.Mise.Engines.PostgreSQL](https://www.nuget.org/packages/Brigade.Net.Mise.Engines.PostgreSQL) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
