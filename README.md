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

## Latest list — 2026-10-23 17:20 UTC

New packages created between 2026-10-23 16:20 UTC and 2026-10-23 17:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T17-20-00-886792Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 16:31:27 | [PeachDrawing.PDF](https://www.nuget.org/packages/PeachDrawing.PDF) | 0.9.24 | PeachDrawing.PDF | A PDF Canvas for PeachDrawing.Core: draw shapes, text, images, gradients and ef… |
| 2026-10-23 16:31:28 | [PeachDrawing.Svg](https://www.nuget.org/packages/PeachDrawing.Svg) | 0.9.24 | PeachDrawing.Svg | A vector SVG Canvas for PeachDrawing.Core - draw shapes, gradients, clips, text… |
| 2026-10-23 16:31:30 | [PeachBrackets](https://www.nuget.org/packages/PeachBrackets) | 0.9.24 | PeachBrackets | Parses HTML, CSS, SVG and MathML, resolves the cascade and lays the document ou… |
| 2026-10-23 16:35:11 | [BGCS.Extension.Android](https://www.nuget.org/packages/BGCS.Extension.Android) | 4.0.0 | FLwolfy | Explicit optional source-generation extension for BGCS; consumer builds remain… |
| 2026-10-23 16:35:12 | [BGCS.Extension.AppleMobile](https://www.nuget.org/packages/BGCS.Extension.AppleMobile) | 4.0.0 | FLwolfy | Explicit optional source-generation extension for BGCS; consumer builds remain… |
| 2026-10-23 16:35:14 | [BGCS.Extension.BrowserWasm](https://www.nuget.org/packages/BGCS.Extension.BrowserWasm) | 4.0.0 | FLwolfy | Explicit optional source-generation extension for BGCS; consumer builds remain… |
| 2026-10-23 16:35:15 | [BGCS.Extension.FreeBsd](https://www.nuget.org/packages/BGCS.Extension.FreeBsd) | 4.0.0 | FLwolfy | Explicit optional source-generation extension for BGCS; consumer builds remain… |
| 2026-10-23 16:35:16 | [BGCS.Extension.NativeAot](https://www.nuget.org/packages/BGCS.Extension.NativeAot) | 4.0.0 | FLwolfy | Explicit optional source-generation extension for BGCS; consumer builds remain… |
| 2026-10-23 16:40:02 | [DubUrl.Provider.DuckDb.Adbc](https://www.nuget.org/packages/DubUrl.Provider.DuckDb.Adbc) | 0.45.0 | Cédric L. Charlier | DuckDB ADBC provider factory and installed native-driver discovery for DubUrl. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
