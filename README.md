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

## Latest list — 2026-10-19 06:21 UTC

New packages created between 2026-10-19 05:20 UTC and 2026-10-19 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T06-21-50-687111Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 05:30:17 | [Meziantou.Framework.Fonts](https://www.nuget.org/packages/Meziantou.Framework.Fonts) | 1.0.0 | meziantou | Fully managed OpenType font reader and text shaper shared by Meziantou.Framewor… |
| 2026-10-19 05:30:20 | [RasterNet.Core](https://www.nuget.org/packages/RasterNet.Core) | 0.26.4301 | Jürgen Gstaltmaier | Fully managed, thread-safe, high-performance reader for georeferenced raster da… |
| 2026-10-19 05:56:53 | [CanadaRidingTagger](https://www.nuget.org/packages/CanadaRidingTagger) | 0.2.1 | Jake Landau | Identifies the Canadian federal riding and province/territory electoral distric… |
| 2026-10-19 05:57:42 | [AvaUnion.Controls](https://www.nuget.org/packages/AvaUnion.Controls) | 6.8.0.3 | drasticactions | Controls that Qt Quick Controls, Kirigami and QtWidgets have and Avalonia does… |
| 2026-10-19 05:57:52 | [AvaUnion.BreezeIcons](https://www.nuget.org/packages/AvaUnion.BreezeIcons) | 6.8.0.3 | drasticactions | Breeze icons for AvaUnion |
| 2026-10-19 06:15:55 | [Wp.Utils.AutoAppSettings](https://www.nuget.org/packages/Wp.Utils.AutoAppSettings) | 0.0.1-alpha | WuPan | 根据appsettings.json生成AppSettings类文件 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
