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

## Latest list — 2026-11-07 01:20 UTC

New packages created between 2026-11-07 00:19 UTC and 2026-11-07 01:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T01-20-12-44826Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 00:46:01 | [ScuroGuardiano.Slugify](https://www.nuget.org/packages/ScuroGuardiano.Slugify) | 1.0.0 | ScuroGuardiano | Package for converting arbitrary text to url friendly slug |
| 2026-11-07 00:48:18 | [Clarity.Audio](https://www.nuget.org/packages/Clarity.Audio) | 0.83.0 | Peter van de Pas | Clarity.Audio for C#: plays the songs (mp3, flac, wav, ogg) of applications gen… |
| 2026-11-07 00:54:36 | [Axiom.LDB.Migration](https://www.nuget.org/packages/Axiom.LDB.Migration) | 0.1.0 | DeadMoon0 | Part of the Axiom family. Schema migrations for LDB tables: add, drop, rename a… |
| 2026-11-07 01:06:45 | [WumxLabs.NoxAeApi](https://www.nuget.org/packages/WumxLabs.NoxAeApi) | 0.7.1 | Wumx Labs,NoxAeApi Contributo… | Official C# / .NET SDK for NoxAeApi Minecraft REST API suite and Velocity Netwo… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
