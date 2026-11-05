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

## Latest list — 2026-11-05 18:20 UTC

New packages created between 2026-11-05 17:21 UTC and 2026-11-05 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T18-20-54-817963Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 17:26:30 | [UkrUtils.Katottg](https://www.nuget.org/packages/UkrUtils.Katottg) | 1.0.1 | Eugene Yakush | Кодифікатор адміністративно-територіальних одиниць та територій територіальних… |
| 2026-11-05 17:26:31 | [UkrUtils.Katottg.Import](https://www.nuget.org/packages/UkrUtils.Katottg.Import) | 1.0.1 | Eugene Yakush | Імпорт офіційного xlsx-файлу КАТОТТГ без сторонніх залежностей. |
| 2026-11-05 17:26:32 | [UkrUtils.Katottg.Tool](https://www.nuget.org/packages/UkrUtils.Katottg.Tool) | 1.0.1 | Eugene Yakush | CLI для КАТОТТГ: імпорт офіційного xlsx, побудова знімка, пошук. |
| 2026-11-05 17:34:27 | [miPDFlib.Rendering](https://www.nuget.org/packages/miPDFlib.Rendering) | 1.2.0 | Wolfgang Mitterbucher | Renders PDF pages to images (PNG or pixels) at any resolution, e.g. for preview… |
| 2026-11-05 17:38:56 | [WebIt.Observability](https://www.nuget.org/packages/WebIt.Observability) | 1.0.7 | Alexandre De Marco Padrão | Biblioteca .NET 9 para observabilidade de APIs e Workers, com logging HTTP, ide… |
| 2026-11-05 17:45:46 | [MediaBoom.Basolia](https://www.nuget.org/packages/MediaBoom.Basolia) | 1.0.0 | Aptivi | MediaBoom! Managed playback library |
| 2026-11-05 17:45:51 | [MediaBoom.Native](https://www.nuget.org/packages/MediaBoom.Native) | 1.0.0 | Aptivi | MediaBoom! Native libraries suppport for Basolia (LibMPV) |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
