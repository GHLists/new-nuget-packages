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

## Latest list — 2026-10-08 01:21 UTC

New packages created between 2026-10-08 00:18 UTC and 2026-10-08 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T01-21-45-380078Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 00:39:33 | [SejilSQL](https://www.nuget.org/packages/SejilSQL) | 3.1.4 | Alaa Masoud, Dany Côté | Collect the logs of your ASP.NET Core applications in SQL Server (Serilog) and… |
| 2026-10-08 00:57:51 | [CodeBrix.TomlParse.BsdLicenseForever](https://www.nuget.org/packages/CodeBrix.TomlParse.BsdLicenseForever) | 1.0.281.57 | Jeremy Ellis | A fully managed, high-performance TOML 1.1 library for .NET: read, parse, updat… |
| 2026-10-08 01:13:26 | [CodeBrix.Platform.GameEngine.CardsAndDice.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.Platform.GameEngine.CardsAndDice.MitLicenseForever) | 1.0.281.72 | Jeremy Ellis | Cards, decks, dice, animated tabletop interactions, and embedded SVG artwork fo… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
