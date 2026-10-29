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

## Latest list — 2026-10-29 12:20 UTC

New packages created between 2026-10-29 11:21 UTC and 2026-10-29 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T12-20-12-454894Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 11:32:29 | [C1.Win.Command.HamburgerMenu](https://www.nuget.org/packages/C1.Win.Command.HamburgerMenu) | 10.0.20262.832 | MESCIUS inc. | The ComponentOne HamburgerMenu for WinForms is a highly customizable navigation… |
| 2026-10-29 11:33:58 | [TheDotSide.Aspire.Templates](https://www.nuget.org/packages/TheDotSide.Aspire.Templates) | 0.2.0 | The Dot Side | Templates Aspire configurables alignés sur le référentiel ADR The Dot Side. |
| 2026-10-29 11:48:16 | [InventiveRhythm.Framework](https://www.nuget.org/packages/InventiveRhythm.Framework) | 2026.1029.0 | ppy Pty Ltd | A fork of osu!framework, with fluXis-specific tweaks. |
| 2026-10-29 12:11:44 | [Keryhe.Telemetry.Sqlite](https://www.nuget.org/packages/Keryhe.Telemetry.Sqlite) | 2.0.2 | Keith Heard | SQLite control-plane implementation for telemetry (tenants, API keys, alert rul… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
