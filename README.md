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

## Latest list — 2026-11-18 03:21 UTC

New packages created between 2026-11-18 02:21 UTC and 2026-11-18 03:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T03-21-55-080854Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 02:29:35 | [Async.HtmlAgilityPack](https://www.nuget.org/packages/Async.HtmlAgilityPack) | 2.0.0 | ZZZ Projects Inc., Andy Fried… | An async-first fork of Html Agility Pack: an HTML parser that builds a read/wri… |
| 2026-11-18 02:32:25 | [Jinxxy.NET](https://www.nuget.org/packages/Jinxxy.NET) | 1.0.0 | dfgHiatus | Unofficial .NET client for the Jinxxy Creator API (v1): products, orders, licen… |
| 2026-11-18 03:02:06 | [CSweet.Agent.Testing](https://www.nuget.org/packages/CSweet.Agent.Testing) | 5.42.0 | C-Sweet | Run standalone agent scenarios through the C-Sweet SDK delivery dispatcher. |
| 2026-11-18 03:11:57 | [GeoPandas.Net.RemoteSensing](https://www.nuget.org/packages/GeoPandas.Net.RemoteSensing) | 0.3.0 | Gravicode Studios (Kang Fadhi… | GeoPandas.Net satellite product readers: Landsat Collection 2 (MTL, scaled refl… |
| 2026-11-18 03:12:00 | [GeoPandas.Net.Survey](https://www.nuget.org/packages/GeoPandas.Net.Survey) | 0.3.0 | Gravicode Studios (Kang Fadhi… | GeoPandas.Net surveying and GNSS: traverse computation and Bowditch/Transit adj… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
