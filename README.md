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

## Latest list — 2026-11-06 22:19 UTC

New packages created between 2026-11-06 21:19 UTC and 2026-11-06 22:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T22-19-42-343542Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 21:42:52 | [SharpEquations](https://www.nuget.org/packages/SharpEquations) | 1.0.1 | Simone Bortolin | Equations converted between MathML, OMML (Word), MTEF (MathType and Equation Ed… |
| 2026-11-06 21:50:50 | [TSharpVision.Graphics](https://www.nuget.org/packages/TSharpVision.Graphics) | 1.2.0 | Lubomir Klimes | Optional pixel graphics views for TSharpVision: GView/GWindow display lists, sh… |
| 2026-11-06 21:50:53 | [TSharpVision.HelpCompiler](https://www.nuget.org/packages/TSharpVision.HelpCompiler) | 1.2.0 | Lubomir Klimes | TSharpVision help compiler (svhc): compiles Turbo Vision-style help source text… |
| 2026-11-06 21:50:54 | [TSharpVision.ResourceCompiler](https://www.nuget.org/packages/TSharpVision.ResourceCompiler) | 1.2.0 | Lubomir Klimes | TSharpVision resource compiler (svrc): compiles .trc resource scripts into bina… |
| 2026-11-06 21:50:55 | [TSharpVision.ResourceTools](https://www.nuget.org/packages/TSharpVision.ResourceTools) | 1.2.0 | Lubomir Klimes | TSharpVision resource inspector (svres): lists, shows, dumps and validates the… |
| 2026-11-06 21:55:33 | [Flowery.NET.Kanban](https://www.nuget.org/packages/Flowery.NET.Kanban) | 4.0.0 | tobitege | Full-featured Kanban board controls for Flowery.NET and Avalonia UI. |
| 2026-11-06 21:55:33 | [Flowery.NET.Skia](https://www.nuget.org/packages/Flowery.NET.Skia) | 4.0.0 | tobitege | SkiaSharp effects for Flowery.NET: live backdrop blur with liquid-glass optics… |
| 2026-11-06 22:04:36 | [Fload.Attribution](https://www.nuget.org/packages/Fload.Attribution) | 1.0.1 | Fload | Fload install attribution for .NET for iOS and Android, with or without MAUI: c… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
