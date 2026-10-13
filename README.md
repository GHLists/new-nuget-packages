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

## Latest list — 2026-10-13 15:22 UTC

New packages created between 2026-10-13 14:21 UTC and 2026-10-13 15:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T15-22-01-173083Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 14:27:43 | [Ternary.Data.Conversion](https://www.nuget.org/packages/Ternary.Data.Conversion) | 10.0.1 | Jacob Dahlke | A framework to simplify working with data from multiple sources, including file… |
| 2026-10-13 14:28:10 | [Maranics.AppStore.SDK.AspNetCore](https://www.nuget.org/packages/Maranics.AppStore.SDK.AspNetCore) | 1.0.0 | Maranics.AppStore.SDK.AspNetC… | Maranics App Store SDK for ASP.NET Core: require AppStore's signed token on an… |
| 2026-10-13 14:42:50 | [Hasbati.Percentage.Calculator](https://www.nuget.org/packages/Hasbati.Percentage.Calculator) | 1.0.1 | Hasbati | A lightweight utility for percentage calculations. For the fully interactive gr… |
| 2026-10-13 14:54:38 | [Linq2Dashboard.AI](https://www.nuget.org/packages/Linq2Dashboard.AI) | 0.2.111-beta | Joakim Dangården | Agent tools for Linq2Dashboard: one dashboard as describe, query and show funct… |
| 2026-10-13 15:00:10 | [ToddHenderson.Maui.MacIdiom.Compatibility](https://www.nuget.org/packages/ToddHenderson.Maui.MacIdiom.Compatibility) | 0.0.3 | Todd Henderson | Compatibility handlers for .NET MAUI applications using the Mac Catalyst Mac UI… |
| 2026-10-13 15:02:21 | [13371337](https://www.nuget.org/packages/13371337) | 1.7.0 | AIOKO | 13371337: autonomous offline CPU AI and project tools for Visual Studio 2022. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
