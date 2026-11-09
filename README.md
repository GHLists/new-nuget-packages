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

## Latest list — 2026-11-09 07:20 UTC

New packages created between 2026-11-09 06:19 UTC and 2026-11-09 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T07-20-23-764681Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 06:26:16 | [Universal.OpenAI.Live.Client](https://www.nuget.org/packages/Universal.OpenAI.Live.Client) | 1.0.0 | Andrew Ong | Client for the OpenAI GPT-Live WebSocket protocol, audio streaming, and backend… |
| 2026-11-09 06:29:30 | [Blobatar](https://www.nuget.org/packages/Blobatar) | 0.1.0 | Hamed Hajiloo | Deterministic geometric avatars ("blobatars") from any string, rendered as SVG.… |
| 2026-11-09 06:30:21 | [Blobatar.Blazor](https://www.nuget.org/packages/Blobatar.Blazor) | 0.1.0 | Hamed Hajiloo | The <Blobatar> Razor component: deterministic geometric avatars from any string… |
| 2026-11-09 06:42:54 | [Primo.Office.DX.Core](https://www.nuget.org/packages/Primo.Office.DX.Core) | 1.0.8 | Rondem | Primo RPA MS Office extra activities |
| 2026-11-09 06:49:27 | [EncDotNet.S100.Datasets.Grib](https://www.nuget.org/packages/EncDotNet.S100.Datasets.Grib) | 0.27.0 | Phillip Hoff | A managed GRIB2 decoder for wind and wave grids: sections 0 to 8 with several m… |
| 2026-11-09 06:49:28 | [EncDotNet.S100.Rendering.Engine](https://www.nuget.org/packages/EncDotNet.S100.Rendering.Engine) | 0.27.0 | Phillip Hoff | Host-neutral S-100 chart rendering engine: the tile compositor (tile grid, rast… |
| 2026-11-09 06:49:29 | [EncDotNet.S100.Datasets.TropicalCyclones](https://www.nuget.org/packages/EncDotNet.S100.Datasets.TropicalCyclones) | 0.27.0 | Phillip Hoff | A tropical cyclone advisory model and a reader for the US National Hurricane Ce… |
| 2026-11-09 06:49:31 | [EncDotNet.S100.Scripting.LuaCSharp](https://www.nuget.org/packages/EncDotNet.S100.Scripting.LuaCSharp) | 0.27.0 | Phillip Hoff | Libraries for manipulating S-100 based nautical charts. |
| 2026-11-09 06:49:34 | [EncDotNet.S100.Datasets.NetCdf](https://www.nuget.org/packages/EncDotNet.S100.Datasets.NetCdf) | 0.27.0 | Phillip Hoff | A managed reader for NetCDF-CF wind and wave grids: NetCDF-3 (classic and 64-bi… |
| 2026-11-09 06:49:37 | [EncDotNet.S100.Datasets.Cap](https://www.nuget.org/packages/EncDotNet.S100.Datasets.Cap) | 0.27.0 | Phillip Hoff | A reader for OASIS Common Alerting Protocol (CAP) 1.2 marine weather warnings:… |
| 2026-11-09 06:49:38 | [EncDotNet.S100.Datasets.Weather](https://www.nuget.org/packages/EncDotNet.S100.Datasets.Weather) | 0.27.0 | Phillip Hoff | The shared in-memory model for wind and wave grids read from GRIB2 and NetCDF-C… |
| 2026-11-09 06:49:39 | [EncDotNet.S100.Datasets.S412](https://www.nuget.org/packages/EncDotNet.S100.Datasets.S412) | 0.27.0 | Phillip Hoff | Libraries for manipulating S-100 based nautical charts. |
| 2026-11-09 07:15:06 | [Zenvoy.Results.AspNetCore](https://www.nuget.org/packages/Zenvoy.Results.AspNetCore) | 10.0.0 | Maxsud Mutalov | ASP.NET Core integration for Zenvoy.Results: converts Result and Result<T> to M… |
| 2026-11-09 07:15:07 | [Zenvoy.Results](https://www.nuget.org/packages/Zenvoy.Results) | 10.0.0 | Maxsud Mutalov | Zenvoy.Results: a high-performance, zero-allocation Result pattern for .NET. Re… |
| 2026-11-09 07:15:08 | [Zenvoy.Results.Mediator](https://www.nuget.org/packages/Zenvoy.Results.Mediator) | 10.0.0 | Maxsud Mutalov | Zenvoy mediator integration for Zenvoy.Results: command/query interfaces, a val… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
