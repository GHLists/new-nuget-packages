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

## Latest list — 2026-10-19 09:20 UTC

New packages created between 2026-10-19 08:22 UTC and 2026-10-19 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T09-20-35-355614Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 08:22:52 | [Beresta](https://www.nuget.org/packages/Beresta) | 2.1.0 | Beresta.NET | Берёста — DOM-библиотека XML на C++17: DOM, XPath 1.0, XML Schema, DTD (обёртка… |
| 2026-10-19 08:28:13 | [X-Ray.PS](https://www.nuget.org/packages/X-Ray.PS) | 26.10.6966 | Curiosity GmbH | Pure managed PostScript, EPS and XPS reader for .NET: a PostScript interpreter,… |
| 2026-10-19 08:28:16 | [X-Ray.Psd.Skia](https://www.nuget.org/packages/X-Ray.Psd.Skia) | 26.10.6966 | Curiosity GmbH | SkiaSharp interop for XRay.Psd: SKBitmap/SKImage conversion, thumbnail decoding… |
| 2026-10-19 08:28:19 | [X-Ray.Psd.Text](https://www.nuget.org/packages/X-Ray.Psd.Text) | 26.10.6966 | Curiosity GmbH | Type-layer re-rendering for XRay.Psd: lays out PSD text from the parsed model (… |
| 2026-10-19 08:30:54 | [X-Ray.Office.Text](https://www.nuget.org/packages/X-Ray.Office.Text) | 26.10.6965 | Curiosity GmbH | Font resolution and metrics, text shaping, Unicode line breaking and paragraph… |
| 2026-10-19 08:30:57 | [X-Ray.Office.Vector](https://www.nuget.org/packages/X-Ray.Office.Vector) | 26.10.6965 | Curiosity GmbH | Importers for embedded vector graphics: WMF, EMF, EMF+ and SVG, decoded into th… |
| 2026-10-19 08:30:59 | [X-Ray.Office.WordProcessing](https://www.nuget.org/packages/X-Ray.Office.WordProcessing) | 26.10.6965 | Curiosity GmbH | Word-processing documents (the LibreOffice Writer equivalent): DOCX/DOCM/DOTX/D… |
| 2026-10-19 08:31:02 | [X-Ray.Office](https://www.nuget.org/packages/X-Ray.Office) | 26.10.6965 | Curiosity GmbH | Renders Word, Excel and PowerPoint documents, with their legacy binary, OpenDoc… |
| 2026-10-19 08:44:47 | [Bibui.App.WaylandManaged](https://www.nuget.org/packages/Bibui.App.WaylandManaged) | 0.10.0 | Navisurg ApS | A bibui app in one package: bibui, a native Wayland window drawn by bibui's man… |
| 2026-10-19 08:44:47 | [Bibui.App.SilkSkiaGl](https://www.nuget.org/packages/Bibui.App.SilkSkiaGl) | 0.10.0 | Navisurg ApS | A bibui app in one package: bibui, a Silk window drawn by Skia on its GL contex… |
| 2026-10-19 08:44:48 | [Bibui.App.SilkManaged](https://www.nuget.org/packages/Bibui.App.SilkManaged) | 0.10.0 | Navisurg ApS | A bibui app in one package: bibui, a Silk window drawn by bibui's managed raste… |
| 2026-10-19 08:44:48 | [Bibui.Gl](https://www.nuget.org/packages/Bibui.Gl) | 0.10.0 | Navisurg ApS | Bibui's GL layer: the GL framebuffer a platform presents (GlTarget) and the GL… |
| 2026-10-19 08:44:49 | [Bibui.App.WaylandSkiaCpu](https://www.nuget.org/packages/Bibui.App.WaylandSkiaCpu) | 0.10.0 | Navisurg ApS | A bibui app in one package: bibui, a native Wayland window drawn by Skia on the… |
| 2026-10-19 08:44:49 | [Bibui.App.SilkSkiaCpu](https://www.nuget.org/packages/Bibui.App.SilkSkiaCpu) | 0.10.0 | Navisurg ApS | A bibui app in one package: bibui, a Silk window drawn by Skia on the CPU, show… |
| 2026-10-19 08:55:09 | [Axial.Hosting.AspNetCore](https://www.nuget.org/packages/Axial.Hosting.AspNetCore) | 0.11.1 | Adam Davies | [Experimental] ASP.NET Core hosting for schema-driven Axial Flow endpoints, wit… |
| 2026-10-19 08:55:11 | [Axial.Hosting.GenHttp](https://www.nuget.org/packages/Axial.Hosting.GenHttp) | 0.11.1 | Adam Davies | [Experimental] GenHTTP hosting for schema-driven Axial Flow endpoints, with tru… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
